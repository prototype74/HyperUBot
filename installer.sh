#!/bin/bash
# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

RED="\033[91m"
GREEN="\033[92m"
YELLOW="\033[93m"
END="\033[0m"

function setColor() {
    echo "$1$2${END}"
}

if ([ -f ./userbot/__init__.py ] && \
    [ -f ./userbot/__main__.py ]) || \
   ([ -d ./HyperUBot ] && \
    [ -f ./HyperUBot/userbot/__init__.py ] && \
    [ -f ./HyperUBot/userbot/__main__.py ]); then
    printf "$(setColor $GREEN 'HyperUBot is installed already')\n"
    exit 0
fi

os_name=$(setColor $RED "Unsupported")

# Check OS
if [ "$OSTYPE" == "linux-android" ]; then
    os_name="Android"
elif [ "$OSTYPE" == "linux-gnu" ]; then
     if [ -f "/etc/debian_version" ]; then
         os_name="Debian"
     elif [ -f "/etc/arch-release" ]; then
         os_name="Arch Linux"
     elif [ -f "/etc/redhat-release" ]; then
         os_name="Red Hat"
     fi
elif [[ "$OSTYPE" =~ "darwin"* ]]; then
    os_name="macOS"
fi

# Generated with ASCII Art Generator: http://patorjk.com/software/taag/
printf " _   _                       _   _ ____        _   \n"
printf "| | | |_   _ _ __   ___ _ __| | | | __ )  ___ | |_ \n"
printf "| |_| | | | | '_ \ / _ \ '__| | | |  _ \ / _ \| __|\n"
printf "|  _  | |_| | |_) |  __/ |  | |_| | |_) | (_) | |_ \n"
printf "|_| |_|\__, | .__/ \___|_|   \___/|____/ \___/ \__|\n"
printf "       |___/|_|                                    \n"
printf "A customizable, modular Telegram userbot, with innovative components.\n\n"

printf "Operating System: $os_name\n"

function printRelease() {
    source /etc/os-release
    echo "Release: $PRETTY_NAME"
    printf "\n"
}

usr_bin=/usr/bin

# Install pre-requisites packages
case "$os_name" in
    "Android")
        release=$(getprop ro.build.version.release)
        release_sdk=$(getprop ro.build.version.sdk)
        usr_bin=$PREFIX/bin
        printf "Release: %s (API: %s)\n\n" $release $release_sdk
        printf "Installing pre-requisites packages...\n"
        pkg update && pkg install python git rust neofetch ffmpeg flac
        ;;
    "Debian")
        printRelease
        printf "Installing pre-requisites packages (sudo needed)...\n"
        sudo apt-get update && sudo apt-get install python3.8 python3-pip git neofetch ffmpeg flac net-tools
        ;;
    "Arch Linux")
        printf "\n"
        printf "Installing pre-requisites packages (sudo needed)...\n"
        sudo pacman -Sy python3 python-pip git neofetch ffmpeg flac
        ;;
    "Red Hat")
        printRelease
        printf "Installing pre-requisites packages (sudo needed)...\n"
        sudo dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm && sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
        sudo dnf install python3 git neofetch ffmpeg flac python3-wheel
        ;;
    "macOS")
        release=$(sw_vers -productVersion)
        printf "Release: %s\n\n" $release
        printf "Checking for Homebrew Package Manager...\n"
        if [ -z $(command -v brew) ]; then
            printf "Installing Homebrew Package Manager (sudo needed)...\n"
            # From https://brew.sh/
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        printf "Installing pre-requisites packages...\n"
        brew install git python3 ffmpeg flac neofetch
        ;;
    *)
        printf "Current operating system is not supported...\n"
        exit 1
        ;;
esac

function ver_lt() {
    printf "$1\n$2\n" | sort -V | tail -1
}

# Python --version >=3.8
printf "Checking for Python...\n"
py_exec=$(find $usr_bin -type f \( -name "python*" -not -name "python*[A-Za-z]" -not -name "python*-config" -not -name "python*[A-Za-z]-config" \) -exec basename {} \; | sort -V | tail -1)

if [ -z $py_exec ]; then
    printf "$(setColor $RED 'Python is not installed')\n"
    exit 1
fi

py_ver_str=$($py_exec --version | cut -d " " -f2)

if [ $(ver_lt $py_ver_str "3.7."*) == "3.7."* ]; then
    printf "$(setColor $YELLOW 'HyperUBot requires at least Python v3.8! Latest installed version is %s')\n" "$py_ver_str"
    exit 1
fi

printf "Python $py_ver_str is installed!\n" 

printf "Fetching latest release from HyperUBot's Repository...\n"
get_release=$(curl --silent -H "Accept: application/json" "https://api.github.com/repos/prototype74/HyperUBot/releases/latest")

tar_pkg=$(grep '"tarball_url"' <<< "$get_release" | cut -d '"' -f4)
if [ -z $tar_pkg ]; then
    message=$(grep '"message"' <<< "$get_release" | cut -d '"' -f4)
    printf "$(setColor $RED 'Failed to download HyperUBot: %s')\n" "$message"
    exit 1
fi

release_ver=$(grep '"tag_name"' <<< "$get_release" | cut -d '"' -f4)
curr_path=$(pwd)
dir_name="HyperUBot"

printf "Downloading HyperUBot ($release_ver)...\n"
curl -L --silent "$tar_pkg" --output HyperUBot.tar.gz || { printf "$(setColor $RED 'Failed to download HyperUBot')\n" && exit 1; }

printf "Creating HyperUBot's directory in '$curr_path'...\n"
mkdir $dir_name || { printf "$(setColor $RED 'Failed to create directory')\n" && exit 1; }

printf "Installing HyperUBot...\n"
tar -xf ./HyperUBot.tar.gz --directory ./$dir_name --strip-components=1 || { printf "$(setColor $RED 'Installation failed!')\n" && exit 1; }
rm -f ./HyperUBot.tar.gz

if [ -d $dir_name ] && \
   [ -f $dir_name/userbot/__init__.py ] && \
   [ -f $dir_name/userbot/__main__.py ]; then
    printf "$(setColor $GREEN 'HyperUBot has been installed successfully!')\n"
else
    printf "$(setColor $RED 'Installation was not successful!')\n"
    exit 1
fi

cd $dir_name
printf "\n"

while true; do
    read -p "Do you wish to start the Setup Assistant now? (y/n): " user_input
    if [[ $user_input =~ ^[yY]$ ]]; then
        printf "Starting Setup Assistant...\n"
        printf "\n"
        $py_exec setup.py
        break
    elif [[ $user_input =~ ^[nN]$ ]]; then
        break
    else
        printf "$(setColor $YELLOW 'Invalid input. Try again...')\n"
    fi
done

exit 0
