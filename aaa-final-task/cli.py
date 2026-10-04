import random
import time

import click

from decorators import log
from pizza import Hawaiian, Margherita, Pepperoni, Pizza

PIZZA_MENU: dict[str, type[Pizza]] = {
    "margherita": Margherita,
    "pepperoni": Pepperoni,
    "hawaiian": Hawaiian,
}


@log("Приготовили за {}с!")
def bake(pizza: Pizza) -> None:
    """Приготавливает пиццу."""
    time.sleep(random.randint(1, 5))


@log("Доставили за {}с!")
def delivery(pizza: Pizza) -> None:
    """Доставляет пиццу курьером."""
    time.sleep(random.randint(1, 5))


@log("Забрали за {}с!")
def pickup(pizza: Pizza) -> None:
    """Передает пиццу клиенту в ресторане."""
    time.sleep(random.randint(1, 5))


@click.group()
def cli() -> None:
    """Управляет заказами пиццерии."""


@cli.command()
def menu() -> None:
    """Показывает доступное меню."""
    for pizza_class in PIZZA_MENU.values():
        pizza = pizza_class()
        ingredients = ", ".join(pizza.ingredients)
        click.echo(f"- {pizza.name} {pizza.icon}: {ingredients}")


@cli.command()
@click.argument(
    "pizza",
    type=click.Choice(tuple(PIZZA_MENU)),
)
@click.option(
    "--delivery",
    "with_delivery",
    is_flag=True,
    help="Доставить заказ курьером.",
)
def order(pizza: str, with_delivery: bool) -> None:
    """Приготавливает заказ и передает его клиенту."""
    pizza_class = PIZZA_MENU[pizza]
    ordered_pizza = pizza_class()

    bake(ordered_pizza)

    if with_delivery:
        delivery(ordered_pizza)
    else:
        pickup(ordered_pizza)


if __name__ == "__main__":
    cli()
