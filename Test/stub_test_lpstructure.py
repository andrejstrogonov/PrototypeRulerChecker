from LPStructure.lpstructure import LPStructure


class TestStub:
    def test_sum(self):
        assert LPStructure.sum(True, False) == True
        pass

    def test_multiplication(self):
        assert LPStructure.multiplication(True, False) == True
        pass

    def test_implication(self):
        assert LPStructure.implication(True, False) == False

    pass
