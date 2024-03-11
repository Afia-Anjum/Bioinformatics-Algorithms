# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:04:14 2020

@author: Asus
"""
import os
helix_cnt = []
sheet_cnt=[]
helix=[]
sheet=[]
#https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html

#directory = 'the/directory/you/want/to/use'
directory="D://ALBERTA//Winter_2020//Algorithms_in_Bioinformatics//Assignment7"
for filename in os.listdir(directory):
    #print(os.getcwd())
    #print(filename)
    if filename.endswith(".pdb"):
        f = open(filename)
        count=0
        for ln in f:
            if ln.startswith("HELIX"):
                ln=ln.strip()
                ln=ln.split()
                length=len(ln)
                helix_cnt.append(ln[5])
                helix_cnt.append(ln[8])
                helix_cnt.append(ln[length-1])
                helix.append(helix_cnt)
                helix_cnt=[]
            elif ln.startswith("SHEET"):
                ln=ln.strip()
                ln=ln.split()
                length=len(ln)
                #if count==0:
                #    sheet_cnt.append(ln[6])
                #    sheet_cnt.append(ln[9])
                #    sheet_cnt.append(ln[5])
                #    sheet_cnt.append(ln[8])
                if count>0 and int(ln[1])==1:
                    continue
                else:
                    sheet_cnt.append(ln[6])
                    sheet_cnt.append(ln[9])
                    sheet_cnt.append(ln[5])
                    sheet_cnt.append(ln[8])
                #sheet_cnt.append(ln[length-1])
                if len(sheet_cnt)>0:
                    sheet.append(sheet_cnt)
                    sheet_cnt=[]
            count+=1
        print(helix)
        print(sheet)
        cnthelix=0
        cntsheet=0
        for i in range(len(helix)):
            cnthelix +=int(helix[i][2])
        for i in range(len(sheet)):
            #print(filename)
            try:
                cntsheet +=int(sheet[i][1])-int(sheet[i][0])
            except ValueError:
                cntsheet +=int(sheet[i][3])-int(sheet[i][2])
        helix=[]
        sheet=[]
        f1=open("true.txt",'a')
        #cntsheet=int(cntsheet/6)
        f1.write(str(cnthelix)+" "+str(cntsheet)+"\n")
        #f1.write(str(cnthelix)+" "+str(cntsheet))
        f1.close()
        f.close()
            