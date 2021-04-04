#!/usr/bin/env bash
#===============================================================================
#
#          FILE: pullDataFromAsterixDB.sh
#
#         USAGE: ./pullDataFromAsterixDB.sh -a [asterixURL] -s [sql++ statement] -f [output format {adm, json(default)}] -o [output file]
#                  Please use 'screen' command to run it as daemon:
#                  $ screen
#                  $ ./pullDataFromAsterixDB.sh
#
#   DESCRIPTION: pull data from AstereixDB to local file.
#                * EXAMPLE:
#                  ./pullDataFromAsterixDB.sh -a http://actinium.ics.uci.edu:19002/query/service \
#                                             -s "select value d from twitter.ds_tweet d where ftcontains(d.text, ['blackberry'], {'mode':'any'}) and d.create_at >= datetime('2017-12-01T08:00:00.000Z') and d.create_at < datetime('2017-12-31T08:00:00.000Z')" \
#                                             -f json \
#                                             -o sampletweet 
#
#       OPTIONS: 
#  REQUIREMENTS: (1) Python 2.7
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Qiushi Bai (), baiqiushi@gmail.com
#  ORGANIZATION: ics.uci.edu
#       CREATED: 8/8/2018 11:06:01 PM PST
#      REVISION:  ---
#===============================================================================
set -o nounset                              # Treat unset variables as an error

asterixURL="http://localhost:19002/query/service"
sql="select * from Metadata.\`Dataset\`"
outformat="json"
outfile="result"

# asterixURL=${1:-"http://localhost:19002/query/service"}
# sql=${2:-"select * from Metadata.\`Dataset\`"}
# outformat=${3:-"ADM"}
# outfile=${4:-"result.${outformat}"}

while getopts a:s:f:o: option
do
	case "${option}"
		in
		a) asterixURL=${OPTARG};;
		s) sql=${OPTARG};;
		f) outformat=${OPTARG};;
		o) outfile=${OPTARG};;
	esac
done

outfile="${outfile}.${outformat}"

echo "Sending query \"${sql}\" to AsterixDB ${asterixURL} ..."

if [ "${outformat}" = "adm" ] ; then
	result=$(curl -v --data-urlencode "statement=${sql};" --data "mode=deferred" --data "format=application/x-adm"  ${asterixURL})
else
	result=$(curl -v --data-urlencode "statement=${sql};" --data "mode=deferred" ${asterixURL})
fi
echo "Result is :" ${result}

status=$(echo $result | python -c "import sys, json; print json.load(sys.stdin)['status']" 2>/dev/null)

if [ "${status}" = "success" ] ; then
	echo "[Good!] Your query has succeeded!"
	handle=$(echo $result | python -c "import sys, json; print json.load(sys.stdin)['handle']" 2>/dev/null)
	echo "Now downloading your query result with output format as ${outformat} to file ${outfile} ......"
	curl ${handle} -o "${outfile}"
	echo "Congratulations! Your query is done! Enjoy your data!"
else
	echo "[Bad!] Your query has failed!"
	echo "Message is here :"
	echo ${result}
fi
