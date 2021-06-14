tb pipe rm gameplays_group_date_game_player_mv --yes 
tb pipe rm gameplays_group_date_game_team_mv --yes 
tb pipe rm gameplays_mv --yes 
tb pipe rm top_players_per_day --yes 
tb pipe rm top_teams_per_day --yes 

tb datasource rm gameplays_string --yes 
tb datasource rm gameplays --yes 
tb datasource rm gameplays_by_date_game_player --yes 
tb datasource rm gameplays_by_date_game_team --yes 