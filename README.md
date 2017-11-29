# ttn-mqtt-py
Python3 MQTT Library for the TTN MQTT server. Currently only supports uplink messages. The full API Docs are located at: https://www.thethingsnetwork.org/docs/applications/mqtt/api.html

## Establish connection
To connect to the TTN MQTT server, you'll need to create a new ttn_mqtt handler:
```python
ttn_mqtt.ttn_mqtt(region, application_id, application_access_key)
```

### TLS
To use TLS, download certificate from TTN: https://console.thethingsnetwork.org/mqtt-ca.pem. If you place it in your applications root directory, TLS will be used by default. Otherwise you need to call the constructor like this to specify the certificates path:
```python
ttn_mqtt.ttn_mqtt(region, application_id, application_access_key, tls=True, mqtt_ca="mqtt-ca.pem")
```
If cert is missing, you'll get a warning and ttn-mqtt-py will fallback to plain mode.

### Plain
NOT RECOMMENDED! To disable TLS and ignore the TLS fallback warning, set ```tls=False```

### Regions
Regions are stored in ttn_constants according to https://www.thethingsnetwork.org/wiki/Backend/Connect/Gateway#connect-a-gateway_server-addresses

|Region|Comment                    |Constant         |
|------|---------------------------|-----------------|
|EU    |EU 433 and EU 863-870      |ttn_constants.EU |
|US    |US 902-928                 |ttn_constants.US |
|CN    |China 470-510 and 779-787  |ttn_constants.CN |
|AU    |Australia 915-928 MHz      |ttn_constants.AU |
|AS    |Southeast Asia 923 MHz     |ttn_constants.AS |
|AS1   |Southeast Asia 920-923 MHz |ttn_constants.AS1|
|AS2   |Southeast Asia 923-925 MHz |ttn_constants.AS2|
|KR    |Korea 920-923 MHz          |ttn_constants.KR |

## Get uplink messages
To receive uplink messages of your node, you need to create a new device object and pass it to the ttn MQTT handler.
### Register device
Class to create devices to listen for data. These devices can be added to an ttn_mqtt object.
```python
test_node = ttn_device.device("device_id") #Creates your device
test_node.set_uplink_callback(test_node_callback) #Sets an uplink data callback
ttn.register_device(test_node) #Adds your devices to the ttn.mqtt handler
```
### Callback
In order to process incoming messages the callback function is required. The incoming data is passed to your function:
```python
def test_node_callback(payload):
    print(payload)
```
The callback is enabled by default. It can be disabled using ```test_node.disable_callbacks()``` and re-enabled by calling ```test_node.enable_callbacks()```
