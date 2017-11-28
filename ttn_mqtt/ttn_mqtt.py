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

    def connect(self):
        if (self.tls):
            self.client.tls_set(ca_certs=self.mqtt_ca)

        self.client.connect(self.host, self.port, 60)
