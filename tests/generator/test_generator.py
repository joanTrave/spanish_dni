import pytest

from spanish_dni.constants import DNITypes
from spanish_dni.dni import DNI
from spanish_dni.generator import generate_dni
from spanish_dni.generator.exceptions import (
    IncompatibleParametersDNIGeneratorException,
    NotValidFirstDNICharactersException,
)
from spanish_dni.validator import validate_dni


def test_incompatible_mode():
    with pytest.raises(IncompatibleParametersDNIGeneratorException):
        assert generate_dni(is_nie=True, first_characters="01234567")


def test_valid_generated_nif():
    generated_dni_str: str = generate_dni()
    validated_generated_dni: DNI = validate_dni(generated_dni_str)
    assert validated_generated_dni.dni_type == DNITypes.NIF


def test_valid_generated_nie():
    generated_dni_str: str = generate_dni(is_nie=True)
    validated_generated_dni: DNI = validate_dni(generated_dni_str)
    assert validated_generated_dni.dni_type == DNITypes.NIE


def test_valid_generated_nif_with_first_characters():
    first_characters: str = ""
    for i in range(8):
        first_characters += str(i)
        generated_dni_str: str = generate_dni(first_characters=first_characters)
        validated_generated_dni: DNI = validate_dni(generated_dni_str)
        assert validated_generated_dni.dni_type == DNITypes.NIF


def test_too_much_characters():
    with pytest.raises(NotValidFirstDNICharactersException):
        assert generate_dni(is_nie=False, first_characters="012345678")


def test_invalid_characters():
    with pytest.raises(NotValidFirstDNICharactersException):
        assert generate_dni(is_nie=False, first_characters="0123456A")
