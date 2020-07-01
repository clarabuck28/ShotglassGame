from random import seed
from random import randint

import statistics

def find_winner(list):
    #check if there is a winner and whO. list1 is people list, list2 is hit list
    # return [0,0] if no winner, [1,k] if winner where k is winner
    for k in range(len(list)):
        if list[k] == 0:
            return k

def play(n):
    #play the game with n people, person 1 always gets the shot first
    #return the winner

    plist = [] #pist is a list of people
    for k in range(n):
        plist.append(k)

    hlist= [] #hilist keeps track of if someone in plist is hit or not
    #0 is not hit and a 1 is hit
    for k in range(n):
        hlist.append(0)

    hasshot = 0
    hlist[hasshot] = 1
    numberhit = 1
    counter = 0
    while numberhit < n-1:
        l = randint(0,1) #0 is heads (go lower), 1 is tails (go highter)
        counter += 1
        if l == 0:
            if hasshot == 0:
                hasshot = n-1
            else:
                hasshot = hasshot-1
        if l==1:
            if hasshot == n-1:
                hasshot = 0
            else:
                hasshot = hasshot+1
        if hlist[hasshot] == 0:
            numberhit = numberhit+1
            hlist[hasshot] = 1
    return find_winner(hlist), counter

def iterategame(numplayers, n):
    #iterate a game with numplayers n times
    #return a list of the number of times each player won
    countlist = []
    for k in range(numplayers):
        countlist.append(0)
    for k in range(n):
        winner,steps = play(numplayers)
        countlist[winner] = countlist[winner] + 1
    return countlist

def lengthofgame(numplayers, n):
    #iterate a game with numplayers n times
    #return a list with an entry for each game representing the length of game
    counterlist = []
    for k in range(n):
        winner, steps = play(numplayers)
        counterlist.append(steps)
    return counterlist

def iteratelengthofgame(minplayers,maxplayers,step, n):
    #play n games with each number of players between minplayers and maxplayers
    #increment by step value
    orderedpairs = []
    currentplayers = minplayers
    while currentplayers <= (maxplayers - step):
        meanval = 0
        standevval = 0
        lengthlist = lengthofgame(currentplayers, n)
        meanval = mean(lengthlist)
        standevval = int(standev(lengthlist))
        orderedpairs.append((currentplayers,meanval,standevval))
        currentplayers += step
    return orderedpairs

def mean(list):
    #return mean of a list
    return sum(list)/len(list)

def standev(list):
    #return standard deviation of a list of numbers
    meanval = 0
    meanval = mean(list)
    sumofsquares = 0
    for value in list:
        sumofsquares = sumofsquares + (value - meanval)**2
    return (sumofsquares/len(list))**.5


#print(iterategame(17,10000))
#print(play(10))
#print(lengthofgame(200,10))
#testerlist = [1,2,-4,-8,16]
#print(iteratelengthofgame(10,400,20,10))
print(lengthofgame(17,100))
