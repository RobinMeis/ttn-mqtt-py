import paho.mqtt.client as mqtt
import json
import base64
import os.path
import warnings

class ttn_mqtt:
    def __init__(self, region, application_id, application_access_key, tls=True, mqtt_ca="mqtt-ca.pem"):
        self.host = "%s.thethings.network" % (region,) #Create hostname
        self.application_id = application_id

        self.mqtt_ca = mqtt_ca
        if (tls): #Check for TLS
            if (os.path.exists(mqtt_ca)):
                self.tls = True
                self.port = 8883
            else: #Fallback if cert not found
                warnings.warn("Warning: mqtt-ca.pem could not be found. Fallback to plain", Warning)
                self.tls = False
                self.port = 1883
        else:
            self.port = 1883
            self.tls = False

        self.client = mqtt.Client() #Prepare MQTT Client
        self.client.username_pw_set(application_id, password=application_access_key)
        if (self.tls): #Setup TLS
            self.client.tls_set(ca_certs=self.mqtt_ca)

        self.client.on_connect = self._on_connect #Register callbacks
        self.client.on_message = self._on_message

        self.devices = [] #Create empty device list

    def connect(self): #Connect to TTN
        self.client.connect_async(self.host, self.port, 60)
        self.client.loop_start()

    def disconnect(self): #Disconnect from TTN
        self.client.disconnect()

    def _on_connect(self, client, userdata, flags, rc):
        if (rc!=0): warnings.warn("Connected with result code "+str(rc), Warning)

        for device in self.devices: #Subscribe devices to MQTT
            client.subscribe("%s/devices/%s/up" % (self.application_id, device.DevID))

    def _on_message(self, client, userdata, msg):
        topic = msg.topic.split("/")
        payload_decoded = json.loads(msg.payload.decode('UTF-8'))

        if (payload_decoded["payload_raw"] != None):
            payload_decoded["payload_bytes"] = [] #Convert payload to bytes
            for byte in base64.b64decode(payload_decoded["payload_raw"]):
                payload_decoded["payload_bytes"].append(byte)

        if (topic[-1] == 'up'): #Handle uplink messages
            for device in self.devices:
                if (device.getDevID() == payload_decoded["dev_id"]):
                    if (device.callbacksActive() and device.uplink_callback): #Fire callback if callbacks are enabled for this device
                        device.uplink_callback(payload_decoded)

        else:
            warnings.warn("Warning: Received (currently) unsupported message topic", Warning)


    def register_device(self, device_object): #Add device object
        self.devices.append(device_object) #Add device object to devices list
        self.client.subscribe("%s/devices/%s/up" % (self.application_id, device_object.DevID)) #Subscribe to topic (if connection is established)
