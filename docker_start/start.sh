#!/bin/bash
# Copyright 2021-2022 nunopenim @github
# Copyright 2021-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

#RED="\033[91m"
#GREEN="\033[92m"
YELLOW="\033[93m"
END="\033[0m"

function setColor() {
    echo "$1$2${END}"
}

printf "Start options:\n"
printf "\n"
printf "[1] Start HyperUBot (auto-select in 5 secs)\n"
printf "[2] Setup Assistant\n"
printf "[3] String-Session-Generator\n"
printf "[4] Secure-Config-Updater\n"
printf "[5] Recovery System\n"
printf "[6] Exit\n"
printf "\n"

while true; do
    read -t 5 -p "Enter option [1-6]: " user_input
    if [[ $? -eq 0 ]]; then
        case "$user_input" in
            1) printf "\n" ; python3 -m userbot ; break ;;
            2) printf "\n" ; python3 setup.py ; break ;;
            3) printf "\n" ; python3 generate_session.py ; break ;;
            4) printf "\n" ; python3 update_secure_cfg.py ; break ;;
            5) printf "\n" ; python3 recovery.py ; break ;;
            6) break ;;
            *) printf "$(setColor $YELLOW 'Invalid input!')\n" ;;
        esac
    else
        printf "\n"
        python3 -m userbot
        break
    fi
done

exit 0
