#!/bin/bash
source formatting.sh
source functions.sh

scriptDirectory=$(cd `dirname $0` && pwd)
defaultSitesDirectory="/var/www/html"
sitesAvailableDirectory="/etc/apache2/sites-available"


projectTitle
projectPath
projectVHOST

function welcome {
    clear
    printf "These are the files and locations that this script will attepmt to edit:\n"
    printf "    1) ${BOLD}/etc/apache2/sites-available${RESET_ALL} (location)\n"
    printf "    2) ${BOLD}/etc/hosts${RESET_ALL} (file)\n"
    echo ""
    printf "The above are owned by the user: ${BOLD}root${RESET_ALL}.\n"
    printf "As a result, you will be prompted to enter your ${BOLD}sudo${RESET_ALL} password before the script continues."
    echo ""

    sudo -v > /dev/null
}

function confirmProjectPath {
    echo ""
    printf "Are your sites in ${BOLD}${defaultSitesDirectory}${RESET_ALL}? [y/n] - "; read pathIsCorrect

    case "${pathIsCorrect}" in
        y|Y)
            createProject
            ;;

        n|N)
            printf "Path of the directory in which you keep your sites - "; read customProjectPath
            setCustomProjectPath ${customProjectPath}
            ;;

        *)
            echo ""
            onlyTheseTwoOptionsAllowed "y" "n"
            confirmProjectPath
            ;;
    esac
}

function setCustomProjectPath {
    defaultSitesDirectory=$1
}

# Accepted default project path
function createProject {
    echo ""
    darkGreyBg " Creating the project directory "

    printf "What is the directory your project will be in? - "; read projectTitle

    projectPath="$defaultSitesDirectory/$projectTitle"

    echo ""
    blueBg " Creating project directory... "
    sleep 0.5

    mkdir "$projectPath"

    if [ -d "$projectPath" ]; then
        greenBg " Project directory created! "
        echo "Viewing output from <strong>${projectTitle}</strong> index.html" > "$projectPath/index.html"
        echo ""

        continueToVHOSTSetup
    else
        redBg "Failed to create directory!"
        exit
    fi
    echo ""
}

# VHost file setup
function replaceSampleVHostValues {
    # Replace path to project
    sudo sed -i s+PROJECT_PATH_OVERRIDE+"$projectPath"+g "$projectVHOST"
    # Replace sample domain
    sudo sed -i s+PROJECT_DIR_OVERWRITE+"$projectTitle"+g "$projectVHOST"

    greenBg " Successfully set up the VHost file for $projectTitle! "
}

function setUpVHOST {
    echo ""
    darkGreyBg " Setting up your VHost "
    echo ""

    sudo cp "$scriptDirectory/vhost-sample.conf" "$sitesAvailableDirectory/${projectTitle}.conf"

    projectVHOST=$sitesAvailableDirectory/${projectTitle}.conf

    if [ -f "$projectVHOST" ]; then
        blueBg " Replacing default VHost file values... "
        sleep 0.5
        
        replaceSampleVHostValues
    else
        redBg "Failed to generate VHost .conf file!"
        exit
    fi
}

function continueToVHOSTSetup {
    local userIsReady
    local userHasTemplateConf

    printf "\nAre you ready to set up your VHost file? [y/n] - "; read userIsReady

    case "${userIsReady}" in
        y|Y)
            setUpVHOST
            ;;
        n|N)
            cleanUp
            ;;
        *)
            onlyTheseTwoOptionsAllowed "y" "n"
            continueToVHOSTSetup
            ;;
    esac

}

# Hosts file edit
function editHostsFile {
    if [ -n "$projectTitle" ] && [ -n "$projectPath" ] && [ -n "$projectVHOST" ]; then
        
        local domain="${projectTitle}.local"
        local hostsString="127.0.0.1 $domain"

        echo ""

        blueBg " Updating hosts... "
        echo "$hostsString" | sudo tee -a /etc/hosts > /dev/null
        greenBg " Hosts updated! "

        echo ""

        blueBg " Enabling site and restarting Apache... "
        handleApache
        greenBg " Site enabled and Apache restarted successfully! "

        echo ""

        victory
    else
        redBg " Something has gone wrong... "
        cleanUp
    fi
}

function victory {
    blueBg " Victory! "
    greenBg " Visit: ${BOLD}http://$projectTitle.local "
}

function handleApache {
    sudo a2ensite "${projectTitle}.conf" > /dev/null
    sudo systemctl reload apache2
}

function cleanUp {
    blueBg " Exiting... "
    sleep 0.5

    if [ -d "$projectPath" ]; then
        blueBg " Removing ${BOLD}${projectTitle} "
        rm -r "$projectPath"
        sleep 0.15
    fi

    if [ -f "$projectVHOST" ]; then
        blueBg " Disabling ${BOLD}${projectTitle} "
        sudo a2dissite "${projectTitle}.conf" > /dev/null
        sleep 0.15
    fi

    if [ -f "$projectVHOST" ]; then
        blueBg " Removing ${BOLD}${projectTitle}.conf "
        sudo rm "${projectVHOST}.conf"
        sleep 0.15
    fi

    redBg "${BOLD}Bye!"
}

function run {
    welcome
    confirmProjectPath
    editHostsFile
}

run

exit