#!/bin/bash

#pyuic5 src/mainwindow.ui -o src/mainwindow.py

UI_FILE=
PY_FILE=

RED='\033[31m'
YELLOW='\033[33m'
RESET='\033[0m'

makeUi_becomePy_args(){
    while [ "$1" ]
    do
        if (echo "$1" | grep -Ew "^-s") >/dev/null;
        then
            if (echo "$2" | grep -E "^-[a-zA-Z]") >/dev/null;
            then
                echo "${YELLOW}ERROR${RESET} in arg ${RED}$2${RESET} unexpected option, just after ${YELLOW}$1${RESET}"
                exit 1
            fi
            UI_FILE="$2"; shift
        elif (echo "$1" | grep -Ew "^-o") >/dev/null;
        then
            if (echo "$2" | grep -E "^-[a-zA-Z]") >/dev/null;
            then
                echo "${YELLOW}ERROR${RESET} in arg ${RED}$2${RESET} unexpected option, just after ${YELLOW}$1${RESET}"
                exit 1
            fi
            PY_FILE="$2"; shift
        fi
        shift
        if [ "${PY_FILE}" != '' ] && [ "${UI_FILE}" != '' ] ; then echo "Done";break ; fi
    done

    echo "${UI_FILE}" "${PY_FILE}"
    pyuic5 "${UI_FILE}" -o "${PY_FILE}"
    return 0
}

makeUi_becomePy(){

    # echo "$1"| sed 's#\(.\+\)\.ui#\1/' match to string 
    # trailing with extension .ui extension
    UI_FILE="$1"
    if (echo "${UI_FILE}" | grep -i ".ui$") >/dev/null
    then
        PY_FILE="$(echo "$1"| sed 's#\(.\+\)\.ui#\1#')"
        PY_FILE="${PY_FILE}.py"

        if [ ! -e "${UI_FILE}" ]
        then echo "${RED}Error${RESET}: No such file or directory: ${UI_FILE}"
            exit 2
        fi


        if ! (pyuic5 "${UI_FILE}" -o "${PY_FILE}") then
            echo -n "${RED}Error${RESET} while " > /dev/stderr
            echo "creating $PY_FILE file !" >/dev/stderr
            exit 1
        fi
        echo "Done"
   fi
   return 0
}


case $# in
    0){
        echo -n "You should give me at least a name"
        echo " of ${YELLOW}*.ui${RESET} file Not empty"
        exit 1
      };;

    1) makeUi_becomePy "$1";;
    *) makeUi_becomePy_args "$@" ;;
esac

exit "$?"
