import argparse

def greet_user(username):
    """Function to greet the user."""
    print(f"Bună ziua, {username}")

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser()
    
    # Add the --user argument
    parser.add_argument("--user", required=True)
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the greeting function
    greet_user(args.user)

if __name__ == "__main__":
    main()
