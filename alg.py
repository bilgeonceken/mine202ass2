import matplotlib.pyplot as plt
import numpy as np


class Zero(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ebv = 0
        self.cbv = 0
        self.tbv = 0

    def __repr__(self):
        return "-"

class Waste(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ebv = -(2.5*(y-1)+4)
        self.cbv = None
        self.tbv = None

    def __repr__(self):
        return "W"


class Ore(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ebv = 66 - (2.5*(y-1)+4) -27
        self.cbv = None
        self.tbv = None

    def __repr__(self):
        return "O"

## 20 column (including zero blocks)
## 12 row (including zero blocks)

## Initiates our 2d array which will hold the block objects
real = [[0 for z in range(20)] for g in range(12)]


## Filling first row and first column with zero blocks
## Their their cbv and tbv values will used as a foundation
## when calculating the rest

## Fills the first column with Zero blocks
for i in range(20):
    real[0][i] = Zero(i,0)

## Fills the first row with Zero blocks
for i in range(12):
    real[i][0] = Zero(0,i)

## Stores the block objects in a 2d array while
## calculating their ebv, cbv and tbv values.
## We have to do it column by to column to be able to
## make tbv calculation.  
## Later(ln. 90) we will pull the data from this objects to
## put in subplots, which is the way we present the data.
for i in range(1,20):
    for k in range(1,12):
        if (8<=i<=12) and (k>=3):
            real[k][i] = Ore(i,k)
            real[k][i].cbv = real[k][i].ebv + real[k-1][i].cbv
            if k==11:
                real[k][i].tbv = real[k][i].cbv + max(real[k-1][i-1].tbv, real[k][i-1].tbv)
            else:
                real[k][i].tbv = real[k][i].cbv + max(real[k-1][i-1].tbv, real[k][i-1].tbv, real[k+1][i-1].tbv)
        else:
            real[k][i] = Waste(i,k)
            real[k][i].cbv = real[k][i].ebv + real[k-1][i].cbv
            if k==11:
                real[k][i].tbv = real[k][i].cbv + max(real[k-1][i-1].tbv, real[k][i-1].tbv)
            else:
                real[k][i].tbv = real[k][i].cbv + max(real[k-1][i-1].tbv, real[k][i-1].tbv, real[k+1][i-1].tbv)


                    ####
## To present the data in an eye pleasing way plotlib library has been used
## Shows the ebv, cbv and tbv values of every block in a seperate subplot.
## Margin is set to 0 so that all thing looks like a grid
                    ####
    
    
## Creates a 2d array to store subplots
layout = [[0 for z in range(20)] for g in range(12)]

# plot counter
i=1

## Takes the relevant data from the block objects and
## puts them in subplots
for y in range(12):
    for x in range(20):
        layout[y][x] = plt.subplot(12,20,i)
        layout[y][x].text(0.1, 0.8, "EBV: "+str(real[y][x].ebv),
                          size=9, alpha=1.0 )
        layout[y][x].text(0.1, 0.6, "CBV: "+str(real[y][x].cbv),
                          size=9, alpha=1.0 )
        layout[y][x].text(0.1, 0.4, "TBV: "+str(real[y][x].tbv),
                          size=9, alpha=1.0 )
        layout[y][x].set_xticklabels([])
        layout[y][x].set_yticklabels([])
        ## color the ore part
        if (8<=x<=12) and (y>=3):
            layout[y][x].set_facecolor("grey")
        elif (x==0) or (y==0):
            layout[y][x].set_facecolor("beige")
        i+=1

plt.xticks(())
plt.yticks(())
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
