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
        
        Atemp = np.zeros(227+4,dtype=int)   # time(4)  + CA(1) + framenumber(1)  +data(8*28 = 224) + 0A (1) 
        Aframe = np.zeros(227+4,dtype=int)
        index = 0
        error = 0
        for line in f :
            print(line)
            temp = line.rstrip().split(',')
            for i in range(0,int(len(temp[1])),2):
                if temp[1][i:i+2] == 'CA':
                    Aframe = np.vstack([Aframe, Atemp])
                    time = temp[0].split('.')
                    Atemp[0] = int(time[0][0:2])
                    Atemp[1] = int(time[0][3:5])
                    Atemp[2] = int(time[0][6:8])
                    Atemp[3] = int(time[1][0:2])
                    index = 0
                    
                else :
                    if index == 227 :
                        index = 0
                        error = error + 1 
                    Atemp[(4+index)] = int(temp[1][i:i+2],16)
                    index = index + 1
                
                #    for i in range(0,int(len(temp[1])),2):
                #        #if i == 0 : print(temp[1])
                #        #Atemp[(4+i)] = bytes.fromhex(temp[1][2*i:2*i+2])
                #        Atemp[(4+index)] = int(temp[1][i:i+2],16)
                #        index = index + 1
                #        #if i == 0 : print(Atemp[(4+i)])

    Atest = Aframe[2:,6:-1]
    Atest = Atest.reshape((413,28,8))
    sns.heatmap(data=Atest[0],square=True)
    plt.show()

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