class Calc:
    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

if __name__ == '__main__':
    calc = Calc()
    result = calc.add(1, 3)
    print(result)
