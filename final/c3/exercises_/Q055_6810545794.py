# Name: Pasin Makcharoen # Student ID: 6810545794

class Player:
    def __init__(self, name: str, skill: int):
        self.name = name
        self.skill = skill

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.__players = []

    def add_player(self, player_name, skill):
        for player in self.__players:
            if player.name == player_name:
                return False
        new_player = Player(player_name, skill)
        self.__players.append(new_player)
        return True
        
    def remove_player(self, player_name):
        for i in self.__players:
            if i.name == player_name:
                self.__players.remove(i)
                return True
            else:
                continue
        return False
        
    def get_report(self):
        cou_ = len(self.__players)
        if cou_ == 0:
            avg_ = 0.0
        else:
            tot_ = 0
            for i in self.__players:
                tot_ += i.skill
            avg_ = tot_ / cou_
        rep_ = "--- Team Report ---\n"
        rep_ += f"Team: {self.team_name}\n"
        rep_ += f"Players: {cou_}\n"
        rep_ += f"Average Skill: {avg_:.1f}"
        return rep_


league_ = {}

while True:
    in_ = input("Enter command: ").strip()

    if in_ == "":
        print("Error: Invalid command.")
        continue

    par_ = in_.split()
    cmd_ = par_[0].lower()

    if cmd_ == "addteam":
        if len(par_) != 2:
            print("Error: Invalid command.")
            continue

        team_ = par_[1]

        if team_ in league_:
            print(f"Error: Team {team_} already exists.")
        else:
            league_[team_] = Team(team_)
            print(f"Team {team_} created.")
    
    elif cmd_ == "addplayer":
        if len(par_) != 4:
            print("Error: Invalid command.")
            continue

        team_ = par_[1]
        name_ = par_[2]
        ski_ = par_[3]

        try:
            ski_ = int(ski_)
        except:
            print("Error: Skill must be an integer.")
            continue

        if team_ not in league_:
            print("Error: Team not found.")
            continue

        add_ = league_[team_].add_player(name_, ski_)

        if add_:
            print(f"Player {name_} added to {team_}.")
        else:
            print(f"Error: Player {name_} already on team.")
    
    elif cmd_ == "removeplayer":
        if len(par_) != 3:
            print("Error: Invalid command.")
            continue

        team_ = par_[1]
        name_ = par_[2]

        if team_ not in league_:
            print("Error: Team not found.")
            continue

        rem_ = league_[team_].remove_player(name_)
        if rem_:
            print(f"Player {name_} removed from {team_}.")
        else:
            print(f"Error: Player {name_} not found on team.")
    
    elif cmd_ == "report":
        if len(par_) != 2:
            print("Error: Invalid command.")
            continue

        team_ = par_[1]

        if team_ not in league_:
            print("Error: Team not found.")
            continue

        print(league_[team_].get_report())
    
    elif cmd_ == "exit":
        print("Goodbye.")
        break

    else:
        print("Error: Invalid command.")