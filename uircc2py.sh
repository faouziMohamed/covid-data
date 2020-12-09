#!/bin/bash

cd "$(dirname "$0")" || exit 1

RESOURCE_FILE="assets/resources.qrc"
RESOURCE_COMPILED="src/generated/resources_rc.py"

UI_FILE="assets/mainwindow.ui"
UI_FILE_COMPILED="src/generated/mainwindow.py"

function compile_resource_file(){
  if ( pyrcc5  "${RESOURCE_FILE}" -o "${RESOURCE_COMPILED}" ) then
    echo -e "Resource file compilation succeed!"
    return 0
  else
    echo -e "An error occur while compiling resource file!"
    return 1
  fi

}

function convert_ui_to_py_file(){
  if ( pyuic5 "${UI_FILE}" -o "${UI_FILE_COMPILED}" ) then
      echo -e "Py file generation succeed!"
      return 0
  else
      echo -e "An error occur while generating py file from ui file!"
      return 1
  fi
}

if [ "$#" -gt 0 ]; then
  case "$1" in
    "-a" | "--all") convert_ui_to_py_file && compile_resource_file;
                    exit $?;;
    "-u" | "--ui")  convert_ui_to_py_file; exit $?;;
    "-q" | "--qrc") compile_resource_file; exit $?;;
    *)
      echo "usage : $(basename "$0") [ (-a|--all) | (-u|--ui) | (-q|--qrc) ]"
      exit 2;;
  esac
fi

convert_ui_to_py_file && compile_resource_file
