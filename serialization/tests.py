from homework import *
import unittest


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car1 = Car(price=1000, type="Diesel", producer="BMW", mileage=10000, number=1234)
        self.car2 = Car(price=1000, type="Diesel", producer="BMW", mileage=10000, number=1234)
        self.car3 = Car(2000, "Van", "Chery", 20000)

    def test_car_change_number_success(self):
        self.car1.change_number('c857fd34-b3e8-476a-833a-e38e1f928f6e')
        self.assertIsInstance(self.car1.number, uuid.UUID)

    def test_car_change_number_fail(self):
        self.car1.change_number(12345)
        self.assertNotIsInstance(self.car1.number, uuid.UUID)

    def test_convert_car_to_dict_success(self):
        expected_result = {
            '__class__': 'Car',
            '__module__': 'homework',
            'price': self.car1.price,
            'type': self.car1.type,
            'producer': self.car1.producer,
            'number': self.car1.number,
            'mileage': self.car1.mileage}
        self.assertEqual(expected_result.items(), self.car1.obj_to_dict().items())

    def test_car_equality_success(self):
        self.assertTrue(self.car1.car_equality(self.car2))

    def test_car_equality_fail(self):
        self.assertFalse(self.car1.car_equality(self.car3))

    def test_convert_car_to_dict_and_back_success(self):
        car3_to_dict = json.dumps(self.car3.obj_to_dict(), cls=JsonEncoder, indent=4)
        car3_to_obj = json.loads(car3_to_dict, object_hook=dict_to_obj)
        self.assertTrue(self.car3.car_equality(car3_to_obj))

    def test_magic_method__str__for_car_success(self):
        expected_result = f"""
        Attributes of current Car:
            price: '{self.car3.price}';
            type: '{self.car3.type}';
            producer: '{self.car3.producer}';
            number: '{self.car3.number}';
            mileage: '{self.car3.mileage}';
        """
        self.assertEqual(str(self.car3), expected_result)

    def test_magic_method__repr__for_car_success(self):
        expected_result = f"Car(price='{self.car3.price}', type='{self.car3.type}', " \
            f"producer='{self.car3.producer}', mileage='{self.car3.mileage}')"
        self.assertEqual(repr(self.car3), expected_result)


class TestGarage(unittest.TestCase):

    def setUp(self):
        self.car1 = Car(1000, "Diesel", "BMW", 10000)
        self.car2 = Car(1000, "Diesel", "BMW", 10000, 'c857fd34-b3e8-476a-833a-e38e1f928f6e')
        self.car3 = Car(2000, "Van", "Chery", 20000, 1111)
        self.garage1 = Garage('Kiev', [self.car1], 2)
        self.garage2 = Garage('Kiev', [self.car1, self.car2], 2)
        self.garage3 = Garage('Kiev', [self.car1, self.car2], 2)

    def test_add_car_to_garage_success(self):
        expected_result = 0
        self.garage1.add_car(self.car2)
        self.assertEqual(self.garage1.free_places(), expected_result)
        self.assertIn(self.car2, self.garage1.cars)

    def test_add_car_to_garage_fail(self):
        expected_result = 0
        self.garage2.add_car(self.car3)
        self.assertEqual(self.garage2.free_places(), expected_result)
        self.assertNotIn(self.car3, self.garage2.cars)

    def test_remove_car_from_garage_success(self):
        expected_result = 2
        self.garage1.remove_car(self.car1)
        self.garage1.remove_car(self.car2)
        self.assertEqual(self.garage1.free_places(), expected_result)
        self.assertNotIn(self.car1, self.garage1.cars)
        self.assertNotIn(self.car2, self.garage1.cars)

    def test_hit_hat_method_for_garage_success(self):
        expected_result = 2000
        self.assertEqual(self.garage2.hit_hat(), expected_result)

    def test_free_places_method_for_garage_success(self):
        expected_result = 0
        self.assertEqual(self.garage2.free_places(), expected_result)

    def test_garage_equality_method_success(self):
        self.assertTrue(self.garage2.garage_equality(self.garage3))

    def test_garage_equality_method_fail(self):
        self.assertFalse(self.garage1.garage_equality(self.garage2))

    def test_convert_garage_to_dict_success(self):
        expected_result = {
            '__class__': 'Garage',
            '__module__': 'homework',
            'town': self.garage1.town,
            'cars': [{
                '__class__': 'Car',
                '__module__': 'homework',
                'price': self.car1.price,
                'type': self.car1.type,
                'producer': self.car1.producer,
                'number': self.car1.number,
                'mileage': self.car1.mileage
            }],
            'places': self.garage1.places,
            'owner': self.garage1.owner
        }

        self.assertEqual(expected_result.items(), self.garage1.obj_to_dict().items())

    def test_convert_garage_to_dict_and_back_success(self):
        garage1_with_dupms = json.dumps(self.garage1.obj_to_dict(), cls=JsonEncoder, indent=4)
        decoding_garage1_with_loads = json.loads(garage1_with_dupms, object_hook=dict_to_obj)
        self.assertTrue(self.garage1.garage_equality(decoding_garage1_with_loads))

    def test_magic_method__str__for_garage_success(self):
        expected_result = f"""
        Attributes of current Garage:
            town: '{self.garage1.town}';
            total cars: '{len(self.garage1.cars)}';
            places: '{self.garage1.places}';
            owner: '{self.garage1.owner}';
        """
        self.assertEqual(str(self.garage1), expected_result)

    def test_magic_method__repr__for_garage_success(self):
        expected_result = f"Garage(town='{self.garage1.town}', cars='{len(self.garage1.cars)}'," \
            f" places='{self.garage1.places}', owner='{self.garage1.owner}')"
        self.assertEqual(repr(self.garage1), expected_result)


class TestCesar(unittest.TestCase):

    def setUp(self):
        self.car1 = Car(1000, "Diesel", "BMW", 10000, 'c857fd34-b3e8-476a-833a-e38e1f928f6e')
        self.car2 = Car(1000, "Diesel", "BMW", 10000, 'c857fd34-b3e8-476a-833a-e38e1f928f6e')
        self.garage1 = Garage('Kiev', [self.car1, self.car2], 2)
        self.garage2 = Garage('Kiev', [], 2)
        self.garage3 = Garage('Kiev', [self.car1], 2)
        self.cesar1 = Cesar("Crappy", [self.garage1], "a9b64780-97e3-47b8-9a70-2a20a3ee8666")
        self.cesar2 = Cesar("Nigga", [self.garage2])
        self.cesar3 = Cesar("Freddy", [])
        self.cesar4 = Cesar("Freddy", [self.garage2, self.garage3], "a9b64780-97e3-47b8-9a70-2a20a3ee1111")
        self.cesar5 = Cesar("Freddy", [self.garage2, self.garage3], "a9b64780-97e3-47b8-9a70-2a20a3ee1111")

    def test_magic_method__str__for_cesar_success(self):
        expected_result = f"""
        Attributes of current Cesar:
            name: '{self.cesar1.name}';
            total garages: '{self.cesar1.garages_count()}';
            register_id: '{self.cesar1.register_id}';
        """
        self.assertEqual(str(self.cesar1), expected_result)

    def test_magic_method__repr__for_cesar_success(self):
        expected_result = f"Cesar(name='{self.cesar1.name}', garages='{self.cesar1.garages_count()}'," \
            f" register_id: '{self.cesar1.register_id}')"
        self.assertEqual(repr(self.cesar1), expected_result)

    def test_hit_hat_method_for_cesar_success(self):
        expected_result_1 = 2000
        expected_result_2 = 0
        self.assertEqual(self.cesar1.hit_hat(), expected_result_1)
        self.assertEqual(self.cesar2.hit_hat(), expected_result_2)

    def test_garages_count_method_for_cesar_success(self):
        expected_result_1 = 1
        expected_result_2 = 0
        self.assertEqual(self.cesar1.garages_count(), expected_result_1)
        self.assertEqual(self.cesar3.garages_count(), expected_result_2)

    def test_cars_count_method_for_cesar_success(self):
        expected_result = 2
        self.assertEqual(self.cesar1.cars_count(), expected_result)

    def test_add_car_to_random_garage_of_cesar_success(self):
        expected_result_1 = 1
        expected_result_2 = 1
        self.cesar4.add_car(self.car2)
        self.assertEqual(self.garage2.free_places(), expected_result_1)
        self.assertEqual(self.garage3.free_places(), expected_result_2)

    def test_add_car_to_specific_garage_for_cesar_success(self):
        expected_result_1 = 2
        expected_result_2 = 0
        self.cesar4.add_car(self.car2, self.garage3)
        self.assertEqual(self.garage2.free_places(), expected_result_1)
        self.assertEqual(self.garage3.free_places(), expected_result_2)

    def test_add_car_to_full_garage_of_cesar_fail(self):
        expected_result = 0
        self.cesar1.add_car(self.car1)
        self.assertEqual(self.garage1.free_places(), expected_result)

    def test_cesar_equality_method_success(self):
        self.assertTrue(self.cesar4.cesar_equality(self.cesar5))

    def test_cesar_equality_method_fail(self):
        self.assertFalse(self.cesar3.cesar_equality(self.cesar4))

    def test_convert_cesar_to_dict_success(self):
        expected_result = {
            '__class__': 'Cesar',
            '__module__': 'homework',
            'name': self.cesar1.name,
            'garages': [
                {'__class__': 'Garage',
                 '__module__': 'homework',
                 'town': self.garage1.town,
                 'cars': [
                    {'__class__': 'Car',
                     '__module__': 'homework',
                     'price': self.car1.price,
                     'type': self.car1.type,
                     'producer': self.car1.producer,
                     'number': self.car1.number,
                     'mileage': self.car1.mileage
                     },
                    {'__class__': 'Car',
                     '__module__': 'homework',
                     'price': self.car2.price,
                     'type': self.car2.type,
                     'producer': self.car2.producer,
                     'number': self.car2.number,
                     'mileage': self.car2.mileage}],
                 'places': self.garage1.places,
                 'owner': self.garage1.owner
                 }],
            'register_id': self.cesar1.register_id
        }
        self.assertEqual(expected_result.items(), self.cesar1.obj_to_dict().items())

    def test_convert_cesar_to_dict_and_back_success(self):
        cesar2_with_dupms = json.dumps(self.cesar2.obj_to_dict(), cls=JsonEncoder, indent=4)
        decoding_cesar2_with_loads = json.loads(cesar2_with_dupms, object_hook=dict_to_obj)
        self.assertTrue(self.cesar2.cesar_equality(decoding_cesar2_with_loads))


if __name__ == "__main__":
    unittest.main()
