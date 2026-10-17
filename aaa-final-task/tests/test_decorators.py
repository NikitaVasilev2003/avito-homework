from unittest.mock import patch

from decorators import log


def test_log_passes_arguments_and_returns_result() -> None:
    @log
    def make_order(pizza: str, count: int) -> str:
        return f"{count} {pizza}"

    result = make_order("pepperoni", count=2)

    assert result == "2 pepperoni"


def test_log_prints_function_name_and_time() -> None:
    @log
    def bake() -> None:
        pass

    with patch(
        "decorators.time.perf_counter",
        side_effect=(1.0, 3.0),
    ), patch("builtins.print") as mock_print:
        bake()

    mock_print.assert_called_once_with("bake — 2с!")


def test_log_uses_custom_template() -> None:
    @log("Доставили за {}с!")
    def delivery() -> None:
        pass

    with patch(
        "decorators.time.perf_counter",
        side_effect=(1.0, 2.0),
    ), patch("builtins.print") as mock_print:
        delivery()

    mock_print.assert_called_once_with("Доставили за 1с!")
