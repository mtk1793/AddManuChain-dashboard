import json
from datetime import datetime, timedelta

# Generate 100 example messages
messages = []
start_time = datetime(2024, 1, 1, 12, 0)

for i in range(100):
    message = {
        "id": i + 1,
        "sender": "User" + str((i % 10) + 1),
        "message": f"This is message {i + 1}",
        "timestamp": (start_time + timedelta(minutes=i)).isoformat() + "Z",
    }
    messages.append(message)

# Write to a JSON file
with open("./data/telegram_messages.json", "w") as file:
    json.dump(messages, file, indent=4)
