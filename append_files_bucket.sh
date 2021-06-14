# get the files from a Google Storage bucket, replace the protocol part, add full url, filter by file name
files=$(gsutil ls gs://tinybird-assets/datasets/demos/games-analytics | sed 's/gs:\/\//https:\/\/storage.googleapis.com\//g' | grep 'gameplays_\d.*.csv' | head -5) # add | head -5 to do it only for some files

# iterate over lines, do appends to tinybird passing each URL
for file in $files
do
    echo Appending $file
    tb datasource append gameplays_string $file
done