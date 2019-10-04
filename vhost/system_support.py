import os
from sys import platform

def os_is_supported():
    if platform not in ['linux', 'linux2']:
        print("Only the Linux OS is supported.")
        return False
    return True

def server_is_supported():
    if not os.path.isdir("/etc/apache2"):
        print("Only Apache2 is supported.")
        return False
    return True