import shutil

class VHostCreate:
    def __init__(self, arguments, working_directory):
        self.arguments = arguments
        self.working_directory = working_directory
        self.sample_conf = self.working_directory + "/sample/vhost.txt"
        self.temp_conf = self.working_directory + "/sample/tmp.vhost.conf"

        self.create_temporary_conf_from_sample()

    def create_temporary_conf_from_sample(self):
        shutil.copy(self.sample_conf, self.temp_conf)

    def write_apache2_conf(self):
        pass