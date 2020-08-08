import numpy as np
from matplotlib import pyplot as plt

def plot_CumEmi(interpolatedyearSSP, cumulco2Emi_org, cumulco2Emi):
    cumu_2020_2100_org = np.array(cumulco2Emi_org[4,10:])   - cumulco2Emi_org[4,9]
    cumu_2020_2100     = np.array(cumulco2Emi[:,1,4,10:].T) - cumulco2Emi[:,1,4,9]
    plt.plot(interpolatedyearSSP[10:],  cumu_2020_2100_org,     c="black",      alpha=1,     label="co2Cum_SSP540")
    plt.plot(interpolatedyearSSP[10:],  cumu_2020_2100[:,0],    c="salmon",     alpha=1,     label="0")
    plt.plot(interpolatedyearSSP[10:],  cumu_2020_2100[:,1],    c="orange",     alpha=1,     label="05")
    plt.plot(interpolatedyearSSP[10:],  cumu_2020_2100[:,2],    c="red",        alpha=1,     label="1")
    plt.plot(interpolatedyearSSP[10:],  cumu_2020_2100[:,3],    c="yellowgreen",alpha=1,     label="2")
    plt.plot(interpolatedyearSSP[10:],  cumu_2020_2100[:,4],    c="limegreen",  alpha=1,     label="4")
    plt.plot(interpolatedyearSSP[10:],  np.ones(len(interpolatedyearSSP[10:]))*1000*3.667,alpha=.5,  c="royalblue", linestyle='--')
    plt.fill_between(interpolatedyearSSP[10:], np.ones(len(interpolatedyearSSP[10:]))*930*3.667, np.ones(len(interpolatedyearSSP[10:]))*1070*3.667, facecolor='royalblue', alpha=0.3)
    plt.ylim(0,10000)
    plt.xlabel("yr")
    plt.ylabel("co2Emi")
    plt.legend(loc=2) 
    plt.show()
    # plt.savefig('co2Cum_SSP5gdp40.ps')
    plt.close()







