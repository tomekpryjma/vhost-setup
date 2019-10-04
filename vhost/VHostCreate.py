import os
import fileinput
import config
from helpers.copy_file import copy_file
from vhost.HostsFileManager import HostsFileManager

class VHostCreate:
    def __init__(self, arguments, working_directory):
        self.arguments = arguments
        self.sample_directory = working_directory + "/sample/"
        self.sample_conf = self.sample_directory + "vhost.txt"
        self.temp_conf = self.sample_directory + "tmp.vhost.conf"
        self.vhost_filename = ""
    
    def init(self):
        arguments = {
            'domain_name': self.arguments.domain_name,
            'tld': self.arguments.tld,
            'web_root': self.arguments.web_root,
            'site_root': self.arguments.site_root
        }

        self.vhost_filename = arguments["domain_name"] + ".conf"

        temp_conf = copy_file(self.sample_conf, self.temp_conf)

        values_replaced = self.replace_placeholder_values(temp_conf, arguments)

        vhost_conf = self.make_vhost_conf(temp_conf)

        apache2_vhost = self.move_vhost_to_apache2_sites_available(vhost_conf)

        if not apache2_vhost:
            return

        hosts_entry_created = self.create_hosts_entry()

    def replace_placeholder_values(self, temp_conf, arguments):
        try:
            with fileinput.FileInput(temp_conf, inplace=True) as file:
                for line in file:
                    line = line.replace("DOMAIN_NAME", arguments["domain_name"])
                    line = line.replace("TLD", arguments["tld"])
                    line = line.replace("WEB_ROOT", arguments["web_root"])
                    line = line.replace("SITE_ROOT", arguments["site_root"])

                    print(line, end="")
            
            return True

        except Exception as err:
            print("FATAL ERROR whilst writing to temp conf file: {0}".format(err))
            

    def make_vhost_conf(self, temp_conf):
        vhost_conf = self.sample_directory + self.vhost_filename

        return copy_file(temp_conf, vhost_conf)

    def move_vhost_to_apache2_sites_available(self, vhost_conf):
        sites_available = config.APACHE2_SITES_AVAILABLE

        if not os.path.exists(sites_available + self.vhost_filename):
            return copy_file(vhost_conf, sites_available + self.vhost_filename)
        else:
            try:
                raise Exception("The VHost " + self.vhost_filename + " already exists!")
            except Exception as error:
                print(error)
    
    def create_hosts_entry(self):
        HostsFileManager.create_entry(self.vhost_filename)