. .e/bin/activate

for day in {01..10}
do
    python3 generate_data.py --date-start=2021-06-$day  --num-games=100000 --format=json --include-start-date-in-filename yes 
done
