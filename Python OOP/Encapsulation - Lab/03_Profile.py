class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
            return
        raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.validate_length(value) and self.check_for_uppercase(value) and self.check_for_digit(value):
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def validate_length(self, password):
        return True if len(password) >= 8 else False

    def check_for_uppercase(self, password):
        uppercase = [sym for sym in password if sym.isupper()]
        return True if uppercase else False

    def check_for_digit(self, password):
        digits = [sym for sym in password if sym.isdigit()]
        return True if digits else False

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {len(self.password) * '*'}"
