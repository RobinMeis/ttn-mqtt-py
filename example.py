from ttn_mqtt import ttn_mqtt
from ttn_mqtt import ttn_constants
from ttn_mqtt import ttn_device

def test_node_callback(payload):
    print("The callback was fired")
    print(payload)

ttn = ttn_mqtt.ttn_mqtt(ttn_constants.EU, "Application ID", "Application access key") #Open connection

test_node = ttn_device.device("node-id") #Register node
test_node.set_uplink_callback(test_node_callback)
ttn.register_device(test_node)

ttn.connect() #Connect to TTN

input("Press button to stop")
ttn.disconnect()
