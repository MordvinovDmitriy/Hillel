#!/usr/bin/python3

class Calc(object):
    def __init__(self, first_n, second_n):
        self.first_n = first_n
        self.second_n = second_n

    def add_n(self):
        try:
            return self.first_n + self.second_n
        except Exception as err:
            print(err)

    def sub_n(self):
        try:
            return self.first_n - self.second_n
        except Exception as err:
            print(err)

    def mult_n(self):
        try:
            return self.first_n * self.second_n
        except Exception as err:
            print(err)

    def div_n(self):
        try:
            self.first_n / self.second_n
        except ZeroDivisionError:
            return 'Cannot divide by zero'
        except Exception as err:
            print(err)
        else:
            return self.first_n / self.second_n

    def exp_n(self):
        try:

            if self.second_n < 0:
                raise Neg_exp
            else:
                return self.first_n ** self.second_n
        except Exception as err:
            print(err)

    def root_n(self):
        try:
            return self.first_n ** 0.5
        except Exception as err:
            print(err)


class Neg_exp(Exception):
    def __init__(self, message='the second operand must not be a negative number'):
        super().__init__(message)


a = 2
b = -2
print(f'a+b: {Calc(a, b).add_n()}')
print(f'a-b: {Calc(a, b).sub_n()}')
print(f'a*b: {Calc(a, b).mult_n()}')
print(f'a/b: {Calc(a, b).div_n()}')
print(f'a ** b: {Calc(a, b).exp_n()}')
print(f'a ** 0.5: {Calc(a, b).root_n()}')
