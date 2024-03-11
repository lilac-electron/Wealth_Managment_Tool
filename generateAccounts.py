import json
import random
from datetime import datetime, timedelta

# Function to generate random UK postal codes
def generate_postcode():
    letters = [chr(random.randint(65, 90)) for _ in range(2)]
    numbers = [str(random.randint(0, 9)) for _ in range(2)]
    return ''.join(letters) + ''.join(numbers) + ' ' + ''.join([str(random.randint(0, 9)) for _ in range(1)])

# Function to generate random transactions
def generate_transactions():
    transactions = []
    current_date = datetime(2024, 1, 1)
    total = 1000 # start with £1000 in the bank
    time_since_bills = 0
    bills_util_next = False
    for _ in range(300):
        transaction_date = current_date.strftime('%Y-%m-%d')
        amount = round(random.uniform(-120, 0), 2)
        total += amount
        print(amount)
        if time_since_bills >= 28:
            total -= amount
            amount = 2500
            total += amount
            description = "Salary Deposit"
            category = "Income"
            time_since_bills = 0
            bills_util_next = True

        elif amount < 0:
            description = random.choice(["Groceries", "Transportation", "Shopping", "Food & Drink", "Dining Out", "Bills & Utilities", "Entertainment"])
            if bills_util_next:
                total -= amount
                amount = -550
                total += amount
                bills_util_next = False
                description = "Monthly Bills & Utilities"
            category = description

        time_since_bills += 1
        merchant = {
            "address": {
                "address": str(random.randint(1, 100)) + " " + random.choice(["High Street", "Main Street", "Elm Street", "Park Avenue", "Station Road"]),
                "city": "London",
                "country": "GB",
                "latitude": round(random.uniform(51.45, 51.55), 4),
                "longitude": round(random.uniform(-0.25, 0.1), 4),
                "postcode": generate_postcode(),
                "region": "Greater London"
            },
            "created": "2010-01-01T00:00:00Z",
            "group_id": "grp_00008zIcpbBOaAr7TTP3sv",
            "id": "merch_" + ''.join([random.choice("0123456789abcdef") for _ in range(22)]),
            "logo": "https://example.com/merchant_logo.jpg",
            "emoji": random.choice(["🛒", "⛽", "📦", "☕️", "🍗", "🏪", "🎥", "🥪", "👗", "🚗", "🍔"]),
            "name": random.choice(["Tesco", "BP", "Amazon", "Starbucks", "Nando's", "Cinema", "Subway", "H&M", "Uber", "McDonald's"]),
            "category": random.choice(["grocery_store", "fuel_station", "online_retail", "coffee_shop", "restaurant", "entertainment", "fashion_store", "transportation"])
        }
        transactions.append({
            "transaction_id": "txn" + str(_ + 1).zfill(3),
            "date": transaction_date,
            "amount": amount,
            "description": description,
            "category": category,
            "merchant": merchant,
            "balance": round(total, 2)  # Running balance
        })
        current_date += timedelta(days=random.randint(1, 5))
    return transactions

# Generate transactions
data = {
    "account": {
        "account_number": "12345678",
        "sort_code": "12-34-56",
        "balance": 2500.00,
        "currency": "GBP",
        "account_holder": "John Doe"
    },
    "transactions": generate_transactions()
}

# Save to JSON file
with open('SimulatedFinanceData/current_account_transactions.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON file generated successfully.")
