# Spanish DNI

SD is a library of utilities for the Python programming language that allows validating both NIE and NIF.
It also can be used to generate NIF/NIE list.
## Installation
Can be installed via PiPI.
```bash
pip install spanish-dni
```
## How to use it

Sample code to validate NIF/NIE list.

```python3
from spanish_dni.dni import DNI
from spanish_dni.validator.exceptions import NotValidDNIException
from spanish_dni.validator import validate_dni

my_dnis: list[str] = [
    "23414538D",
    "Y2853959H",
    "23418D",
    "U2853959H",
    "23414538T",
]

for dni in my_dnis:
    valid = True
    try:
        dni_parsed: DNI = validate_dni(dni)
        print(f"DNI {dni} is type {dni_parsed.dni_type}")
    except NotValidDNIException:
        valid = False
        print(f"DNI {dni} is not valid")
```

Sample code to generate random NIF list of 8 elements with no initial characters provided.

```python3
from spanish_dni.generator import generate_dni


for _ in range(8):
    print(generate_dni())

```

Sample code to generate random NIF list of 8 elements which all of them start with number 0.

```python3
from spanish_dni.generator import generate_dni


for _ in range(8):
    print(generate_dni(first_characters="0"))

```

Sample code to generate random NIE list of 8 elements.

```python3
from spanish_dni.generator import generate_dni


for _ in range(8):
    print(generate_dni(is_nie=True))

```


## Limitations

For the moment, it can not be used to generate random NIE with first character parameter.
If it is tried, it will raise an ``IncompatibleParametersDNIGeneratorException`` exception.