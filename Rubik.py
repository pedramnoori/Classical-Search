from Algorithms import *

class State():
    def __init__(self):
        self.value = []
        self.path = []
        self.dep = 0


class Problem():

    def initialState(self):
        state = State()
        state.dep = 1
        state.value = ['','y', 'b', 'y', 'b', 'g', 'y', 'g', 'y', 'w', 'g', 'w', 'g', 'b', 'w', 'b', 'w', 'r', 'r', 'r' ,'r', 'o', 'o', 'o', 'o']

        return state


    def actions(self, state):
        self.possibleActions = []

        self.possibleActions.append("T")
        self.possibleActions.append("TC")
        self.possibleActions.append("F")
        self.possibleActions.append("FC")
        self.possibleActions.append("R")
        self.possibleActions.append("RC")

        return self.possibleActions

    def result(self, state, action):
        temp = copy.deepcopy(state)

        if action == "F":
            temp.value[7] = state.value[8]
            temp.value[5] = state.value[7]
            temp.value[6] = state.value[5]
            temp.value[8] = state.value[6]

            temp.value[18] = state.value[9]
            temp.value[20] = state.value[10]
            temp.value[3] = state.value[20]
            temp.value[4] = state.value[18]

            temp.value[21] = state.value[3]
            temp.value[23] = state.value[4]
            temp.value[9] = state.value[23]
            temp.value[10] = state.value[21]

        elif action == "FC":
            temp.value[7] = state.value[5]
            temp.value[5] = state.value[6]
            temp.value[6] = state.value[8]
            temp.value[8] = state.value[7]

            temp.value[18] = state.value[4]
            temp.value[20] = state.value[3]
            temp.value[3] = state.value[21]
            temp.value[4] = state.value[23]

            temp.value[21] = state.value[10]
            temp.value[23] = state.value[9]
            temp.value[9] = state.value[18]
            temp.value[10] = state.value[20]

        elif action == "T":
            temp.value[1] = state.value[3]
            temp.value[2] = state.value[1]
            temp.value[4] = state.value[2]
            temp.value[3] = state.value[4]

            temp.value[21] = state.value[16]
            temp.value[22] = state.value[15]
            temp.value[5] = state.value[21]
            temp.value[6] = state.value[22]

            temp.value[16] = state.value[17]
            temp.value[15] = state.value[18]
            temp.value[17] = state.value[5]
            temp.value[18] = state.value[6]

        elif action == "TC":
            temp.value[1] = state.value[2]
            temp.value[2] = state.value[4]
            temp.value[4] = state.value[3]
            temp.value[3] = state.value[1]

            temp.value[21] = state.value[5]
            temp.value[22] = state.value[6]
            temp.value[5] = state.value[17]
            temp.value[6] = state.value[18]

            temp.value[16] = state.value[21]
            temp.value[15] = state.value[22]
            temp.value[17] = state.value[16]
            temp.value[18] = state.value[15]

        elif action == "R":
            temp.value[22] = state.value[21]
            temp.value[21] = state.value[23]
            temp.value[23] = state.value[24]
            temp.value[24] = state.value[22]

            temp.value[2] = state.value[6]
            temp.value[4] = state.value[8]
            temp.value[6] = state.value[10]
            temp.value[8] = state.value[12]

            temp.value[10] = state.value[14]
            temp.value[12] = state.value[16]
            temp.value[14] = state.value[2]
            temp.value[16] = state.value[4]

        elif action == "RC":
            temp.value[22] = state.value[24]
            temp.value[21] = state.value[22]
            temp.value[23] = state.value[21]
            temp.value[24] = state.value[23]

            temp.value[2] = state.value[14]
            temp.value[4] = state.value[16]
            temp.value[6] = state.value[2]
            temp.value[8] = state.value[4]

            temp.value[10] = state.value[6]
            temp.value[12] = state.value[8]
            temp.value[14] = state.value[10]
            temp.value[16] = state.value[12]

        return temp

    def goalTest(self, state):
        color = ''
        for i in range(0, 25):
            if i % 4 == 1:
                color = state.value[i]
            elif color != state.value[i]:
                return False
        return True

    def stepCost(self, state , action):
        return 1

print("BFS : \n")
G = Problem()
Alg7 = Algorithms(G)
Alg7.BFS(G.initialState())
print("=======================")

print("DFS_LIMITED : \n")
H = Problem()
Alg8 = Algorithms(H)
Alg8.DFS_Limited(H.initialState(), 14)
print("=======================")


print("DFS_ADITIVE : \n")
W = Problem()
Alg9 = Algorithms(W)
Alg9.DFS_Aditive(W.initialState(), 1)


