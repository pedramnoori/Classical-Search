from Algorithms import *

class State():
    def __init__(self):
        self.path = []
        self.value = [[] for i in range(3)]
        self.costUntilNow = 0
        self.Hu = 0
        self.dep = 0

    def paid(self):
        return self.costUntilNow + self.Hu


class Problem():


    def initialState(self):
        state = State()
        state.value = [['1','2','0'],['3','4','5'],['6','7','8']]
        state.Hu = self.huristic(state)
        state.dep = 1

        return state

    def actions(self,state):

        self.possibleActions = []

        for i in range(3):
            for j in range(3):
                if state.value[i][j] == '0':
                    if i == 0:
                        self.possibleActions.append('D')
                    elif i == 1:
                        self.possibleActions.append('D')
                        self.possibleActions.append('U')
                    else:
                        self.possibleActions.append('U')

                    if j == 0:
                        self.possibleActions.append('R')
                    elif j == 1:
                        self.possibleActions.append('R')
                        self.possibleActions.append('L')
                    else:
                        self.possibleActions.append('L')


                    return self.possibleActions


    def result(self, state, action):

        for i in range(3):
            for j in range(3):
                if state.value[i][j] == '0':
                    if action == 'U':
                        state.value[i][j] = state.value[i-1][j]
                        state.value[i-1][j] = '0'

                    elif action == 'D':
                        state.value[i][j] = state.value[i+1][j]
                        state.value[i+1][j] = '0'

                    elif action == 'R':
                        state.value[i][j] = state.value[i][j+1]
                        state.value[i][j+1] = '0'

                    elif action == 'L':
                        state.value[i][j] = state.value[i][j-1]
                        state.value[i][j-1] = '0'

                    return state

    def goalTest(self,state):
        goal = [['0','1','2'],['3','4','5'],['6','7','8']]

        if state.value == goal:
            return True

        return False

    def stepCost(self, state , action):
        return 1


    def huristic(self, state):
        goalState = {'0':(0,0),
                     '1':(0,1),
                     '2':(0,2),
                     '3':(1,0),
                     '4':(1,1),
                     '5':(1,2),
                     '6':(2,0),
                     '7':(2,1),
                     '8':(2,2)
                    }

        huristic = 0

        for i in range(3):
            for j in range(3):
                huristic = huristic + abs(goalState.get(state.value[i][j])[0] - i) + abs(goalState.get(state.value[i][j])[1] - j)

        return huristic

    def initializeGoal(self):
        state = State()
        state.value = [['0','1','2'],['3','4','5'],['6','7','8']]

        return state



P = Problem()
Alg = Algorithms(P)
print("DFS : \n")
Alg.DFS(P.initialState())
print("=======================")

#
D = Problem()
Alg2 = Algorithms(D)
print("UCS : \n")
Alg2.UCS(D.initialState())
print("=======================")

#
C = Problem()
Alg3 = Algorithms(C)
print("BIDIRECTIONAL : \n")
Alg3.bidirectional(C.initialState(), C.initializeGoal())
#
print("=======================")

A = Problem()
Alg4 = Algorithms(A)
print("A_STAR : \n")
Alg4.A_star(A.initialState())
