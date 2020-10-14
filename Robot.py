from Algorithms import *


class State():

    row = 0
    col = 0
    barrierMap = []
    numOfWall = 0

    def __init__(self, value_1, value_2):
        self.value = [value_1, value_2]
        self.path = []
        self.Hu = 0
        self.costUntilNow = 0
        self.dep = 0

    def paid(self):
        return self.costUntilNow + self.Hu

class Problem():



    def initialState(self):
        state = State(1,1)
        state.row = 5
        state.col = 5

        state.numOfWall = 4
        arr = [
            ((3, 2), (4, 2)),
            ((3, 3), (4, 3)),
            ((2, 3), (2, 4)),
            ((3, 3), (3, 4)),
        ]

        state.Hu = self.huristic(state)

        state.dep = 1
        state.barrierMap = arr


        return state

    def actions(self, state):

        self.possibleActions = []

        if state.value[0] != state.row:
            self.possibleActions.append("D")
            for line in state.barrierMap:
                if line[0] == state.value:
                    if line[1][1] == state.value[1]:
                        if line[1][0] == state.value[0] + 1 :
                            self.possibleActions.remove("D")



        if (state.value[0] != 1) :
            self.possibleActions.append("U")
            for line in state.barrierMap:
                if line[0] == state.value:
                    if line[1][1] == state.value[1]:
                        if line[1][0] == state.value[0] - 1 :
                            self.possibleActions.remove("U")


        if (state.value[1] != state.col):
            self.possibleActions.append("R")
            for line in state.barrierMap:
                if line[0] == state.value:
                    if line[1][0] == state.value[0]:
                        if line[1][1] == state.value[1] + 1 :
                            self.possibleActions.remove("R")

        if (state.value[1] != 1):
            self.possibleActions.append("L")
            for line in state.barrierMap:
                if line[0] == state.value:
                    if line[1][0] == state.value[0]:
                        if line[1][1] == state.value[1] - 1:
                            self.possibleActions.remove("L")


        return self.possibleActions



    def result(self, state, action):
        if action == "D":
            state.value[0] += 1
        elif action == "U":
            state.value[0] -= 1
        elif action == "R":
            state.value[1] += 1
        elif action == "L":
            state.value[1] -= 1

        return state


    def goalTest(self, state):
        goal = [state.row, state.col]

        if (state.value == goal):
            return True

        return False

    def initializeGoal(self):
        state = State(5, 5)

        return state

    def stepCost(self, state , action):
        return 1

    def huristic(self, state):
        cost = 0

        cost = (state.row - state.value[0]) + (state.col - state.value[1])

        return cost




print("DFS : \n")
C = Problem()
Alg7 = Algorithms(C)
Alg7.DFS(C.initialState())
print("=========================")


print("UCS : \n")
B = Problem()
Alg6 = Algorithms(B)
Alg6.UCS(B.initialState())
print("=========================")


# print("BIDIRECTIONAL : \n")
# D = Problem()
# Alg8 = Algorithms(D)
# Alg8.bidirectional(D.initialState(), D.initializeGoal())
# print("=========================")


print("A_STAR : \n")
E = Problem()
Alg9 = Algorithms(E)
Alg9.A_star(E.initialState())
print("=========================")