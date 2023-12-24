from functools import reduce

from ActivationFunctions import ActivationFunctions
from lpstructure import LPStructure

facts = [0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1]
weights = [0.23, 0.25, 0.5, 0.75, 0.99, 1.0]
pre_image_1 = (1, 1, 1)
pre_image_2 = (1, 0, 1)
pre_image_3 = (1, 1, 0)
layer_1 = reduce(LPStructure.multiplication, pre_image_1)
print(layer_1)
layer_1_1 = reduce(LPStructure.multiplication, pre_image_2)
print(layer_1_1)
layer_2 = (layer_1, layer_1_1)
print(layer_2)
layer_2_sum = reduce(LPStructure.sum, layer_2)
print(layer_2_sum)

result_impl = reduce(LPStructure.implication, facts)

result_sum = reduce(LPStructure.sum, facts)
print(result_sum)
result_mul = reduce(LPStructure.multiplication, facts)


def activation_function(weights):
    return list(map(lambda x: ActivationFunctions.relu(x) * x, weights))


sort = list(filter(lambda x: x > 0.5, activation_function(weights)))
print(sort)
