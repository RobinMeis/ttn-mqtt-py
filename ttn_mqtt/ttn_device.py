class device:
    def __init__(self, DevID): #Creates a new device object
        self.DevID = DevID
        self.uplink_callback = None
        self.callbacks_active = True

    def set_uplink_callback(self, callback): #Configure function to be called on received uplink
        self.uplink_callback = callback

    def enable_callbacks(self): #Activate callbacks (enabled by default)
        self.callbacks_active = True

    def disable_callbacks(self): #Disable callbacks
        self.callbacks_active = False

    def getDevID(self): #Returns Device ID
        return self.DevID

    def callbacksActive(self): #Returns true if callbacks are active
        return self.callbacks_active
