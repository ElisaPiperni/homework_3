import random
import timeit
from collections import OrderedDict
from BinarySearchTree import BST
import matplotlib.pyplot as plt
import math


insDict = OrderedDict()
getRandomDict = OrderedDict()
getMaxDict = OrderedDict()
deleteRandomDict = OrderedDict()

#insertion

check_points = [1, 10, 50, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]
tree = BST()
randoms = random.sample(range(10000), 10000)


for i in range(len(randoms)):
    tree.insert(randoms[i])

    if i in check_points:

        tot_time = 0
        for n in range(100):
            t1 = timeit.timeit('tree.insert(randoms[i])',  number=1, globals=globals())
            tot_time += t1
            tree.delete(randoms[i])
        xAxis1 = i
        insDict[xAxis1] = tot_time/100



size = [10, 100, 1000, 10000, 100000]

for x in size:
    randoms = random.sample(range(x), x)
    tree = BST()
    for n in randoms:
        tree.insert(n)

#get random element
    tot_time2 = 0

    for i in range(100):
        rand = random.choice(randoms)

        t2 = timeit.timeit('tree.find(rand)' , number=1, globals=globals())
        tot_time2 += t2

    xAxis2 = x
    getRandomDict[xAxis2] = tot_time2/100



#get max element
    tot_time3 = 0

    for i in range(100):
        t3 = timeit.timeit('tree.maximum()' , number=1, globals=globals())
        tot_time3 += t3

    xAxis3 = x
    getMaxDict[xAxis3] = tot_time3/100



#delete random element
    tot_time4 = 0

    for i in range(100):
        rand = random.choice(randoms)

        t4 = timeit.timeit('tree.delete(rand)' , number=1, globals=globals())
        tot_time4 += t4
        tree.insert(rand)

    xAxis4 = x
    deleteRandomDict[xAxis4] = tot_time4/100




#plot

plt.figure(1)
plt.scatter(list(insDict.keys()), list(insDict.values()), color='b')
plt.plot(list(insDict.keys()), list(insDict.values()), color='b')
plt.title('insertion execution time')
plt.ylabel('time')
plt.xlabel('index')
plt.grid(True)
plt.ylim(min(insDict.values()), max(insDict.values()))




plt.figure(2)
plt.subplot(221)
plt.plot(list(getRandomDict.keys()), list(getRandomDict.values()), color='r')
plt.scatter(list(getRandomDict.keys()), list(getRandomDict.values()), color='r')
plt.title('get random element execution time', color='r')
plt.grid(True)
plt.ylabel('time')
plt.xlabel('size')
plt.ylim(min(getRandomDict.values()),max(getRandomDict.values()))

plt.subplot(222)
plt.plot(list(getMaxDict.keys()), list(getMaxDict.values()), color='g')
plt.scatter(list(getMaxDict.keys()), list(getMaxDict.values()), color='g')
plt.title('get maximum element execution time', color='g')
plt.grid(True)
plt.ylabel('time')
plt.xlabel('size')
plt.ylim(min(getMaxDict.values()),max(getMaxDict.values()))

plt.subplot(223)
plt.plot(list(deleteRandomDict.keys()), list(deleteRandomDict.values()), color='b')
plt.scatter(list(deleteRandomDict.keys()), list(deleteRandomDict.values()), color='b')
plt.title('delete random element execution time', color='b')
plt.grid(True)
plt.ylabel('time')
plt.xlabel('size')
plt.ylim(min(deleteRandomDict.values()),max(deleteRandomDict.values()))

plt.subplot(224)
plt.plot(list(getRandomDict.keys()), list(getRandomDict.values()), color='r', label = 'get random')
plt.scatter(list(getRandomDict.keys()), list(getRandomDict.values()), color='r',)
plt.plot(list(getMaxDict.keys()), list(getMaxDict.values()), color='g', label ='get max')
plt.scatter(list(getMaxDict.keys()), list(getMaxDict.values()), color='g')
plt.plot(list(deleteRandomDict.keys()), list(deleteRandomDict.values()), color='b', label='delete random')
plt.scatter(list(deleteRandomDict.keys()), list(deleteRandomDict.values()), color='b')
plt.legend(bbox_to_anchor=(1,0.2))
plt.title('comparison')


plt.show()










