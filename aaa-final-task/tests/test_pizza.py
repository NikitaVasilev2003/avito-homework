from pizza import Hawaiian, Margherita, Pepperoni, PizzaSize


def test_pizza_recipes() -> None:
    assert Margherita().ingredients == (
        "tomato sauce",
        "mozzarella",
        "tomatoes",
    )
    assert Pepperoni().ingredients == (
        "tomato sauce",
        "mozzarella",
        "pepperoni",
    )
    assert Hawaiian().ingredients == (
        "tomato sauce",
        "mozzarella",
        "chicken",
        "pineapples",
    )


def test_pizza_sizes() -> None:
    assert Margherita().size == PizzaSize.L
    assert Margherita(PizzaSize.XL).size == PizzaSize.XL


def test_pizza_dict() -> None:
    assert Pepperoni().dict() == {
        "name": "Pepperoni",
        "icon": "🍕",
        "size": "L",
        "ingredients": ["tomato sauce", "mozzarella", "pepperoni"],
    }


def test_pizza_equality() -> None:
    assert Margherita() == Margherita()
    assert Margherita() != Pepperoni()
    assert Margherita(PizzaSize.L) != Margherita(PizzaSize.XL)
