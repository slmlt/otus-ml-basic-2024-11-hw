characters = input()
parts = characters.split(sep='.')
parts_count = parts.__len__()


def is_number_or_empty(block: str) -> bool:
    return not block or block.isdigit()


if parts_count == 2:
    print(
        (is_number_or_empty(parts[0]) and parts[1].isdigit()) or
        (parts[0].isdigit() and is_number_or_empty(parts[1]))
    )
elif parts_count == 1:
    print(parts[0].isdigit())
else:
    print(False)
