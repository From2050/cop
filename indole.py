import tkinter as tk
from tkinter import filedialog
import numpy as np
import mne
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import Slider

def main():

    #filepath = "./2022_04_27_16_48_41/2022_04_27_16_48_41_insoleL.txt"
    filepath = "./2022_05_17_16_20_00_insoleR.txt"

    def readfile(filepath):
        with open(filepath,'r') as f:
            
            Atemp = np.zeros(227+4,dtype=int)   # time(4)  + CA(1) + framenumber(1)  +data(8*28 = 224) + 0A (1) 
            Aframe = np.zeros(227+4,dtype=int)
            index = 0
            error = 0
            F_error = 0
            for line in f :
                temp = line.rstrip().split(',')
                for i in range(0,int(len(temp[1])),2):
                    if temp[1][i:i+2] == 'CA':
                        if F_error :    F_error = 0
                        else :          Aframe = np.vstack([Aframe, Atemp])
                        time = temp[0].split('.')
                        Atemp[0] = int(time[0][0:2])
                        Atemp[1] = int(time[0][3:5])
                        Atemp[2] = int(time[0][6:8])
                        Atemp[3] = int(time[1][0:2])
                        index = 0
                        
                    else :
                        if index == 227 :
                            index = 0
                            F_error = 1
                            error = error + 1 
                        Atemp[(4+index)] = int(temp[1][i:i+2],16)
                        index = index + 1
        return Aframe[2:,6:-1], Aframe[2:,0:4]




    Atemp, Atime = readfile(filepath)

    As = 60*60*100*Aframe[2:,0] + 60*100*Aframe[2:,1] + 100*Aframe[2:,2] + Aframe[2:,3] - (60*60*100*Aframe[2,0] + 60*100*Aframe[2,1] + 100*Aframe[2,2] + Aframe[2,3]) 
    frame_num_max = Atemp.shape[0]
    Atest = Atemp.reshape((frame_num_max,28,8))
    #temp_sum = 0
    Fswing =0
    pre = Atime[0,0]
    Lsum = []
    Ltemp = [0]*10

    gate = 20
    PF_swap = 0
    PF_swing = 0
    F_swap = 0
    F_swing = 0
    LF_swap = []
    LF_swing = [] 
    L_indole = []
    for i in range(0,frame_num_max):
        F_swap = int((Atest[i,14:,0:].sum() > 50))
        F_swing = int((Atest[i,0:14,0:].sum() < 10))
        Fswing = 0
        if (F_swing - PF_swing) == 1: Fswing =1
        if (F_swap - PF_swap) == 1: Fswing =2
        #if (Atest[i,0:,0:].sum() > gate) :Fswing = 0
        #else                             :Fswing = 1


        if  (Atime[i,0] != pre) or (i ==frame_num_max) : 
            if (Atime[i,0]/10).astype(int) - pre == 2:
                Lsum = Lsum + Ltemp
                Ltemp = [0]*10
                Lsum = Lsum + Ltemp
            else : Lsum = Lsum + Ltemp
            Ltemp = [0]*10
            pass
        if Ltemp[(Atime[i,1]/10).astype(int)] == 0 :Ltemp[(Atime[i,1]/10).astype(int)] = Fswing
        else : buff = Fswing
        if Atime[i,0] == 25 :print('25 '+str(i)+" " +str(Fswing)+" "+ str(Ltemp))
        if Atime[i,0] == 26 :print('26 '+str(i)+" " +str(Fswing)+" "+ str(Ltemp))
        if Atime[i,0] == 27 :print('27 '+str(i)+" " +str(Fswing)+" "+ str(Ltemp))
        if Atime[i,0] == 28 :print('28 '+str(i)+" " +str(Fswing)+" "+ str(Ltemp))
        if Atime[i,0] == 29 :print('29 '+str(i)+" " +str(Fswing)+" "+ str(Ltemp))
        LF_swap.append(F_swap)
        LF_swing.append(F_swing)
        L_indole.append(Fswing)
        #if Atime[i] == pre :            
        #    #temp_sum = temp_sum + Aframe[i,6:-1].sum()
        #    if Atemp[i,0:].sum() < 20 : 
        #        Fswing =1
                
        #else :
        #    Lsum.append(Fswing)
        #    #Fswing = 0
        #    #temp_sum = 0
        pre = Atime[i,0]
        PF_swap = F_swap
        PF_swing = F_swing
        #print(i,Atest[i,24:,0:].sum(),Atest[i,0:6,0:].sum(),Fswing)

    print(Lsum)
    pad = 0
    #for i in range(0,len(Lsum)):
    #    if Lsum[i] == None : Lsum[i] = pad
    #    else : pad = Lsum[i]
    #pad = Lsum[i]
    print(Lsum)


    #Atest = Atemp.reshape((frame_num_max,28,8))
    #sns.heatmap(data=Atest[0],square=True)
    #plt.show()



    fig, ax = plt.subplots(2,2)

    plt.subplots_adjust(bottom=0.25)
    
    #t = np.arange(0.0, 100.0, 0.1)
    #s = np.sin(2*np.pi*t)
    #l, = plt.plot(t,s)
    #plt.axis([0, 10, -1, 1])
    sns.heatmap(ax = ax[0][0],data=Atest[0],square=True,cbar = 0,annot=True)
    ax[0][0].set_title(str(Atime[0,0]) + str(Lsum[ (Atime[0,1]/10).astype(int)]))
    ax[0][1].set_title(str(Atime[0,0]) +"  " + str(L_indole[0]))
    #ax[1][0] = fig.add_axes([0, 0, 1, 1])
    ax[1][0].plot(LF_swap)
    ax[1][1].plot(Lsum)
    #sns.heatmap(ax = ax,data=Atest[3],square=True)
    axcolor = 'lightgoldenrodyellow'
    axpos = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)

    spos = Slider(axpos, 'Pos', 0, frame_num_max-1, valstep = 1)
    
    def update(val):
        pos = spos.val
        #print(pos)
        #print(ax)
        #ax.axis([pos,pos+10,-1,1])
        ax[0][0].clear()

        sns.heatmap(ax = ax[0][0],data=Atest[pos],square=True,cbar = 0,annot=True)
        ax[0][0].set_title(str(Atime[pos,0]) +"."+ str(Atime[pos,1]) +"s " + str(Lsum[(Atime[pos,0]*10).astype(int) + (Atime[0,1]/10).astype(int)])+"  F"+str (pos) + " "+ str(L_indole[pos]))
        #ax[0][1].set_title(str(Atime[pos,1]) +"  " + str(L_indole[pos]))
        #ax[1][1].axis([(Atime[0,1]/10).astype(int)]) - 10,(Atime[0,1]/10).astype(int)])+10,0,2])
        fig.canvas.draw_idle()
    
    spos.on_changed(update)
    
    plt.show()

    np.savetxt("2022_05_17_16_20_00_insoleR.csv", Lsum, delimiter =",",fmt ='% s')

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

    fig, ax = plt.subplots(1,6)

    plt.subplots_adjust(bottom=0.25)
    start_frame = 148
    #pos = start_frame + i + j
    for i in range(0,6) :
        #for j in range(0,4):
            pos = start_frame + i
            print(pos)
            sns.heatmap(ax = ax[i],data=Atest[pos],square=True,cbar = 0,annot=True)
            ax[i].set_title( "F" + str(pos) + " " + str(Atime[pos,0]) +"."+ str(Atime[pos,1])+"s  " + str(L_indole[pos]) )
    
    plt.show()

    #Atime = Atime[np.where(Adata == "CA")]      # getting time tag by finding index of CA  
    
    




    ##aa








if __name__ == '__main__':
    main()