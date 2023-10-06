class TestParser:
    weight = {1: "normal", 2: "not good"}
    risk = {1: "low_medium", 2: "low"}
    cholester = {1: "low", 2: "medium", 3: "much more"}
nk
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

    @classmethod
    def holstercalc(cls):
        if TestParser.cholester[1] == "low":
            return False
        elif TestParser.cholester[2] == "low":
            return True
        else:
            return 0.5

        pass


pass

if __name__ == '__main__':
    TestParser.calculator()
    TestParser.riskcalc()
