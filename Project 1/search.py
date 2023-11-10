# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import json

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


from ast import literal_eval


# def getDirFromStr(path):
#     from game import Directions
#     for dir in [Directions.WEST, Directions.NORTH, Directions.SOUTH, Directions.EAST]:
#         if dir in path:
#             return dir
#
#     return None
#
#
# def getDirection(listPath):
#     listPath.pop(0)
#     # print(listPath)
#     listDir = []
#     for path in listPath:
#         try:
#             path = literal_eval(path)
#             listDir.append(path[1])
#         except Exception:
#             path = getDirFromStr(path)
#             listDir.append(path)
#             # print(path)
#     return listDir
#
#
# def getDirectionNotStr(listPath):
#     listPath.pop(0)
#     # print(listPath)
#     listDir = []
#     for path in listPath:
#         # path= literal_eval(path)
#         listDir.append(path[1])
#     return listDir


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # listPath = []
    #
    # def getFullPath(currentState, stateFatherDict):
    #     try:
    #         listPath.append(stateFatherDict[currentState])
    #     except Exception:
    #         return listPath
    #     getFullPath(stateFatherDict[currentState], stateFatherDict)

    visitedState = []
    # stateFatherDict = {}
    stack = util.Stack()
    stackPath = util.Stack()
    stack.push((problem.getStartState(),0))
    stackPath.push([])
    while True:
        try:
            currentState = stack.pop()
            currentStatePath = stackPath.pop()
        except Exception:
            return
        # if currentStateFull == problem.getStartState():
        #     currentState = currentStateFull
        # else:
        #     currentState = currentStateFull[0]
        if problem.isGoalState(currentState[0]):
            return currentStatePath
            # listPath.append(str(currentStateFull))
            # getFullPath(str(currentStateFull), stateFatherDict)
            # listPath.reverse()
            # return getDirection(listPath)
        if currentState[0] in set(visitedState):
            continue
        visitedState.append(currentState[0])
        currentNeibourList = problem.getSuccessors(currentState[0])
        for currentNeibour in currentNeibourList:
            if str(currentNeibour[0]) not in visitedState:
                # stateFatherDict[str(currentNeibour)] = str(currentStateFull)
                stack.push((currentNeibour[0], currentNeibour[2]))
                newPath = currentStatePath.copy() + [currentNeibour[1]]
                stackPath.push(newPath)

    util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # listPath = []
    #
    # def getFullPath(currentState, stateFatherDict):
    #     try:
    #         listPath.append(stateFatherDict[currentState])
    #     except Exception:
    #         return listPath
    #     getFullPath(stateFatherDict[currentState], stateFatherDict)

    visitedState = []
    # stateFatherDict = {}
    queue = util.Queue()
    queuePath = util.Queue()
    queue.push((problem.getStartState(), 0))
    queuePath.push([])
    while True:
        try:
            currentState = queue.pop()
            currentStatePath = queuePath.pop()
        except Exception:
            return
        # if currentStateFull == problem.getStartState():
        #     currentState = currentStateFull
        # else:
        #     currentState = currentStateFull[0]
        if problem.isGoalState(currentState[0]):
            return currentStatePath
            # listPath.append(str(currentStateFull))
            # getFullPath(str(currentStateFull), stateFatherDict)
            # listPath.reverse()
            # return getDirection(listPath)
        if currentState[0] in visitedState:
            continue
        visitedState.append(currentState[0])
        currentNeibourList = problem.getSuccessors(currentState[0])
        for currentNeibour in currentNeibourList:
            if str(currentNeibour[0]) not in visitedState:
                # stateFatherDict[str(currentNeibour)] = str(currentStateFull)
                queue.push((currentNeibour[0], currentNeibour[2]))
                newPath = currentStatePath.copy() + [currentNeibour[1]]
                queuePath.push(newPath)

    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # listPath = []
    #
    # def getFullPath(currentState, stateFatherDict):
    #     try:
    #         listPath.append(stateFatherDict[currentState])
    #     # if currentState not in stateFatherDict:
    #     except Exception:
    #         # listPath.append(currentState)
    #         return listPath
    #     # print(stateFatherDict[currentState])
    #     # print(listPath)
    #     getFullPath(stateFatherDict[currentState], stateFatherDict)

    visitedState = []
    visitedStateCost = []
    priorityQueue = util.PriorityQueue()
    priorityQueuePath = util.PriorityQueue()
    priorityQueue.push((problem.getStartState(), 0), 0)
    priorityQueuePath.push([], 0)
    while True:
        try:
            currentState, pathCostTotal = priorityQueue.pop()
            thisPath = priorityQueuePath.pop()
        except Exception:
            return
        if currentState in visitedState:
            if visitedStateCost[visitedState.index(currentState)] <= pathCostTotal:
                continue
            visitedStateCost[visitedState.index(currentState)] = pathCostTotal
        else:
            visitedState.append(currentState)
            visitedStateCost.append(pathCostTotal)
        if problem.isGoalState(currentState):
            return thisPath
        currentNeibourList = problem.getSuccessors(currentState)
        for currentNeibour in currentNeibourList:
            neibTotalCost = currentNeibour[2] + pathCostTotal
            if currentNeibour[0] in visitedState:
                if visitedStateCost[visitedState.index(currentNeibour[0])] <= neibTotalCost:
                    continue
                # pathTotalCostDict[currentNeibour[0]] = neibTotalCost
            # heuristicAndTotalCost = neibTotalCost + heuristic(currentNeibour[0], problem)
            priorityQueue.push((currentNeibour[0], neibTotalCost), neibTotalCost)
            priorityQueuePath.push(thisPath + [currentNeibour[1]], neibTotalCost)

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visitedState = []
    visitedStateCost = []
    priorityQueue = util.PriorityQueue()
    priorityQueuePath = util.PriorityQueue()
    priorityQueue.push((problem.getStartState(),0), 0)
    priorityQueuePath.push([], 0)
    while True:
        try:
            currentState, pathCostTotal = priorityQueue.pop()
            thisPath = priorityQueuePath.pop()
        except Exception:
            return
        if currentState in visitedState:
            if visitedStateCost[visitedState.index(currentState)] <= pathCostTotal:
                continue
            visitedStateCost[visitedState.index(currentState)] = pathCostTotal
        else:
            visitedState.append(currentState)
            visitedStateCost.append(pathCostTotal)
        if problem.isGoalState(currentState):
            return thisPath
        currentNeibourList = problem.getSuccessors(currentState)
        for currentNeibour in currentNeibourList:
            neibTotalCost = currentNeibour[2] + pathCostTotal
            if currentNeibour[0] in visitedState:
                if visitedStateCost[visitedState.index(currentNeibour[0])] <= neibTotalCost:
                    continue
                # pathTotalCostDict[currentNeibour[0]] = neibTotalCost
            heuristicAndTotalCost = neibTotalCost + heuristic(currentNeibour[0], problem)
            priorityQueue.push((currentNeibour[0], neibTotalCost), heuristicAndTotalCost)
            priorityQueuePath.push(thisPath + [currentNeibour[1]], heuristicAndTotalCost)
            # thisPathNew.append(currentNeibour[1])

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
