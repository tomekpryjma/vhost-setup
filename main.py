import argparse
import config
from option_parser import define_options
from vhost.VHostManager import VHostManager

def main():
    parser = argparse.ArgumentParser(description="Parse options")

    parser = define_options(parser)

    arguments = parser.parse_args()

    manager = VHostManager(arguments)

    manager.init()

if __name__ == "__main__":
    main()