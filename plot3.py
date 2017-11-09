import numpy as np
import matplotlib.pyplot as plt
import sys
import mpld3

np.random.seed(19680801)
ccps = []
i = 0
maxsize = 0
names = []
for line in sys.stdin:
    line = line.split()
    name=line[0]
    names.append(name)
    size,pannot,minlen,maxlen,diff = tuple([float(x) for x in line[1:6]])
    if size > maxsize: maxsize = size;
    ccps.append([(int(c),int(size)) for c in line[6:]])
    i+=1
print(maxsize)
#each column of ccps is a different group to plot
ccps = np.array(ccps)
group = []
for i in range(0,len(ccps[0,:])):
    group.append(ccps[:,i])
data = tuple(group)
# need 6 colors
colors = ("red", "green", "blue","orange","purple","pink")
groups = ('30%','80%','90%','95%','99%')
#groups = [i.__repr__() for i in range(len(group))]

# Create plot
#fig = plt.figure()
fig, ax = plt.subplots()
#ax = fig.add_subplot(1, 1, 1,axisbg="1.0")
ax.set_xlabel('Number of connected components')
ax.set_ylabel('Size of family')
 
grouppts = []
i = 0
groupnames = []
for d, color, group in zip(data, colors, groups):
    x, y = d[:,0],d[:,1]
    a = ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
    size = len(x)
    groupnames.append(list(names[i:i+size]))
    i+= size
    grouppts.append(a)
scale = 1.1

#leg = ax.legend(handles=grouppts,loc='upper left', fancybox=True, shadow=True)
leg = ax.legend(handles=grouppts, fancybox=True, shadow=True)
#leg = ax.legend(handles=[],loc='upper left', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.4)

lines = grouppts
lined = dict()
#for k in lmap.keys():
    #print(k)
texts = leg.get_texts()
for i in range(len(texts)):
    texts[i].set_picker(5)
    lined[texts[i]] = lines[i]

def onpick(event):
    # on the pick event, find the orig line corresponding to the
    # legend proxy line, and toggle the visibility
    legline = event.artist
    origline = lined[legline]
    vis = not origline.get_visible()
    origline.set_visible(vis)
    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled
    if vis:
        legline.set_alpha(1.0)
    else:
        legline.set_alpha(0.2)
    fig.canvas.draw()

fig.canvas.mpl_connect('pick_event', onpick)

#i = 0
#for grp in grouppts:
#    #tooltip = mpld3.plugins.PointLabelTooltip(grp,labels=groupnames[i])
#    #mpld3.plugins.connect(fig, tooltip)
#    i+=1

#mpld3.show()



plt.title('Title')
plt.show()
