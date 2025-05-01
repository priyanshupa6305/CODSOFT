def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2 if n2 != 0 else "Error: Division by zero is not allowed"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    while True:
        print("\n===== Calculator =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("======================")

        sel = input("Select operation (1-5): ").strip()

        if sel == "5":
            print("Exiting the calculator. Goodbye!")
            break
        elif sel in {"1", "2", "3", "4"}:
            n1 = get_number("Enter first number: ")
            n2 = get_number("Enter second number: ")

            operations = {"1": add, "2": sub, "3": mul, "4": div}
            symbols = {"1": "+", "2": "-", "3": "*", "4": "/"}

            result = operations[sel](n1, n2)
            print(f"{n1} {symbols[sel]} {n2} = {result}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

