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
        help="This is the name of the folder where your site's files are.")

    parser.add_argument(
        "-d",
        "--disable",
        default=False,
        action="store_true",
        dest="disable",
        help="Tell the script to disable an existing VHost.")

    parser.add_argument(
        "-w",
        "--web-root",
        type=str,
        default="/var/www/html",
        metavar="/path/to/sites",
        dest="web_root",
        help="Tell the script where your domain's folder is.")

    parser.add_argument(
        "-s",
        "--site-root",
        type=str,
        default=None,
        metavar="/path/to/site/files",
        dest="site_root",
        help="Tell the script where your domain's files are. Uses DOMAIN by default.")

    parser.add_argument(
        "-t",
        "--tld",
        type=str,
        default="local",
        dest="tld",
        help="Tell the script what legal TLD you want your domain to end with.")

    parser.add_argument(
        "-r",
        "--remove-domain-folder",
        default=False,
        action="store_true",
        dest="disable",
        help="Tell the script if you want the domain folder to be deleted.")

    return parser

def with_concatonated_site_root(arguments):
    default_site_root = arguments.web_root + '/' + arguments.domain_name

    if arguments.site_root is None:
        arguments.site_root = default_site_root
    else:
        arguments.site_root = default_site_root + "/" + arguments.site_root
    
    return arguments