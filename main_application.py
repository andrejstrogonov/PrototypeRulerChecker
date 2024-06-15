import sys

class TestParser:
    weight = {1: "normal", 2: "not good"}
    risk = {1: "low_medium", 2: "low"}
    cholester = {1: "low", 2: "medium", 3: "much more"}
    start = {1: "True", 2: "False"}

    @staticmethod
    def calculator():
        if TestParser.weight[1] == "normal":
            return True
        else:
            return False

    @staticmethod
    def riskcalc():
        if TestParser.risk[1] == "low_medium":
            return True
        else:
            return False

    @classmethod
    def holstercalc(cls):
        if TestParser.cholester[1] == "low":
            return False
        elif TestParser.cholester[2] == "low":
            return True
        else:
            return 0.5

    @classmethod
    def startcalc(cls):
        if TestParser.start[1] == "True":
            return True
        elif TestParser.start[2] == "False":
            return False
        else:
            return "not correct"


if __name__ == '__main__':
    TestParser.calculator()
    TestParser.riskcalc()
    TestParser.startcalc()
