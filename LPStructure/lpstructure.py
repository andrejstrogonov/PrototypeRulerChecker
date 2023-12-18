class LPStructure:
    @staticmethod
    def sum(a=True, b=False):
        return a or b

    pass

    @staticmethod
    def multiplication(a=True, b=False):
        return a and b

    pass

    @staticmethod
    def implication(a=True, b=False):
        return not a or b

    pass

    @staticmethod
    def print_method():
        print(LPStructure.sum())
        print(LPStructure.multiplication())
        print(LPStructure.implication())

    pass


if __name__ == '__main__':
    LPStructure.print_method()
