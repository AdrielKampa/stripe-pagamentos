import os
from flask import Flask, render_template, jsonify, request
import stripe

# Configurar chaves de API do Stripe a partir de variáveis de ambiente

app = Flask(__name__)

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
