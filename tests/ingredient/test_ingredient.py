from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient('farinha')
    ingredient2 = Ingredient('farinha')
    ingredient3 = Ingredient('carne')
    assert ingredient.name == 'farinha'
    assert ingredient.restrictions == {Restriction.GLUTEN}
    assert ingredient.__hash__() == hash('farinha')
    assert ingredient.__repr__() == "Ingredient('farinha')"
    assert ingredient == ingredient2
    assert ingredient != ingredient3

