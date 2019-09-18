#!/bin/bash
source formatting.sh
source functions.sh

domain=""
extension="local"


checkCommandSuccess() {
    if [ $? -eq 0 ]; then
        greenBg "OK"
    else
        redBg "FAILED"
        exiting
    fi
}

exiting() {
    redBg "Failed to remove the VHost."
    exit
}

removeVhost() {
    sudo rm temp-vhosts/$domain.$extension.conf

    checkCommandSuccess
}

removeHostsEntry() {
    sudo sed -i "s/127.0.0.1 ${domain}.${extension}//g" hosts-sample

    checkCommandSuccess
}

usage() {
    echo
    echo "Usage"
    echo "--------------"
    echo "  -u <domain>          Removes the VHost, hosts entry & domain from your webroot."
    echo "  -e [extension]       Set the extension of your domain, default is 'local'. (e.g. domain.local)"
}

run() {
    sudo -v > /dev/null

    echo "Removing $domain.$extension..."

    removeVhost

    removeHostsEntry

    if [ $? -eq 0 ]; then
        greenBg "Successfully removed the VHost!"

    else
        exiting
    fi
}

while getopts ":u:e:h" option; do
    case "${option}" in
        u)
            domain=${OPTARG}
            ;;
        e)
            extension=${OPTARG}
            ;;

        h)
            usage
            exit
            ;;

        *)
            echo "Option $1 not supported."
            ;;
    esac
done
shift $((OPTIND-1))

if [ ! -z "$domain" ]; then
    run
else
    echo "Missing required options. Run -h to see a list of options."
    exit
fi