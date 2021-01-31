import sys


class ParkingCar:

    def __init__(self):
        """
        Initialization of Variables so that we can use them in all other functions
        :param self:
        :return:  
        """
        self.initial_space = 0
        self.nearest_slot = 1
        self.available_slots = 0
        self.current_slot_available = 0
        self.total_occupied_slots = 0
        self.count = 0
        self.slots_list = []
        self.age_car_number = {}
        self.car_slot_number = {}

    def park_vehicle(self, split_txt):
        """
        :param self:
        :param split_txt: Text coming from Split the Input.
        :return: Data Appended to List for driver and Slot Details . Lists :-  age_car_number, car_slot_number,
         slot_number_of_driver_age
        """
        car_number = split_txt[1]
        driver_age = split_txt[3]
        if self.count == self.available_slots:
            print("Parking Space is Not Available. It is full")
            return "Full"
        if len(car_number) < 13 or len(car_number) > 13:
            print("Car number is not of Valid Length. It should be Exactly 13")
            return "Length"

        if driver_age.isnumeric():
            driver_age = int(driver_age)
        else:
            print('Data is Invalid. Driver Age should be in Integers')
            sys.exit()
        # Finding if Car is Already Parked or Not.
        for item in self.slots_list:
            try:
                if item["Car_Number"] == car_number:
                    print("Car is Already Parked at slot number {}".format(self.car_slot_number[car_number]))
                    return
            except KeyError:
                pass            
        self.slots_list[self.nearest_slot - 1] = {"Car_Number": car_number, "Driver_age": driver_age}
        # Vehicle Registration numbers for all cars which are parked by the driver of a certain age.
        if self.age_car_number.get(driver_age):
            self.age_car_number[driver_age].append(car_number)
        else:
            self.age_car_number[driver_age] = [car_number]
        # Slot number in which a car with a given vehicle registration plate is parked.
        self.car_slot_number[car_number] = self.nearest_slot
        # Slot number of all slots where cars of drivers of a particular age are parked.
        self.get_print_ticket(car_number)
        # Available slots - 1 so that we can get index to iterate over a List.
        for iterator in range(self.nearest_slot, self.available_slots):
            if not self.slots_list[iterator]:
                self.nearest_slot = iterator + 1
                break
        self.count += 1
        return "Parked"

    def get_print_ticket(self, car_number):
        """
        :param self:
        :param car_number: Input the car number for printing.
        :return: Printing Car Number with its slot number
        """
        print("Car with vehicle registration number {} has been parked at slot number {}".format(car_number,
                                                                                                 self.nearest_slot))

    def get_slot_numbers_for_driver(self, split_txt):
        
        """
        :param self: 
        :param split_txt: Input of Age will be extracted from the split_txt
        :return: Print all the slots Comma Separated
        """
        
        driver_age = split_txt[1]
        all_slots = []
        if driver_age.isnumeric():
            driver_age = int(driver_age)
        else:
            print('Age Should be in Integers')
            sys.exit()
        try:   
            driver_age_list = self.age_car_number.get(driver_age)
            for car_number in driver_age_list:
                all_slots.append(self.car_slot_number.get(car_number))
            print(", ".join(repr(e) for e in all_slots))
            return "Created Slots"
        except KeyError:
            print("No slots found for driver age {} ".format(driver_age))
            return "No Slots"
        except Exception:
            print("No slots found for driver age {} ".format(driver_age))
            return "No Slots"
                            
    def get_slot_numbers_for_car(self, split_txt):
        """                
        :param self: 
        :param split_txt: Get the car number from the split_txt 
        :return: Print the car number 
        """
        car_number = split_txt[1]
        try:
            slot_number = self.car_slot_number.get(car_number)
            print(slot_number)
            try:
                int(slot_number)
                return "Passed"
            except Exception:
                return "Not Passed"
        except KeyError:
            print("Invalid car number {}".format(car_number))
            return "Exception"
        except Exception:
            print("Invalid car number {}".format(car_number))
            return "Exception"


class MainCarPark(ParkingCar):

    def leave_parking_space(self, split_txt):
        """
        :param self:
        :param split_txt: Get slot number from the split_txt
        :return: print the vacated slot number
        """
        slot_number = split_txt[1]
        if slot_number.isnumeric():
            slot_number = int(slot_number)
        else:
            print('Slot Number should be in integers.')
            sys.exit()
        index_of_slot = slot_number - 1
        if index_of_slot > len(self.slots_list) or index_of_slot is -1:
            print("Slot is not Present check your number Again.")
            return "Big"
        empty_slot = bool(self.slots_list[index_of_slot])
        if empty_slot is False:
            print("Slot number {} is Already Empty".format(slot_number))
            return "Not Present"
        if self.slots_list[index_of_slot]:
            car_number = self.slots_list[index_of_slot].get('Car_Number')
            driver_age = self.slots_list[index_of_slot].get('Driver_age')
            self.slots_list[index_of_slot] = {}
            self.age_car_number[driver_age].remove(car_number)
            self.car_slot_number.pop(car_number)
            if slot_number < self.nearest_slot:
                self.nearest_slot = slot_number
            print("Slot number {} vacated, the car with vehicle registration number {} left the space, the driver "
                  "of the car was of age {}".format(slot_number, car_number, driver_age))
            self.count -= 1
            return "Success"

    def create_parking_lot(self, file_slot):
        """
        :param file_slot:
        :return: Creating Slot List According to List or input given
        """
        if file_slot.isnumeric():
            file_slot = int(file_slot)
        else:
            print('ERROR :- Creating Lots should be in integers. WRONG FORMAT FOUND')
            sys.exit()

        if self.available_slots == 0:
            self.available_slots = file_slot
            self.current_slot_available = 0
            self.slots_list = [{}] * file_slot
            print('Created parking space of {0} slots'.format(file_slot))
            return "Parked"
        else:
            print("No slots are available")

    def get_vehicle_registration_number(self, split_txt):
        """
        :param self:
        :param split_txt: Get the driver age from split text.
        :return: Vehicle Registration Number
        """
        driver_age = split_txt[1]
        try:
            key = self.age_car_number[int(driver_age)]
            for item in key:
                slot_number = self.car_slot_number[item]
                print("Car with vehicle registration number {} has been parked at slot number {}"
                      .format(item, slot_number))
            return "Parked"
        except KeyError:
            print("null")
            return "null"
        except Exception:
            print("null")
            return "null"
