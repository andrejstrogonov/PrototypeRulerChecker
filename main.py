class TestParser:
    weight = {1: "normal", 2: "not good"}

    @staticmethod
    def calculator(weight):
        if TestParser.weight[1] == "normal":
            return True
        else:
            return False
        pass


pass

if __name__ == '__main__':
    TestParser.calculator(TestParser.weight[1])
