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
    
    #horizontal


    for i in range(len(board)):
        if len(set(board[i])) == 1:
            return board[i][0] 

    boardset = set()
    boardlist = list()
    for i in range(len(board)):
        for j in range(len(board)):
            boardset.add(board[j][i])
        if len(boardset) == 1:
            return (str(boardset.pop()))
        boardset = set()
    
    for i in range(len(board)):
        boardset.add(board[i][i])
    if len(boardset) == 1:
        return(str(boardset.pop()))
    else:
        boardset = set()
    
    for i in range(len(board)):
        boardset.add(board[len(board) - i - 1][i])
    if len(boardset) == 1:
        return(str(boardset.pop()))
    else:
        boardset = set()
    
    return "NO WINNER"
    

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
    stop1st = first_stop
    laststop = second_stop
    time = 0

    for key in route_map:
        if(key[0] == stop1st):
            time = time + route_map[key]['travel_time_mins']
            stop1st = key[1]
            if key[1] == laststop:
                break
        else:
            continue 
    return int(time)

legs = {
    ("upd","admu"):{
        "travel_time_mins":10
    },
    ("admu","dlsu"):{
        "travel_time_mins":35
    },
    ("dlsu","ust"):{
        "travel_time_mins":55
    },
    ("ust","upd"):{
        "travel_time_mins":5
    }
}


x = eta("upd", "dlsu", legs)
print(x)

