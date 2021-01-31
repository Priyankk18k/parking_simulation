import unittest
from parking_functions import *


class TestMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = MainCarPark()
        self.obj.create_parking_lot("4")

    def tearDown(self) -> None:
        print("\n")
        print("*****************************************TEST CASE PASSED*********************************************")
        print("\n")

    def test_park_vehicle(self):
        self.assertEqual(self.obj.park_vehicle("Park KA-01-HH-1234 driver_age 21".split()),
                         "Parked")
        self.assertEqual(self.obj.park_vehicle("Park KA-01-HH-1235 driver_age 21".split()),
                         "Parked")
        self.assertEqual(self.obj.park_vehicle("Park KA-01-HH-1236 driver_age 21".split()),
                         "Parked")
        self.assertEqual(self.obj.park_vehicle("Park PB-01-HH-1234 driver_age 21".split()),
                         "Parked")
        self.assertEqual(self.obj.park_vehicle("Park KA-01-HH-1237 driver_age 21".split()),
                         "Full")

    def test_slot_numbers_for_driver(self):
        self.test_park_vehicle()
        self.assertEqual(self.obj.get_slot_numbers_for_driver("Slot_numbers_for_driver_of_age 21".split()),
                         "Created Slots")
        self.assertEqual(self.obj.get_slot_numbers_for_driver("Slot_numbers_for_driver_of_age 32".split()),
                         "No Slots")
        self.assertEqual(self.obj.get_slot_numbers_for_driver("Slot_numbers_for_driver_of_age 33".split()),
                         "No Slots")

    def test_slot_numbers_for_car(self):
        self.test_slot_numbers_for_driver()
        self.assertEqual(self.obj.get_slot_numbers_for_car("Slot_number_for_car_with_number PB-01-HH-1234".split()),
                         "Passed")
        self.assertEqual(self.obj.get_slot_numbers_for_car("Slot_number_for_car_with_number PB-02-HH-1244".split()),
                         "Not Passed")
        self.assertEqual(self.obj.get_slot_numbers_for_car("Slot_number_for_car_with_number PB-02-HH-1634".split()),
                         "Not Passed")

    def test_leave(self):
        self.test_slot_numbers_for_car()
        self.assertEqual(self.obj.leave_parking_space("Leave 2".split()),
                         "Success")
        self.assertEqual(self.obj.leave_parking_space("Leave 2".split()),
                         "Not Present")
        self.assertEqual(self.obj.leave_parking_space("Leave 0".split()),
                         "Big")
        self.assertEqual(self.obj.leave_parking_space("Leave 99".split()),
                         "Big")

    def test_vehicle_registration_number(self):
        self.test_leave()
        self.assertEqual(self.obj.get_vehicle_registration_number("Vehicle_registration_number_for_driver_of_age 21"
                                                                   .split()),
                         "Parked")
        self.assertEqual(self.obj.get_vehicle_registration_number("Vehicle_registration_number_for_driver_of_age 99"
                                                                   .split()),
                         "null")


if __name__ == '__main__':
    unittest.main()
