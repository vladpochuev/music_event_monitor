import unittest

from parse_dumpsys import get_object_fields, remove_redundant_comas


class TestMain(unittest.TestCase):
    def test_get_object_fields_basic(self):
        obj = "{state=PLAYING, position=0}"
        self.assertEqual(get_object_fields(obj), "state=PLAYING, position=0")

    def test_get_object_fields_multiple_braces(self):
        obj = "outer{inner={key=value}}outer_end"
        self.assertEqual(get_object_fields(obj), "inner={key=value}")

    def test_get_object_fields_no_braces(self):
        obj = "no braces here"
        self.assertEqual(get_object_fields(obj), obj)

    def test_get_object_fields_one_braces(self):
        obj = "Object {no braces here"
        self.assertEqual(get_object_fields(obj), obj)

    def test_remove_redundant_comas(self):
        self.assertEqual(remove_redundant_comas(",a,b,"), "a,b")
        self.assertEqual(remove_redundant_comas("a,b"), "a,b")
        self.assertEqual(remove_redundant_comas(",a,b"), "a,b")
        self.assertEqual(remove_redundant_comas("a,b,"), "a,b")
