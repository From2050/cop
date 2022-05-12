import tkinter as tk
from tkinter import filedialog
import numpy as np
import mne
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    print('hellow')
    print('this is cop data plot')

    filepath = "./2022_04_27_16_48_41/2022_04_27_16_48_41_insoleL.txt"

    with open(filepath,'r') as f:
        #Atemp = np.zeros(227+5,dtype=bytes)
        #Aframe = np.zeros(227+5,dtype=bytes)
        Atemp = np.zeros(227+5,dtype=int)
        Aframe = np.zeros(227+5,dtype=int)
        index = 0
        for line in f :
            print(l)
            temp = line.rstrip().split(',')
            if temp[1] == 'CA':
                Aframe = np.vstack([Aframe, Atemp])
                time = temp[0].split('.')
                #Atemp[0] = bytes([int(time[0][0:2])])
                #Atemp[1] = bytes([int(time[0][3:5])])
                #Atemp[2] = bytes([int(time[0][6:8])])
                #Atemp[3] = bytes([int(time[1][0:2])])
                Atemp[0] = int(time[0][0:2])
                Atemp[1] = int(time[0][3:5])
                Atemp[2] = int(time[0][6:8])
                Atemp[3] = int(time[1][0:2])
                index = 0
            else :
                for i in range(0,int(len(temp[1])),2):
                    #if i == 0 : print(temp[1])
                    #Atemp[(4+i)] = bytes.fromhex(temp[1][2*i:2*i+2])
                    Atemp[(4+index)] = int(temp[1][i:i+2],16)
                    index = index + 1
                    #if i == 0 : print(Atemp[(4+i)])





    #Ain = np.loadtxt(filepath,dtype=str,delimiter=',')

    #Atime, Adata = np.hsplit(Ain, [1])
    #Adata = Adata.reshape(-1)                   #expand to line
    
    #frame = []
    #temp = ''
    #for a in Adata :
    #    if a == "CA" :
    #        frame = frame.append(temp)
    #        temp = ''
    #        #pass
    #    else :
    #        temp = temp + a
    #        #pass
    #Aframe = np.array(frame)



    #Atime = Atime[np.where(Adata == "CA")]      # getting time tag by finding index of CA  
    
    




    ##aa








if __name__ == '__main__':
    main()