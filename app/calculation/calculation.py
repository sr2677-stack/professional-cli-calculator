from app.operation.operations import Operations

class Calculation:

    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        return self.operation(self.a, self.b)


class CalculationFactory:

    @staticmethod
    def create_calculation(a, b, operation_name):
        operations = {
            "add": Operations.add,
            "subtract": Operations.subtract,
            "multiply": Operations.multiply,
            "divide": Operations.divide,
        }

        if operation_name not in operations:
            raise ValueError("Invalid operation")

        return Calculation(a, b, operations[operation_name])