# Đọc input
n, m = map(int, input().split())
A = list(map(int, input().split()))

# Nếu đã có đủ chỗ ngay (1 chỗ tường)
if m <= 1:
    print(0)
    exit()

# Sắp xếp các ổ giảm dần (chọn ổ có Ai lớn trước)
A.sort(reverse=True)

available = 1  # chỗ có điện ban đầu
used = 0
for ai in A:
    # cắm ổ ai: tiêu 1 chỗ, thêm ai chỗ => lợi ích ròng ai-1
    available += ai - 1
    used += 1
    if available >= m:
        print(used)
        break
else:
    # hết ổ mà vẫn chưa đủ
    print(-1)