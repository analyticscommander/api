import requests
import json

r"""
Main starting point of baseball program

@param - None
@return - None
"""
def main():
    teams = get_api_response(url)
#def save_team_by_season():
#def save_roster_by_team():
#def save_player_by_roster():

r"""
Retrieves api data from url and returns the response

@param - String - url - url to pull api response
@return - Dictionary - API data
"""
def get_api_response(url):
    api_response = requests.get(url)
    #json loads function translates text into python language
    #text function from requests library accesses info from url
    #utf-8 translates all character possibilities from the text pulled
    return(json.loads(api_response.text.encode('utf-8').strip()))

r"""
Retrieves a list of major league teams that were active provided season
Returns team and team_id based on year

@param - String - year - year to get teams for
@return - Dictionary - teams - teams and their team id
"""
def get_teams_by_season(year):
    url = """http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?
    sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='%s'""" % year
    data = get_api_response(url)
    teams = []
    for row in (data["team_all_season"]["queryResults"]["row"]):
        if row["sport_code_display"] == "Major League Baseball":
            teams.append({
                "team_name": row["name_display_full"],
                "team_id": row["team_id"]
            })
    return teams

r"""
Retrieve a teams roster between a given start and end season
provided a team_id, start season year, and end season year

Returns list of names and player id during that period of time

@param - String - team_id - team id for each team
@param - String - start_season_year - start season you want team roster
@param - String - end_season_year - end season you want team roster

@return - Dictionary - players - name of players and their player id
"""
def get_rosters_by_team(start_season_year, end_season_year, team_id):
#breaking up URL into multi-line caused an error for some unknown reason
    url = """http://lookup-service-prod.mlb.com/json/named.roster_team_alltime.bam?start_season='%s'&end_season='%s'&team_id='%s'""" % (start_season_year, end_season_year, team_id)
    data = get_api_response(url)
    players = []
    for row in data["roster_team_alltime"]["queryResults"]["row"]:
        players.append({
            "player_name": row["name_first_last"],
            "player_id": row["player_id"]
        })
    return players

r"""
Retrieve a players hitting stats for a given season provided a player_id,
season year, and game type

@param - String - game_type - The type of games you want career stats for
@param - String - season_year - season you want stats for
@param - String - player_id - player you want hitting stats for

@return - Dictionary - hitting_stats - player id and their hitting stats
"""
def get_hitting_stats_by_player(game_type, season_year, player_id):
#breaking up URL into multi-line caused an error for some unknown reason
    url = "http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type='%s'&season='%s'&player_id='%s'" % (game_type, season_year, player_id)
    data = get_api_response(url)
    hitting_stats = []
    stats = data["sport_hitting_tm"]["queryResults"]["row"]
    hitting_stats.append({
            "team_name": stats["team_full"],
            "team_id": stats["team_id"],
            "player_id": stats["player_id"],
            "team_league": stats["league_full"],
            "batting_average": stats["avg"],
            "on-base_percentage": stats["obp"],
            "on-base_plus_slugging": stats["ops"],
            "slugging_percentage": stats["slg"],
            "total_plate_appearance": stats["tpa"],
            "hits": stats["h"],
            "at_bats": stats["ab"],
            "runs": stats["r"],
            "home_run": stats["hr"],
            "walks": stats["bb"],
            "runs_batted_in": stats["rbi"],
            "strikeouts": stats["so"],
            "intentional_walk": stats["ibb"],
            "batting_average_on_balls_in_play": stats["babip"],
            "extra_base_hits": stats["xbh"]
        })
    return(hitting_stats)
#Figure out the mystery baseball player with the player_id of '493316' and attach his name to his own stats during 2017 regular season
#get_hitting_stats_by_player('R','2017','493316')
#
mystery_person_stats = get_hitting_stats_by_player('R', '2017', '493316')
#
teams = get_teams_by_season('2017')
for team in teams:
    team_rosters_by_season = get_rosters_by_team('2017','2017',mystery_person_stats["team_id"])

    print(mystery_person_stats)
