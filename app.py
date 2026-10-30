# Simple Python script with intentional errors for debugging/testing

def calculate_average(numbers):
    total = sum(numbers)
    # Error 1: ZeroDivisionError if list is empty
    return total / len(numbers)

def greet(name):
    # Error 2: TypeError - concatenating None/invalid type or missing conversion
    message = "Hello, " + name
    return message

def main():
    print("Running buggy application...")
    
    # Bug 1: Calling with an empty list triggers ZeroDivisionError
    numbers = []
    print("Calculating average:")
    avg = calculate_average(numbers)
    
    # Bug 2: TypeError (can't concatenate str and float)
    print("Result: " + avg)

if __name__ == "__main__":
    main()
