## Parking_simulation

# Setup steps

1 - Clone the Repositery 
```
git clone 
```
2 - cd to your folder where you have cloned the code. For example suppose you have cloned it in document/priyank
```
cd Documents/priyank
```
3 - Install All the requirements mentioned in requirements.txt . You need to have python and pip installed in your system. You can also Download it from [here](https://www.python.org/downloads/)
```
pip install -r requirements.txt
```
NOTE :- In the code I have not used any external libraries so ```requirements.txt``` will be empty.  All the dependencies and In-built libraries will be auto installed with python.

4 - Run the Code with the command
```
python parking_functions.py --in <your input file name with .txt extension>
```



# Edge Cases Covered
1 - If length of car is less than (<) or Greater than (>) function will Return and Print the Appropriate message. 
```
Car number is not of Valid Length. It should be Exactly 13.
```

2 - If Parking Space is full and a vechicle tries to enter then function will show the appropriate message. 
```
Parking Space is Not Available. It is full.
```

3 - If a Car is Already parked and we try to park the same car then the function will show the message 
```
Car is already parked at slot Number 4.
```

# Assumptions
1 - All Car Number Length should be 13.

2 - All Car will have Unique registration number.

3 - Commands Will be in Right Format

4 - Create_parking_lot function will be at starting of the Code file.
