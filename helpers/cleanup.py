import os
import config
from helpers.copy_file import copy_file
import helpers.apachectl as apachectl

def cleanup(arguments, working_directory):
    if os.path.isfile(config.APACHE2_SITES_AVAILABLE + arguments.domain_name + ".conf"):
        apachectl.a2dissite(arguments.domain_name + ".conf")
        remove_samples(working_directory)
        remove_apache2_vhost(arguments)
        remove_hosts_entries(arguments)
        apachectl.systemctl_reload_apache2()
    else:
        print("Nothing of this site is left to clean")

    print("Cleanup complete!")

def remove_samples(working_directory):
    sample_directory = working_directory + "/sample/"

    for file in os.listdir(sample_directory):
        if file.endswith(".conf"):
            os.remove(sample_directory + file)

    print("Sample files removed")

def remove_apache2_vhost(arguments):
    vhost_file = config.APACHE2_SITES_AVAILABLE + arguments.domain_name + ".conf"

    if os.path.exists(vhost_file):
        os.remove(vhost_file)

    print("Apache2 conf file removed")

def remove_hosts_entries(arguments):
    vhost_filename = arguments.domain_name + "." + arguments.tld
    prefixed_vhost_filename = "www." + arguments.domain_name + "." + arguments.tld
    hosts_entry = "127.0.0.1 " + vhost_filename
    hosts_entry_alias = "127.0.0.1 " + prefixed_vhost_filename
    hosts_infile = None
    hosts_backup = copy_file(config.HOSTS_FILE, config.HOSTS_FILE + "__backup");
    
    if hosts_backup:
        with open(config.HOSTS_FILE, 'r') as read_hosts:
            hosts_infile = read_hosts.readlines()

        with open(config.HOSTS_FILE, "w") as hosts:
            for line in hosts_infile:
                if line.strip("\n") not in [hosts_entry, hosts_entry_alias]:
                    hosts.write(line)
        os.remove(hosts_backup)


        print("Hosts file entries removed")

    else:
        raise Exception("Failed to create a backup hosts file. Aborting.");