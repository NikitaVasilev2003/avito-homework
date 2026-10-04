from enum import StrEnum


class PizzaSize(StrEnum):
    """Доступные размеры пиццы."""

    L = "L"
    XL = "XL"


class Pizza:
    """Базовый класс пиццы с рецептом и выбранным размером."""

    name = "Pizza"
    icon = ""
    ingredients: tuple[str, ...] = ()

    def __init__(self, size: PizzaSize = PizzaSize.L) -> None:
        """Создает пиццу выбранного размера."""
        if not isinstance(size, PizzaSize):
            raise ValueError(f"Unsupported pizza size: {size}")

        self.size = size

    def dict(self) -> dict[str, object]:
        """Возврщает описание пиццы в виде словаря."""
        return {
            "name": self.name,
            "icon": self.icon,
            "size": self.size.value,
            "ingredients": list(self.ingredients),
        }

    def __eq__(self, other: object) -> bool:
        """Сравнивает пиццы по виду, размеру и рецепту."""
        if not isinstance(other, Pizza):
            return NotImplemented

        return (
            type(self) is type(other)
            and self.size == other.size
            and self.ingredients == other.ingredients
        )


class Margherita(Pizza):
    """Рецепт пиццы «Маргарита»."""

    name = "Margherita"
    icon = "🧀"
    ingredients = ("tomato sauce", "mozzarella", "tomatoes")


class Pepperoni(Pizza):
    """Рецепт пиццы «Пепперони»."""

    name = "Pepperoni"
    icon = "🍕"
    ingredients = ("tomato sauce", "mozzarella", "pepperoni")


class Hawaiian(Pizza):
    """Рецепт гавайской пиццы."""

    name = "Hawaiian"
    icon = "🍍"
    ingredients = (
        "tomato sauce",
        "mozzarella",
        "chicken",
        "pineapples",
    )
