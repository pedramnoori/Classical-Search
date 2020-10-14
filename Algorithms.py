import copy


class Algorithms():

    def __init__(self,problem):
        self.problem = problem
        self.f_list = []
        self.e_list = []
        self.cost = 0
        self.path = []
        self.e_list_2 = []
        self.f_list_2 = []

    def DFS(self, start):

        currentState = start


        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)


            for ac in possibleActions :
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notIn(nextState, self.e_list, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    if self.problem.goalTest(nextState):
                        print "Finded"
                        self.pathFunction(nextState, len(self.e_list), len(self.e_list), len(self.e_list) + len(self.f_list), self.problem, "")
                        return

            if len(self.f_list) == 0 :
                print "This problem haven't solution"
                break

            currentState = self.f_list.pop(-1)

    def DFS_TREE(self, start):

        currentState = start


        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)


            for ac in possibleActions :
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notInTree(nextState, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    if self.problem.goalTest(nextState):
                        print "Finded"
                        self.pathFunction(nextState, len(self.e_list), len(self.e_list), len(self.e_list) + len(self.f_list), self.problem, "")
                        return

            if len(self.f_list) == 0 :
                print "This problem haven't solution"
                break

            currentState = self.f_list.pop(-1)

    def DFS_Limited(self, start, limit):

        currentState = start

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)


            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notIn(nextState, self.e_list, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    nextState.dep = currentState.dep + 1
                    if self.problem.goalTest(nextState):
                        print "Finded"
                        self.pathFunction(nextState, len(self.e_list), len(self.e_list),
                                          len(self.e_list) + len(self.f_list), self.problem, "")
                        return

            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break

            counter = 0
            for state3 in self.f_list:
                if state3.dep > limit:
                    counter = counter + 1

            if (counter == len(self.f_list)):
                print "This problem haven't solution"
                return

            if self.f_list[len(self.f_list) - 1].dep <= limit:
                currentState = self.f_list.pop(-1)
            else:
                min = 1000
                for state in self.f_list:
                    if state.dep <= min:
                        min = state.dep
                for state2 in reversed(self.f_list):
                    if state2.dep == min:
                        currentState = state2
                        self.f_list.remove(currentState)

    def DFS_Limited_Tree(self, start, limit):

        currentState = start

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)


            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notInTree(nextState, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    nextState.dep = currentState.dep + 1
                    if self.problem.goalTest(nextState):
                        print "Finded"
                        self.pathFunction(nextState, len(self.e_list), len(self.e_list),
                                          len(self.e_list) + len(self.f_list), self.problem, "")
                        return

            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break

            counter = 0
            for state3 in self.f_list:
                if state3.dep > limit:
                    counter = counter + 1

            if (counter == len(self.f_list)):
                print "This problem haven't solution"
                return

            if self.f_list[len(self.f_list) - 1].dep <= limit:
                currentState = self.f_list.pop(-1)
            else:
                min = 1000
                for state in self.f_list:
                    if state.dep <= min:
                        min = state.dep
                for state2 in reversed(self.f_list):
                    if state2.dep == min:
                        currentState = state2
                        self.f_list.remove(currentState)

    def DFS_Aditive(self, start, limit):
        currentState = start

        self.e_list = []
        self.f_list = []

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)

            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notIn(nextState, self.e_list, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    nextState.dep = currentState.dep + 1
                    if self.problem.goalTest(nextState):
                        print "Finded"
                        self.pathFunction(nextState, len(self.e_list), len(self.e_list),
                                          len(self.e_list) + len(self.f_list), self.problem, "")
                        return

            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break

            counter = 0
            for state3 in self.f_list:
                if state3.dep > limit:
                    counter = counter + 1

            if (counter == len(self.f_list)):
                print "This problem haven't solution"
                return self.DFS_Aditive(start, limit + 1)

            if self.f_list[len(self.f_list) - 1].dep <= limit:
                currentState = self.f_list.pop(-1)
            else:
                min = 1000
                for state in self.f_list:
                    if state.dep <= min:
                        min = state.dep
                for state2 in reversed(self.f_list):
                    if state2.dep == min:
                        currentState = state2
                        self.f_list.remove(currentState)

    def DFS_Aditive_Tree(self, start, limit):
        currentState = start

        self.e_list = []
        self.f_list = []

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)

            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notInTree(nextState, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    nextState.dep = currentState.dep + 1
                    if self.problem.goalTest(nextState):
                        print "Finded"
                        self.pathFunction(nextState, len(self.e_list), len(self.e_list),
                                          len(self.e_list) + len(self.f_list), self.problem, "")
                        return

            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break

            counter = 0
            for state3 in self.f_list:
                if state3.dep > limit:
                    counter = counter + 1

            if (counter == len(self.f_list)):
                print "This problem haven't solution"
                return self.DFS_Aditive(start, limit + 1)

            if self.f_list[len(self.f_list) - 1].dep <= limit:
                currentState = self.f_list.pop(-1)
            else:
                min = 1000
                for state in self.f_list:
                    if state.dep <= min:
                        min = state.dep
                for state2 in reversed(self.f_list):
                    if state2.dep == min:
                        currentState = state2
                        self.f_list.remove(currentState)

    def UCS(self, start):

        currentState = start

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)


            if self.problem.goalTest(currentState):
                print "Finded"
                self.pathFunction(currentState, len(self.e_list), len(self.e_list), len(self.e_list) + len(self.f_list), self.problem, "")
                break

            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notIn(nextState, self.e_list, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    nextState.costUntilNow = currentState.costUntilNow + self.problem.stepCost(currentState, ac)
                else:
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    for f in self.f_list:
                        if nextState.value == f.value:
                            if nextState.paid() < f.paid():
                                f.path = nextState.path

            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break


            min = 10000
            for state in self.f_list:
               if state.costUntilNow < min:
                   min = state.costUntilNow

            for state in self.f_list:
                if state.costUntilNow == min:
                    currentState = state;
                    self.f_list.remove(state)
                    break


    def UCS_Tree(self, start):

        currentState = start

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)


            if self.problem.goalTest(currentState):
                print "Finded"
                self.pathFunction(currentState, len(self.e_list), len(self.e_list), len(self.e_list) + len(self.f_list), self.problem, "")
                break

            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notInTree(nextState, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    nextState.costUntilNow = currentState.costUntilNow + self.problem.stepCost(currentState, ac)
                else:
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    for f in self.f_list:
                        if nextState.value == f.value:
                            if nextState.paid() < f.paid():
                                f.path = nextState.path

            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break


            min = 10000
            for state in self.f_list:
               if state.costUntilNow < min:
                   min = state.costUntilNow

            for state in self.f_list:
                if state.costUntilNow == min:
                    currentState = state;
                    self.f_list.remove(state)
                    break

    def BFS(self, start):
        currentState = start

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)


            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notIn(nextState, self.e_list, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    if self.problem.goalTest(nextState):
                        print "Finded"
                        self.pathFunction(nextState, len(self.e_list), len(self.e_list),
                                          len(self.e_list) + len(self.f_list), self.problem, "")
                        return

            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break

            currentState = self.f_list.pop(0)


    def BFS_Tree(self, start):
        currentState = start

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)


            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notInTree(nextState, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    if self.problem.goalTest(nextState):
                        print "Finded"
                        self.pathFunction(nextState, len(self.e_list), len(self.e_list),
                                          len(self.e_list) + len(self.f_list), self.problem, "")
                        return

            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break

            currentState = self.f_list.pop(0)


    def bidirectional(self, start, end):

        currentState = start
        goalState = end
        counter = 0

        self.f_list.append(start)

        while True:
            possibleActionGoal = self.problem.actions(goalState)
            self.e_list_2.append(goalState)

            for ac in possibleActionGoal:
                nextStateGoal = self.problem.result(copy.deepcopy(goalState), ac)
                if self.notIn(nextStateGoal, self.e_list_2, self.f_list_2, ""):
                    self.f_list_2.append(nextStateGoal)
                    nextStateGoal.path = goalState.path + [{'state': goalState, 'action': ac}]
                foundStateCur = self.notIn(nextStateGoal, [], self.f_list, "bi")
                if foundStateCur is not None:
                    print "Finded"
                    goalState.path = nextStateGoal.path + goalState.path
                    path3 = []
                    for path in goalState.path:
                        if path.get('action') == "U":
                            path['action'] = "D"
                        elif path.get('action') == "D":
                            path['action'] = "U"
                        elif path.get('action') == "R":
                            path['action'] = "L"
                        elif path.get('action') == "L":
                            path['action'] = "R"

                    for step in foundStateCur.path:
                        path3.append(step.get('action'))
                    for step2 in goalState.path:
                        path3.append(step2.get('action'))

                    print("Path : "+str(path3))

                    self.pathFunction(goalState, len(self.e_list) + len(self.e_list_2), len(self.e_list) + len(self.e_list_2), len(self.e_list) + len(self.e_list_2) + len(self.f_list) + len(self.f_list_2), self.problem, "bi")
                    return


            possibleAction = self.problem.actions(currentState)
            self.e_list.append(currentState)
            if counter == 0:
                self.f_list.remove(start)

            counter = 10
            for ac in possibleAction:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notIn(nextState, self.e_list, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                foundStateGoal = self.notIn(nextState, [], self.f_list_2, "bi")
                if foundStateGoal is not None:
                    print "Finded"
                    currentState.path = nextState.path + currentState.path
                    path2 = []
                    for path1 in foundStateGoal.path:
                        if path1.get('action') == "U":
                            path1['action'] = "D"
                        elif path1.get('action') == "D":
                            path1['action'] = "U"
                        elif path1.get('action') == "R":
                            path1['action'] = "L"
                        elif path1.get('action') == "L":
                            path1['action'] = "R"

                    for step in currentState.path:
                        path2.append(step.get('action'))
                    for step in foundStateGoal.path:
                        path2.append(step.get('action'))

                    print("Path2 "+str(path2))


                    self.pathFunction(currentState, len(self.e_list) + len(self.e_list_2), len(self.e_list) + len(self.e_list_2), len(self.e_list) + len(self.e_list_2) + len(self.f_list) + len(self.f_list_2), self.problem, "bi")
                    return


            if len(self.f_list) == 0 and len(self.f_list_2) == 0:
                print "This problem haven't solution"
                break
                    
            if len(self.f_list) != 0:
                currentState = self.f_list.pop(0)

            if len(self.f_list_2) != 0:
                currentState = self.f_list_2.pop(0)

    def bidirectional_Tree(self, start, end):

        currentState = start
        goalState = end
        counter = 0

        self.f_list.append(start)

        while True:
            possibleActionGoal = self.problem.actions(goalState)
            self.e_list_2.append(goalState)

            for ac in possibleActionGoal:
                nextStateGoal = self.problem.result(copy.deepcopy(goalState), ac)
                if self.notInTree(nextStateGoal, self.f_list_2, ""):
                    self.f_list_2.append(nextStateGoal)
                    nextStateGoal.path = goalState.path + [{'state': goalState, 'action': ac}]
                foundStateCur = self.notInTree(nextStateGoal, self.f_list, "bi")
                if foundStateCur is not None:
                    print "Finded"
                    goalState.path = nextStateGoal.path + goalState.path
                    path3 = []
                    for path in goalState.path:
                        if path.get('action') == "U":
                            path['action'] = "D"
                        elif path.get('action') == "D":
                            path['action'] = "U"
                        elif path.get('action') == "R":
                            path['action'] = "L"
                        elif path.get('action') == "L":
                            path['action'] = "R"

                    for step in foundStateCur.path:
                        path3.append(step.get('action'))
                    for step2 in goalState.path:
                        path3.append(step2.get('action'))

                    print("Path : " + str(path3))

                    self.pathFunction(goalState, len(self.e_list) + len(self.e_list_2),
                                      len(self.e_list) + len(self.e_list_2),
                                      len(self.e_list) + len(self.e_list_2) + len(self.f_list) + len(self.f_list_2),
                                      self.problem, "bi")
                    return

            possibleAction = self.problem.actions(currentState)
            self.e_list.append(currentState)
            if counter == 0:
                self.f_list.remove(start)

            counter = 10
            for ac in possibleAction:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notInTree(nextState, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                foundStateGoal = self.notInTree(nextState, self.f_list_2, "bi")
                if foundStateGoal is not None:
                    print "Finded"
                    currentState.path = nextState.path + currentState.path
                    path2 = []
                    for path1 in foundStateGoal.path:
                        if path1.get('action') == "U":
                            path1['action'] = "D"
                        elif path1.get('action') == "D":
                            path1['action'] = "U"
                        elif path1.get('action') == "R":
                            path1['action'] = "L"
                        elif path1.get('action') == "L":
                            path1['action'] = "R"

                    for step in currentState.path:
                        path2.append(step.get('action'))
                    for step in foundStateGoal.path:
                        path2.append(step.get('action'))

                    print("Path2 " + str(path2))

                    self.pathFunction(currentState, len(self.e_list) + len(self.e_list_2),
                                      len(self.e_list) + len(self.e_list_2),
                                      len(self.e_list) + len(self.e_list_2) + len(self.f_list) + len(self.f_list_2),
                                      self.problem, "bi")
                    return

            if len(self.f_list) == 0 and len(self.f_list_2) == 0:
                print "This problem haven't solution"
                break

            if len(self.f_list) != 0:
                currentState = self.f_list.pop(0)

            if len(self.f_list_2) != 0:
                currentState = self.f_list_2.pop(0)


    def A_star(self, start):
        currentState = start

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)

            if (self.problem.goalTest(currentState)):
                print "Finded"
                self.pathFunction(currentState, len(self.e_list), len(self.e_list), len(self.e_list) + len(self.f_list),
                                  self.problem, "")
                break

            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notIn(nextState, self.e_list, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    nextState.Hu = self.problem.huristic(nextState)
                    nextState.costUntilNow = currentState.costUntilNow + self.problem.stepCost(currentState, ac)
                else:
                    for f in self.f_list:
                        if nextState.value == f.value:
                            if nextState.paid() < f.paid():
                                f.path = nextState.path


            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break

            min = 10000
            for state in self.f_list:
                if (state.paid() < min):
                    min = state.paid()

            for state in self.f_list:
                if (state.paid() == min):
                    currentState = state
                    self.f_list.remove(state)
                    break


    def A_star_Tree(self, start):
        currentState = start

        while True:
            possibleActions = self.problem.actions(currentState)
            self.e_list.append(currentState)

            if (self.problem.goalTest(currentState)):
                print "Finded"
                self.pathFunction(currentState, len(self.e_list), len(self.e_list), len(self.e_list) + len(self.f_list),
                                  self.problem, "")
                break

            for ac in possibleActions:
                nextState = self.problem.result(copy.deepcopy(currentState), ac)
                if self.notInTree(nextState, self.f_list, ""):
                    self.f_list.append(nextState)
                    nextState.path = currentState.path + [{'state': currentState, 'action': ac}]
                    nextState.Hu = self.problem.huristic(nextState)
                    nextState.costUntilNow = currentState.costUntilNow + self.problem.stepCost(currentState, ac)
                else:
                    for f in self.f_list:
                        if nextState.value == f.value:
                            if nextState.paid() < f.paid():
                                f.path = nextState.path


            if len(self.f_list) == 0:
                print "This problem haven't solution"
                break

            min = 10000
            for state in self.f_list:
                if (state.paid() < min):
                    min = state.paid()

            for state in self.f_list:
                if (state.paid() == min):
                    currentState = state
                    self.f_list.remove(state)
                    break


    def notIn(self, targetState, e_list, f_list ,str):

        if str == "bi":
            for e in e_list:
                if targetState.value == e.value:
                    return e

            for f in f_list:
                if targetState.value == f.value:
                    return f
        else:
            for e in e_list:
                if targetState.value == e.value:
                    return False

            for f in f_list:
                if targetState.value == f.value:
                    return False

            return True

    def notInTree(self, targetState, f_list, str):

        if str == "bi":
            for f in f_list:
                if targetState.value == f.value:
                    return f
        else:

            for f in f_list:
                if targetState.value == f.value:
                    return False

            return True






    def pathFunction(self, state, numOfSeenNodes, numOfExpandNodes, mem, problem, strr):


        self.path = []
        self.cost = 0

        if strr != "bi":
            for step in state.path:
                self.path.append(step.get('action'))
                self.cost = self.cost + problem.stepCost(step.get('state') , step.get('action'))


            print 'Path = ' + str(self.path)
        print 'Cost = ' + str(self.cost)
        print 'Number of seen nodes = ' + str(numOfSeenNodes)
        print 'Number of expanded nodes = ' + str(numOfExpandNodes)
        print 'Memory used : ' + str(mem)




