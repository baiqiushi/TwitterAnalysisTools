# remove the first "[" in the first line
sed -i.bak '1 s/^\[//' sample.adm

# remove the last "]" in the last line
sed -i '$ s/\]$//' sample.adm

# remove the first comma in every line
sed -i 's/^,//' sample.adm


# combine together
sed -i '1 s/^\[//; $ s/\]$//; s/^,//' sample.adm



# gzip the file for later ingestion
gzip sample.adm

# to ingest this sample.adm.gz file into asterixdb
# follow the step 4 in 'twittermap-Install-AsterixDB-and-Ingest-Tweet-data.txt'
# to create the 'fileFeed.sh' script,
# and follow the step 5 to create 'ingest-file.sh' script,
# but no need to call 'geotag.sh' file during the pipeline,
# replace the following line 
gunzip -c $f | ./geotag.sh 1 2> /dev/null | grep '^{' | ./fileFeed.sh;
# into 
gunzip -c $f | ./fileFeed.sh;
# directly gunzip the file in continuous mode and then pipeline to 'fileFeed.sh' to ingest into asterixdb