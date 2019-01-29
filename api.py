import requests
import json

r"""
Main starting point of baseball program

@param - None
@return - None
"""
def main():
    teams = get_api_response(url)

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

#def save_team_by_season():

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

#Retrieves a team’s 40 man roster based on team_id
#def save_roster_by_team():

# def save_player_by_roster():

teams = get_teams_by_season('2018')
for team in teams:
    team_rosters_by_season = get_rosters_by_team('2018','2018',team["team_id"])
    print(team_rosters_by_season)
