player = ['Tom', 'Khalil', 'Benjamin', 'Antonio', 'Sami']
scores = [10, 1, 17, 16, 16]
import matplotlib.pyplot as plt
def diagram():
 fig = plt.figure()             #this step creates the area the plot will be drawn onto
 plt.bar(player, scores)        #this step decides the kind of plot we will create
 plt.show()                     #this step displays the plot
scores = [  (101, 97, 79),      #after a few games
            (67, 85, 103),
            (48, 201, 105),
            (132, 132, 131),
            (122, 134, 143)
         ]
maxscore=[]
for i in scores:                #pick the highest score
    maxscore.append(max(i))
scores=maxscore
diagram()                       #make a graph