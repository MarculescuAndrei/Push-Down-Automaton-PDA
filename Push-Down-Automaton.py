import copy
f = open("Source2.txt", 'r')

Checker = 0
print("Criteria Choices: ")
print("1 = By Empty Stack")
print("2 = By Final State")
print("3 = By Empty Stack & Final State")

Criteria = input("The criteria is: ")

def Validation(Word, Adjacency, CurrentState):
    NextState = ['0', '1']
    global Checker
    print(CurrentState)
    if Word == '':

        if CurrentState[0] in Adjacency:
            for Arc in Adjacency[CurrentState[0]]:
                if Arc[1] == '&':
                    if Arc[2] == 'Pop':
                        if CurrentState[1][-1] == Arc[3]:
                            NextState[0] = Arc[0]
                            NextState[1] = NextState[1] = copy.deepcopy(CurrentState[1][:-1])
                            Validation(Word, Adjacency, NextState)
                    elif Arc[2] != 'Pop' and Arc[2] !='-':
                        if CurrentState[1][-1] == Arc[3]:
                            NextState[0] = Arc[0]
                            NextState[1] = copy.deepcopy(CurrentState[1])
                            if len(Arc[2]) > 1:
                                for i in range(len(Arc[2])):
                                    NextState[1].append(Arc[2][i])
                            else:
                                NextState[1].append(Arc[2])
                            Validation(Word, Adjacency, NextState)
                    elif Arc[2] == '-':
                        NextState[0] = Arc[0]
                        NextState[1] = copy.deepcopy(CurrentState[1])
                        Validation(Word, Adjacency, NextState)

        if Criteria == '2':
            if CurrentState[0] in Final and CurrentState[1] != []:
                Checker += 1000

        elif Criteria == '1':
            if CurrentState[1] == []:
                Checker += 1000

        elif Criteria == '3':
            if CurrentState[0] in Final and CurrentState[1] == []:
                Checker += 1000

    else:
        if CurrentState[0] in Adjacency:
            for Arc in Adjacency[CurrentState[0]]:
                if Word[0] == Arc[1]:
                    if Arc[2] == 'Pop':
                        if CurrentState[1][-1] == Arc[3]:
                            NextState[0] = Arc[0]
                            NextState[1] = copy.deepcopy(CurrentState[1][:-1])
                            Validation(Word[1:], Adjacency, NextState)
                    elif Arc[2] != 'Pop' and Arc[2] !='-':
                        if CurrentState[1][-1] == Arc[3]:
                            NextState[0] = Arc[0]
                            NextState[1] = copy.deepcopy(CurrentState[1])
                            if len(Arc[2]) > 1:
                                for i in range(len(Arc[2])):
                                    NextState[1].append(Arc[2][i])
                            else:
                                NextState[1].append(Arc[2])
                            Validation(Word[1:], Adjacency, NextState)
                    elif Arc[2] == '-':
                        NextState[0] = Arc[0]
                        NextState[1] = copy.deepcopy(CurrentState[1])
                        Validation(Word[1:], Adjacency, NextState)
                elif Word[0] == '&':
                    if Arc[2] == 'Pop':
                        if CurrentState[1][-1] == Arc[3]:
                            NextState[0] = Arc[0]
                            NextState[1] = copy.deepcopy(CurrentState[1][:-1])
                            Validation(Word, Adjacency, NextState)
                    elif Arc[2] != 'Pop' and Arc[2] !='-':
                        if CurrentState[1][-1] == Arc[3]:
                            NextState[0] = Arc[0]
                            NextState[1] = copy.deepcopy(CurrentState[1])
                            if len(Arc[2]) > 1:
                                for i in range(len(Arc[2])):
                                    NextState[1].append(Arc[2][i])
                            else:
                                NextState[1].append(Arc[2])
                            Validation(Word, Adjacency, NextState)
                    elif Arc[2] == '-':
                        NextState[0] = Arc[0]
                        NextState[1] = copy.deepcopy(CurrentState[1])
                        Validation(Word, Adjacency, NextState)

poz = f.readline()
poz = poz[:-1]

CurrentState = [poz, ['Z0']]
Final = f.readline().split()
L = f.readline().split()
Adjacency = {}

while L:
    if L[0] not in Adjacency.keys():
        Adjacency[L[0]] = [(L[1], L[2], L[3], L[4])]

    else:
        Adjacency[L[0]].append((L[1], L[2], L[3], L[4]))
    L = f.readline().split()

print("The PDA Form is: ")
print(Adjacency)
print('\n')

Word = input("The word is: ")
Validation(Word, Adjacency, CurrentState)

if Checker > 0:
    print("The word is accepted by the PDA")
else:
    print("The word is not accepted by the PDA")
