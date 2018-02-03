from ttn_mqtt import ttn_mqtt
from ttn_mqtt import ttn_constants
from ttn_mqtt import ttn_device

def test_node_callback(payload):
    print(payload)

ttn = ttn_mqtt.ttn_mqtt(ttn_constants.EU, "Application ID (name, not EUI)", "Application access key (ttn-account-v2...)") #Open connection
ttn.connect() #Connect to TTN

test_node = ttn_device.device("node-id (name, not EUI)") #Register node
test_node.set_uplink_callback(test_node_callback)
ttn.register_device(test_node)


input("Press button to stop")
ttn.disconnect()
