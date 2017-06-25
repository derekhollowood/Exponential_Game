# python3
import sys
import random
import math

def game(players, num_players, num_rounds):
    print("Let the game begin!")
    scores = [0 for _ in range(num_players)]
    for round in range(num_rounds):
        if round == num_rounds-1:
            print("Last Round!")
        else:
            print("Round", round+1)
        for i in range(num_players):
            index = (i + round) % num_players
            player = players[index]
            print(player, "'s turn.  Input your power ", player, ":", sep="")
            power = float(sys.stdin.readline())
            dist = math.ceil(random.expovariate(1/power) - 0.5)
            if dist < 10:
                print("Distance is ", dist, ".  Geez my grandma could throw further than you.", sep="")
                scores[index] += dist
            elif dist < 90:
                print("Distance is ", dist, ".", sep="")
                scores[index] += dist
            elif dist > 100:
                print("Distance is ", dist, ".  Looks like you overshot!  No points for ", player, ".", sep="")
            else:
                print("Distance is ", dist, ".  Wow nice shot!", sep="")
                scores[index] += dist
        print("Scores are:")
        for i in range(num_players):
            max_index = 0
            if scores[i] > scores[max_index]:
                max_index = i
            print(players[i], ": ", scores[i], sep="")
        if round == num_rounds-1:
            print(players[max_index], " wins with ", scores[max_index], " points!  Congratulations ", players[max_index], ".", sep="")
        else:
            print(players[max_index], " is in the lead with ", scores[max_index], " points.", sep="")


def main():
    print("Welcome to the Exponential Game! Would you like to know how to play? Enter Y for yes or just enter for no.")
    response = input()
    if response == 'Y':
        print("Players will play a number of rounds earning a score at each round.  Whoever has the highest score in the end wins.  During each round the players take turns throwing a ball with user-specified power p.  The distance the ball travels is exponentially distributed with parameter 1/p.  If your ball goes beyond the 100 mark you get a score of zero.  Otherwise your score for the round is the distance traveled by the ball.")
    print("How many players?")
    num_players = int(sys.stdin.readline())
    print("How many rounds?  Preferably a multiple of the number of players.")
    num_rounds = int(sys.stdin.readline())
    players = []
    for k in range(num_players):
        print("Enter Player ", k+1, "'s name:", sep="")
        players += [sys.stdin.readline().strip()]
    game(players, num_players, num_rounds)

if __name__ == '__main__':
    main()
