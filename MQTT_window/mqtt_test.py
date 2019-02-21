import paho.mqtt.client as mqtt
import csv
import threading
TEMP_filename = "Data/Temp.csv"
HUMI_filename = "Data/Humi.csv"
TH_filename = "Data/Th.csv"
CDS_filename = "Data/Temp.csv"
VR_filename = "Data/Humi.csv"
SOUND_filename = "Data/Temp.csv"
ULTRA_filename = "Data/Ultra.csv"
all_filename = "Data/alldata.csv"

def writeCsv(filename, data):
    f = open(filename, "a", encoding="utf-8", newline="")
    print(data)
    list_data = data.split(",")
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=",")           # delimiter 는 다음 값을 연결할때 쓰일 문자를 적음
    writer.writerow(list_data)
    # out_data = data+","
    # f.write(out_data)
    f.close()


def on_connect(client, userdata, flags, rc):
    # client.subscribe("icore-sdp/temp")
    # client.subscribe("icore-sdp/humi")
    # client.subscribe("icore-sdp/temp-humi")
    client.subscribe("icore-all")


def on_message(client, userdata, msg):
    str_topic = msg.topic
    str_payload = msg.payload.decode()
    # if str_topic == "icore-sdp/temp":
    #     #print(str_payload)
    #     writeCsv(TEMP_filename, str_payload)
    # if str_topic == "icore-sdp/humi":
    #     #print(str_payload)
    #     writeCsv(HUMI_filename, str_payload)
    # if str_topic == "icore-sdp/temp-humi":
    #     writeCsv(TH_filename, str_payload)
    if str_topic == "icore-all":
        writeCsv(all_filename, str_payload)


try:
    # all_label = "Temp,Humi,Light,Ultrasonic,Cds,Vr,Sound"
    # writeCsv(all_filename,all_label)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("192.168.101.101", 1883, 60)
    client.loop_forever()
finally:
    print("cleanup")
    client.disconnect()
