import sys
from vhost.VHostCreate import VHostCreate
from vhost.system_support import os_is_supported, server_is_supported

class VHostManager:
    def __init__(self, config):
        self.config = config
    
    def init(self):

        if os_is_supported() and server_is_supported():
            if self.config["disable"]:
                print("Will disable the VHOST.")
            else:
                print("Setting up...")
        else:
            sys.exit()

    def enable():
        pass

    def write_apache2_conf():
        pass