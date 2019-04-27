import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg, signal

def normalize(x): return x/np.sqrt(np.sum(np.abs(x)**2))

def jakes_fading(
        NN_sym = 256, # number of symbols
        NN_sps = 256, # number of samples per symbol
        NN_pth = 256, # number of paths
        FF_dop =   1, # maximum doppler shift (Hz)
        FF_car =   0, # carrier frequency (Hz)
        FF_sym =   1  # symbol rate (baud)
):

    # global NN_sym, NN_sps, NN_pth
    # global FF_dop, FF_car, FF_sym
    global TT_sym, TT_sam, NN_sam, FF_sam
    global n, tt_n, xx_n
    global l, ps_l, xi_l, al_l

    # Scalars
    NN_sam = NN_sps * NN_sym
    TT_sym = 1/FF_sym      # symbol period (s)
    TT_sam = TT_sym/NN_sps # sample period (s)
    FF_sam = 1/TT_sam      # sample rate (Hz)

    # Sets
    n = np.arange(NN_sam) # samples
    l = np.arange(NN_pth) # paths
    
    # Fixed Variables
    tt_n  = n * TT_sam # sample time (s)
    tt_nl = np.meshgrid(tt_n,l)[0] # add path index

    # Path angle relative to receiver motion
    ps_l = (np.random.rand(l.size) - 0.5) * 2*np.pi #

    # Path Doppler shift
    xi_l  = FF_dop * np.sin(ps_l)                     #   path doppler shift
    xi_nl = np.meshgrid(n,xi_l)[1]

    # Complex Path amplitude
    al_l = normalize(np.random.randn(l.size) + 1j*np.random.randn(l.size))
    
    # Multipath Doppler shifted signal before fading
    xx_nl = np.exp(2j*np.pi*(FF_car + xi_nl)*tt_nl)

    # Multipath Rayleigh Fading
    xx_n =  np.dot(al_l,xx_nl)
