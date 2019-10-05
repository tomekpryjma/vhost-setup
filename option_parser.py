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
        "-p",
        "--provision",
        default=False,
        action="store_true",
        dest="provision",
        help="Automatically creates the site folder in your WEB_ROOT.")

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

    return parser

def sanitise(arguments):
    arguments = remove_trailing_slash_in_path_arguments(arguments)
    arguments = with_concatonated_site_root(arguments)
    return arguments

def with_concatonated_site_root(arguments):
    default_site_root = arguments.web_root + '/' + arguments.domain_name

    if arguments.site_root is None:
        arguments.site_root = default_site_root
    else:
        arguments.site_root = default_site_root + "/" + arguments.site_root
    
    return arguments

def remove_trailing_slash_in_path_arguments(arguments):
    web_root = arguments.web_root
    site_root = arguments.site_root

    if web_root.endswith("/"):
        arguments.web_root = web_root[:-1]
    
    if site_root is not None and site_root.endswith("/"):
        arguments.site_root = site_root[:-1]
    
    return arguments
    
