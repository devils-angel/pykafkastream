import os
from flask import Flask
from models import db, Stock

def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Routes
    @app.route('/')
    def hello():
        return 'Hello from Python + Docker!'

    @app.route('/stocks')
    def get_stocks():
        stocks = Stock.query.all()
        return {stock.symbol: stock.last for stock in stocks}

    return app
#T22101998
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
    
