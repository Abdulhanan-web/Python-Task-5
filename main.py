from email_service import send_email
from contact_loader import load_csv, load_json
from template_manager import load_template, personalize
from history_manager import save_history, view_history
from utils import retry_send, is_valid_email
from getpass import getpass
import time
from utils import is_valid_email, retry_send
from email_service import send_email
from history_manager import save_history
from template_manager import personalize

contacts = []
template = ""

def load_contacts():
    global contacts
    path = input("Enter file path: ")

    if path.endswith(".csv"):
        contacts = load_csv(path)
    elif path.endswith(".json"):
        contacts = load_json(path)
    else:
        print("Unsupported format!")
        return

    print(f"{len(contacts)} contacts loaded.")


def choose_template():
    global template
    name = input("Enter template name: ")
    template = load_template(name)

    if template:
        print("Template loaded.")


def send_bulk():
    global contacts, template

    if not contacts:
        print("❌ Load contacts first!")
        return

    if not template:
        print("❌ Choose template first!")
        return

    sender = input("Enter your email: ")
    password = getpass("Enter app password: ")  # 🔒 hidden

    subject = input("Enter subject: ")

    # ✅ Multi-line message input
    print("\nEnter your message (type END to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    user_message = "\n".join(lines)

    attachment = input("Attachment path (optional): ").strip()

    for user in contacts:
        email = user.get("email", "").lower()

        if not is_valid_email(email):
            print(f"⚠️ Invalid email skipped: {email}")
            continue

        # ✅ Personalize template with message
        body = personalize(template, user, user_message)

        def attempt():
            return send_email(
                sender,
                password,
                email,
                subject,
                body,
                is_html=True,
                attachment_path=attachment if attachment else None
            )

        success, msg = retry_send(attempt)

        status = "Sent" if success else "Failed"
        save_history(email, subject, status)

        print(f"{email} → {status}")

        time.sleep(1)  # avoid spam detection


def main():
    while True:
        print("\n==== MENU ====")
        print("1. Load Contacts")
        print("2. Choose Template")
        print("3. Send Email")
        print("4. View History")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            load_contacts()
        elif choice == "2":
            choose_template()
        elif choice == "3":
            send_bulk()
        elif choice == "4":
            view_history()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()