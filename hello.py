# This is a simple greeting module

def greet(name):
    """Print a greeting message."""
    if not name:
        print("Bonjour, anonyme!")
    else:
        print(f"Bonjour, {name}!")

if __name__ == "__main__":
    greet("Git")