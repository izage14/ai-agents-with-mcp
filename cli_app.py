import argparse

def greet_user(username):
    """
    Function to greet the user.
    Args:
        username: user to greet
    """
    message = f"Bună ziua, {username}"
    print(message)
    return message

def log_message(message):
    """
    Logs the message into the log file inside project folder.
    Args:
        message: Can log the message
    """
    import os
    from datetime import datetime

    # Log folder inside project
    ## Read about format strings.
    ## You can use like this:
    ### 1. app_name = "ai-agents-with-mcp"
    ### 2. log_dir = os.path.join(os.path.expanduser("~"), "log", app_name)
    #### os.path.expanduser("~") is a special symbol, known as tilde and it will
    #### Expands ~ to the current user’s home directory.
    #### on Linux/macOS → /home/username
    #### on Windows → C:\Users\username
    log_dir = r"C:\Users\Izabela\Desktop\HW\log\ai-agents-with-mcp" # can be replaced with line with 1 and 2, so that it can across any machine.
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "message.log")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} - {message}\n")



def main():
    ## Very good to use the ArgumentParser library. Good work.
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Un program CLI care saluta utilizatorul si logheaza fiecare rulare.")

    # Add the --user argument
    parser.add_argument("--user", required=True, help="Numele utilizatorului")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Greet the user
    message = greet_user(args.user)

    # Log the message to file
    ## Very helpful website, for quick examples: https://pymotw.com/3/
    ## Great work with logging the message to file, we will use the logging library
    ## as it comes with default options, like to create logs based on level,
    ## It will be nice to have logs with logging level, so that we can have
    ## information for warning, failure, critical. info and debug messages will
    ## be used for development purpose.
    ## https://pymotw.com/3/logging/index.html
    log_message(message)

if __name__ == "__main__":
    ## We did this, because we want to run the main with parent process only,
    ## not the spawned child processes
    main()
