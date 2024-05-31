from LPStructure.lpstructure import LPStructure


class TestStub:

    def test_sum(self):
        if LPStructure.sum(True, False):
            assert LPStructure.sum(True, False) == True
        pass

    def test_multiplication(self):
        assert LPStructure.sum(True, False) == False

    pass

    def test_implication(self):
        assert LPStructure.sum(True, False) == True

    pass
