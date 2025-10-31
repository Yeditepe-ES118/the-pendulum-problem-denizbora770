import numpy as np

def find_period (L0, L1):
    if (L0 < 0) or (L0 == 0):
        print ("Please enter a value bigger than 0.")
    elif (L1 < 0) or (L1 == 0):
        print ("Please enter a value bigger than 0.")
    elif (L0 > L1):
        print ("Please enter a value for L1 that is greater than the value of L0.")
    elif L1 > L0 > 0:
        for L in range (L0,L1+1,1): # L is in meters
            g = 9.81 # in m/s^2 
            T = 2 * np.pi * np.sqrt(L/g) # in 
            print ("When L = %4.1f m, T = %3.1f s" % (L,T))
    return (L0, L1)

find_period(2, 10)