import pytz
import random
from click.termui import prompt
import pandas as pd
import click

from datetime import date, timedelta, datetime
import numpy as np


people_team_game_df = pd.read_csv('data/people_team_game.csv')


def generate_datetimes(start: datetime, end: datetime, n: int):
    # based on https://stackoverflow.com/questions/50559078/generating-random-dates-within-a-given-range-in-pandas
    start_u = int(start.timestamp())
    end_u = int(end.timestamp())
    return pd.DatetimeIndex((np.random.randint(start_u, end_u, n, dtype=np.int64)).view('M8[s]'))


@click.command()
@click.option('--date-start', type=click.DateTime(formats=["%Y-%m-%d"]), default='2021-05-01', prompt=True)
@click.option('--date-end', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--num-games', type=click.INT, default=100000, prompt=True)
@click.option('--include-start-date-in-filename', '-i', type=click.BOOL, default=False, prompt=True)
@click.option('--format', 'format_', type=click.Choice(['json', 'csv']), default='csv', prompt=True)
def generate_gameplays(date_start, date_end, num_games, format_, include_start_date_in_filename):
    date_start = pytz.timezone('utc').localize(date_start)
    if not date_end:
        date_end = date_start + timedelta(days=1)
    else:
        date_end = pytz.timezone('utc').localize(date_end)
    # click.echo(f"Start: {date_start}, End: {date_end}, num_games: {num_games}, {type(num_games)}")
    gameplays_df = people_team_game_df.sample(num_games, replace=True)
    gameplays_df['datetime'] = generate_datetimes(start=date_start, end=date_end, n=num_games)
    gameplays_df['score'] = (np.exp(np.random.normal(loc=5, scale=1, size=num_games)) + 1).astype(int)
    gameplays_df.sort_values('datetime', inplace=True)
    filename = 'gameplays'
    if include_start_date_in_filename:
        filename = f'{filename}_{date_start.date().isoformat()}'
    if format_== 'csv':
        filepath = f'data/{filename}.csv'
        gameplays_df.to_csv(filepath, index=False)
        print(f'Saved to {filepath}')
    elif format_ == 'json':
        filepath = f'data/{filename}.json'
        gameplays_df.to_json(filepath, orient='records', lines=True, date_format='iso') # generate ndjson
        print(f'Saved to {filepath}')


if __name__ == '__main__':
    generate_gameplays()
