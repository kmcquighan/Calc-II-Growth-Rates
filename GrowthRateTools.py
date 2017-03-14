"""
Created on Wed Mar  4 14:17:03 2015

A function for comparing the growth rates of various functions

@author: mcquighan
"""
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 20
from matplotlib.ticker import MaxNLocator

    
########## MAIN FUNCTION ##############
def compare_rates(show_log,show_power,show_log_power,show_power2,show_exp,show_factorial,show_power_exp,q,p,r,s,b,n_max):
    
    n = np.linspace(1,n_max,n_max)
    fig = plt.figure(figsize=(20, 10))
    ax = fig.gca()
    
    if show_log: 
        f1 = np.log(n)**q
        ax.plot(n,f1,'o',markersize='13',label=r'$log^q n$')
    if show_power: 
        f2 = n**p
        ax.plot(n,f2,'o',markersize='13',label=r'$n^p$')
    if show_log_power: 
        f3 = n**p*np.log(n)**r
        ax.plot(n,f3,'o',markersize='13',label=r'$n^plog^r n$')
    if show_power2: 
        f4 = n**(p+s)
        ax.plot(n,f4,'o',markersize='13',label=r'$n^{p+s}$')
    if show_exp:
        f5 = b**n
        ax.plot(n,f5,'o',markersize='13',label=r'$b^n$')
    if show_factorial:
        f6 = np.ones(n_max)
        for i in range(n_max-1):
            f6[i+1] = f6[i]*(i+1)
        ax.plot(n,f6,'o',markersize='13',label=r'$n!$')
    if show_power_exp: 
        f7 = n**n
        ax.plot(n,f7,'o',markersize='13',label=r'$n^n$')
    
    ax.set_xlabel('n')
    ax.set_ylabel(r'$a_n$')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.axhline(0.,color='k',linewidth='1')
    ax.axvline(0.,color='k',linewidth='1')
    ax.legend(loc=2)