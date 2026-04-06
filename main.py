import greet  # importing greet.py

def main():
    print("main.py: Now I'm running under main()...")
    name = input("Enter your name (press Enter for default): ")
    if not name:
        name = "World"
    greet.say_hello(name)

# Uncommenting the following line will cause main to run twice when external.py imports main.py, which is not desirable.
# main()

# Uncommenting the following block to create safe guard so that main() only runs when main.py is executed directly, and not when imported.
if __name__ == "__main__":
    print("main.py: This block runs only when main.py is executed directly.")
    main()