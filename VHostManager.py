class VHostManager:
    def __init__(self, config):
        self.config = config
    
    def init(self):
        if self.config["disable"]:
            print("Will disable the VHOST.")
        else:
            print("Setting up...")