import tkinter as tk
from tkinter import filedialog
import numpy as np
import mne
import matplotlib.pyplot as plt


def main():
    print('hellow')
    print('this is cop data plot')

    filepath = "C:/Users/Jay/Desktop/2022_04_27_16_48_41/2022_04_27_16_48_41_insoleL.txt"
    #with open(filepath,'r') as f:
    #    for line in lines
    Ain = np.loadtxt(filepath,dtype=str,delimiter=',')

    Atime, Adata = np.hsplit(Ain, [1])
    Adata = Adata.reshape(-1)                   #expand to line
    Atime = Atime[np.where(Adata == "CA")]      # getting time tag by finding index of CA  
    
    




    ##aa








if __name__ == '__main__':
    main()