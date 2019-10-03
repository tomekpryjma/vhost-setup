DEFAULTS = {
    "disable": False,
    "domain_name": "",
    "web_root": "/var/www/html",
    "tld": "local",
    "remove_domain_folder": False
}

AVAILABLE_OPTIONS = [
    "disable",
    "domain_name",
    "web_root",
    "tld"
]

def update(config, arguments):
    for option_name in DEFAULTS.keys():
        config[option_name] = getattr(arguments, option_name)
    
    return config