class TestParser:
    weight = {1: "normal", 2: "not good"}
    risk = {1: "low_medium", 2: "low"}

    @staticmethod
    def calculator():
        if TestParser.weight[1] == "normal":
            return True
        else:
            return False
        pass

    @staticmethod
    def riskcalc():
        if TestParser.risk[1] == "low_medium":
            return True
        else:
            return False

        pass


pass

if __name__ == '__main__':
    TestParser.calculator()
    TestParser.riskcalc()
