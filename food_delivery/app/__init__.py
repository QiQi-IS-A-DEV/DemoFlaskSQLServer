from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

#Tạo db
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Kết nối database vào app
    db.init_app(app)

    with app.app_context():
        # Import models và routes bên trong context để tránh lỗi vòng lặp
        from . import models, routes
        
        # lệnh tạo bảng trong database nếu chưa tồn tại
        db.create_all()

    return app