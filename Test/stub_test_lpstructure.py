from LPStructure.lpstructure import LPStructure


class TestStub:
    def test_sum(self):
        if LPStructure.sum(True, False):
            return True

        pass

    def test_multiplication(self):
        if LPStructure.multiplication(True, False):
            return True
        pass

    def test_implication(self):
        if not LPStructure.implication(True, False):
            return True

    pass
