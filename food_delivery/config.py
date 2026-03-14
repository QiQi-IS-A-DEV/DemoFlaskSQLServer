import os

class Config:
    
    DRIVER = "ODBC Driver 17 for SQL Server" 
    
    # 2. Server Name MSSQL LocalDB thường có dạng (localdb)\InstanceName, ví dụ: (localdb)\MSSQLLocalDB
    # Dùng dấu r"" để Python không hiểu nhầm dấu gạch chéo \
    SERVER = r"(localdb)\MSSQLLocalDB"
    
    # 3. Database: Tên cái thùng chứa bạn sẽ tạo trong SSMS
    DATABASE = "FoodDeliveryDB"
    
    # 4. Chuỗi kết nối tối ưu cho LocalDB
    # Thêm TrustServerCertificate=yes để khớp với cấu hình trong ảnh của bạn
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://@{SERVER}/{DATABASE}?"
        f"driver={DRIVER}&trusted_connection=yes&TrustServerCertificate=yes"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "quan-delivery-secret"