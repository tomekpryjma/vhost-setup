import os
import shutil
import fileinput
from helpers.copy_file import copy_file

class StarterSite:
    def __init__(self, sample_directory, arguments):
        self.sample_directory = sample_directory
        self.arguments = arguments

    def init(self):
        directory_made = self.create_starter_site_directory()

        if not directory_made:
            raise Exception("Could not make site directory.")
    
        html_file = self.create_starter_html_file()

        self.move_html_file_to_site_directory(html_file)

        self.amend_permissions()

    def create_starter_site_directory(self):
        site_folder = self.arguments["site_root"]

        if not os.path.isdir(site_folder):
            os.mkdir(site_folder) # os.mkdir() doesn't return anything
            return True
        
        raise Exception("The site folder " + site_folder + " already exists!")
    
    def create_starter_html_file(self):
        html_file = copy_file(self.sample_directory + "index.html.txt", self.sample_directory + "index.html")

        try:
            with fileinput.FileInput(html_file, inplace=True) as file:
                for line in file:
                    line = line.replace("DOMAIN_NAME", self.arguments["domain_name"] + "." + self.arguments["tld"])

                    print(line, end="")
            
            return html_file

        except Exception as err:
            print("FATAL ERROR whilst writing to HTML file: {0}".format(err))
        
    def move_html_file_to_site_directory(self, html_file):
        site_directory = self.arguments["site_root"]
        return shutil.move(html_file, site_directory)

    def amend_permissions(self):
        site_directory = self.arguments["web_root"] + "/" + self.arguments["domain_name"]

        shutil.chown(site_directory, user=1000, group=1000)
        os.chmod(site_directory, 0o754)

        shutil.chown(site_directory + "/index.html", user=1000, group=1000)
        os.chmod(site_directory + "/index.html", 0o644)