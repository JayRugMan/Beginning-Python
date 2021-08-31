#!/bin/bash
# used pdfseparate and pdfunite to extract and combine
# pages from a PDF file


function fusage() {
  cat <<EOF
Usage for ${scriptName}:

 -h                  Prints usage

 -i                  Enter interactive mode

 -s <integer>        Starting page of PDF to splice. If blank,
                     page 1 is assumed

 -e <integer>        Ending page to splice. If blank, the
                     last page is assumed.

 -f <file>           Enter File - first usage is input file
                                  second usage is ouput file

 -d                  Delete the original file

Example:
${scriptName} -s 3 -e 14 -f myfile.pdf -f myfile_3-14.pdf

EOF
}


function testInt() {
  # Tests whether input is integer
  re='^[0-9]+$'
  if [[ ${1} =~ $re ]]; then
    return 0
  else
    return 1
  fi
}


function interactiveMode() {
  # Interactive Mode
  read -p "Input File Name: " -e iFile
  read -p "Output File Name: " -e oFile
  read -p "First Page (leave blank if page 1): " -e firstPage
  if [[ -z $firstPage ]]; then
    firstPage=1;
  elif ! testInt $firstPage; then
    fusage
    exit
  fi
  read -p "Last Page (leave blank if last page): " -e lastPage
  if [[ -z $lastPage ]]; then
    lastPage=$(pdfinfo $iFile | awk '/Pages:/ {print $2}');
  elif ! testInt $lastPage; then
    fusage
    exit
  fi
  while true; do
    read -p "Do you want to delete the original file ('y' or 'n'): " -e delBit
    if [[ $delBit == "y" ]] || [[ $delBit == "n" ]]; then
      if [[ $delBit == "y" ]]; then
        deleteOriginal=true
        break
      fi
    fi
  done
}


function getOptions() {
  local OPTIND OPTION h i s e f d
  while getopts "his:e:f:d" OPTION; do
    case "$OPTION" in
      h) # prints help/usage
        fusage
	exit 0
        ;;
      i) # Interactive Mode
        interactiveMode
        ;;
      s) # first page
        firstPage="$OPTARG"
        if ! testInt $firstPage; then fusage; exit; fi
        ;;
      e) # last page
        lastPage="$OPTARG"
	      if ! testInt $lastPage; then fusage; exit; fi
        ;;
      f) # takes two arguments, input file and output file
	      Files+=("${OPTARG}")
        ;;
      d) # Delete if designated
        deleteOriginal=true
        ;;
      ?)
        fusage
        exit 1
        ;;
    esac
  done
  shift "$((OPTIND -1))"
  if [[ ! -z $Files ]]; then
    iFile=${Files[0]}
    oFile=${Files[1]}
  fi
  if [[ $oFile == "" ]]; then oFile=PDF_OutputFile.pdf; fi
  if [[ $lastPage -eq 0 ]]; then lastPage=$(pdfinfo "${iFile}" | awk '/Pages:/ {print $2}'); fi
}


function parseFile() {
  # Where the magic happens
  ##JH numOfPages=$(( $((lastPage + 1)) - firstPage))
  # separate pdf into temp files from input file
  pdfseparate -f ${firstPage} -l ${lastPage} "${iFile}" tempFile-%d.pdf
  tmpFileArray=()
  # Create an array with file names of temp
  ##JH for i in $(seq 1 $numOfPages); do
  for i in $(seq ${firstPage} ${lastPage}); do
    tmpFileArray+=(tempFile-${i}.pdf)
  done
  # Unite temp files, then delete them
  pdfunite ${tmpFileArray[@]} "${oFile}"
  rm -f tempFile-*.pdf
  # Delete original if designated
  if ${deleteOriginal} ; then
    rm -f ${iFile}
  fi
}


function main() {
  # Main Function
  getOptions ${@}
  parseFile
}

#### Declare GLOBAL arguments ####

scriptName=${0}
iFile=""
oFile=""
firstPage=1
lastPage=0
deleteOriginal=false

#### Execute main function ####

main ${@}
