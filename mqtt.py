# ======================================================
try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("MQTT client not find. Please install as follow:")
    print("git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git")
    print("cd org.eclipse.paho.mqtt.python")
    print("sudo python setup.py install")
    print("or pip install paho-mqtt")


# connect addr
strBroker = "mqtt-broker.rootcloud.com"
# connect port
port = 1883
# username
username = 'wmmp-zl'
# password
password = 'wmmpwmmp'
# subscribe topic
subscribe_topic = 'v4/s/set/thing/live/json/1.0'
# publish topic
publish_topic = 'v4/p/post/thing/live/json/1.1'


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(publish_topic)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


# Log
def on_log(mqttc, obj, level, string):
    print("Log:" + string)


# Set action
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

# Set username and password,this is optional
client.username_pw_set(username="wmmp-zl", password="wmmpwmmp")

# Set the server addr and port and connect timeout
client.connect("mqtt-broker.rootcloud.com", 1883, 60)

# Publish message to server
# payload need to construct
client.publish(topic=publish_topic,
               payload='''{"body":{"things":[{"id":"test1111","items":[{"properties":{"wendu":66.67},"qBad":[],"ts":1605431052409}],"thingType":"Device"}]}}''',
               qos=0)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
