from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient('farinha')
    ingreTest = {
        'farinha',
        Restriction.GLUTEN
    }
    assert ingredient.name == 'farinha'
    assert ingredient.restrictions == {Restriction.GLUTEN}
    assert ingredient.__hash__() == hash('farinha')
    assert ingredient.__eq__(ingreTest) == True
    assert ingredient.__repr__() == "Ingredient('farinha')"
    ingredient2 = Ingredient('carne')
    assert ingredient2.__eq__(ingreTest) == False

