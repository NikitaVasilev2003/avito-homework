from unittest.mock import patch

from click.testing import CliRunner

from cli import cli
from pizza import Margherita


def test_menu_shows_all_pizzas() -> None:
    result = CliRunner().invoke(cli, ["menu"])

    assert result.exit_code == 0
    assert "Margherita 🧀: tomato sauce, mozzarella, tomatoes" in result.output
    assert "Pepperoni 🍕: tomato sauce, mozzarella, pepperoni" in result.output
    assert (
        "Hawaiian 🍍: tomato sauce, mozzarella, chicken, " "pineapples"
    ) in result.output


def test_order_with_delivery() -> None:
    with patch("cli.bake") as bake, patch("cli.delivery") as delivery:
        result = CliRunner().invoke(cli, ["order", "margherita", "--delivery"])

    assert result.exit_code == 0
    bake.assert_called_once_with(Margherita())
    delivery.assert_called_once_with(Margherita())


def test_order_with_pickup() -> None:
    with patch("cli.bake") as bake, patch("cli.pickup") as pickup:
        result = CliRunner().invoke(cli, ["order", "margherita"])

    assert result.exit_code == 0
    bake.assert_called_once_with(Margherita())
    pickup.assert_called_once_with(Margherita())


def test_order_with_unknown_pizza() -> None:
    result = CliRunner().invoke(cli, ["order", "unknown"])

    assert result.exit_code != 0
    assert "Invalid value" in result.output
