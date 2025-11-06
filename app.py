import os
import threading
from flask import Flask, jsonify, request
from models import db, Stock, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from kafka import KafkaConsumer

def consume_stock_updates(app):
    """Kafka consumer thread that updates database with new stock data."""
    consumer = KafkaConsumer(
        "stock_updates",
        bootstrap_servers=["kafka:9092"],  # or "localhost:9092" if running locally
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="stock-group",
        api_version=(2, 5, 0)
    )

    with app.app_context():
        print("Kafka consumer started and listening for stock updates...")
        for message in consumer:
            data = message.value
            print(f"Consumed from Kafka: {data}")

            # Update or insert stock
            stock = Stock.query.filter_by(symbol=data["symbol"]).first()
            if stock:
                stock.price_volume = data["price_volume"]
                stock.time = data["time"]
            else:
                stock = Stock(
                    symbol=data["symbol"],
                    name=data["name"],
                    last=data["last"],
                    change=data["change"],
                    percent_change=data["percent_change"],
                    price_volume=data["price_volume"],
                    time=data["time"]
                )
                db.session.add(stock)
            db.session.commit()


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
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
        # Serialize SQLAlchemy objects to JSON-safe structure
        result = [
            {
                "id": s.id,
                "symbol": s.symbol,
                "name": s.name,
                "last": s.last,
                "change": s.change,
                "percent_change": s.percent_change,
                "price_volume": s.price_volume,
                "time": s.time.isoformat() if s.time else None,
            }
            for s in stocks
        ]
        return jsonify(result)
        #return {stock.symbol: stock.last for stock in stocks}

    return app
        #T22101998
if __name__ == '__main__':
    app = create_app()

    consumer_thread = threading.Thread(target=consume_stock_updates, args=(app,), daemon=True)
    consumer_thread.start()
    app.run(host='0.0.0.0', port=5000)
    
