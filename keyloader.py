# send_to_firebase.py
import os
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timezone
datetime.now(timezone.utc)




# --- CONFIG: change these or set environment variables ---
KEY_PATH = os.environ.get("FIREBASE_KEY_PATH", "firebase-key.json")
DB_URL  = os.environ.get("FIREBASE_DB_URL", "https://keylogger-v1-default-rtdb.firebaseio.com/k/")

# --- Initialize Firebase Admin SDK ---
if not os.path.isfile(KEY_PATH):
    raise FileNotFoundError(f"Service account key not found at: {KEY_PATH}")

cred = credentials.Certificate(KEY_PATH)
firebase_admin.initialize_app(cred, {'databaseURL': DB_URL})

# Reference (node) where typing entries will be stored
ref = db.reference('typing_log')   # will create /typing_log in your DB

def main():
    print("Type text and press Enter to save it to Firebase.")
    print("Type 'exit' or 'quit' to stop.")
    while True:
        user_input = input("> ")
        if user_input.strip().lower() in ('exit', 'quit'):
            print("Goodbye.")
            break

        entry = {
            "text_input": user_input,
            "timestamp_utc": datetime.now(timezone.utc).isoformat()
        }

        # push to Firebase (each push creates a unique key)
        try:
            ref.push(entry)
            print("Saved ✅")
        except Exception as e:
            print("Failed to save:", e)

if __name__ == "__main__":
    main()
