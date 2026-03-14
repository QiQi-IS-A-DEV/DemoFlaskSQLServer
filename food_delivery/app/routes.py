from flask import render_template, redirect, url_for, request 
from . import db
from .models import Food
from flask import current_app as app

@app.route('/')
def index():
    # Lấy danh sách món ăn từ database
    items = Food.query.all()
    return render_template('index.html', items=items)


# thêm món ăn
@app.route('/add', methods=['GET', 'POST'])
def add_food():
    if request.method == 'POST':
        # Lấy dữ liệu từ form HTML
        name = request.form.get('name')
        price = request.form.get('price')
        description = request.form.get('description')
        image_url = request.form.get('image_url')

        # Tạo đối tượng mới và lưu vào SQL Server
        new_food = Food(name=name, price=price, description=description, image_url=image_url)
        db.session.add(new_food)
        db.session.commit() 
        
        return redirect(url_for('index'))
    
    return render_template('add.html')

# xóa món ăn theo ID
@app.route('/delete/<int:id>')
def delete_food(id):
    food_to_delete = Food.query.get_or_404(id)
    try:
        db.session.delete(food_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return "Có lỗi xảy ra khi xóa món này!"