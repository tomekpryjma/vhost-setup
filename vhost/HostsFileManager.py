import config

class HostsFileManager:
    def create_entry(vhost_name):
        entry = "127.0.0.1 " + vhost_name + "\n"
        entry_alias = "127.0.0.1 " + "www." + vhost_name + "\n"

        try:
            with open(config.HOSTS_FILE, 'a') as hosts:
                hosts.write(entry)
                hosts.write(entry_alias)

            return True

        except Exception as error:
            print(error)
