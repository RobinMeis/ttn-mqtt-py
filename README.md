# ttn-mqtt-py
Python3 MQTT Library for TTN

=== TLS ===
To use TLS download certificate from TTN: https://console.thethingsnetwork.org/mqtt-ca.pem

=== Regions ===
Regions are stored in ttn_constants according to https://www.thethingsnetwork.org/wiki/Backend/Connect/Gateway#connect-a-gateway_server-addresses

|Region|Comment|Constant|
|------|-------|--------|
|EU    |EU 433 and EU 863-870      |ttn_constants.EU |
|US    |US 902-928                 |ttn_constants.US |
|CN    |China 470-510 and 779-787  |ttn_constants.CN |
|AU    |Australia 915-928 MHz      |ttn_constants.AU |
|AS    |Southeast Asia 923 MHz     |ttn_constants.AS |
|AS1   |Southeast Asia 920-923 MHz |ttn_constants.AS1|
|AS2   |Southeast Asia 923-925 MHz |ttn_constants.AS2|
|KR    |Korea 920-923 MHz          |ttn_constants.KR |
