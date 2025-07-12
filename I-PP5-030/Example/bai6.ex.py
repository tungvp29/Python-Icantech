import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ 2 file CSV
df_customers = pd.read_csv('data7.1.csv')
df_purchases = pd.read_csv('data7.2.csv')

print("=== THÔNG TIN KHÁCH HÀNG ===")
print(df_customers.head())
print("\n=== THÔNG TIN MUA HÀNG ===")
print(df_purchases.head())

# Làm sạch tên cột (loại bỏ khoảng trắng thừa)
df_customers.columns = df_customers.columns.str.strip()
df_purchases.columns = df_purchases.columns.str.strip()

print("\n=== TÊN CỘT SAU KHI CLEAN ===")
print("Customers columns:", df_customers.columns.tolist())
print("Purchases columns:", df_purchases.columns.tolist())

# Kết hợp 2 dataframe dựa trên ID khách hàng
merged_df = pd.merge(df_customers, df_purchases, on='ID khách hàng', how='inner')
print("\n=== DỮ LIỆU SAU KHI MERGE ===")
print(merged_df.head())

# Xử lý dữ liệu thiếu và encoding
# Loại bỏ khoảng trắng thừa trong các cột text
for col in merged_df.select_dtypes(include=['object']).columns:
    merged_df[col] = merged_df[col].astype(str).str.strip()

# Encoding categorical variables
le_gender = LabelEncoder()
le_job = LabelEncoder()

merged_df['Giới tính_encoded'] = le_gender.fit_transform(merged_df['Giới tính'])
merged_df['Nghề nghiệp_encoded'] = le_job.fit_transform(merged_df['Nghề nghiệp'])

# Chuẩn bị dữ liệu cho mô hình
# Features: Tuổi, Thu nhập, điểm tín dụng, Giới tính_encoded, Nghề nghiệp_encoded
# Target: Giá (dự đoán giá trị sản phẩm mà khách hàng có thể mua)

features = ['Tuổi', 'Thu nhập', 'điểm tín dụng', 'Giới tính_encoded', 'Nghề nghiệp_encoded']
X = merged_df[features]
y = merged_df['Giá']

print("\n=== THÔNG TIN DỮ LIỆU TRAINING ===")
print("Features shape:", X.shape)
print("Target shape:", y.shape)
print("Features info:")
print(X.describe())

# Chia dữ liệu train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Tạo và huấn luyện mô hình Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n=== KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH ===")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Hiển thị hệ số của mô hình
print("\n=== HỆ SỐ CỦA MÔ HÌNH ===")
coefficients = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_
})
print(coefficients)
print(f"Intercept: {model.intercept_:.2f}")

# Dự đoán cho khách hàng mới
print("\n=== DỰ ĐOÁN CHO KHÁCH HÀNG MỚI ===")

def predict_customer_behavior(age, income, credit_score, gender, job):
    """
    Dự đoán giá trị sản phẩm mà khách hàng có thể mua
    """
    # Encoding giới tính và nghề nghiệp
    try:
        gender_encoded = le_gender.transform([gender])[0]
    except:
        gender_encoded = 0  # Default value nếu không tìm thấy
        
    try:
        job_encoded = le_job.transform([job])[0]
    except:
        job_encoded = 0  # Default value nếu không tìm thấy
    
    # Tạo array input
    input_data = np.array([[age, income, credit_score, gender_encoded, job_encoded]])
    
    # Dự đoán
    predicted_price = model.predict(input_data)[0]
    
    return predicted_price

# Ví dụ dự đoán
examples = [
    (35, 55000, 720, 'Nam', 'Kỹ sư phần mềm'),
    (28, 45000, 650, 'Nữ', 'Giáo viên'),
    (45, 80000, 780, 'Nam', 'Bác sĩ')
]

for age, income, credit_score, gender, job in examples:
    predicted_price = predict_customer_behavior(age, income, credit_score, gender, job)
    print(f"Khách hàng: {age} tuổi, {gender}, {job}")
    print(f"Thu nhập: {income:,}, Điểm tín dụng: {credit_score}")
    print(f"Dự đoán giá sản phẩm sẽ mua: ${predicted_price:.2f}")
    print("-" * 50)

# Vẽ biểu đồ so sánh actual vs predicted
plt.figure(figsize=(12, 8))

# Subplot 1: Actual vs Predicted
plt.subplot(2, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted Prices')

# Subplot 2: Residuals
plt.subplot(2, 2, 2)
residuals = y_test - y_pred
plt.scatter(y_pred, residuals, alpha=0.7)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Price')
plt.ylabel('Residuals')
plt.title('Residual Plot')

# Subplot 3: Feature Importance
plt.subplot(2, 2, 3)
feature_importance = abs(model.coef_)
plt.bar(features, feature_importance)
plt.xlabel('Features')
plt.ylabel('Absolute Coefficient Value')
plt.title('Feature Importance')
plt.xticks(rotation=45)

# Subplot 4: Distribution of predictions
plt.subplot(2, 2, 4)
plt.hist(y_pred, bins=10, alpha=0.7, label='Predicted')
plt.hist(y_test, bins=10, alpha=0.7, label='Actual')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Prices')
plt.legend()

plt.tight_layout()
plt.show()

# Phân tích correlation
print("\n=== PHÂN TÍCH CORRELATION ===")
correlation_matrix = merged_df[features + ['Giá']].corr()
print(correlation_matrix)

# Vẽ heatmap correlation
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()

# Tạo function để dự đoán và phân loại khách hàng
def classify_customer_behavior(age, income, credit_score, gender, job):
    """
    Phân loại thói quen mua hàng của khách hàng
    """
    predicted_price = predict_customer_behavior(age, income, credit_score, gender, job)
    
    if predicted_price < 600:
        category = "Tiết kiệm"
        recommendation = "Sản phẩm giá rẻ, chương trình khuyến mãi"
    elif predicted_price < 1000:
        category = "Trung bình"
        recommendation = "Sản phẩm chất lượng tốt, giá hợp lý"
    else:
        category = "Cao cấp"
        recommendation = "Sản phẩm premium, dịch vụ VIP"
    
    return {
        'predicted_price': predicted_price,
        'category': category,
        'recommendation': recommendation
    }

print("\n=== PHÂN LOẠI VÀ KHUYẾN NGHỊ ===")
for age, income, credit_score, gender, job in examples:
    result = classify_customer_behavior(age, income, credit_score, gender, job)
    print(f"Khách hàng: {age} tuổi, {gender}, {job}")
    print(f"Phân loại: {result['category']}")
    print(f"Dự đoán chi tiêu: ${result['predicted_price']:.2f}")
    print(f"Khuyến nghị: {result['recommendation']}")
    print("-" * 60)