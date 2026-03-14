import pyodbc

# Kết nối trực tiếp tới master database để tạo database mới
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=(localdb)\MSSQLLocalDB;'
    r'DATABASE=master;'
    r'trusted_connection=yes;'
)
conn.autocommit = True
cursor = conn.cursor()  


try:
    cursor.execute("CREATE DATABASE FoodDeliveryDB")
    print("Đã tạo Database FoodDeliveryDB thành công!")
except Exception as e:
    print("Có thể Database đã tồn tại hoặc lỗi:", e)

cursor.close()
conn.close()