from string import *
import random


class Password:
    def __init__(self, length, nr_special_char, nr_upper_letters, nr_lower_letters, nr_digits):
        """
        :param length: length of the password
        :param nr_special_char: number of special char
        :param nr_upper_letters: number of upper letters
        :param nr_lower_letters: number of lower letters
        :param nr_digits: number of digits
        """
        self.length = length
        self.nr_special_char = nr_special_char
        self.nr_upper_letters = nr_upper_letters
        self.nr_lower_letters = nr_lower_letters
        self.nr_digits = nr_digits
        self.password = ""
        self.what_to_add = []  # list of what action to use
        self.length_from_user = self.nr_digits + self.nr_special_char + self.nr_lower_letters + self.nr_upper_letters
        # checking the password requirements
        if self.nr_special_char > 0:
            self.what_to_add.append("nr_special_char")
        if self.nr_digits > 0:
            self.what_to_add.append("nr_digits")
        if self.nr_lower_letters > 0:
            self.what_to_add.append("nr_lower_letters")
        if self.nr_upper_letters > 0:
            self.what_to_add.append("nr_upper_letters")

    def checking_params(self):
        """
        :return: 0 if the the password needs to contain more letters than it is length 1 otherwise
        """
        if self.length_from_user > self.length:
            print("The number of letters,digits and special char is bigger than the length of the password")
            return 0
        elif self.length_from_user < self.length:
            print("Will add random char to complete the length")
            self.add_random_char()
        return 1

    def add_random_char(self):
        """
        If the password length is lower than the length from all the other  then it will add
        """
        for i in range(0, self.length - self.length_from_user):
            self.password += random.choice(printable)

    def add_upper_letters(self):
        """
        Add random uppercase letter to the password
        """
        self.password += random.choice(ascii_uppercase)
        self.nr_upper_letters -= 1
        if self.nr_upper_letters == 0:
            self.what_to_add.remove("nr_upper_letters")

    def add_lower_letters(self):
        """
        Add random lowercase letter to the password
        """
        self.password += random.choice(ascii_lowercase)
        self.nr_lower_letters -= 1
        if self.nr_lower_letters == 0:
            self.what_to_add.remove("nr_lower_letters")

    def add_number(self):
        """
        Add random number to the password
        """
        self.password += random.choice(digits)
        self.nr_digits -= 1
        if self.nr_digits == 0:
            self.what_to_add.remove("nr_digits")

    def add_special_char(self):
        """
        Add special char to the password
        """
        self.password += random.choice(punctuation)
        self.nr_special_char -= 1
        if self.nr_special_char == 0:
            self.what_to_add.remove("nr_special_char")

    def what_action_to_take(self, action):
        """
        Add upper letter,lower letter,digit or special char to the password
        """
        if action == "nr_upper_letters":
            self.add_upper_letters()
        elif action == "nr_digits":
            self.add_number()
        elif action == "nr_lower_letters":
            self.add_lower_letters()
        elif action == "nr_special_char":
            self.add_special_char()

    def create_password(self):
        """
        Start creating the password
        """
        if self.checking_params() == 0:
            return 0
        else:
            while self.what_to_add:
                action = random.choice(self.what_to_add)
                self.what_action_to_take(action)


if __name__ == '__main__':
    password = Password(8, 0, 1, 1, 1)
    password.create_password()
    print(password.password)
