#!/usr/bin/python3
<<<<<<< HEAD
"""A unit test module for the amenity model.
"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
from datetime import datetime
import os


class TestAmenity(unittest.TestCase):
    """Represents the test class for the Amenity class.
    """

    def test_init(self):
        """Tests the initialization of the Amenity class.
        """
        self.assertIsInstance(Amenity(), BaseModel)
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertIsInstance(Amenity.name, str)
        self.assertEqual(Amenity().name, '')
        self.assertEqual(Amenity('gaming room').name, '')
        self.assertEqual(Amenity(name='Electricity').name, 'Electricity')
        self.assertEqual(Amenity('Library', name='Toilet').name, 'Toilet')

    def test_str(self):
        """Tests the __str__ function of the Amenity class.
        """
        datetime_now = datetime.today()
        datetime_repr = repr(datetime_now)
        test_mdl = Amenity()
        test_mdl.id = '012345'
        test_mdl.created_at = test_mdl.updated_at = datetime_now
        test_mdl_str = str(test_mdl)
        self.assertIn("[Amenity] (012345)", test_mdl_str)
        self.assertIn("'id': '012345'", test_mdl_str)
        self.assertIn("'created_at': " + datetime_repr, test_mdl_str)
        self.assertIn("'updated_at': " + datetime_repr, test_mdl_str)
        self.assertIn("'id': ", str(Amenity()))
        self.assertIn("'created_at': ", str(Amenity()))
        self.assertIn("'updated_at': ", str(Amenity()))
        self.assertIn(
            "'gender': 'female'",
            str(Amenity(gender='female', id='m-77'))
        )
        self.assertNotIn(
            "'created_at': ",
            str(Amenity(gender='female', id='u-88'))
        )
        self.assertNotIn(
            "'updated_at': ",
            str(Amenity(gender='female', id='u-55'))
        )
        self.assertRegex(
            str(Amenity()),
            r'\[Amenity\] \([0-9a-zA-Z]+(?:-[0-9a-zA-Z]+)*\) \{.+\}'
        )
        self.assertEqual(
            str(Amenity(id='m-345')),
            "[Amenity] (m-345) {'id': 'm-345'}"
        )
        self.assertEqual(
            str(Amenity(id=45)),
            "[Amenity] (45) {'id': 45}"
        )
        self.assertEqual(
            str(Amenity(id=None)),
            "[Amenity] (None) {'id': None}"
        )
        with self.assertRaises(AttributeError):
            str(Amenity(gender='female'))

    def test_to_dict(self):
        """Tests the to_dict function of the Amenity class.
        """
        # Tests if it's a dictionary
        self.assertIsInstance(Amenity().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', Amenity().to_dict())
        self.assertIn('created_at', Amenity().to_dict())
        self.assertIn('updated_at', Amenity().to_dict())
        # Tests if to_dict contains added attributes
        test_mdl = Amenity()
        test_mdl.firstname = 'George'
        test_mdl.lastname = 'Jungle'
        self.assertIn('firstname', test_mdl.to_dict())
        self.assertIn('lastname', test_mdl.to_dict())
        self.assertIn('firstname', Amenity(firstname='George').to_dict())
        self.assertIn('lastname', Amenity(lastname='Jungle').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(Amenity().to_dict()['created_at'], str)
        self.assertIsInstance(Amenity().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        test_mdl = Amenity()
        test_mdl.id = '012345'
        test_mdl.created_at = test_mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': 'Amenity',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(test_mdl.to_dict(), to_dict)
        self.assertDictEqual(
            Amenity(id='u-b34', age=13).to_dict(),
            {
                '__class__': 'Amenity',
                'id': 'u-b34',
                'age': 13
            }
        )
        self.assertDictEqual(
            Amenity(id='u-b34', age=None).to_dict(),
            {
                '__class__': 'Amenity',
                'id': 'u-b34',
                'age': None
            }
        )
        # Tests to_dict output contradiction
        test_mdl_d = Amenity()
        self.assertIn('__class__', Amenity().to_dict())
        self.assertNotIn('__class__', Amenity().__dict__)
        self.assertNotEqual(test_mdl_d.to_dict(), test_mdl_d.__dict__)
        self.assertNotEqual(
            test_mdl_d.to_dict()['__class__'],
            test_mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            Amenity().to_dict(None)
        with self.assertRaises(TypeError):
            Amenity().to_dict(Amenity())
        with self.assertRaises(TypeError):
            Amenity().to_dict(45)

    def tearDown(self):
        """Deconstructs this test class.
        """
        super().tearDown()
        if os.path.isfile('file.json'):
            os.unlink('file.json')
=======
"""
Test suits for amenities
"""
import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    a = Amenity()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
>>>>>>> 609421b453560090372d1db16e15fc5384933a2e
