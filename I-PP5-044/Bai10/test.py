import pygame
import cv2
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Hand Gesture Control - Show open hand to start!')

pygame.display.update()

# Khởi tạo camera
cap = cv2.VideoCapture(0)

# Kiểm tra xem camera có hoạt động không
if not cap.isOpened():
    print("Không thể mở camera. Bỏ qua gesture detection.")
    camera_available = False
else:
    camera_available = True
    print("Camera đã sẵn sàng!")

# Biến để theo dõi gesture
gesture_detected = False
gesture_timer = 0
required_gesture_frames = 30  # Số frame cần thiết để xác nhận gesture

# Biến để theo dõi diện tích tay trước đó (cho phát hiện nắm tay)
previous_hand_area = 0
fist_cooldown = 0  # Để tránh phát hiện liên tục

# Hàm đơn giản để phát hiện "open hand" bằng contour
def detect_open_hand_simple(frame):
    global gesture_timer, gesture_detected
    
    # Chuyển đổi sang HSV để dễ dàng phát hiện màu da
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Định nghĩa phạm vi màu da (có thể cần điều chỉnh tùy theo ánh sáng)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    # Tạo mask cho màu da
    skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Làm mịn mask
    kernel = np.ones((3,3), np.uint8)
    skin_mask = cv2.morphologyEx(skin_mask, cv2.MORPH_OPEN, kernel)
    skin_mask = cv2.morphologyEx(skin_mask, cv2.MORPH_CLOSE, kernel)
    
    # Tìm contours
    contours, _ = cv2.findContours(skin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    hand_detected = False
    if contours:
        # Lấy contour lớn nhất
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)
        
        # Nếu area đủ lớn, coi như có tay
        if area > 5000:  # Ngưỡng có thể điều chỉnh
            # Vẽ contour lên frame
            cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
            
            # Tính convex hull
            hull = cv2.convexHull(largest_contour)
            cv2.drawContours(frame, [hull], -1, (0, 0, 255), 2)
            
            # Kiểm tra defects để xác định có phải open hand không
            hull_indices = cv2.convexHull(largest_contour, returnPoints=False)
            if len(hull_indices) > 3:
                defects = cv2.convexityDefects(largest_contour, hull_indices)
                
                if defects is not None:
                    defect_count = 0
                    for i in range(defects.shape[0]):
                        s, e, f, d = defects[i, 0]
                        depth = d / 256.0
                        if depth > 20:  # Ngưỡng độ sâu để coi là khe giữa các ngón tay
                            defect_count += 1
                    
                    # Nếu có 3-4 defects (khe giữa các ngón tay), coi như open hand
                    if defect_count >= 3:
                        hand_detected = True
                        cv2.putText(frame, "Open hand detected!", (10, 30), 
                                  cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Đếm số frame liên tiếp phát hiện được tay
    if hand_detected:
        gesture_timer += 1
    else:
        gesture_timer = 0
    
    # Trả về True nếu phát hiện gesture đủ lâu và chưa được phát hiện trước đó
    if gesture_timer >= required_gesture_frames and not gesture_detected:
        gesture_detected = True
        return True
    
    return False

# Hàm reset gesture detection
def reset_gesture_detection():
    global gesture_detected, gesture_timer, previous_hand_area, fist_cooldown
    gesture_detected = False
    gesture_timer = 0
    previous_hand_area = 0
    fist_cooldown = 0

# Hàm phát hiện cử chỉ "rock" (nắm tay) - cải tiến
def detect_fist_gesture(frame):
    global previous_hand_area, fist_cooldown
    
    # Giảm cooldown
    if fist_cooldown > 0:
        fist_cooldown -= 1
        return False
    
    # Chuyển đổi sang HSV để dễ dàng phát hiện màu da
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Định nghĩa phạm vi màu da (mở rộng phạm vi)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([25, 255, 255], dtype=np.uint8)
    
    # Tạo mask cho màu da
    skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Làm mịn mask mạnh hơn
    kernel = np.ones((5,5), np.uint8)
    skin_mask = cv2.morphologyEx(skin_mask, cv2.MORPH_OPEN, kernel)
    skin_mask = cv2.morphologyEx(skin_mask, cv2.MORPH_CLOSE, kernel)
    
    # Tìm contours
    contours, _ = cv2.findContours(skin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Lấy contour lớn nhất
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)
        
        # Ngưỡng thấp hơn cho nắm tay
        if area > 2000:  # Giảm ngưỡng từ 3000 xuống 2000
            # Vẽ contour lên frame
            cv2.drawContours(frame, [largest_contour], -1, (255, 0, 0), 2)
            
            # Tính convex hull
            hull = cv2.convexHull(largest_contour)
            cv2.drawContours(frame, [hull], -1, (0, 255, 255), 2)
            
            # Phương pháp 1: Kiểm tra tỷ lệ solidity
            hull_area = cv2.contourArea(hull)
            if hull_area > 0:
                solidity = area / hull_area
                
                # Phương pháp 2: Kiểm tra tỷ lệ chiều dài/chiều rộng
                x, y, w, h = cv2.boundingRect(largest_contour)
                aspect_ratio = float(w) / h
                
                # Phương pháp 3: Kiểm tra extent (tỷ lệ diện tích/diện tích bounding box)
                rect_area = w * h
                extent = float(area) / rect_area
                
                # Phương pháp 4: Kiểm tra sự thay đổi diện tích (nắm tay = giảm diện tích)
                area_change_ratio = 1.0
                if previous_hand_area > 0:
                    area_change_ratio = area / previous_hand_area
                
                # Hiển thị thông tin debug
                cv2.putText(frame, f"Area: {int(area)}", (10, 90), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(frame, f"Solidity: {solidity:.2f}", (10, 110), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(frame, f"Aspect: {aspect_ratio:.2f}", (10, 130), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(frame, f"Area Change: {area_change_ratio:.2f}", (10, 150), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
                # Điều kiện nhận diện nắm tay (linh hoạt hơn)
                fist_detected = False
                
                # Điều kiện 1: Solidity cao và aspect ratio gần vuông
                if solidity > 0.75 and 0.5 < aspect_ratio < 2.0:
                    fist_detected = True
                
                # Điều kiện 2: Diện tích nhỏ nhưng đặc (có thể là nắm tay xa)
                elif area < 4000 and solidity > 0.8:
                    fist_detected = True
                
                # Điều kiện 3: Sự giảm đột ngột diện tích (từ xoè tay -> nắm tay)
                elif previous_hand_area > 0 and area_change_ratio < 0.7:
                    fist_detected = True
                
                # Điều kiện 4: Kiểm tra defects ít
                hull_indices = cv2.convexHull(largest_contour, returnPoints=False)
                if len(hull_indices) > 3:
                    defects = cv2.convexityDefects(largest_contour, hull_indices)
                    
                    defect_count = 0
                    if defects is not None:
                        for i in range(defects.shape[0]):
                            s, e, f, d = defects[i, 0]
                            depth = d / 256.0
                            if depth > 10:  # Ngưỡng thấp hơn
                                defect_count += 1
                    
                    cv2.putText(frame, f"Defects: {defect_count}", (10, 170), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    
                    # Nếu có ít defects (0-2), có thể là nắm tay
                    if defect_count <= 2 and solidity > 0.7:
                        fist_detected = True
                
                # Cập nhật diện tích trước đó
                previous_hand_area = area
                
                if fist_detected:
                    cv2.putText(frame, "FIST DETECTED! JUMP!", (10, 60), 
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    fist_cooldown = 15  # Cooldown 15 frames để tránh phát hiện liên tục
                    return True
    
    return False

# Trạng thái game
game_started = False
waiting_for_gesture = True

clock = pygame.time.Clock()
x_velocity = 5
y_velocity = 8
bg_x = 0
bg_y = 0
robot_x = 0
robot_y = 230
spike_x = 550
spike_y = 230
score = 99
font = pygame.font.SysFont('Arial', 25)
font_end = pygame.font.SysFont('Arial', 50)
bg = pygame.image.load('background.jpg')
robot = pygame.image.load('robot.png')
spike = pygame.image.load('spike.png')
jump = True
pausing = False
status = True

while status:
  clock.tick(60)
  
  # Xử lý camera và nhận diện cử chỉ tay
  if camera_available:
    ret, frame = cap.read()
    if ret:
      # Lật frame để hiển thị như gương
      frame = cv2.flip(frame, 1)
      
      # Kiểm tra cử chỉ open hand để khởi động game (vẽ tracking lên frame gốc)
      if waiting_for_gesture and detect_open_hand_simple(frame):
        game_started = True
        waiting_for_gesture = False
        print("Phát hiện cử chỉ 'open hand'! Game bắt đầu!")
      
      # Kiểm tra cử chỉ nắm tay để nhảy (vẽ tracking lên frame gốc)
      elif game_started and not pausing:
        if detect_fist_gesture(frame):
          if robot_y == 230:  # Chỉ nhảy khi robot đang ở mặt đất
            jump = True
            print("Phát hiện nắm tay! Robot nhảy!")
      
      # Resize frame SAU KHI đã vẽ tracking để giữ lại các đường tracking
      height, width = frame.shape[:2]
      new_width = 1200
      new_height = int(height * (new_width / width))
      frame_display = cv2.resize(frame, (new_width, new_height))
      
      # Hiển thị hướng dẫn trên frame hiển thị
      if waiting_for_gesture:
        cv2.putText(frame_display, "OPEN HAND to start", (10, new_height-40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
      elif game_started and not pausing:
        cv2.putText(frame_display, "FIST to JUMP (or press F)", (10, new_height-40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
      
      # Thêm thông tin điều khiển
      cv2.putText(frame_display, "Press 'q' to quit", (10, new_height-20), 
                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
      
      # Hiển thị camera feed với tracking
      cv2.imshow('Hand Gesture Control', frame_display)
  else:
    # Nếu không có camera, tự động bắt đầu game sau 3 giây
    if waiting_for_gesture:
      import time
      if not hasattr(clock, 'start_time'):
        clock.start_time = time.time()
      elif time.time() - clock.start_time > 3:
        game_started = True
        waiting_for_gesture = False
        print("Không có camera - tự động bắt đầu game!")
  
  screen.fill((255,255,255))
  
  # Nếu chưa bắt đầu game, hiển thị hướng dẫn
  if waiting_for_gesture:
    if camera_available:
      instruction_text = font.render('Xoè tay để bắt đầu game!', True, (255,0,0))
      instruction_text2 = font.render('Sau đó nắm tay để nhảy!', True, (0,0,255))
      screen.blit(instruction_text2, (150, 180))
    else:
      instruction_text = font.render('Nhấn SPACE để bắt đầu game!', True, (255,0,0))
    screen.blit(instruction_text, (150, 150))
  elif game_started:
    # Logic game chính
    bg_rect1 = screen.blit(bg, (bg_x, bg_y))
    bg_rect2 = screen.blit(bg, (bg_x+600, bg_y))
    score_text = font.render('Điem so: '+ str(score), True, (0,0,0))
    screen.blit(score_text, (10, 10))
    
    # Hiển thị hướng dẫn điều khiển
    if camera_available:
      control_text = font.render('Nắm tay để nhảy', True, (0,100,0))
    else:
      control_text = font.render('SPACE để nhảy', True, (0,100,0))
    screen.blit(control_text, (10, 40))
    
    bg_x = bg_x - x_velocity
    if bg_x+600 <= 0:
      bg_x = 0
    spike_x = spike_x - x_velocity
    if spike_x <= -20:
      spike_x = 550
      score += 1
    if 230 >= robot_y>=80:
      if jump == True:
        robot_y = robot_y - y_velocity
    else:
      jump = False
    if robot_y < 230:
      if jump == False:
        robot_y = robot_y + y_velocity
    robot_rect = screen.blit(robot, (robot_x, robot_y))
    spike_rect = screen.blit(spike, (spike_x, spike_y))
    if robot_rect.colliderect(spike_rect):
      pausing = True
      end_text = font_end.render('THUA', True, (0,0,0))
      screen.blit(end_text, (200, 200))
      x_velocity = 0
      y_velocity = 0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      status = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        if waiting_for_gesture:
          # Bắt đầu game bằng phím space khi chờ gesture
          game_started = True
          waiting_for_gesture = False
          print("Bắt đầu game bằng phím SPACE!")
        elif game_started and robot_y == 230:
          # Nhảy trong game
          jump = True
        elif pausing == True:
          # Reset game khi thua
          x_velocity = 5
          y_velocity = 8
          bg_x = 0
          bg_y = 0
          robot_x = 0
          robot_y = 230
          spike_x = 550
          spike_y = 230
          score = 99
          pausing = False
      elif event.key == pygame.K_f and game_started and not pausing:
        # Phím F để test cử chỉ nắm tay
        if robot_y == 230:
          jump = True
          print("Robot nhảy bằng phím F!")
      elif event.key == pygame.K_r:  # Reset game để chờ cử chỉ mới
        game_started = False
        waiting_for_gesture = True
        # Reset gesture detection
        reset_gesture_detection()
        x_velocity = 5
        y_velocity = 8
        bg_x = 0
        bg_y = 0
        robot_x = 0
        robot_y = 230
        spike_x = 550
        spike_y = 230
        score = 99
        pausing = False
        print("Game đã được reset! Xoè tay để bắt đầu lại.")
    # Thoát camera bằng phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
      status = False
  
  pygame.display.flip()

# Dọn dẹp
cap.release()
cv2.destroyAllWindows()
pygame.quit()


