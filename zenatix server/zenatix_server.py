import time
def read_cloud():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://bmp180-1569c-default-rtdb.firebaseio.com', None)
    result = firebase.get('/main_test/1-set', '')

    file = open('bmp_180.csv','a')
    timer = str(result['timestamp'])
    value = str(result['sensor_data'])
    sensor = str(result['sensor'])
    data = ",".join([timer,value,sensor])
    file.write(data)
    print(data)
    time.sleep(3)

while True:
    read_cloud()