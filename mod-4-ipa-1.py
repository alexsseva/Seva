'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

from lib2to3.pytree import BasePattern


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    followerflag = False
    followedbyflag = False
    for i in range(len(social_graph[from_member]["following"])):
        if social_graph[from_member]["following"][i] == to_member:
            followerflag = True
    for i in range(len(social_graph[to_member]["following"])):
        if social_graph[to_member]["following"][i] == from_member:
            followedbyflag = True
    if followedbyflag and followerflag:
        return "friends"
    elif not followedbyflag and not followerflag:
        return "no relationship"
    elif followerflag and not followedbyflag:
        return "follower"
    else:
        return "followed by"

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    for i in range(len(board)):
        if len(set(board[i])) == 1:
            if (board[i][0] != ' '):
                return board[i][0] 

    boardset = set()
    boardlist = list()
    for i in range(len(board)):
            for j in range(len(board)):
                if (' ' not in boardset):
                    boardset.add(board[j][i])
            if len(boardset) == 1:
                if (' ' not in boardset):
                    return (str(boardset.pop()))
            boardset = set()
    
    for i in range(len(board)):
        if (' ' not in boardset):
            boardset.add(board[i][i])
    if len(boardset) == 1:
        if (' ' not in boardset):
            return(str(boardset.pop()))
    else:
        boardset = set()
    
    for i in range(len(board)):
        boardset.add(board[len(board) - i - 1][i])
    if len(boardset) == 1:
        if (' ' not in boardset):
            return(str(boardset.pop()))
    else:
        boardset = set()
    
    return "NO WINNER"

board1 = [
[' ','O','O'],
['X',' ','X'],
['X','X',' '],
]

x = tic_tac_toe(board1)
print(x)

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    stops = list(route_map.keys())
    travel_time = list(route_map.values())
    stop1stlist = [stops[i][0] for i in range(len(stops))]
    laststoplist = [stops[i][1] for i in range(len(stops))]
    time_list = [travel_time[x]["travel_time_mins"] for x in range(len(travel_time))]

    stop1stindex = stop1stlist.index(first_stop)
    laststopindex = laststoplist.index(second_stop)

    start = stop1stindex
    time = time_list[start]
    while start != laststopindex:
        time += time_list[(start + 1) % len(time_list)]
        start = (start + 1) % len(time_list)
    return time
