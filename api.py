import requests
import json

r"""
Main starting point of baseball program

@param - None
@return - None
"""
def main():
    teams = get_api_response(url)

def get_api_response():
    url = host + path
    host = "http://lookup-service-prod.mlb.com"
    path = "/json/named.[endpoint].bam"
    r = requests.get(url)
    print(r)
    print(json.loads(r.text.encode('utf-8').strip()))

r"""
Retrieves a list of major league teams that were active during 2018 season
Provides team_id and much more unnecessary info

@param - String - year - year to get teams for
@return - Dictionary - none - details for all teams
"""
def get_teams_by_season(year):
    url = """http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?
    sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='%s'""" % year
    api_response = requests.get(url)
    #json loads function translates text into python language
    #text function from requests library accesses info from url
    #utf-8 translates all character possibilities from the text pulled
    return(json.loads(api_response.text.encode('utf-8').strip()))

#def save_team_by_season():

#Retrieves a teams roster during 2018 season based on team_id
def get_rosters_by_team():
    url = "http://lookup-service-prod.mlb.com/json/named.roster_team_alltime.bam?start_season='2018'&end_season='2018'" + "&team_id='121'"
    r = requests.get(url)
    print(r)
    print(json.loads(r.text.encode('utf-8').strip()))

#Retrieves a team’s 40 man roster based on team_id
#def save_roster_by_team():


# def get_players_by_roster():
# def save_player_by_roster():
# get_rosters_by_team()
season_teams = get_teams_by_season('2016')
print(season_teams)
