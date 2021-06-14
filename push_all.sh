files=$(ls datasources)
for ds in $files
do
    tb push datasources/$ds
done

files=$(ls pipes)
for file in $files
do
    tb push pipes/$file
done

tb datasource append gameplays_string https://storage.googleapis.com/tinybird-assets/datasets/demos/games-analytics/gameplays.csv