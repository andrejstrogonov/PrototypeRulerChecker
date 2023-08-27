from email.parser import Parser

testdata = "if age>5 then good"


class TestParser:
    @staticmethod
    def parser(testdata):
        parser = Parser()
        parser.parse(testdata)
        return "good"

    pass


if __name__ == '__main__':
    TestParser.parser()
