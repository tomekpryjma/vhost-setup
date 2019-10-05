# VHost Setup

The script is meant to make it quick and painless to set up & remove vhosts.

### Usage

**Since the script writes to `/etc/hosts`, `/etc/apache/sites-available` & runs `ctl` commands, it needs `sudo` privilages.**

**Example:**

`sudo python3 main.py project --web-root /is/somehwere/else --provision`


------------

#### Full list of options

```
usage: main.py [-h] [-d] [-p] [-w /path/to/sites] [-s /path/to/site/files]
               [-t local]
               domain_name

Parse options

positional arguments:
  domain_name           This is the name of the folder where your site's files
                        are.

optional arguments:
  -h, --help            show this help message and exit
  -d, --disable         Tell the script to disable an existing VHost.
  -p, --provision       Automatically creates the site folder in your
                        WEB_ROOT.
  -w /path/to/sites, --web-root /path/to/sites
                        Tell the script where your domain's folder is.
  -s /path/to/site/files, --site-root /path/to/site/files
                        Tell the script where your domain's files are. Uses
                        DOMAIN by default.
  -t local, --tld local
                        Tell the script what legal TLD you want your domain to
                        end with. Default is local.
```


## Support

So far the script only supports Linux machines running the Apache2 webserver.