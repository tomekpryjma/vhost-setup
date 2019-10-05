import os

def apachectl(vhost_name):
    os.system("sudo apachectl configtest")
    a2ensite(vhost_name)
    systemctl_reload_apache2()

def a2ensite(vhost_name):
    return os.system("sudo a2ensite " + vhost_name)

def a2dissite(vhost_name):
    return os.system("sudo a2dissite " + vhost_name)

def systemctl_reload_apache2():
    return os.system("sudo systemctl reload apache2")