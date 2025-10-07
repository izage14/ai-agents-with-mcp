import argparse

def greet_user(username):
    """Function to greet the user."""
    message = f"Bună ziua, {username}"
    print(message)
    return message
    
def log_message(message):
    """Logs the message into the log file inside project folder."""
    import os
    from datetime import datetime

    # Log folder inside project
    log_dir = r"C:\Users\Izabela\Desktop\HW\log\ai-agents-with-mcp"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "message.log")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} - {message}\n")



def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Un program CLI care saluta utilizatorul si logheaza fiecare rulare.")
    
    # Add the --user argument
    parser.add_argument("--user", required=True, help="Numele utilizatorului")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Greet the user
    message = greet_user(args.user)
    
    # Log the message
    log_message(message)

if __name__ == "__main__":
    main()
