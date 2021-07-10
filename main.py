import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

ser = serial.Serial("COM2", 9600)
#print(ser.readline())
a = []
str1 = str(ser.readline())
a = str1.split(",")

A_X = a[0]
A_X = A_X[8:]
A_Y = a[1]
A_Y = A_Y[6:]
A_Z = a[2]
A_Z = A_Z[7:]
SW = a[3]
SW = SW[0:][:-5]

print(A_X)
print(A_Y)
print(A_Z)
print(SW)

res = 1
i = 0
time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
    cc = str(1234)
    #print(cc)
    val = cc
    firebase1 = firebase.FirebaseApplication('https://earthquake-prediction-54c20-default-rtdb.firebaseio.com/', None)

    for i in range(0, 4):
        #string1 = "123"
        # string1=str(ser.readline())
        # string1=string1[9:][:-6]
        data = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': A_X,
                'time': datetime.now().strftime("%H:%M")
                }
        result = firebase1.patch(
            'https://earthquake-prediction-54c20-default-rtdb.firebaseio.com/' + '/A_X_data/' + str(i), data)
        print(result)

    for i in range(0, 4):
        #string2 = "123"
        # string1=str(ser.readline())
        # string1=string1[9:][:-6]
        data1 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': A_Y,
                 'time': datetime.now().strftime("%H:%M")
                 }
        result1 = firebase1.patch('https://earthquake-prediction-54c20-default-rtdb.firebaseio.com/' + '/A_Y_data/' + str(i),
                                  data1)
        print(result1)
    for i in range(0, 4):
        # string1 = "123"
        # string1=str(ser.readline())
        # string1=string1[9:][:-6]
        data = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': A_Z,
                'time': datetime.now().strftime("%H:%M")
                }
        result = firebase1.patch(
            'https://earthquake-prediction-54c20-default-rtdb.firebaseio.com/' + '/A_Z_data/' + str(i), data)
        print(result)
    for i in range(0, 4):
        # string1 = "123"
        # string1=str(ser.readline())
        # string1=string1[9:][:-6]
        data = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': SW,
                'time': datetime.now().strftime("%H:%M")
                }
        result = firebase1.patch(
            'https://earthquake-prediction-54c20-default-rtdb.firebaseio.com/' + '/SW_data/' + str(i), data)
        print(result)
    res = 0

