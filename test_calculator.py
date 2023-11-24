def test_add():
    result = add("")
    assert result == 0


def test_single_number():
    result = add("1")
    assert result == 1


def test_two_numbers():
    result = add("1,2")
    assert result == 3


def test_multiple_numbers():
    result = add("1,2,3,4,5,6,7")
    assert result == 28


def test_newline():
    result = add("1,2\n3")
    assert result == 6


def test_newline_invalid():
    result = add("2,\n3")
    assert result == "invalido"


def test_separator_endline():
    result = add("1,2,")
    assert result == "invalido"


def test_custom_delimiter1():
    result = add("//;\n1; 3")
    assert result == 4


def test_custom_delimiter2():
    result = add("//|\n1|2|3")
    assert result == 6


def test_custom_delimiter3():
    result = add("//sep\n2sep5")
    assert result == 7


def test_custom_delimiter4():
    result = add("//|\n1|2,3")
    assert result == "invalido"


def add(numbers: str):

    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return int(numbers[0])

    if ",\n" in numbers or numbers[-1] == ',':
        return "invalido"

    if "//" in numbers:
        newline_index = numbers.find("\n")
        delimiter = numbers[2: newline_index]
        numbers = numbers.split("\n")[1]
        split = numbers.split(delimiter)
        soma = 0

        for i in split:
            try:
                soma = soma + int(i)
            except:
                return "invalido"

        return soma

    numbers = numbers.replace("\n", ",")
    split = numbers.split(",")

    soma = 0

    for i in split:
        soma = soma + int(i)

    return soma
