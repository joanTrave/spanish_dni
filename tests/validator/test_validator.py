import pytest

from spanish_dni.validator.exceptions import NotValidDNIException
from spanish_dni.validator import validate_dni

VALID_NIF: str = "23414538D"
VALID_NIE: str = "Y2853959H"
NOT_VALID_FORMAT_DNI: str = "23418D"
NOT_VALID_FIRST_CHARACTER_NIE: str = "U2853959H"
NOT_VALID_NIF_CONTROL_DIGIT: str = "23414538T"


def test_valid_nif():
    assert validate_dni(VALID_NIF) is not None


def test_valid_nie():
    assert validate_dni(VALID_NIE) is not None


def test_not_valid_format_dni():
    with pytest.raises(NotValidDNIException):
        assert validate_dni(NOT_VALID_FORMAT_DNI)


def test_not_valid_first_character_nie():
    with pytest.raises(NotValidDNIException):
        assert validate_dni(NOT_VALID_FIRST_CHARACTER_NIE)


def test_not_valid_nif_control_digit():
    with pytest.raises(NotValidDNIException):
        assert validate_dni(NOT_VALID_NIF_CONTROL_DIGIT)
