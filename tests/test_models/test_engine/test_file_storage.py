#!/usr/bin/python3
<<<<<<< HEAD
"""A unit test module for the file storage.
"""
import os
import unittest
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from tests import write_text_file, reset_store


class TestFileStorage(unittest.TestCase):
    """Represents the test class for the FileStorage class.
    """

    def test_init(self):
        """Tests the initialization of the FileStorage class.
        """
        self.assertFalse(hasattr(FileStorage, '__file_path'))
        self.assertFalse(hasattr(FileStorage, '__objects'))

    def test_all(self):
        """Tests the all function of the FileStorage class.
        """
        write_text_file('file.json', '{}')
        store = FileStorage()
        store.reload()
        self.assertEqual(len(store.all()), 0)
        test_mdl = BaseModel()
        store.new(test_mdl)
        self.assertEqual(len(store.all()), 1)
        test_mdl = User()
        store.new(test_mdl)
        test_mdl = City()
        store.new(test_mdl)
        test_mdl = State()
        store.new(test_mdl)
        test_mdl = Amenity()
        store.new(test_mdl)
        test_mdl = Place()
        store.new(test_mdl)
        test_mdl = Review()
        store.new(test_mdl)
        self.assertEqual(len(store.all()), 7)
        with self.assertRaises(TypeError):
            store.all(test_mdl, None)
        with self.assertRaises(TypeError):
            store.all(test_mdl, test_mdl)
        with self.assertRaises(TypeError):
            store.all(None)
        with self.assertRaises(TypeError):
            store.all(store)

    def test_save(self):
        """Tests the save function of the FileStorage class.
        """
        store = FileStorage()
        test_mdl = User(**{'id': '5'})
        store.new(test_mdl)
        if os.path.isfile('file.json'):
            os.unlink('file.json')
        self.assertFalse(os.path.isfile('file.json'))
        store.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertGreater(os.stat('file.json').st_size, 10)
        with self.assertRaises(TypeError):
            store.save(test_mdl)
        with self.assertRaises(TypeError):
            store.save(test_mdl, None)
        with self.assertRaises(TypeError):
            store.save(test_mdl, test_mdl)
        with self.assertRaises(TypeError):
            store.save(None)

    def test_reload(self):
        """Tests the reload function of the FileStorage class.
        """
        reset_store(storage)
        store = FileStorage()
        reset_store(store)
        self.assertEqual(len(store.all()), 0)
        if os.path.isfile('file.json'):
            os.unlink('file.json')
        self.assertFalse(os.path.isfile('file.json'))
        store.reload()
        self.assertFalse(os.path.isfile('file.json'))
        test_mdl = User(id='5')
        test_mdl1 = City(id='7', name='Lagos')
        self.assertEqual(len(store.all()), 0)
        store.new(test_mdl)
        store.new(test_mdl1)
        if os.path.isfile('file.json'):
            os.unlink('file.json')
        store.save()
        self.assertEqual(len(store.all()), 2)
        store2 = FileStorage()
        with open('file.json', mode='w') as file:
            file.write('{}')
        self.assertTrue(store2.all() is not None)
        reset_store(store2)
        store2.reload()
        self.assertEqual(len(store2.all()), 0)
        store.save()
        store2.reload()
        self.assertEqual(len(store2.all()), 2)
        with open('file.json', mode='w') as file:
            file.write('{}')
        store2.reload()
        self.assertEqual(len(store2.all()), 0)
        with self.assertRaises(TypeError):
            store.reload(test_mdl)
        with self.assertRaises(TypeError):
            store.reload(test_mdl, None)
        with self.assertRaises(TypeError):
            store.reload(test_mdl, test_mdl)
        with self.assertRaises(TypeError):
            store.reload(None)

    def tearDown(self):
        """Deconstructs this test class.
        """
        super().tearDown()
        if os.path.isfile('file.json'):
            os.unlink('file.json')
=======
""" Check Filestorage class """
import unittest
from os import path
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_storage(unittest.TestCase):
    """ check the class """

    def setUp(self):
        """ check empty """
        try:
            remove('file.json')
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ check remove class """
        try:
            remove('file.json')
        except Exception:
            pass

    def test_no_objs(self):
        """ check empty class  """
        self.assertEqual(storage.all(), {})

    def test_all(self):
        """ check  all function """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_save_create(self):
        """ Save  """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])

    def test_new_empty(self):
        """ check new method """
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_classes(self):
        """ check  new method is valid """
        obj = BaseModel(id='123')
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User(id='01')
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City(id='02')
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity(id='03')
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place(id='04')
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review(id='05')
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State(id='06')
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(storage.all(), {})
        obj.id = 123
        storage.new(obj)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])

    def test_reload(self):
        """ check reload classes """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id
        storage.save()

        self.assertTrue(path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}

        storage.reload()

        self.assertTrue(obj_key in storage.all().keys())
        self.assertEqual(obj.id, storage.all()[obj_key].id)
        self.assertTrue(obj1_key in storage.all().keys())
        self.assertEqual(obj1.id, storage.all()[obj1_key].id)
        self.assertTrue(obj2_key in storage.all().keys())
        self.assertEqual(obj2.id, storage.all()[obj2_key].id)
        self.assertTrue(obj3_key in storage.all().keys())
        self.assertEqual(obj3.id, storage.all()[obj3_key].id)
        self.assertTrue(obj4_key in storage.all().keys())
        self.assertEqual(obj4.id, storage.all()[obj4_key].id)
        self.assertTrue(obj5_key in storage.all().keys())
        self.assertEqual(obj5.id, storage.all()[obj5_key].id)
        self.assertTrue(obj6_key in storage.all().keys())
        self.assertEqual(obj6.id, storage.all()[obj6_key].id)
>>>>>>> 609421b453560090372d1db16e15fc5384933a2e
