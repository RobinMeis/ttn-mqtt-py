import paho.mqtt.client as mqtt
import json
import base64
import os.path
import warnings

class ttn_mqtt:
    def __init__(self, region, application_id, application_access_key, tls=True, mqtt_ca="mqtt-ca.pem"):
        self.host = "%s.thethings.network" % (region,) #Create hostnamee

        self.mqtt_ca = mqtt_ca
        if (tls): #Check for TLS
            if (os.path.exists(mqtt_ca)):
                self.tls = True
                self.port = 8883
            else:
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

    def connect(self): #Connect to TTN
        self.client.connect_async(self.host, self.port, 60)
        self.client.loop_start()

    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def register_device(self):
        pass
