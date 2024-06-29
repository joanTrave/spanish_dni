from spanish_dni.constants import CONTROL_DIGIT, DNITypes, NIE_FIRST_DIGITS
from spanish_dni.dni import DNI


def normalize_nie(dni: str) -> str:
    """
    :param dni: Validated DNI format
    :return: NIE normalized in NIF format
    """
    if DNI.get_dni_type(dni) == DNITypes.NIE:
        dni = NIE_FIRST_DIGITS[dni[0]] + dni[1:]
    return dni


def get_control_digit(dni: str) -> str:
    """
    Get control digit from dni with validated format
    :param dni: DNI (NIF or NIE) with validated format
    :return: its control_digit
    """
    dni_number: str = dni[:8]
    normalized_dni: str = normalize_nie(dni_number)
    return CONTROL_DIGIT[int(normalized_dni) % 23]
