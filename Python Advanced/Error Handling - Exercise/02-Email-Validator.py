class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class TooManyAtSymbols(Exception):
    pass


def validate_email(email):
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    try:
        username, domain, *rest = email.split("@")
        domain = domain.split('.')[-1]
    except ValueError:
        raise MustContainAtSymbolError("The email must contain only one @ symbol")

    if rest:
        raise TooManyAtSymbols("The email must contain only one @ symbol")
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: .{', .'.join(VALID_DOMAINS)}")
    print("Email is valid")


VALID_DOMAINS = ['com', 'bg', 'org', 'net']

email = input()
while not email == "End":
    validate_email(email)
    email = input()
