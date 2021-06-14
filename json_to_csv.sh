# iterates over the files in data that match the pattern
for fullfile in `find data -name "gameplays*.json"`; do # add | head -n 1 to process only some files
    echo Converting $fullfile to CSV
    # extracts the filename as seen in https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash
    filename=$(basename -- "$fullfile")
    extension="${filename##*.}"
    filename="${filename%.*}"
    csv_output=$(echo data/json_to_csv/$filename.csv)
    # converts an ndjson file to a csv file with 1 column
    jq -r '[. | tostring] | @csv' $fullfile  > $csv_output
    echo "CSV file saved in $csv_output"
done
