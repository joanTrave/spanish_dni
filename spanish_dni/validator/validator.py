import re

from spanish_dni.constants import REGEXP
from spanish_dni.control_digit import get_control_digit
from spanish_dni.dni import DNI
from spanish_dni.validator.exceptions import NotValidDNIException


def validate_dni(dni: str) -> DNI:
    """
    :param dni: raw string with DNI to validate
    :return: DNI object of validated data
    :raises: NotValidDNIException
    """
    dni: str = dni.upper()
    if not re.match(REGEXP, dni):
        raise NotValidDNIException
    dig_control: str = dni[8]
    if not get_control_digit(dni) == dig_control:
        raise NotValidDNIException
    return DNI(number=dni, control_digit=dig_control)
