from . import db

class Food(db.Model):
    __tablename__ = 'Foods' # Tên bảng trong SQL Server
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))
    image_url = db.Column(db.String(500)) # Link ảnh món ăn

    def __repr__(self):
        return f'<Food {self.name}>'