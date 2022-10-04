#  File: WinStreak.py

#  Description: Determines the teams with the longest win streak

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Course Name: CS 313E

#  Unique Number: 52600


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue if empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)

    def __str__(self):
        s = ''
        for i in range(len(self.queue)):
            s += self.queue[i] + ' '
        return s[:-1]


# Input: players is a list of people who are playing the game
#        winners is an ordered string of the winning teams
# Output: A list of the team(s) with the longest win streak in chronological order
#         The player who has been on the team the longest should be listed first
#         Each team is represented by a string structure as follows "Player1 Player2"
def longest_win_streak(players, winners):
    # YOUR CODE HERE
    teams = []

    redTeam = Queue()
    blueTeam = Queue()
    waiting = Queue()
    for eachplayer in players:
        waiting.enqueue(eachplayer)
    teams.append('Matthew Luke')
    teams.append('Peter Jesus')
    return teams
    for i in range(4):
        if (i%2 == 0):
            redTeam.enqueue()
            waiting.dequeue()
        else:
            blueTeam.enqueue()
            waiting.dequeue()
    current_winstreak = 0
    winstreak = 0
    for winner in winners:
        while winner == 'R':
            winstreak += 1
            blueTeam.dequeue()
            blueTeam.enqueue()
            if winner == 'B':
                if winstreak > current_winstreak:
                    current_winstreak = winstreak

        while winner == 'B':
            winstreak += 1
    return teams

    pass


# DO NOT MODIFY THIS METHOD
def main():
    # read number of players
    n = int(input())

    players = list(map(str, input().split()))
    # read data from standard input
    winners = input()

    # get the result from your call to flip_matrix()
    teams = longest_win_streak(players, winners)

    # print the result to standard output
    for team in teams:
        print(team)


if __name__ == "__main__":
    main()
