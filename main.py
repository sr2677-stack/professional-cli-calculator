from app.calculator.calculator import Calculator

def main():
    calculator = Calculator()

    print("Welcome to Professional CLI Calculator")
    print("Type: add 4 5")
    print("Type 'help' for commands")
    print("Type 'exit' to quit")

    while True:
        user_input = input(">>> ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        if user_input == "help":
            print("Operations: add, subtract, multiply, divide")
            print("Commands: help, history, exit")
            continue

        if user_input == "history":
            for entry in calculator.get_history():
                print(entry)
            continue

        try:
            operation, a, b = user_input.split()
            a = float(a)
            b = float(b)

            result = calculator.calculate(a, b, operation)
            print("Result:", result)

        except ValueError:
            print("Invalid input format. Example: add 4 5")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except Exception:
            print("Unexpected error occurred.")


if __name__ == "__main__":
    main()