"""
There are n (nis even) players, conveniently labelled 1, 2, ...n. These players will play m round of games,
ineach round of games, the players are split into two teams of n/2.Two players x < y are said to
have played against eachother if they were on different teams for one of the m games

You are givem three arguments: n, m, games. Your task is to check that for all pairs of players
1 <= x, y <= n, player x has played against y. games is a 2-dimensional list with
m rows and n columns, where games{i] is a permutation of 1,2,3,...,n representing round number i. In particular for round i
for round i, games([i][0]), games[i][1], games[i][n/2-1] is on one team, games{i][n/2] gamesfil[n/2+1], games|i][n-1] is on the other team.



check(n, m, games) should return a boolean, True if and only if al pairs of the players have played each other in the m rounds of games

Exapmles

check(2, 1, [[1, 2]]) = True
check(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]]) = False
check(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]]) = True

"""


def check(n, m, games):
    played = set()
    for round in games:
        team1 = set(round[:n // 2])
        team2 = set(round[n // 2:])
        for player1 in team1:
            for player2 in team2:
                played.add((player1, player2))
                played.add((player2, player1))
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) not in played:
                return False
    return True


print(check(2, 1, [[1, 2]]))
print(check(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]]))
print(check(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]]))
