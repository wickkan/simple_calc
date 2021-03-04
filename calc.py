
"""
A simple calculator that can add, subtract, divide and multiply.
"""

import webbrowser

url = 'https://github.com/wickkan'

class Calc:

    def __init__(self):
        self.int1 = None
        self.int2 = None
        self.op = None
        self.menu = None
        self.prev_cal = None
        self.res = 0

    def add(self, int1, int2) -> int:
        """
        Adds two integers
        """
        assert type(int1) == int and type(int2) == int, "Arguments should be integers"
        self.res += int1 + int2
        return self.res

    def subtract(self, int1, int2) -> int:
        """
        Subtracts two integers
        """
        assert type(int1) == int and type(int2) == int, "Arguments should be integers"
        self.res += int1 - int2
        return self.res

    def multiply(self, int1, int2) -> int:
        """
        Multiplies two integers
        """
        assert type(int1) == int and type(int2) == int, "Arguments should be integers"
        self.res += int1 * int2
        return self.res

    def divide(self, int1, int2) -> int:
        """
        Divides two integers
        """
        assert type(int1) == int and type(int2) == int, "Arguments should be integers"
        assert int2 != 0, "Denominator cannot be negative"
        self.res += int1/int2
        return self.res

    def calc_interface(self):
        """
        The calculator interface
        """
        print("----- CALCULATOR -----")
        print("1. Calculate\n2. Continue\n3. Exit")

        while self.menu is None:
            try:
                self.menu = int(input("Enter option: "))
                if self.menu == 2 and (self.int1 is None or self.int2 is None):
                    print("ERROR: No previous calculations")
                    self.menu = None
            except ValueError:
                print("ERROR: Please provide proper input")

            if self.menu == 1:  # If user wants to calculate
                while self.int1 is None:
                    try:
                        self.int1 = int(input("Enter first integer: "))
                    except ValueError:
                        print("Only integers are permitted!")

                while self.int2 is None:
                    try:
                        self.int2 = int(input("Enter second integer: "))
                    except ValueError:
                        print("Only integers are permitted!")

                while self.op is None:
                    print("Note: Add = '+', Subtract = '-', Multiply = '*', Divide = '/'")
                    self.op = str(input("Enter operation: "))
                    if self.op != '+' and self.op != '-' and self.op != '*' and self.op != '/':
                        print("Only permitted operations allowed")
                        self.op = None
                    elif self.op == '+':
                        print('----------------------')
                        print("Result =", self.add(self.int1, self.int2))
                        self.res = 0
                        self.menu = None
                        print("----- CALCULATOR -----")
                        print("1. Calculate\n2. Continue\n3. Exit")
                    elif self.op == '-':
                        print('----------------------')
                        print("Result =", self.subtract(self.int1, self.int2))
                        self.res = 0
                        self.menu = None
                        print("----- CALCULATOR -----")
                        print("1. Calculate\n2. Continue\n3. Exit")
                    elif self.op == '*':
                        print('----------------------')
                        print("Result =", self.multiply(self.int1, self.int2))
                        self.res = 0
                        self.menu = None
                        print("----- CALCULATOR -----")
                        print("1. Calculate\n2. Continue\n3. Exit")
                    elif self.op == '/':
                        if self.int2 == 0:
                            print("0 will result in an invalid integer. Please select another integer.")
                            self.int2 = None
                            while self.int2 is None:
                                try:
                                    self.int2 = int(input("Enter second integer: "))
                                except ValueError:
                                    print("Only integers are permitted!")
                        print('----------------------')
                        print("Result =", self.divide(self.int1, self.int2))
                        self.res = 0
                        self.menu = None
                        print("----- CALCULATOR -----")
                        print("1. Calculate\n2. Continue\n3. Exit")
            elif self.menu == 2:    # If users want to keep using the calculator
                self.int1 = None
                self.int2 = None
                self.op = None
                while self.int1 is None:
                    try:
                        self.int1 = int(input("Enter first integer: "))
                    except ValueError:
                        print("Only integers are permitted!")

                while self.int2 is None:
                    try:
                        self.int2 = int(input("Enter second integer: "))
                    except ValueError:
                        print("Only integers are permitted!")

                while self.op is None:
                    print("Note: Add = '+', Subtract = '-', Multiply = '*', Divide = '/'")
                    self.op = str(input("Enter operation: "))
                    if self.op != '+' and self.op != '-' and self.op != '*' and self.op != '/':
                        print("Only permitted operations allowed")
                        self.op = None
                    elif self.op == '+':
                        print('----------------------')
                        print("Result =", self.add(self.int1, self.int2))
                        self.res = 0
                        self.menu = None
                        print("----- CALCULATOR -----")
                        print("1. Calculate\n2. Continue\n3. Exit")
                    elif self.op == '-':
                        print('----------------------')
                        print("Result =", self.subtract(self.int1, self.int2))
                        self.res = 0
                        self.menu = None
                        print("----- CALCULATOR -----")
                        print("1. Calculate\n2. Continue\n3. Exit")
                    elif self.op == '*':
                        print('----------------------')
                        print("Result =", self.multiply(self.int1, self.int2))
                        self.res = 0
                        self.menu = None
                        print("----- CALCULATOR -----")
                        print("1. Calculate\n2. Continue\n3. Exit")
                    elif self.op == '/':
                        if self.int2 == 0:
                            print("0 will result in an invalid integer. Please select another integer.")
                            self.int2 = None
                            while self.int2 is None:
                                try:
                                    self.int2 = int(input("Enter second integer: "))
                                except ValueError:
                                    print("Only integers are permitted!")
                        print('----------------------')
                        print("Result =", self.divide(self.int1, self.int2))
                        self.res = 0
                        self.menu = None
                        print("----- CALCULATOR -----")
                        print("1. Calculate\n2. Continue\n3. Exit")

            elif self.menu == 3:  # If users want to exit the program
                print(
                    '*****------------------------------------------*****\n''Thanks for trying: Simple Calculator\n''Click the link to check out more of my projects:\n',url)
                print('*****------------------------------------------*****')


if __name__ == '__main__':
    Calc().calc_interface()
