"""         TECHGIG CODE GLADIATORS 2020 SOLUTIONS  """

'''Tyson is all prepared for the Beyblade World Championship. The tournament is team-based and each team can have N members. A player can fight against a single-player only. Team G-Revolution is all excited and pumped up as they have practiced a lot. Kenny, the mind of team G-Revolution, has created a database where he has the data about the power of other teams members and his own team members. The tournament is going to start in some time and Kenny moves to the cafeteria to have a snack before the competition.





The team G-Revolution is to fight in some time and they are tensed up as someone has kidnapped Kenny 
from the cafeteria. They have made a police complaint and the police are searching for Kenny. Luckily, 
they have found his device with all the data. The problem is, the data is present randomly and not in the
order they have to fight the opponent. Team G-Revolution wants to win at any cost and for that, they need
the order in which they have to fight optimally to win the maximum number of battles.

A player can win only when his/her Beyblade power is strictly greater than the opponent's Beyblade power.

Example:
Consider the team size is 3, N = 3
The 3 players of both the teams are shown with their Beyblade powers.
Team G-Revolution is presented in the order: Tyson, Max, Ray

Constraints
1<= T <=100000
1<= N <=100000
0<= Power of Beyblade <= LLONG_MAX 


Output Format
For each test case, print the maximum number of fights Team G-Revolution can win if they go to fight in 
an optimal manner.'''





class myException_1(Exception):
    pass


class myException_2(Exception):
    pass


class myException_3(Exception):
    pass


def main():
    lists = []
    try:
        testcases = int(input("Enter the testcase value :>> "))
        if testcases <= 0:
            raise myException_3("Number should not be negative or zero")
    except ValueError:
        print("Value should in number")
    except myException_3 as e:
        print(e)
    else:
        for i in range(testcases):
            try:
                num_of_player = int(input("Number of player :>> "))

                g_team_power = list(
                    map(int, input("Power of beyblades team-G:>> ").strip().split())
                )
                g_team_power.sort(reverse=True)

                other_team_power = list(
                    map(int, input("Power of beyblades team-Other:>>").strip().split())
                )
                other_team_power.sort(reverse=True)

                if num_of_player != len(g_team_power):
                    raise myException_1(
                        "number of g_team_power should be equal to number_of_player"
                    )
                elif num_of_player != len(other_team_power):
                    raise myException_2(
                        "Error:number of other_team_power should be equal to number_of_player"
                    )
                else:
                    pass

            except ValueError:
                print("Error:Wrong Input Format")
            except myException_1 as e:
                print(e)
            except myException_2 as e:
                print(e)

            else:
                p = 0
                for i in range(num_of_player):
                    for j in range(p, num_of_player):
                        if g_team_power[i] > other_team_power[j]:
                            p = j + 1
                            lists.append(g_team_power[i])
                            break

                print(
                    f"maximum no of player won by team-G is {len(lists)} power of beyblades won by {set(lists)}"
                )


main()