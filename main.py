import os
import sys
import argparse
from option_parser import define_options, sanitise
from vhost.VHostManager import VHostManager

def main():
    working_directory = os.path.dirname(os.path.realpath(__file__))

    parser = argparse.ArgumentParser(description="Parse options")

    parser = define_options(parser)

    arguments = parser.parse_args()

    arguments = sanitise(arguments)

    manager = VHostManager(arguments, working_directory)

    manager.init()

    sys.exit()

if __name__ == "__main__":
    main()