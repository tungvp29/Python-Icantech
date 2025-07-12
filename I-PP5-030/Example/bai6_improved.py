import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

class CustomerBehaviorPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.le_gender = LabelEncoder()
        self.le_job = LabelEncoder()
        self.feature_names = ['Tuổi', 'Thu nhập', 'điểm tín dụng', 'Giới tính_encoded', 'Nghề nghiệp_encoded']
        
    def load_and_prepare_data(self):
        """Tải và xử lý dữ liệu"""
        # Đọc dữ liệu
        df_customers = pd.read_csv('data7.1.csv')
        df_purchases = pd.read_csv('data7.2.csv')
        
        # Làm sạch tên cột
        df_customers.columns = df_customers.columns.str.strip()
        df_purchases.columns = df_purchases.columns.str.strip()
        
        # Kết hợp dữ liệu
        merged_df = pd.merge(df_customers, df_purchases, on='ID khách hàng', how='inner')
        
        # Làm sạch dữ liệu text
        for col in merged_df.select_dtypes(include=['object']).columns:
            merged_df[col] = merged_df[col].astype(str).str.strip()
        
        # Encoding categorical variables
        merged_df['Giới tính_encoded'] = self.le_gender.fit_transform(merged_df['Giới tính'])
        merged_df['Nghề nghiệp_encoded'] = self.le_job.fit_transform(merged_df['Nghề nghiệp'])
        
        return merged_df
    
    def train_model(self, df):
        """Huấn luyện mô hình"""
        X = df[self.feature_names]
        y = df['Giá']
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Huấn luyện mô hình
        self.model.fit(X_scaled, y)
        
        # Cross-validation để đánh giá
        cv_scores = cross_val_score(self.model, X_scaled, y, cv=3, scoring='r2')
        
        print("=== KẾT QUẢ HUẤN LUYỆN ===")
        print(f"Cross-validation R² scores: {cv_scores}")
        print(f"Mean CV R² score: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
        
        return X_scaled, y
    
    def predict_price(self, age, income, credit_score, gender, job):
        """Dự đoán giá sản phẩm cho khách hàng"""
        try:
            gender_encoded = self.le_gender.transform([gender])[0]
        except:
            gender_encoded = 0
            
        try:
            job_encoded = self.le_job.transform([job])[0]
        except:
            job_encoded = 0
        
        # Tạo input và scale
        input_data = np.array([[age, income, credit_score, gender_encoded, job_encoded]])
        input_scaled = self.scaler.transform(input_data)
        
        predicted_price = self.model.predict(input_scaled)[0]
        return max(0, predicted_price)  # Đảm bảo giá không âm
    
    def analyze_customer_segments(self, df):
        """Phân tích phân khúc khách hàng"""
        # Tạo các nhóm khách hàng dựa trên thu nhập và tuổi
        df['Income_Group'] = pd.cut(df['Thu nhập'], 
                                   bins=[0, 40000, 60000, float('inf')], 
                                   labels=['Thấp', 'Trung bình', 'Cao'])
        
        df['Age_Group'] = pd.cut(df['Tuổi'], 
                                bins=[0, 30, 50, float('inf')], 
                                labels=['Trẻ', 'Trung niên', 'Lớn tuổi'])
        
        # Phân tích theo nhóm
        segment_analysis = df.groupby(['Income_Group', 'Age_Group']).agg({
            'Giá': ['mean', 'count'],
            'điểm tín dụng': 'mean'
        }).round(2)
        
        print("\n=== PHÂN TÍCH PHÂN KHÚC KHÁCH HÀNG ===")
        print(segment_analysis)
        
        return segment_analysis
    
    def visualize_results(self, X, y):
        """Tạo biểu đồ trực quan"""
        # Dự đoán cho toàn bộ dataset
        y_pred = self.model.predict(X)
        
        plt.figure(figsize=(15, 10))
        
        # 1. Actual vs Predicted
        plt.subplot(2, 3, 1)
        plt.scatter(y, y_pred, alpha=0.7, color='blue')
        plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
        plt.xlabel('Actual Price')
        plt.ylabel('Predicted Price')
        plt.title('Actual vs Predicted Prices')
        
        # 2. Feature Importance
        plt.subplot(2, 3, 2)
        feature_importance = abs(self.model.coef_)
        plt.bar(self.feature_names, feature_importance)
        plt.xlabel('Features')
        plt.ylabel('Coefficient Value')
        plt.title('Feature Importance')
        plt.xticks(rotation=45)
        
        # 3. Residuals
        plt.subplot(2, 3, 3)
        residuals = y - y_pred
        plt.scatter(y_pred, residuals, alpha=0.7)
        plt.axhline(y=0, color='r', linestyle='--')
        plt.xlabel('Predicted Price')
        plt.ylabel('Residuals')
        plt.title('Residual Plot')
        
        # 4. Price Distribution
        plt.subplot(2, 3, 4)
        plt.hist(y, bins=10, alpha=0.7, label='Actual', color='blue')
        plt.hist(y_pred, bins=10, alpha=0.7, label='Predicted', color='red')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.title('Price Distribution')
        plt.legend()
        
        # 5. Model Performance Metrics
        plt.subplot(2, 3, 5)
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        
        metrics = ['MSE', 'MAE', 'R²']
        values = [mse, mae, r2]
        
        plt.bar(metrics, values)
        plt.title('Model Performance Metrics')
        plt.ylabel('Score')
        
        # 6. Prediction Intervals
        plt.subplot(2, 3, 6)
        sorted_indices = np.argsort(y)
        plt.plot(y.iloc[sorted_indices], label='Actual', marker='o')
        plt.plot(y_pred[sorted_indices], label='Predicted', marker='s')
        plt.xlabel('Sample Index (sorted by actual price)')
        plt.ylabel('Price')
        plt.title('Predictions vs Actual (Sorted)')
        plt.legend()
        
        plt.tight_layout()
        plt.show()
        
        return mse, mae, r2

def main():
    # Khởi tạo predictor
    predictor = CustomerBehaviorPredictor()
    
    # Tải và chuẩn bị dữ liệu
    print("=== ĐANG TẢI VÀ XỬ LÝ DỮ LIỆU ===")
    df = predictor.load_and_prepare_data()
    print(f"Tổng số khách hàng: {len(df)}")
    print("\nThông tin dữ liệu:")
    print(df.info())
    
    # Huấn luyện mô hình
    print("\n=== ĐANG HUẤN LUYỆN MÔ HÌNH ===")
    X_scaled, y = predictor.train_model(df)
    
    # Phân tích phân khúc khách hàng
    segment_analysis = predictor.analyze_customer_segments(df)
    
    # Trực quan hóa kết quả
    print("\n=== TẠO BIỂU ĐỒ TRỰC QUAN ===")
    mse, mae, r2 = predictor.visualize_results(X_scaled, y)
    
    print(f"\nMSE: {mse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R² Score: {r2:.3f}")
    
    # Dự đoán cho khách hàng mới
    print("\n=== DỰ ĐOÁN CHO KHÁCH HÀNG MỚI ===")
    
    test_customers = [
        {"age": 35, "income": 55000, "credit_score": 720, "gender": "Nam", "job": "Kỹ sư phần mềm"},
        {"age": 28, "income": 45000, "credit_score": 650, "gender": "Nữ", "job": "Giáo viên"},
        {"age": 45, "income": 80000, "credit_score": 780, "gender": "Nam", "job": "Bác sĩ"},
        {"age": 32, "income": 42000, "credit_score": 690, "gender": "Nữ", "job": "Chủ doanh nghiệp"},
        {"age": 55, "income": 65000, "credit_score": 750, "gender": "Nam", "job": "Nghỉ hưu"}
    ]
    
    for customer in test_customers:
        predicted_price = predictor.predict_price(
            customer["age"], customer["income"], customer["credit_score"],
            customer["gender"], customer["job"]
        )
        
        # Phân loại khách hàng
        if predicted_price < 600:
            category = "🔵 Tiết kiệm"
            recommendation = "Sản phẩm cơ bản, giá rẻ"
        elif predicted_price < 1000:
            category = "🟡 Trung bình"
            recommendation = "Sản phẩm chất lượng, giá hợp lý"
        else:
            category = "🔴 Cao cấp"
            recommendation = "Sản phẩm premium, dịch vụ VIP"
        
        print(f"\n👤 Khách hàng: {customer['age']} tuổi, {customer['gender']}, {customer['job']}")
        print(f"💰 Thu nhập: ${customer['income']:,}")
        print(f"📊 Điểm tín dụng: {customer['credit_score']}")
        print(f"🎯 Dự đoán giá sản phẩm: ${predicted_price:.2f}")
        print(f"📋 Phân loại: {category}")
        print(f"💡 Khuyến nghị: {recommendation}")
        print("-" * 60)
    
    # Tạo báo cáo tổng hợp
    print("\n=== BÁO CÁO TỔNG HỢP ===")
    print("🔍 Những yếu tố ảnh hưởng đến thói quen mua hàng:")
    
    feature_importance = abs(predictor.model.coef_)
    feature_ranking = sorted(zip(predictor.feature_names, feature_importance), 
                           key=lambda x: x[1], reverse=True)
    
    for i, (feature, importance) in enumerate(feature_ranking, 1):
        print(f"{i}. {feature}: {importance:.2f}")
    
    print(f"\n📈 Độ chính xác mô hình: {r2:.1%}")
    if r2 > 0.8:
        print("✅ Mô hình có độ chính xác cao")
    elif r2 > 0.6:
        print("⚠️ Mô hình có độ chính xác trung bình")
    else:
        print("❌ Mô hình cần cải thiện thêm")

if __name__ == "__main__":
    main()
