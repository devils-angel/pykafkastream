import json
import time
from kafka import KafkaProducer
from datetime import datetime
import random

# --------------------------
# Configure the Kafka producer
# --------------------------
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    api_version=(2, 5, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# --------------------------
# Stock template
# --------------------------
stock = {
    "symbol": "AMZN",
    "name": "Amazon.com Inc",
    "last": 244.22,
    "change": "+21.36",
    "percent_change": "+9.58%",
    "price_volume": "40,594,100",
    "time": "10/31/25 09:30:00"
}

print("Kafka Producer started. Producing stock updates every minute...")

while True:
    # Generate a random price_volume (between 1 million and 50 million)
    random_volume = random.randint(1_000_000, 50_000_000)
    stock["price_volume"] = f"{random_volume:,}"

    # Update timestamp
    stock["time"] = datetime.now().strftime("%m/%d/%y %H:%M:%S")

    # Send to Kafka
    producer.send("stock_updates", stock)
    producer.flush()  # ensure it’s sent immediately
    print(f" Produced stock update: {stock}")

    # Wait 1 minute
    time.sleep(1)
