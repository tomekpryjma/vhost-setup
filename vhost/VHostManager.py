import sys
from helpers.cleanup import cleanup
from vhost.VHostCreate import VHostCreate
from vhost.system_support import os_is_supported, server_is_supported

class VHostManager:
    def __init__(self, arguments, working_directory):
        self.arguments = arguments
        self.working_directory = working_directory
        self.creator = VHostCreate(arguments, working_directory)
    
    def init(self):

        if os_is_supported() and server_is_supported():
            if self.arguments.disable:
                print("===============")
                print("Disabling VHost")
                print("")
                cleanup(self.arguments, self.working_directory)
            else:
                print("==============")
                print("Enabling VHost")
                print("")
                self.creator.init()
        else:
            sys.exit()