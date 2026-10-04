import time
from functools import wraps
from typing import Any, Callable


def log(
    function_or_template: Callable[..., Any] | str,
) -> Callable[..., Any]:
    """Выводит время работы функции по стандартному или заданному шаблону."""

    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            started_at = time.perf_counter()
            result = function(*args, **kwargs)
            elapsed_seconds = round(time.perf_counter() - started_at)

            if isinstance(function_or_template, str):
                message = function_or_template.format(elapsed_seconds)
            else:
                message = f"{function.__name__} — {elapsed_seconds}с!"

            print(message)
            return result

        return wrapper

    if callable(function_or_template):
        return decorator(function_or_template)

    return decorator
