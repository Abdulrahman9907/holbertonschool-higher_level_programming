from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_file():
    products = []
    try:
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
    except (FileNotFoundError, ValueError):
        return []
    return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)

@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error_message="Wrong source")

    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()

    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html', error_message="Product not found")
            products = filtered_products
        except ValueError:
            return render_template('product_display.html', error_message="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)