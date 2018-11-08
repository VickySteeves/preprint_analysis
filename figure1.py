import numpy as np
import matplotlib.pyplot as plt

downloadX = ['2017-10', '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', 
             '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', 
             '2018-10']

downloads = [10630, 18827, 5963, 4783, 4992, 3204, 2736, 1462, 1557, 1350, 1615, 
             1286, 1442]

submissions = [28, 70, 22, 17, 10, 6, 15, 7, 6, 2, 3, 12, 6, 14, 6, 1, 13, 7, 8, 5, 
               8, 5, 6, 4, 9, 9, 7, 8, 8, 8, 11, 5, 8, 8, 9, 7, 8, 8, 5, 4, 1, 6, 10, 
               5, 12, 1, 5, 5, 17, 8, 9,10]

preprints = [15, 12, 8, 3, 9, 5, 14, 7, 5, 2, 3, 9, 5, 7, 6, 1, 12, 6, 8, 4, 8, 3, 
             5, 3, 8, 7, 7, 8, 6, 8, 10, 4, 7, 7, 9, 7, 7, 8, 4, 4, 1, 5, 10, 5, 12, 
             1, 5, 5, 15, 4, 8, 10]

postprints = [13, 58, 14, 14, 1, 1, 1, 0, 1, 0, 0, 3, 1, 7, 0, 0, 1, 1, 0, 1, 0, 2, 
              1, 1, 1, 2, 0, 0, 2, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 
              0, 0, 0, 2, 4, 1, 0]

ticks = list(range(2,54,2))
N = len(preprints)

tPre = []
tPos = []
sumPre = preprints[0]
sumPos = postprints[0]
for i in range(N):
    if i == 0:
        tPre.append( sumPre )
        tPos.append( sumPos )
    else:
        sumPre += preprints[i] 
        sumPos += postprints[i] 
        tPre.append(sumPre)
        tPos.append(sumPos)

ind = np.arange(N)+1    # the x locations for the groups
width = 0.4      # the width of the bars: can also be len(x) sequence

plt.figure(figsize=(25,20))
plt.rcParams.update({'font.size': 20})

plt.subplot(3, 1, 1)
p1 = plt.bar(ind, tPre, width, align='edge')
p2 = plt.bar(ind, tPos, width, align='edge', bottom=tPre)
plt.ylabel('Papers at EarthArXiv')
plt.xlabel('Weeks Since Inception')
plt.title('Cummulative Number of Ppaers at EarthArXiv')
plt.xticks(ticks)
plt.legend((p1[0], p2[0]), ('Preprints', 'Postprints'))

plt.subplot(3, 1, 2)
plt.bar(ind, submissions)
plt.ylabel('Papers Submitted')
plt.xticks(ticks)
plt.xlabel('Weeks Since Inception')
plt.title('EarthArXiv Submission Rate')

plt.subplot(3, 1, 3)
plt.bar( np.arange(0,len(downloads),1), downloads)
plt.ylabel('Downloads')
plt.xlabel('Month')
plt.xticks(list(range(13)), downloadX)
plt.title('EarthArXiv Monthly Downloads')

plt.subplots_adjust(hspace=.4)

plt.savefig('./figure1.png', bbox_inches='tight')