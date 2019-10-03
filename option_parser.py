"""
Need:

1. Web Root [/var/www/html]
2. Domain name
3. TLD [local]
4. Remove domain folder [false]

"""
def define_options(parser):

    parser.add_argument(
        "domain_name",
        nargs=1,
        help="This is the name of the folder where your site's files are.")

    parser.add_argument(
        "-d",
        "--disable",
        default=False,
        action="store_true",
        help="Tell the script to disable an existing VHost.")

    parser.add_argument(
        "-w",
        "--web-root",
        nargs=1,
        default="/var/www/html",
        metavar="/path/to/sites",
        help="Tell the script where your domain's folder is.")

    parser.add_argument(
        "-t",
        "--tld",
        nargs=1,
        default="local",
        help="Tell the script what legal TLD you want your domain to end with.")

    parser.add_argument(
        "-r",
        "--remove-domain-folder",
        default=False,
        action="store_true",
        help="Tell the script if you want the domain folder to be deleted.")

    return parser