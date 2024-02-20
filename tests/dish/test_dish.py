from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish = Dish('Pizza', 49.90)
    dish2 = Dish('Pizza', 49.90)
    dish3 = Dish('Hamburger', 23.90)
    assert dish.name == 'Pizza'
    assert dish.__hash__() == dish2.__hash__()
    assert dish.__hash__() != dish3.__hash__()
    assert dish == dish2
    assert dish != dish3
    assert dish.__repr__() == "Dish('Pizza', R$49.90)"
    assert dish.get_restrictions() == set()
    dish.add_ingredient_dependency('presunto', 6)
    assert dish.get_ingredients() == {'presunto'}
    with pytest.raises(TypeError):
        Dish('Pizza', '49.90')
    with pytest.raises(ValueError):
        Dish('Pizza', 0)

