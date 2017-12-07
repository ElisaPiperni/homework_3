import random
from timeit import Timer
from collections import OrderedDict
import matplotlib.pyplot as plt


l =[10, 100, 1000]
dquick= OrderedDict()
dmerge= OrderedDict()

for x in l:
    randoms = random.sample(range(x),x)

    s1 = 'merge(' + str(randoms) + ')'
    t1 = Timer(s1, 'from sorting import merge')
    time1 = t1.timeit(10)/10
    dquick[x] = time1

    s2 = 'quicksort(' + str(randoms) + ')'
    t2 = Timer(s2, 'from sorting import quicksort')
    time2 = t2.timeit(10)/10
    dmerge[x] = time2


plt.plot(dquick.keys(),dquick.values(), label = 'quick sort')
plt.plot(dmerge.keys(),dmerge.values(), label = 'merge sort')
plt.xlabel('length of the list')
plt.ylabel('time')
plt.title('Sorting execution time')
plt.legend(bbox_to_anchor=(1,0.2))
plt.show()
