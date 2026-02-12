from app.calculation.calculation import CalculationFactory

class Calculator:

    def __init__(self):
        self.history = []

    def calculate(self, a, b, operation_name):
        calculation = CalculationFactory.create_calculation(a, b, operation_name)
        result = calculation.perform()
        self.history.append((a, b, operation_name, result))
        return result

    def get_history(self):
        return self.history