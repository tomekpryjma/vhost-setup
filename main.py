#!/usr/bin/python

import argparse
import config
from option_parser import define_options
from vhost.VHostManager import VHostManager

def main():
    user_config = config.DEFAULTS

    available_options = config.AVAILABLE_OPTIONS

    parser = argparse.ArgumentParser(description="Parse options")

    parser = define_options(parser)

    arguments = parser.parse_args()

    user_config = config.update(user_config, arguments)

    manager = VHostManager(user_config)

    manager.init()

if __name__ == "__main__":
    main()