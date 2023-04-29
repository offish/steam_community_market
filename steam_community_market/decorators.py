from .currencies import SteamCurrency, SteamLegacyCurrency
from .enums import AppID, SteamLanguage
from .exceptions import (
    InvalidCurrencyException,
    InvalidLanguageException,
    LegacyCurrencyException,
)

from functools import wraps
from inspect import signature
from typing import Any, Callable, Optional, Union, get_args, get_origin


def _sanitize_app_id_value(
    value: Union[AppID, int, list[Union[AppID, int]]]
) -> Union[int, list[int]]:
    return [int(item) for item in value] if isinstance(value, list) else int(value)


def _sanitize_currency_value(
    value: Optional[Union[SteamCurrency, SteamLegacyCurrency, int, str]]
) -> SteamCurrency:
    if isinstance(value, (SteamCurrency, SteamLegacyCurrency)):
        if isinstance(value, SteamLegacyCurrency):
            raise LegacyCurrencyException(value)

        return value

    if isinstance(value, str):
        value = value.upper()

    try:
        if isinstance(value, int):
            value = SteamCurrency(value)

        elif value in SteamLegacyCurrency:
            raise LegacyCurrencyException(value)

        else:
            value = SteamCurrency[value]

    except KeyError as e:
        raise InvalidCurrencyException(value) from e

    return value


def _sanitize_items_dict(
    value: dict[Union[AppID, int], list[str]]
) -> dict[int, list[str]]:
    return {int(app_id): list(items) for app_id, items in value.items()}


def _sanitize_language_value(
    value: Optional[Union[SteamLanguage, str]]
) -> SteamLanguage:
    if isinstance(value, SteamLanguage):
        return value

    lanuage = SteamLanguage.from_string(value)
    if lanuage is None:
        raise InvalidLanguageException(value)

    return lanuage


def _sanitize_market_hash_name_value(value: str) -> str:
    return value.replace("/", "-")


_sanitize_funcs = {
    "app_id": _sanitize_app_id_value,
    "currency": _sanitize_currency_value,
    "items_dict": _sanitize_items_dict,
    "language": _sanitize_language_value,
    "market_hash_name": _sanitize_market_hash_name_value,
}


def _sanitize_value(value: Any, param_name: str) -> Any:
    sanitize_func = _sanitize_funcs.get(param_name)
    return sanitize_func(value) if sanitize_func is not None else value


def _typecheck_dict_value(value: dict, expected_type_args: tuple[Any, ...]) -> bool:
    return all(
        _typecheck_value(k, expected_type_args[0])
        and _typecheck_value(v, expected_type_args[1])
        for k, v in value.items()
    )


def _typecheck_list_value(value: list, expected_type_args: tuple[Any, ...]) -> bool:
    return all(_typecheck_value(x, expected_type_args[0]) for x in value)


def _typecheck_set_value(value: set, expected_type_args: tuple[Any, ...]) -> bool:
    return all(_typecheck_value(x, expected_type_args[0]) for x in value)


def _typecheck_tuple_value(value: tuple, expected_type_args: tuple[Any, ...]) -> bool:
    return all(_typecheck_value(x, t) for x, t in zip(value, expected_type_args))


_typecheck_funcs = {
    dict: _typecheck_dict_value,
    list: _typecheck_list_value,
    set: _typecheck_set_value,
    tuple: _typecheck_tuple_value,
}


def _typecheck_value(value: Any, expected_type: Any) -> bool:
    origin = get_origin(expected_type)
    args = get_args(expected_type)

    if origin is None:
        return isinstance(value, expected_type)

    if origin is Union:
        return any(_typecheck_value(value, arg) for arg in args)

    if check_func := _typecheck_funcs.get(origin):
        return check_func(value, args)

    return False


def sanitized(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to sanitize arguments before passing them to a function.

    :param sanitize_args: The names of the arguments to sanitize, if not specified all known arguments will be sanitized.
    :type sanitize_args: str
    :return: The decorator function.
    :rtype: Callable[..., Any]

    .. versionadded:: 1.3.0
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = signature(func)
        param_names = list(sig.parameters.keys())
        sanitize_param_names = list(_sanitize_funcs.keys())

        args_list = list(args)

        for i, arg in enumerate(args_list):
            arg_name = param_names[i]
            if arg_name in sanitize_param_names:
                args_list[i] = _sanitize_value(arg, arg_name)

        for kwarg_name, kwarg_value in kwargs.items():
            if kwarg_name in sanitize_param_names:
                kwargs[kwarg_name] = _sanitize_value(kwarg_value, kwarg_name)

        return func(*tuple(args_list), **kwargs)

    return wrapper


def typechecked(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to typecheck arguments before passing them to a function.

    :param func: The function to decorate.
    :type func: Callable[..., Any]
    :return: The decorated function.
    :rtype: Callable[..., Any]

    .. versionadded:: 1.3.0
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        sig = signature(func)
        param_names = list(sig.parameters.keys())

        for i, arg in enumerate(args):
            arg_name = param_names[i]
            if arg_name in annotations and not _typecheck_value(
                arg, annotations[arg_name]
            ):
                raise TypeError(
                    f"Expected argument '{arg_name}' to be of type '{annotations[arg_name]}', not '{type(arg).__name__}'."
                )

        for kwarg_name, kwarg_value in kwargs.items():
            if kwarg_name in annotations and not _typecheck_value(
                kwarg_value, annotations[kwarg_name]
            ):
                raise TypeError(
                    f"Expected argument '{kwarg_name}' to be of type '{annotations[kwarg_name]}', not '{type(kwarg_value).__name__}'."
                )

        return func(*args, **kwargs)

    return wrapper
