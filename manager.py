import os

PASS_FILE = "passwords.txt"

def load_passwords():
    if not os.path.exists(PASS_FILE):
        return []
    with open(PASS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_password(entry):
    with open(PASS_FILE, "a") as f:
        f.write(entry + "\n")

def view_passwords():
    passwords = load_passwords()
    if not passwords:
        print("🔐 No saved passwords.")
    else:
        print("\n🔐 Saved Passwords:")
        for idx, entry in enumerate(passwords, 1):
            print(f"{idx}. {entry}")
    print()

def search_password():
    keyword = input("Enter site or username to search: ").strip().lower()
    found = False
    for line in load_passwords():
        if keyword in line.lower():
            print(f"🔍 Found: {line}")
            found = True
    if not found:
        print("❌ No match found.")
    print()

while True:
    print("🔐 Password Manager")
    print("[1] Add new password")
    print("[2] View all")
    print("[3] Search")
    print("[4] Quit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        site = input("Enter site name: ").strip()
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        entry = f"{site} | {username} | {password}"
        save_password(entry)
        print("✅ Password saved.\n")
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        search_password()
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Pick 1–4.\n")
