class device:
    def __init__(self, DevID):
        self.DevID = DevID
        self.uplink_callback = None
        self.active = True

    def set_uplink_callback(self, callback):
        self.uplink_callback = callback
