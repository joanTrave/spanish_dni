import random as rd

from spanish_dni.constants import NIE_FIRST_DIGITS
from spanish_dni.generator.exceptions import (
    NotValidFirstDNICharactersException,
    IncompatibleParametersDNIGeneratorException,
)
from spanish_dni.control_digit import get_control_digit
from spanish_dni.dni import DNI


def _validate_first_characters(first_characters: str = "") -> None:
    if not len(first_characters):
        return
    if len(first_characters) > 8 or not first_characters.isdigit():
        raise NotValidFirstDNICharactersException


def _generate_number(first_characters: str = "") -> str:
    _validate_first_characters(first_characters)
    dni_str: str = first_characters[:]
    for _ in range(8 - len(first_characters)):
        dni_str += str(rd.randint(0, 9))
    return dni_str


def _compute_control_digit(dni_str: str) -> str:
    return get_control_digit(dni_str)


def _map_dni_to_nie(dni_str: str) -> str:
    eligible_nie_characters: list[str] = list(NIE_FIRST_DIGITS.keys())
    return rd.choice(eligible_nie_characters) + dni_str[1:]


def generate_dni(is_nie: bool = False, first_characters: str = "") -> str:
    """
    Generates one random DNI/NIE taking as first characters those informed by parameter.

    :param is_nie: If True, generates NIE
    :param first_characters: First characters to take as a reference
    :return: String containing new DNI
    """
    if len(first_characters) and is_nie:
        raise IncompatibleParametersDNIGeneratorException("Cannot assign first characters using NIE mode")
    dni_str: str = _generate_number(first_characters)
    if is_nie:
        dni_str = _map_dni_to_nie(dni_str)
    control_digit: str = _compute_control_digit(dni_str)
    return str(DNI(number=dni_str, control_digit=control_digit))
