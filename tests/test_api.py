#!/usr/bin/env python3

"""
Test for the DB module of the API
"""

from unittest import TestCase
from api.auth.db import database

class TestDBModule(TestCase):
    """
    Class with unittest to run
    For the database module of the
    db package
    """
    @classmethod
    def setUp(cls):
        """
        Setup resources for testing
        """
        cls.db_object = database.db_object
        cls.cursor_object = database.cursor_object

    @classmethod
    def tearDown(cls):
        """
        Clean up actions after running
        The test that required the resources
        Setup in the SetUp method
        """
        del cls.db_object
        del cls.cursor_object
        return

    def test_module_documentataion(self):
        """Make sure the module is well documented"""
        self.assertIsNotNone(database.__doc__)
