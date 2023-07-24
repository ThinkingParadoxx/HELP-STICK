# import serial
# import tensorflow as tf
# # from tensorflow import keras
# from tensorflow import keras
# import numpy as np

# # Configure the serial port

# port = "COM4"

# baudrate = 19200

# # Open the serial port
# ser = serial.Serial(port, baudrate)

# model = keras.models.load_model("finalModel2.h5")

# data_entry=[]
# def process_data(data):
#     predi=model.predict(data)
#     if predi[0]>0.5:
#         print("Predictions: Fall")
#     else:
#         print("Predictions: Not Fall")
        
# # Read and print the real-time data
# while True:
#     try:
#         # Read a line from the serial port
#         line = ser.readline().decode().strip()
        
#         # Split the line into individual values
#         values = line.split(",")
#         values = np.array(values)
#         values = values.astype(float)
#         data_entry.append(values)
#         # Print the values
#         # print("AccX: {}, AccY: {}, AccZ: {}, GyroX: {}, GyroY: {}, GyroZ: {}, Roll: {}, Pitch: {}, Yaw: {}".format(
#         #     values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]
#         # ))
#         if len(data_entry) == 50:
#             process_data(np.array([data_entry]))
#             data_entry = []
        
#     except KeyboardInterrupt:
#         # Exit the loop if Ctrl+C is pressed
#         break

# # Close the serial port
# ser.close()
import serial
import tensorflow as tf
from tensorflow import keras
import numpy as np
import codecs

# Configure the serial port
port = "COM4"
baudrate = 19200

# Open the serial port
ser = serial.Serial(port, baudrate)

model = keras.models.load_model("modelpresentation.h5")
data_entry=[]
def process_data(data):
    predi=model.predict(data)
    if predi[0]>0.5:
        data="1"
        ser.write(data.encode("utf-8"))        
        print("Predictions: Fall")
    else:
        data="0"
        ser.write(data.encode("utf-8"))
        print("Predictions: Not Fall")
        
# Read and print the real-time data
while True:
    try:
        # Read a line from the serial port
        line = ser.readline().decode("utf-8").strip()
        
        # Split the line into individual values
        values = line.split(",")
        values = np.array(values)
        values = values.astype(float)
        data_entry.append(values)
        # Print the values
        # print("AccX: {}, AccY: {}, AccZ: {}, GyroX: {}, GyroY: {}, GyroZ: {}, Roll: {}, Pitch: {}, Yaw: {}".format(
        #     values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]
        # ))
        if len(data_entry) == 50:
            process_data(np.array([data_entry]))
            data_entry = []
        
    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        break

# Close the serial port
ser.close()