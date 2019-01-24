# def get_teams_by_season():
# def save_team_by_season():
# def get_rosters_by_team():
# def save_roster_by_team():
# def get_players_by_roster():
# def save_player_by_roster():

import requests
import json
url = "http://lookup-service-prod.mlb.com/json/named.roster_team_alltime.bam?start_season='2016'&end_season='2017'&team_id='121'"
r = requests.get(url)
print(r)
import pdb; pdb.set_trace()
print(json.loads(r.text.encode('utf-8').strip()))


def get_rosters_by_team(url):
    print(response.read())


def get_api_response(url):
    print(url)
def main():
    teams = get_api_response(url)
