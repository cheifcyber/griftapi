from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__, static_folder=os.path.abspath('.'))
CORS(app, resources={r"/*": {"origins": "*"}})

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('larkin.csv')

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('.', path)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = df['LarkinProduct'].unique().tolist()
        return jsonify(products)
    except Exception as e:
        return str(e)

@app.route('/product/<name>', methods=['GET'])
def get_product(name):
    # Filter the DataFrame based on the product name
    name = name.lower().strip()
    product = df[df['LarkinProduct'].str.lower().str.strip() == name]
    if product.empty:
        return jsonify({'error': 'Product not found'}), 404
    else:
        # Check if "Not_sold" is in the comment
        if "Not_sold" in str(product['Comments'].iloc[0]):
            return jsonify(product[['RealProduct', 'RealPrice', 'Comments', 'RealLinks']].iloc[0].to_dict()), 200
        return jsonify(product[['RealProduct', 'RealPrice', 'RealLinks']].iloc[0].to_dict()), 200

@app.route('/link/<name>', methods=['GET'])
def get_link(name):
    # Filter the DataFrame based on the product name
    name = name.lower().strip()
    product = df[df['LarkinProduct'].str.lower().str.strip() == name]
    if product.empty:
        return jsonify({'error': 'Product not found'}), 404
    else:
        # Check if "Not_sold" is in the comment
        if "Not_sold" in str(product['Comments'].iloc[0]):
            return jsonify(product[['RealLinks', 'Comments']].iloc[0].to_dict()), 200
        return jsonify({'RealLinks': product['RealLinks'].iloc[0]}), 200

@app.route('/markup/<name>', methods=['GET'])
def get_markup(name):
    # Filter the DataFrame based on the product name
    name = name.lower().strip()
    product = df[df['LarkinProduct'].str.lower().str.strip() == name]
    if product.empty:
        return jsonify({'error': 'Product not found'}), 404
    else:
        # Calculate the markup
        larkin_price = float(product['LarkinPrice'].iloc[0].replace('$', '').replace(',', ''))
        real_price = product['RealPrice'].iloc[0]
        if "_&_Free" in real_price:
            real_price = real_price.split('_&_Free')[0].replace('$', '')
            real_price = float(real_price) if real_price else 0.0
        else:
            real_price = float(real_price.replace('$', '').replace(',', ''))
        markup = larkin_price - real_price
        percent_markup = (markup / real_price) * 100 if real_price != 0 else 0
        # Check if "Not_sold" is in the comment
        if "Not_sold" in str(product['Comments'].iloc[0]):
            return jsonify({'markup': f'${markup:.2f}', 'percent_markup': f'{percent_markup:.2f}%', 'RealPrice': product['RealPrice'].iloc[0], 'LarkinPrice': product['LarkinPrice'].iloc[0], 'comment': product['Comments'].iloc[0]}), 200
        return jsonify({'markup': f'${markup:.2f}', 'percent_markup': f'{percent_markup:.2f}%', 'RealPrice': product['RealPrice'].iloc[0], 'LarkinPrice': product['LarkinPrice'].iloc[0]}), 200

@app.route('/archive/<name>', methods=['GET'])
def get_archive(name):
    # Filter the DataFrame based on the product name
    name = name.lower().strip()
    product = df[df['LarkinProduct'].str.lower().str.strip() == name]
    if product.empty:
        return jsonify({'error': 'Product not found'}), 404
    else:
        # Check if "Not_sold" is in the comment
        if "Not_sold" in str(product['Comments'].iloc[0]):
            return jsonify({'LarkinArchive': product['LarkinArchive'].iloc[0], 'comment': product['Comments'].iloc[0]}), 200
        return jsonify({'LarkinArchive': product['LarkinArchive'].iloc[0]}), 200

@app.route('/real/<name>', methods=['GET'])
def get_real(name):
    # Filter the DataFrame based on the product name
    name = name.lower().strip()
    product = df[df['LarkinProduct'].str.lower().str.strip() == name]
    if product.empty:
        return jsonify({'error': 'Product not found'}), 404
    else:
        # Check if "Not_sold" is in the comment
        if "Not_sold" in str(product['Comments'].iloc[0]):
            return jsonify({'RealProduct': product['RealProduct'].iloc[0], 'comment': product['Comments'].iloc[0]}), 200
        return jsonify({'RealProduct': product['RealProduct'].iloc[0]}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)