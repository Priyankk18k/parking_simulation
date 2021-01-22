import fileinput
import argparse
from parking_functions import parking_car


def main_execution(file_name):
    parking_obj = parking_car()
    for line in fileinput.input(files=(file_name)):
        split_txt = line.split()
        if split_txt[0] == 'Create_parking_lot':
            parking_obj.Create_parking_lot(split_txt[1])
        elif split_txt[0] == 'Park':
            parking_obj.park_vehicle(split_txt)
        elif split_txt[0] == 'Slot_numbers_for_driver_of_age':
            parking_obj.get_all_slots_of_driver_age(split_txt)
        elif split_txt[0] == 'Slot_number_for_car_with_number':
            parking_obj.get_slot_number_of_car_number(split_txt)
        elif split_txt[0] == 'Leave':
            parking_obj.leave_parking_space(split_txt)  
        elif split_txt[0] == 'Vehicle_registration_number_for_driver_of_age':
            parking_obj.get_vechical_registration_number(split_txt)
        else:
            print("Command Not found. Kindly check your commad and change it in your input file :- ", split_txt[0])    


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-in", "--input_file", required=True, help="name of the user")
    args = vars(ap.parse_args())
    main_execution(args['input_file'])
       