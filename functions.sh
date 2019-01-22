source formatting.sh

# Text formatting functions
function greenText {
    printf "${GREEN}$1${NC}"
}
function redText {
    printf "${RED}$1${NC}"
}

function greenBg {
    printf "${BG_GREEN}$1${RESET_ALL}\n"
}
function blueBg {
    printf "${BG_BLUE}$1${RESET_ALL}\n"
}
function redBg {
    printf "${BG_RED}$1${RESET_ALL}\n"
}
function darkGreyBg {
    printf "${BG_DARK_GREY}$1${RESET_ALL}\n"
}

# Message functions
function onlyTheseTwoOptionsAllowed {
    printf "Only ${BOLD}$1${RESET_ALL} and ${BOLD}$2${RESET_ALL} are accepted.\n"
}