import unittest
from models.base import Base


class BaseTest(unittest.TestCase):

    def setUp(self):
        """Reset class counter for each test to ensure consistency"""
        Base._Base__nb_objects = 0

    def test_default_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_string_id(self):
        b = Base("abc")
        self.assertEqual(b.id, "abc")

    def test_float(self):
        b = Base(3.14)
        self.assertEqual(b.id, 3.14)

    def test_mixed_ids(self):
        b1 = Base()
        b2 = Base(42)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 42)
        self.assertEqual(b3.id, 2)

    def test_bulk_creation(self):
        instances = [Base() for _ in range(5)]
        expected_ids = list(range(1, 6))
        self.assertEqual([obj.id for obj in instances], expected_ids)



if __name__ == "__main__":
    unittest.main()
