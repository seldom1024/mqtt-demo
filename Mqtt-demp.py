# doc https://pypi.org/project/paho-mqtt/#publishing


#!/usr/bin/python

import datetime

# ======================================================
try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("MQTT client not find. Please install as follow:")
    print("git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git")
    print("cd org.eclipse.paho.mqtt.python")
    print("sudo python setup.py install")
    print("or pip install paho-mqtt")

# 服务器地址
strBroker = "mqtt-broker.rootcloud.com"
# 通信端口
port = 1883
# 用户名
username = 'wmmp-zl'
# 密码
password = 'wmmpwmmp'
# 订阅主题名
topic = 'v4/s/set/thing/live/json/1.0'


# ======================================================
def on_connect(mqttc, obj, rc):
    print("OnConnetc, rc: " + str(rc))


def on_publish(mqttc, obj, mid):
    print("OnPublish, mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print("Log:" + string)


def on_message(mqttc, obj, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
    print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    on_exec(str(msg.payload))


def on_exec(strcmd):
    print("Exec:", strcmd)


# =====================================================
if __name__ == '__main__':
    mqttc = mqtt.Client("test")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.on_log = on_log

    # 设置账号密码（如果需要的话）
    mqttc.username_pw_set(username=username, password=password)

    mqttc.connect(strBroker, port, 60)
    print(mqttc.is_connected())
    mqttc.subscribe(topic, 0)
    mqttc.loop_start()
