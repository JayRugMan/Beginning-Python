#!/bin/bash
# uses pdfseparate and pdfunite to extract and combine
# pages from a PDF file


function usage() {
  cat <<EOF
Usage for ${SCRIPT_NAME}:

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
${SCRIPT_NAME} -s 3 -e 14 -f myfile.pdf -f myfile_3-14.pdf

EOF
}


function test_int() {
  # Tests whether input is integer
  re='^[0-9]+$'
  if [[ ${1} =~ $re ]]; then
    return 0
  else
    return 1
  fi
}


function interactive_mode() {
  # Interactive Mode
  read -p "Input File Name: " -e INPUT_FILE
  read -p "Output File Name: " -e OUTPUT_FILE
  read -p "First Page (leave blank if page 1): " -e FIRST_PAGE
  if [[ -z $FIRST_PAGE ]]; then
    FIRST_PAGE=1;
  elif ! test_int $FIRST_PAGE; then
    usage
    exit
  fi
  read -p "Last Page (leave blank if last page): " -e LAST_PAGE
  if [[ -z $LAST_PAGE ]]; then
    LAST_PAGE=$(pdfinfo $INPUT_FILE | awk '/Pages:/ {print $2}');
  elif ! test_int $LAST_PAGE; then
    usage
    exit
  fi
  while true; do
    read -p "Do you want to delete the original file ('y' or 'n'): " -e del_bit
    if [[ $del_bit == "y" ]] || [[ $del_bit == "n" ]]; then
      if [[ $del_bit == "y" ]]; then
        DEL_ORIGINAL=true
      fi
      break
    fi
  done
}


function get_options() {
  local OPTIND the_opt h i s e f d
  while getopts "his:e:f:d" the_opt; do
    case "$the_opt" in
      h) # prints help/usage
        usage
	    exit 0
        ;;
      i) # Interactive Mode
        interactive_mode
		break
        ;;
      s) # first page
        FIRST_PAGE="$OPTARG"
        if ! test_int $FIRST_PAGE; then usage; exit; fi
        ;;
      e) # last page
        LAST_PAGE="$OPTARG"
	    if ! test_int $LAST_PAGE; then usage; exit; fi
        ;;
      f) # takes two arguments, input file and output file
	    the_files+=("${OPTARG}")
        ;;
      d) # Delete if designated
        DEL_ORIGINAL=true
        ;;
      ?)
        usage
        exit 1
        ;;
    esac
  done
  shift "$((OPTIND-1))"
  if [[ ! -z $the_files ]]; then
    INPUT_FILE=${the_files[0]}
    OUTPUT_FILE=${the_files[1]}
  fi
  if [[ $OUTPUT_FILE == "" ]]; then OUTPUT_FILE=PDF_OutputFile.pdf; fi
  if [[ $LAST_PAGE -eq 0 ]]; then LAST_PAGE=$(pdfinfo "${INPUT_FILE}" | awk '/Pages:/ {print $2}'); fi
}


function parse_file() {
  # Where the magic happens
  ##JH numOfPages=$(( $((LAST_PAGE + 1)) - FIRST_PAGE))
  # separate pdf into temp files from input file
  pdfseparate -f ${FIRST_PAGE} -l ${LAST_PAGE} "${INPUT_FILE}" tempFile-%d.pdf
  tmp_file_array=()
  # Create an array with file names of temp
  ##JH for i in $(seq 1 $numOfPages); do
  for i in $(seq ${FIRST_PAGE} ${LAST_PAGE}); do
    tmp_file_array+=(tempFile-${i}.pdf)
  done
  # Unite temp files, then delete them
  pdfunite ${tmp_file_array[@]} "${OUTPUT_FILE}"
  rm -f tempFile-*.pdf
  # Delete original if designated
  if ${DEL_ORIGINAL} ; then
    rm -f ${INPUT_FILE}
  fi
}


function main() {
  # Main Function
  get_options ${@}
  parse_file
}

#### Declare GLOBAL arguments ####

SCRIPT_NAME=${0}
INPUT_FILE=""
OUTPUT_FILE=""
FIRST_PAGE=1
LAST_PAGE=0
DEL_ORIGINAL=false

#### Execute main function ####

main ${@}
