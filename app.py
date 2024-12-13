from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Налаштування бази даних для Render
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')  # Замість 'default.db' вставити URL вашої БД на Render
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Моделі бази даних
class ProductEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<ProductEntity {self.name}>'

# Основний маршрут API
@app.route('/api/v1/productentitiestool-ui-admin/partner/getAll', methods=['POST'])
def get_all_products():
    products = ProductEntity.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

if __name__ == '__main__':
    app.run(debug=True)
