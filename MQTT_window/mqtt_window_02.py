import paho.mqtt.client as mqtt
import time
import csv
import matplotlib.pyplot as plt
from matplotlib import colors, rc, font_manager

TEMP_filename = "Data/Temp.csv"
HUMI_filename = "Data/Humi.csv"
CDS_filename = "Data/Temp.csv"
VR_filename = "Data/Humi.csv"
SOUND_filename = "Data/Temp.csv"
ULTRA_filename = "Data/Ultra.csv"

def MOTOR_msg_cntl(payload):
    if payload == 'CW':
        client.publish("icore-sdp/dc_motor", "CW")
    elif payload == 'SB':
        client.publish("icore-sdp/dc_motor", "STOP")

def PIR_msg_cntl(payload):
    if int(payload) % 10:
        pass
    else:
        client.publish("icore-sdp/buzzer", "ON")

def on_connect(client, userdata, flags, rc):
    # client.subscribe("icore-sdp/temp")
    #client.subscribe("icore-sdp/humi")
    client.subscribe("icore-sdp/cds")
    client.subscribe("icore-sdp/vr")
    client.subscribe("icore-sdp/sound")
    client.subscribe("icore-sdp/ir")
    client.subscribe("icore-sdp/jogsw")
    client.subscribe("icore-sdp/jogsw_active")
    client.subscribe("icore-sdp/pir")
    client.subscribe("icore-sdp/ultrasonic")

def on_message(client, userdata, msg):
    str_topic = msg.topic
    str_payload = msg.payload.decode()
    if str_topic == "icore-sdp/cds":
        client.publish("icore-sdp/tlcd1", msg.payload)
    if str_topic == "icore-sdp/vr":
        client.publish("icore-sdp/tlcd2", msg.payload)
    # if str_topic == "icore-sdp/sound":
    #     client.publish("icore-sdp/fnd", msg.payload)
    # if str_topic == "icore-sdp/jogsw":
    #     print("msg:", str_payload)
    if str_topic == "icore-sdp/jogsw_active":
        print("msg:", str_payload)
    if str_topic == "icore-sdp/ir":
        print("msg:", str_payload)
    if str_topic == "icore-sdp/cds":
        if int(str_payload[0:4]) < 1500:
            client.publish("icore-sdp/led1", "ON")
            client.publish("icore-sdp/led2", "ON")
        else:
            client.publish("icore-sdp/led1", "OFF")
            client.publish("icore-sdp/led2", "OFF")

    #if str_topic == "icore-sdp/pir":
        #client.publish("icore-sdp/fnd", msg.payload)
        #PIR_msg_cntl(str_payload)
    if str_topic == "icore-sdp/ultrasonic":
        client.publish("icore-sdp/ultrasonic_fnd", msg.payload)
    # str_payload = float(str_payload)
    # print(str_topic, str_payload)

    if str_topic == "icore-sdp/humi":
        if float(str_payload) > 40.0:
            MOTOR_msg_cntl("CW")
        else:
            MOTOR_msg_cntl("SB")

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)

    client.loop_forever()
finally:
    print("cleanup")
    #GPIO.cleanup()
    client.disconnect()
