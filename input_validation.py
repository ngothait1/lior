from project_exceptions import InvalidInput


def mustBeNumberCheck(category: str, value:str):
    if value.isdigit() ==  False or int(value) < 0:
        raise InvalidInput(category, value)
    return int(value)