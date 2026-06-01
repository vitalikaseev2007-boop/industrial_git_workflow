# This is a simple greeting module

def greet(name):
    """Print a greeting message."""
    if not name:
        print("Hello, anonymous!")   # fallback for empty name
    else:
        print(f"Bonjour, {name}!")
        print(f"Hola, {name}!")

if __name__ == "__main__":
    greet("Git")