import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS  # Importe a extensão Flask-CORS
import stripe

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar chaves de API do Stripe a partir de variáveis de ambiente
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

app = Flask(__name__)
# Configurar CORS para permitir todas as origens durante o desenvolvimento
CORS(app)

@app.route('/')
def index():
    return render_template('index.html', publishable_key=os.getenv('STRIPE_PUBLISHABLE_KEY'))

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    item_id = request.form.get('item_id')

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Nome do Produto',
                    },
                    'unit_amount': 2000,  # $20.00 em centavos
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='https://seusite.com/success',
        cancel_url='https://seusite.com/cancel',
    )

    return jsonify({'sessionId': session['id']})

if __name__ == '__main__':
    app.run(debug=True)
