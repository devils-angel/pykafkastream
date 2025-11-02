import os
from flask import Flask,jsonify
from models import db, Stock
from werkzeug.security import generate_password_hash, check_password_hash

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

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Validate fields
        if not name or not email or not password:
            return jsonify({"error": "Missing fields"}), 400

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "Email already registered"}), 409

        # Hash password and store user
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({"error": "Missing email or password"}), 400

        # Find user
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Verify password
        if not check_password_hash(user.password, password):
            return jsonify({"error": "Invalid credentials"}), 401

        # Success
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        }), 200

            #Simple route to query database
    @app.route('/data')
    def get_stocks():
        stocks = Stock.query.all()
        return jsonify(stocks)
        #return {stock.symbol: stock.last for stock in stocks}

    return app
        #T22101998
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
    
