class LPStructure:
    @staticmethod
    def sum(a=True, b=False):
        return a or b

    @staticmethod
    def multiplication(a=True, b=False):
        return a and b

    @staticmethod
    def implication(a=True, b=False):
        return not a or b

    @staticmethod
    def print_method():
        print(LPStructure.sum())
        print(LPStructure.multiplication())
        print(LPStructure.implication())



if __name__ == '__main__':
    LPStructure.print_method()
