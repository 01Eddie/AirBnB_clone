#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.user import User
from models.base_model import BaseModel
import pep8

class TestUser(unittest.TestCase):
    """" Test cases class of User """

    def test_pep8_user(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/user.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_user(self):
        new_user = User()
        self.assertIs(type(new_user.email), str)
        self.assertIs(type(new_user.password), str)
        self.assertIs(type(new_user.firstname), str)
        self.assertIs(type(new_user.last_name), str)

    def test_inherit_User(self):
        new_inherit = User()
        self.assertNotIsInstance(type(new_inherit), BaseModel)

if __name__ == "__main__":
    unittest.main()