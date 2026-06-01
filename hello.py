# This is a simple greeting module

def greet(name):
    """Print a greeting message."""
    if not name:
        print("Hello, anonymous!")
    else:
        print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Git")