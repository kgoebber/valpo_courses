#! /usr/bin/env python

import sys

models = ['ssef_cn','ST2','2km','nam_12km']
pcents = [50.,60.,70.,80.,90.,95.,98.,99.]

for model in models:

    ouf = 'threshs.out_'+model+'.txt' #for use later

    inf = 'array.out.pass_'+model
    file = open(inf,'r')
    lines= file.readlines()
    print "len(lines)=",len(lines)
    file.close()

    new = []
    for i in range(0,len(lines)):
	a = lines[i].split()
	for j in range(0,len(a)):
		b = float(a[j])
		new.append(b)	

    new.sort()
    new.reverse() #Orders the array from highest value to lowest
    print "length =",len(new)

    out = open(ouf,'w') #Filename specified earlier
    for pcent in pcents:
        print "pcent =",pcent
        frac = pcent/100

        #Writes out the value of the xth percentile
        num = int(len(new)*(1-frac))
        thresh = new[num-1]
        print num
        print "new thresh =",new[num-1]
        out.write(str(pcent)+' '+str(thresh)+'\n')
    out.close()
