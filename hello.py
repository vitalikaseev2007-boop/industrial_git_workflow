# This is a simple greeting module

def greet(name):
    """Print a greeting message."""
    if not name:
        print("Hola, anónimo!")
    else:
        print(f"Hola, {name}!")

if __name__ == "__main__":
    greet("Git")