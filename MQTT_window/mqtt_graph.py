import paho.mqtt.client as mqtt
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors, rc, font_manager
TEMP_filename = "Data/Temp.csv"
HUMI_filename = "Data/Humi.csv"
TH_filename = "Data/Th.csv"
CDS_filename = "Data/Temp.csv"
VR_filename = "Data/Humi.csv"
SOUND_filename = "Data/Temp.csv"
ULTRA_filename = "Data/Ultra.csv"
all_filename = "Data/alldata.csv"


def readCsv(filename):
    f = open(filename, "r", encoding="utf-8")
    temp = []
    for row in csv.reader(f):                      # csv.reader()함수를 이용하면 리스트로 보내준다
        temp.append(row)
    f.close()
    return temp


# temp = readCsv(TEMP_filename)
# humi = readCsv(HUMI_filename)
# temp_humi = readCsv(TH_filename)

all_data = readCsv(all_filename)


temp_arr = []
humi_arr = []
light_arr = []
ultra_arr = []
cds_arr = []
vr_arr = []
sound_arr = []
bar_width = 0.45
print(len(all_data))
for i in range(0, len(all_data)):
    if i == 0:
        pass
    else:
        temp_arr.append(float(all_data[i][0]))
        humi_arr.append(float(all_data[i][1]))
        light_arr.append(float(all_data[i][2]))
        ultra_arr.append(float(all_data[i][3]))
        cds_arr.append(int(all_data[i][4]))
        vr_arr.append(int(all_data[i][5]))
        sound_arr.append(int(all_data[i][6]))


x = np.arange(len(temp_arr))
y = np.array(all_data[0])
print(y)
print(x)
plt.plot(x, temp_arr, "ro-", label="Temp")
plt.plot(x, humi_arr, "go-", label="Humi")
plt.plot(x, light_arr, "bo-", label="Light")
plt.plot(x, ultra_arr, "ko-", label="Ultra")
plt.plot(x, cds_arr, "co-", label="Cds")
plt.legend(loc=5)
plt.legend(loc="upper center", bbox_to_anchor=(0.3,1.2), ncol=3)

plt.xlabel("Count")
plt.ylabel("Value")
plt.tight_layout()
# plt.plot(x, vr_arr, color="wo")

# plt.subplot(1, 2, 1)
# plt.bar(x, temp_arr, bar_width, color="r")
# plt.bar(x+0.2, humi_arr, bar_width, color="g")
# plt.bar(x+0.4, light_arr, bar_width, color="b")
# plt.bar(x+0.6, ultra_arr, bar_width, color="k")
# plt.subplot(1, 2, 2)
# plt.bar(x+0.2, cds_arr, bar_width, color="r")
# plt.bar(x+0.4, vr_arr, bar_width, color="g")
# plt.bar(x+0.6, sound_arr, bar_width, color="b")
# plt.xlabel("Count")
# plt.ylabel("%")
# plt.tight_layout()


plt.show()
