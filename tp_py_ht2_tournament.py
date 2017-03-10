import random
from math import log2

teams = ['FC Spartak Moscow',
         'PFC CSKA Moscow',
         'FC Bayern Munich',
         'FC Borussia Dortmund',
         'FC Marseille',
         'FC Paris Saint-Germain',
         'FC Liverpool',
         'FC Manchester United',
         'FC Chelsea',
         'FC Manchester City',
         'FC Juventus',
         'FC Milan',
         'FC Internazionale Milan',
         'FC Napoli',
         'FC Real Madrid',
         'FC Barcelona']

def match_info(stage, team1, team2, match_score):
    """
    function: makes a dictionary with info
    about match (teams, score, stage)
    """
    info = {}
    info["stage"] = stage
    info["Winner"] = team1
    info["Looser"] = team2
    info["score"] = match_score
    return info

def match(stage, team1, team2):
    """
    function: modelling of the match 
    between team1 and team2 (uses random)
    """
    goals1 = random.randint(0, 5)
    goals2 = random.randint(0, 5)
    if goals1 == goals2:
        ext_time_goals1 = random.randint(0, 2)
        ext_time_goals2 = random.randint(0, 2)
        if ext_time_goals1 == ext_time_goals2:
            pens1 = 0
            pens2 = 0
            while pens1 == pens2:
                pens1 = random.randint(0, 6)
                pens2 = random.randint(0, 6)
            if pens1 > pens2:
                match_score = str(goals1) + "-" + str(goals2)
                match_score += (" ; extended time: ") 
                match_score += (str(ext_time_goals1) + "-" + str(ext_time_goals2))
                match_score += (" ; penalties: " + str(pens1) + "-" + str(pens2))
                return match_info(stage, team1, team2, match_score)
            else:
                match_score = str(goals2) + "-" + str(goals1)
                match_score += (" ; extended time: ") 
                match_score += (str(ext_time_goals2) + "-" + str(ext_time_goals1))
                match_score += (" ; penalties: " + str(pens2) + "-" + str(pens1))
                return match_info(stage, team2, team1, match_score)
        elif ext_time_goals1 > ext_time_goals2:
            match_score = str(goals1) + "-" + str(goals2)
            match_score += (" ; extended time: ")
            match_score += (str(ext_time_goals1) + "-" + str(ext_time_goals2))
            return match_info(stage, team1, team2, match_score)
        else:
            match_score = str(goals2) + "-" + str(goals1)
            match_score += (" ; extended time: ")
            match_score += (str(ext_time_goals2) + "-" + str(ext_time_goals1))
            return match_info(stage, team2, team1, match_score)
    elif goals1 > goals2:
        match_score = str(goals1) + "-" + str(goals2)
        return match_info(stage, team1, team2, match_score)
    else:
        match_score = str(goals2) + "-" + str(goals1)
        return match_info(stage, team2, team1, match_score)

def make_stages(num):
    """
	function: generator of stages in tournament
	"""
    for i in range(num, 0, -1):
        if i > 1:
            yield '1/' + str(2 ** (i - 1))
        else:
            yield 'Final'
    
def tournament(teams):
    """
    function: modelling of the tournament (play-off)
    """
    my_teams = teams[:]
    tournament = {}
    num_stages = int(log2(len(teams)))
    stages = tuple(make_stages(num_stages))
    
    for i in range(num_stages):
        while len(my_teams):
            team1 = random.choice(my_teams)
            my_teams.remove(team1)
            team2 = random.choice(my_teams)
            my_teams.remove(team2)
            new_match = match(stages[i], team1, team2)
            if i == 0:
                tournament[team1] = [new_match]
                tournament[team2] = [new_match]
            else:
                tournament[team1].append(new_match)
                tournament[team2].append(new_match)
    
        for team in tournament.keys():
            if i < len(tournament[team]):
                my_teams.append(tournament[team][i]["Winner"])
        
        my_teams = set(my_teams)
        my_teams = list(my_teams)
        
    for team in tournament.keys():
	    cond1 = len(tournament[team]) == num_stages
		cond2 = team == tournament[team][i]["Winner"]
        if cond1 and cond2:
            winner_output = "The winner of this tournament is "
            winner_output += team + "\n"
            print(winner_output)
    
    return tournament

def print_info(team, tournament):
    output = 'Path of ' + team + "\n"
    for match in tournament[team]:
        match_info = 'Stage ' + match["stage"] + ": "
        match_info += (match["Winner"] + " vs " + match["Looser"])
        match_info += (" : " + match["score"] + "\n")
        output += match_info
    print(output)

def main():
    champions_league = tournament(teams)
    for team in champions_league.keys():
        print_info(team, Champions_League)
    
main()