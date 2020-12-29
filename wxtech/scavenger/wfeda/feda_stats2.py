#!/usr/bin/env python

import sys,re
import Scientific.Statistics as ss
#import matplotlib
#from pylab import *

#sys.agv[1] = lightning file 
#sys.agv[2] = date 
#sys.agv[3] = report file 
#sys.agv[4] = restart 


def count(fname):
	new=[] # initialize a list of lists
	inf=open(fname,'r')
	file=inf.readlines() #reads in the lines
	for i in range(0,len(file)): #loops over each line
	  a=file[i].split(',') #split string at the comma
	  new.append(a) #appends each line to new 

	return new #returns list of list

#function checking for forecast in a category
#def category(light,num,rep):

def category(inf): #stratify by forecaster
	count_num = 0
	count_no = 0
	count_rep = 0
	restart = 'w'
	for j in range(0,len(inf)):
	    day = inf[j][0]
	    forecaster = inf[j][1]
	    for col in [2,8,14,20]:
	        count_num = int(inf[j][col]) + int(inf[j][col+1])
		if inf[j][col+3] == '-9999':
		    count_no = 0
		else:
	            count_no = int(inf[j][col+3])
		if inf[j][col+4] == '-9999':
	            count_rep = 0
		else:
	            count_rep = int(inf[j][col+4])
		
	        if col == 2:
	            out_nt = day+','+forecaster+','+str(count_num)+','+str(count_no)+','+str(count_rep)
		    d = count_num
	        elif col == 8:
	            out_n0 = str(count_num)+','+str(count_no)+','+str(count_rep)
		    e = count_num
	        elif col == 14:
	            out_n1 = str(count_num)+','+str(count_no)+','+str(count_rep)
		    f = count_num
	        elif col == 20:
	            out_n2 = str(count_num)+','+str(count_no)+','+str(count_rep)
		    g = count_num
            outstring = out_nt+','+out_n0+','+out_n1+','+out_n2
	    if d+e+f+g != 6063:
		print day
	    ouf= open('rep_data2.txt',restart)
	    ouf.write(outstring+'\n')
	    ouf.close()
            restart = 'a'	
#read in data file
data = 'all_catfin_dep2.txt'

#get data
list = count(data)

#append = sys.argv[1]
#if append == 'append':
#	restart = 'a'
#else:
#	restart = 'w'

category(list)


#Reads in newly created file
#parsed = 'rep_data.txt'
#parsed = count(parsed)
#print parsed

#Striates by forecaster
#forecasters = ['dahl','gatzen','groenemeijer','tuschy','van der velde']
#for forecaster in forecasters:
#    name = 'fcasts_'+forecaster+'.txt'
#    restart = 'w'
#    for j in range(0,len(parsed)):
#        if parsed[j][1].lower() == forecaster: 
#	    file = open(name,restart)
# 	    file.write(str(parsed[j])+'\n')
#	    file.close()
#            restart = 'a' 
