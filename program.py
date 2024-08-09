import random
import sys

import PySimpleGUI as sg

# set the theme of the GUI to 'LightBrown 13'
sg.theme('LightBrown 13')
# Set the background color of the theme to white
sg.theme_background_color("white")
sg.theme_text_element_background_color("white")
sg.theme_element_background_color("white")


# define a class Team for teams in the tournament
class Team:
    def __init__(self, name):
        # The __init__ method is the constructor for the class and is called when a new object of the class is created
        self.name = name  # attributes of a team
        self.games = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_against = 0
        self.goal_difference = 0
        self.points = 0

    # a special method in Python that is used to define how an object of a class should be represented as a string
    def __str__(self):
        return f"{self.name}: W{self.wins} D{self.draws} L{self.losses} GS{self.goals_scored} GA{self.goals_against} " \
               f"GD{self.goal_difference} Pts{self.points}"


# create classes
class Group:
    # '*' is used to initialize to a tuple receiving any excess positional
    def __init__(self, name, *matches):
        # parameters, defaulting to the empty tuple
        self.name = name
        self.teams = []
        self.matches = list(matches)

    def add_team(self, team):
        self.teams.append(team)  # append each team to list teams

    def add_match(self, team1, team2):
        # append each match to list matches
        self.matches.append((team1, team2))


class Round16:
    def __init__(self, *matches):
        self.matches = list(matches)

    def add_match(self, team1, team2):
        self.matches.append((team1, team2))


class QuarterFinals:
    def __init__(self, *matches):
        self.matches = list(matches)

    def add_match(self, team1, team2):
        self.matches.append((team1, team2))


class Semifinals:
    def __init__(self, *matches):
        self.matches = list(matches)

    def add_match(self, team1, team2):
        self.matches.append((team1, team2))


class ThirdPlaceMatch:
    def __init__(self, *matches):
        self.matches = list(matches)

    def add_match(self, team1, team2):
        self.matches.append((team1, team2))


class Finals:
    def __init__(self, *matches):
        self.matches = list(matches)

    def add_match(self, team1, team2):
        self.matches.append((team1, team2))


class Winners:
    def __init__(self):
        self.winners16 = []
        self.winners_quarter = []
        self.winners_semi = []
        self.match_thirdP = []
        self.winner_final = []

    # create winners' list to hold winners' data and use them for next stages

    def add_winners16(self, team):
        self.winners16.append(team)

    def add_winners_quarter(self, team):
        self.winners_quarter.append(team)

    def add_winners_semi(self, team):
        self.winners_semi.append(team)

    def add_match_thirdP(self, team):
        self.match_thirdP.append(team)

    def add_winner_final(self, team):
        self.winner_final.append(team)


winners = Winners()  # Assign an object of class Winners to the variable 'winners'

# define a dictionary of countries and their flags
countries = {
    'Kazakhstan': 'flags/flag-kazakhstan_1f1f0-1f1ff.png',
    'Ukraine': 'flags/flag-ukraine_1f1fa-1f1e6.png',
    'Kyrgyzstan': 'flags/flag-kyrgyzstan_1f1f0-1f1ec.png',
    'Argentina': 'flags/flag-argentina_1f1e6-1f1f7.png',
    'Brazil': 'flags/flag-brazil_1f1e7-1f1f7.png',
    'England': 'flags/flag-england_1f3f4-e0067-e0062-e0065-e006e-e0067-e007f.png',
    'France': 'flags/flag-france_1f1eb-1f1f7.png',
    'Spain': 'flags/flag-spain_1f1ea-1f1f8-2.png',
    'Belgium': 'flags/flag-belgium_1f1e7-1f1ea.png',
    'Portugal': 'flags/flag-portugal_1f1f5-1f1f9-2.png',
    'Germany': 'flags/flag-germany_1f1e9-1f1ea-2.png',
    'Netherlands': 'flags/flag-netherlands_1f1f3-1f1f1-2.png',
    'Uruguay': 'flags/flag-uruguay_1f1fa-1f1fe-2.png',
    'Croatia': 'flags/flag-croatia_1f1ed-1f1f7-2.png',
    'Denmark': 'flags/flag-denmark_1f1e9-1f1f0.png',
    'Mexico': 'flags/flag-mexico_1f1f2-1f1fd-2.png',
    'United States': 'flags/flag-united-states_1f1fa-1f1f8-2.png',
    'Senegal': 'flags/flag-senegal_1f1f8-1f1f3-2.png',
    'Wales': 'flags/flag-wales_1f3f4-e0067-e0062-e0077-e006c-e0073-e007f-2.png',
    'Poland': 'flags/flag-poland_1f1f5-1f1f1-2.png',
    'Australia': 'flags/flag-australia_1f1e6-1f1fa-2.png',
    'Japan': 'flags/flag-japan_1f1ef-1f1f5-2.png',
    'Morocco': 'flags/flag-morocco_1f1f2-1f1e6-2.png',
    'Switzerland': 'flags/flag-switzerland_1f1e8-1f1ed-2.png',
    'Ghana': 'flags/flag-ghana_1f1ec-1f1ed-2.png',
    'Korea Republic': 'flags/flag-south-korea_1f1f0-1f1f7-2.png',
    'Cameroon': 'flags/flag-cameroon_1f1e8-1f1f2-2.png',
    'Serbia': 'flags/flag-serbia_1f1f7-1f1f8-2.png',
    'Canada': 'flags/flag-canada_1f1e8-1f1e6-2.png',
    'Costa Rica': 'flags/flag-costa-rica_1f1e8-1f1f7-2.png',
    'Tunisia': 'flags/flag-tunisia_1f1f9-1f1f3-2.png',
    'Saudi Arabia': 'flags/flag-saudi-arabia_1f1f8-1f1e6-2.png',
    'Iran': 'flags/flag-iran_1f1ee-1f1f7-2.png',
    'Ecuador': 'flags/flag-ecuador_1f1ea-1f1e8-2.png',
    'Qatar': 'flags/flag-qatar_1f1f6-1f1e6-2.png'
}

# define a dictionary of countries and their flags but in emojis
flags = {
    'Kazakhstan': '🇰🇿',
    'Ukraine': '🇺🇦',
    'Kyrgyzstan': '🇰🇬',
    'Argentina': '🇦🇷',
    'Brazil': '🇧🇷',
    'England': '🏴󠁧󠁢󠁥󠁮󠁧󠁿',
    'France': '🇫🇷',
    'Spain': '🇪🇸',
    'Belgium': '🇧🇪',
    'Portugal': '🇵🇹',
    'Germany': '🇩🇪',
    'Netherlands': '🇳🇱',
    'Uruguay': '🇺🇾',
    'Croatia': '🇭🇷',
    'Denmark': '🇩🇰',
    'Mexico': '🇲🇽',
    'United States': '🇺🇸',
    'Senegal': '🇸🇳',
    'Wales': '🏴󠁧󠁢󠁷󠁬󠁳󠁿',
    'Poland': '🇵🇱',
    'Australia': '🇦🇺',
    'Japan': '🇯🇵',
    'Morocco': '🇲🇦',
    'Switzerland': '🇨🇭',
    'Ghana': '🇬🇭',
    'Korea Republic': '🇰🇷',
    'Cameroon': '🇨🇲',
    'Serbia': '🇷🇸',
    'Canada': '🇨🇦',
    'Costa Rica': '🇨🇷',
    'Tunisia': '🇹🇳',
    'Saudi Arabia': '🇸🇦',
    'Iran': '🇮🇷',
    'Ecuador': '🇪🇨',
    'Qatar': '🇶🇦'
}


def create_teams(teams):
    # create layout
    layout = [[sg.Text('Enter 32 teams separated by a comma:', font='Helvetica 16', )],
              [sg.InputText(do_not_clear=False, font='Helvetica 14',
                            background_color='white')],
              [sg.Button('Add teams', font='Helvetica 16'), sg.Button('Exit', font='Helvetica 16')]]

    window = sg.Window(
        'Create teams', resizable=True).layout(layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break  # exits while loop if window was closed
        if event == 'Exit':
            sys.exit()  # exits whole simulation if exit button was pushed
        if event == 'Add teams':
            # remove comas in string and store teams in the list
            team_names = values[0].split(',')
            for team_name in team_names:
                team_name = team_name.strip()  # remove leading/trailing whitespace
                teams.append(Team(team_name))

            # Show an error message and clear the teams list
            if len(teams) < 32:
                sg.Popup('Not enough teams!', keep_on_top=True,
                         font='Helvetica 16', title="Error")
                # Close the window and call the create_teams function again
                teams.clear()
                window.Close()
                return create_teams(teams)
            elif len(teams) > 32:
                # Show an error message and clear the teams list
                sg.Popup('Too many teams!', keep_on_top=True,
                         font='Helvetica 16', title="Error")
                teams.clear()
                window.Close()
                return create_teams(teams)

            # Shuffle the teams list
            random.shuffle(teams)
            # Close the window
            window.Close()
# function to display team statistics


def group_stage():
    global groups
    groups = [Group('A'), Group('B'), Group('C'), Group(
        'D'), Group('E'), Group('F'), Group('G'), Group('H')]

    for i, team in enumerate(teams):
        # adding 32 teams to 8 different groups (i.e. teams № 1,9,17,25 are in team A)
        groups[i % 8].add_team(team)

    for group in groups:
        matches = []
        for i in range(0, len(group.teams) - 1):
            for j in range(i + 1, len(group.teams)):
                # adding 6 matches to each group
                matches.append((group.teams[i], group.teams[j]))
        # replacing these matches to regularize them
        matches[1], matches[5] = matches[5], matches[1]

        for i in range(0, len(matches)):
            match = matches[i]
            team1, team2 = match  # get two teams from each match for design and for inputs of goals

            flag1 = sg.Image(countries.get(team1.name))
            # assigning countries' flags to variable
            flag2 = sg.Image(countries.get(team2.name))

            layout = [
                [sg.Text(f'Group {group.name}', font='Helvetica 20 bold',
                         justification='center', key="GROUP")],
                # 1st element of layout with group's name
                [sg.Column([[flag1, sg.Text(f'{team1.name}', key="MATCH", font='Helvetica 16 bold'),
                             sg.Text('vs', font='Helvetica 16 bold'),
                             sg.Text(f'{team2.name}', key="MATCH", font='Helvetica 16 bold'), flag2]])],
                # 2nd element with teams' countries and flags, column is used to show them all in one row

                [sg.Text(f'Enter number of goals scored by {team1.name}:', font='Helvetica 16'),
                 sg.InputText(do_not_clear=False, key='Team1', font='Helvetica 14', background_color='white')],
                [sg.Text(f'Enter number of goals scored by {team2.name}:', font='Helvetica 16'),
                 sg.InputText(do_not_clear=False, font='Helvetica 14', key="Team2", background_color='white')],
                # 3rd and 4th elements with inputs of goals
                [sg.Text("")],  # for more space between 4th and 6th rows
                [sg.Text(
                    f'{team1.name}: {team1.games} games, {team1.wins} W, {team1.draws} D, {team1.losses} L, {team1.goals_scored} GS, {team1.goals_against} GA, {team1.goal_difference} GD, {team1.points} PTS ',
                    key="RESULTS", font='Helvetica 16')],
                [sg.Text(
                    f'{team2.name}: {team2.games} games, {team2.wins} W, {team2.draws} D, {team2.losses} L, {team2.goals_scored} GS, {team2.goals_against} GA, {team2.goal_difference} GD, {team2.points} PTS ',
                    key="RESULTS", font='Helvetica 16')],
                # to display teams' statistics
                [sg.Button('Add results', font='Helvetica 16'), sg.Button('Exit', font='Helvetica 16')]]
            # to allow user to push two buttons: add results and exit
            window = sg.Window('Group Simulation', resizable=True,
                               size=(600, 260), ).layout(layout)

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == 'Exit':
                    sys.exit()

                try:
                    goals1 = int(values["Team1"])
                    # gets values written in inputs by user using keys (team1/team2)
                    goals2 = int(values["Team2"])

                except (ValueError, IndexError, TypeError):
                    sg.Popup('Please enter a valid number of goals',
                             title="Error", keep_on_top=True, font='Helvetica 13')

                else:
                    window.Close()

                    team1.games += 1
                    team2.games += 1

                    team1.goals_scored += goals1
                    team1.goals_against += goals2
                    team1.goal_difference = team1.goals_scored - team1.goals_against

                    team2.goals_scored += goals2
                    team2.goals_against += goals1
                    team2.goal_difference = team2.goals_scored - team2.goals_against
                    # adds values to both teams' statistics

                    if goals1 > goals2:
                        team1.wins += 1
                        team2.losses += 1
                        team1.points += 3
                    elif goals2 > goals1:
                        team2.wins += 1
                        team1.losses += 1
                        team2.points += 3
                    else:
                        team1.draws += 1
                        team2.draws += 1
                        team1.points += 1
                        team2.points += 1
                    # adds points and result (W/D/L) according to goals

        group.teams.sort(key=lambda x: (-x.points, -
                         x.goal_difference, -x.goals_scored))
        # sorts points, goal differences and amount of scored goals in a descending order
        # lambda is used to execute given function only here and avoid extra lines of code
        display_team_stats(group)  # display teams' statistics of certain group
    show_results()  # activates the given function after all 8 groups are done


def display_team_stats(group):
    table_data = []
    # Add a row for the headings
    headings = ["Team", "Games", "Wins", "Draws", "Losses", "Goals Scored", "Goals Against", "Goals Difference",
                "Points"]
    # Add a row for each team in the group
    for team in group.teams:
        flag = flags.get(team.name)
        team_stats = [team.name + " " + flag, team.games, team.wins, team.draws, team.losses, team.goals_scored,
                      team.goals_against,
                      team.goal_difference, team.points]
        table_data.append(team_stats)

    # Create a table for the group
    table = sg.Table(values=table_data, num_rows=4, headings=headings, header_font="Helvetica 16 bold",
                     header_text_color="white", header_background_color="#800020", justification='center',
                     font='Helvetica 16', auto_size_columns=True)

    # Create the form layout
    layout = [[sg.Text(f'Group {group.name}', font='Helvetica 18 bold ', justification='center')],
              [table],
              [sg.Button("Close", font='Helvetica 16')]]

    # Create the window and show the form
    window = sg.Window(
        "Team Stats").layout(layout)

    # Run the event loop to process user input
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Close":
            break

    # Close the window
    window.close()


def show_results():
    layout = [[sg.Text('Group Stage is finished', font='Helvetica 18 bold', justification='center')],
              [sg.Image(filename="pics/trophy.png", )],
              [sg.Button('Start Round 16', font='Helvetica 16'), sg.Button('Show results', font='Helvetica 16')]]
    # layout to indicate the end of group stage and allow user to view results or start playoff

    window = sg.Window('Groups finished', resizable=True, size=(650, 445),
                       element_justification="center").layout(layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Show results':
            window.Close()
            display_group_stats(groups)

        if event == "Start Round 16":
            window.Close()


def display_group_stats(groups):
    # Create a list of tabs
    tabs = []
    for group in groups:
        heading = ["Team", "Games", "Wins", "Draws", "Losses", "Goals Scored", "Goals Against", "Goal Difference",
                   "Points"]
        # Create a list of lists to hold the table data for each group
        table_data = []
        # Add a row for the headings
        # Add a row for each team in the group
        for team in group.teams:
            flag = flags.get(team.name)
            table_data.append(
                [team.name + " " + flag, team.games, team.wins, team.draws, team.losses, team.goals_scored,
                 team.goals_against, team.goal_difference, team.points])
        # Create the tab for the group and add it to the list of tabs

        tabs.append(sg.Tab(group.name, [
            [sg.Table(values=table_data, headings=heading, key="table", num_rows=4, auto_size_columns=False,
                      header_font="Helvetica 16 bold",
                      header_text_color="white", header_background_color="#800020",
                      justification='center',
                      font='Helvetica 16')]]))
    # Create the form layout with the tabs

    layout = [[sg.TabGroup([tabs], title_color="white", selected_background_color="#4f0316",
                           selected_title_color="white", tab_background_color="#800020")],
                           [sg.Button("Close", font='Helvetica 16')]]

    # Create the window
    window = sg.Window("Group Stats", font='Helvetica 18').layout(layout)
    # Run the event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Close":  # check if the user closes the window
            break  # break the loop
    window.close()

# create list to hold data for winners  and users
third_place_winner = []
final_loser = []
final_win = []


def round_16():
    print("Round 16!")
    round16 = Round16()  # Assigns an object of class Round16 to the variable 'round16'
    for i in range(0, 8, 2):
        round16.add_match(groups[i].teams[0], groups[i + 1].teams[1])
        # one group's first team against another group's second team
    for i in range(0, 8, 2):
        round16.add_match(groups[i].teams[1], groups[i + 1].teams[0])
    # adds 8 matches between teams similarly to how it is done in world cup
    # so that 2 teams from 1 group can face each other only in final

    for team1, team2 in round16.matches:
        input_goals(team1, team2, "Round16")
    # activates input_goals function for every game of round 16
    show_winners("Round 16")
    # shows winners of round 16 matches in the end of stage


# same processes for other stages of playoff

def quarterfinals():
    print("Quarterfinals!")
    quarter = QuarterFinals()

    for i in range(0, 8, 2):
        quarter.add_match(winners.winners16[i], winners.winners16[i + 1])
    # 4 matches

    for team1, team2 in quarter.matches:
        input_goals(team1, team2, "Quarterfinals")

    show_winners("Quarterfinals")


def semifinals():
    semi = Semifinals()
    print("Semifinals")
    for i in range(0, 4, 2):
        semi.add_match(
            winners.winners_quarter[i], winners.winners_quarter[i + 1])
    # 2 matches

    for team1, team2 in semi.matches:
        input_goals(team1, team2, "Semifinals")

    show_winners("Semifinals")


def third_place_match():
    third_place = ThirdPlaceMatch()
    print("Match for the third place")
    third_place.add_match(winners.match_thirdP[0], winners.match_thirdP[1])
    # 1 match

    for team1, team2 in third_place.matches:
        input_goals(team1, team2, "Match for the third place")


def finals():
    final = Finals()
    print("Final")
    final.add_match(winners.winners_semi[0], winners.winners_semi[1])
    # 1 match

    for team1, team2 in final.matches:
        input_goals(team1, team2, "Final")

    final_winner()
    # activate this function to show the winners of tournament


def input_goals(team1, team2, name):
    flag1 = sg.Image(countries.get(team1.name))
    # assigning countries' flags to variable
    flag2 = sg.Image(countries.get(team2.name))
    layout = [[sg.Text(f'{name}', key="GROUP", font='Helvetica 16 bold')],
              # 1st element of layout with stage's name
              [sg.Column([
                  [flag1, sg.Text(f'{team1.name}', key="MATCH", font='Helvetica 16 bold'),
                   sg.Text('vs', font='Helvetica 16 bold'),
                   sg.Text(f'{team2.name}', key="MATCH", font='Helvetica 16 bold'), flag2]
              ])],
              # 2nd element with teams' countries and flags, column is used to show them all in one row
              [sg.Text("")],
              # for more empty space
              [sg.Text(f'Enter number of goals scored by {team1.name}:', font='Helvetica 16'),
               sg.InputText(do_not_clear=False, key="TEAM1", font='Helvetica 14', background_color='white')],
              # input of goals for team1
              [sg.Text("")],
              [sg.Text(f'Enter number of goals scored by {team2.name}:', font='Helvetica 16'),
               sg.InputText(do_not_clear=False, key="TEAM2", font='Helvetica 14', background_color='white')],
              # input of goals for team2
              [sg.Text("")],
              [sg.Button('Add result', font='Helvetica 16'), sg.Button('Exit', font='Helvetica 16')]]
    # to allow user to push two buttons: add result and exit

    # Create the Window
    window = sg.Window(f'{name}', layout,
                       size=(640, 240))
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'Exit':
            sys.exit()

        try:
            goals1 = int(values["TEAM1"])
            goals2 = int(values["TEAM2"])
            # Make sure the inputs are integer

        except (ValueError, IndexError, TypeError) as err:
            sg.Popup('Please enter a valid number of goals',
                     title="Error", keep_on_top=True, font='Helvetica 16')
        # does not allow to proceed further until valid values are entered

        else:
            # add winners of the match (or losers of semifinal for 3rd place match) to the lists according to stage
            if goals1 > goals2:
                if name == "Round16":
                    winners.add_winners16(team1)

                elif name == "Quarterfinals":
                    winners.add_winners_quarter(team1)

                elif name == "Semifinals":
                    winners.add_winners_semi(team1)
                    winners.add_match_thirdP(team2)

                elif name == "Match for the third place":
                    third_place_winner.append(team1)

                elif name == "Final":
                    winners.add_winner_final(team1)
                    final_win.append(team1)
                    final_loser.append(team2)
                    # add both teams in final and winner of 3rd place match to display in the end

                print(f"The winner of the match is {team1.name}")
                print("")
                window.Close()

            elif goals1 < goals2:
                if name == "Round16":
                    winners.add_winners16(team2)

                elif name == "Quarterfinals":
                    winners.add_winners_quarter(team2)

                elif name == "Semifinals":
                    winners.add_winners_semi(team2)
                    winners.add_match_thirdP(team1)

                elif name == "Match for the third place":
                    third_place_winner.append(team2)

                elif name == "Final":
                    winners.add_winner_final(team2)
                    final_win.append(team2)
                    final_loser.append(team1)

                print(f"The winner of the match is {team2.name}")
                print("")
                window.Close()

            elif goals1 == goals2:
                window.Close()
                penalties(team1, team2, name)
                # call penalties function to decide the winner

            break


def penalties(team1, team2, stage):
    flag1 = sg.Image(countries.get(team1.name))
    flag2 = sg.Image(countries.get(team2.name))
    # create the layout for the penalty table
    layout = [[sg.Text(f'Penalty of {stage}', key="GROUP", font='Helvetica 16 bold')],
              [sg.Column([
                  [flag1, sg.Text(f'{team1.name}', key="MATCH", font='Helvetica 16 bold'),
                   sg.Text('vs', font='Helvetica 16 bold'),
                   sg.Text(f'{team2.name}', key="MATCH", font='Helvetica 16 bold'), flag2]
              ])],
              [sg.Text("")],
              [sg.Text(f'Enter number of penalty goals scored by {team1.name}:', font='Helvetica 16'),
               sg.InputText(do_not_clear=False, key="TEAM1", font='Helvetica 14', background_color='white')],
              [sg.Text("")],
              [sg.Text(f'Enter number of penalty goals scored by {team2.name}:', font='Helvetica 16'),
               sg.InputText(do_not_clear=False, key="TEAM2", font='Helvetica 14', background_color='white')],
              [sg.Text("")],
              [sg.Button('Add result', font='Helvetica 16'), sg.Button('Exit', font='Helvetica 16')]]

    # Create the window and show the form
    window = sg.Window('Penalties', resizable=True,
                       element_justification="center", size=(640, 240)).layout(layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'Exit':
            sys.exit()

        try:
            goals1 = int(values["TEAM1"])
            goals2 = int(values["TEAM2"])
        except (ValueError, IndexError, TypeError):
            sg.Popup('Please enter a valid number of goals',
                     title="Error", keep_on_top=True, font='Helvetica 16')

        else:
            if not (0 <= goals1 <= 5 and 0 <= goals2 <= 5):
                window.Close()
                # in penalties there are restricted amount of goals
                sg.Popup('Please enter values between 0 and 5',
                         title="Error", keep_on_top=True, font='Helvetica 16')
                penalties(team1, team2, stage)
                break

            if goals1 > goals2:
                if stage == "Round16":
                    winners.add_winners16(team1)

                elif stage == "Quarterfinals":
                    winners.add_winners_quarter(team1)

                elif stage == "Semifinals":
                    winners.add_winners_semi(team1)
                    winners.add_match_thirdP(team2)

                elif stage == "Match for the third place":
                    third_place_winner.append(team1)

                elif stage == "Final":
                    winners.add_winner_final(team1)
                    final_win.append(team1)
                    final_loser.append(team2)

                print(f"The winner of the match is {team1.name}")
                print("")
                window.Close()

            if goals1 < goals2:
                if stage == "Round16":
                    winners.add_winners16(team2)

                elif stage == "Quarterfinals":
                    winners.add_winners_quarter(team2)

                elif stage == "Semifinals":
                    winners.add_winners_semi(team2)
                    winners.add_match_thirdP(team1)

                elif stage == "Match for the third place":
                    third_place_winner.append(team2)

                elif stage == "Final":
                    winners.add_winner_final(team2)
                    final_win.append(team2)
                    final_loser.append(team1)

                print(f"The winner of the match is {team2.name}")
                print("")
                window.Close()

            if goals1 == goals2:
                window.Close()
                penalties(team1, team2, stage)


# function to show the winners of a specific stage
def show_winners(stage):
    layout = [[sg.Text(f'The winners of {stage}:', font='Helvetica 16 bold', justification='center')],
              [sg.Text("")]]

    # Check which teams are the winners of the provided stage
    if stage == "Round 16":
        winner_team = winners.winners16
    elif stage == "Quarterfinals":
        winner_team = winners.winners_quarter
    else:
        winner_team = winners.winners_semi

    # Add the winner team's name and flag to the layout
    for i in range(len(winner_team)):
        flag = sg.Image(countries.get(winner_team[i].name))
        layout.append([sg.Text(
            f'{winner_team[i].name}', font='Helvetica 16 bold', justification='center'), flag])
    layout.append([sg.Text("")])
    layout.append([sg.Button('Next Stage', font='Helvetica 16', )])

    # Create a window to show the layout
    window = sg.Window('Results',
                       element_justification="center").layout(layout)

    # Listen for events
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "Next Stage":
            window.Close()


def final_winner():
    # add image to layout
    layout = [[sg.Image(filename="pics/trophyy.png", )], ]
    # get the name of the winning team
    winner_team = winners.winner_final

    # add the winning team's name and flag to the layout
    for i in range(len(winner_team)):
        flag = sg.Image(countries.get(winner_team[i].name))
        layout.append([sg.Text(f'{winner_team[i].name} is the winner of the World Cup!', font='Helvetica 20 bold',
                               justification='center'), flag])

        # add a button to show the top 3 teams
    layout.append([sg.Button('Show Top-3 Teams', font='Helvetica 18', )])
    # create the window and show the layout

    window = sg.Window('Winner',
                       element_justification="center").layout(layout)

    # run the event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

        # close the current window and call the top3() function
        if event == "Show Top-3 Teams":
            window.Close()
            top3()


def top3():
    # load the flags of the top 3 teams
    flag1 = sg.Image(countries.get(final_win[0].name))
    flag2 = sg.Image(countries.get(final_loser[0].name))
    flag3 = sg.Image(countries.get(third_place_winner[0].name))
    # load the images of the rank
    first_place = sg.Image(filename="pics/1st_place.png")
    second_place = sg.Image(filename="pics/2nd_place.png")
    third_place = sg.Image(filename="pics/3rd_place.png")

    # create the layout
    layout = [[first_place, sg.Text(f"{final_win[0].name}", font='Helvetica 20 bold', ), flag1],
              [second_place, sg.Text(
                  f"{final_loser[0].name}", font='Helvetica 20 bold', ), flag2],
              [third_place, sg.Text(
                  f"{third_place_winner[0].name}", font='Helvetica 20 bold', ), flag3],
              [sg.Button('Finish', font='Helvetica 18', )]]

    # create the window
    window = sg.Window('Top-3', element_justification="center").layout(
        layout)

    while True:
        event, values = window.read()
        # check if the user closes the window or clicks "Finish" button
        if event == sg.WIN_CLOSED:  # check if the user closes the window or clicks "Finish" button
            break  # break the loop

        if event == "Finish":
            window.Close()


def main():
    global teams
    teams = []
    create_teams(teams)
    group_stage()
    round_16()
    quarterfinals()
    semifinals()
    third_place_match()
    finals()
# call all necessary functions


if __name__ == "__main__":
    main()
# activate main()
