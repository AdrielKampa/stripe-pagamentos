import os
from flask import Flask, render_template
import stripe

# Configurar chaves de API do Stripe a partir de variáveis de ambiente
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', publishable_key=os.getenv('STRIPE_PUBLISHABLE_KEY'))

if __name__ == '__main__':
    app.run(debug=True)
