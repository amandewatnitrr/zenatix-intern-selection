# Zenatix-Intern-Selection
<p align="center"><img style="float=left;" src="https://github.com/amandewatnitrr/evolution-hacknitr/blob/main/imgs/bb0cc783196fa9b2119864ff90eb5702.gif" width="50%"/></p>

## Problem Statement:

Consider that an IoT device publishes data to your middleware software which is then published to the cloud.

While you are developing an IoT solution, you do not have access to all the physical sensors and therefore you decide to simulate all types of sensors that exist in a candy factory. A CSV is shared which contains simulated sensor data.

As an IoT developer, 

### Edge Program - 
You have to write a forever executable python program to read sensor data and send it to the cloud server.
### Server Program - 
A simple python HTTP server or MQTT broker to accept data(as per your convenience) and save it in a CSV file.

## Goals:

### Server Program - 
Expose a route on an HTTP server or a topic on MQTT broker which accepts data. It should randomly give success or failure for the received data. Each new data should append to a CSV file.<br>

### Edge Program
1. Each data point should be read after every 60-sec delay and publish to the cloud(live data)
2. If the server returns failure or server is stopped the data point is buffered locally(it now becomes buffered data). 
3. Publish all the buffered data after every 5 seconds. While cleaning the buffered data the live data should not be stopped, i.e. the program should be properly multithreaded.
4. Example: 1st & 2nd minute, 1st & 2nd data points published successfully, 3rd & 4th minute, 3rd & 4th data points failed and got buffered, 5th min 5th datapoint and all the buffered data published.
5. Expose a function to get the count of successfully transmitted and buffered data at any point in time.


## Guidelines:

1. For local buffering of data on the Edge program, you can use any queueing mechanism or open-source software.
2. Please do add requirements.txt file in code

# Solution
!['IoT Architecture'](https://github.com/amandewatnitrr/zenatix-intern-selection/blob/main/iot_architecture.png)

## Setting Up 
1. cd to the directory where requirements.txt is located.
2. Run in shell below command.
```Terminal
pip install -r requirements.txt
```

## Edit config section in the Edge code

1. You must have created your own Realtime Firebase Database

```Python
config = {
  "apiKey": "database-secret", # Found in Service Settings
  "authDomain": "bmp180-1569c.firebaseapp.com", # Replace 'bmp180-1569c' with your database id
  "databaseURL": "https://bmp180-1569c-default-rtdb.firebaseio.com", # Create a relational database and replace the link here
  "storageBucket": "bmp180-1569c.appspot.com" # Replace 'bmp180-1569c' with your database id
}
```
2. This particular section will obtain the previous data from firebase before pushing the live data

```Python
firebase = firebase.FirebaseApplication('https://bmp180-1569c-default-rtdb.firebaseio.com', None) # Replace with the Relational Database link here
result = firebase.get('/main_test/1-set/','') # Replace with name of the branch node where you are storing the data
```
3. Edit this ection in edge file to make sure data is being writtten to a specific node with name of your choice.
```Python
data = {"timestamp":t,"sensor_data":float(k),"sensor":s} # Name of the nodes respective to variable 
db.child("main_test").child("1-set").set(data) # Node Brach name where data is being pushed
```
