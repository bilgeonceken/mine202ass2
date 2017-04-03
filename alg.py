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

## 20 column with zeros
## 13 row with zeros

real = [[0 for z in range(20)] for g in range(12)]

##COLUMN
for i in range(20):
    real[0][i] = Zero(i,0)

## ROW
for i in range(12):
    real[i][0] = Zero(0,i)

## NEXT COLUMNS
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


layout = [[0 for z in range(20)] for g in range(12)]
i=1
for y in range(12):
    for x in range(20):
        # layout[y][x] = Ore(x,y)
        layout[y][x] = plt.subplot(12,20,i)
        layout[y][x].text(0.1, 0.8, "EBV: "+str(real[y][x].ebv),
                        #   ha='center',
                        #   va='center',
                          size=9, alpha=1.0 )
        # layout[y][x].text(0.1, 0.4, "POS: "+Ore(x,y).get_pos(),
        #                 #   ha='center',
        #                 #   va='center',
        #                   size=7, alpha=1.0 )
        layout[y][x].text(0.1, 0.6, "CBV: "+str(real[y][x].cbv),
                        #   ha='center',
                        #   va='center',
                          size=9, alpha=1.0 )
        layout[y][x].text(0.1, 0.4, "TBV: "+str(real[y][x].tbv),
                        #   ha='center',
                        #   va='center',
                          size=9, alpha=1.0 )
        layout[y][x].set_xticklabels([])
        layout[y][x].set_yticklabels([])
        if (8<=x<=12) and (y>=3):
            layout[y][x].set_facecolor("grey")

        i+=1


plt.xticks(())
plt.yticks(())
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
