import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, index):
        self.char = char
        self.index = index

    def __str__(self):
        return f"Username contains illegal character '{self.char}' at index {self.index}."


class UsernameTooShort(Exception):
    def __str__(self):
        return "Username is too short. Must be between 3 and 16 characters."


class UsernameTooLong(Exception):
    def __str__(self):
        return "Username is too long. Must be between 3 and 16 characters."


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "Password is missing a required character."


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)."


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)."


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)."


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)."


class PasswordTooShort(Exception):
    def __str__(self):
        return "Password is too short. Must be between 8 and 40 characters."


class PasswordTooLong(Exception):
    def __str__(self):
        return "Password is too long. Must be between 8 and 40 characters."


def check_input(username, password):
    if not (3 <= len(username) <= 16):
        if len(username) < 3:
            raise UsernameTooShort()
        else:
            raise UsernameTooLong()

    for index, char in enumerate(username):
        if not (char.isalnum() or char == '_'):
            raise UsernameContainsIllegalCharacter(char, index)

    if not (8 <= len(password) <= 40):
        if len(password) < 8:
            raise PasswordTooShort()
        else:
            raise PasswordTooLong()

    if not any(c.isupper() for c in password):
        raise PasswordMissingUppercase()
    if not any(c.islower() for c in password):
        raise PasswordMissingLowercase()
    if not any(c.isdigit() for c in password):
        raise PasswordMissingDigit()
    if not any(c in string.punctuation for c in password):
        raise PasswordMissingSpecial()

    print("OK")


def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            break
        except Exception as e:
            print(e)
            print("Please try again.")


main()
