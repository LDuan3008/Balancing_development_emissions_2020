import numpy as np
import cdutil
from matplotlib import pyplot as plt


def get_histCtry0610(var1, countryList):
    tmp1 = np.zeros(2)         
    for i in range(264):       # total country number
        i = i+5
        if var1[i][1] in countryList:
            tmp_x = var1[i][1]
            tmp_y = var1[i][58]             #14->169, 13->170, 10->172
            tmp_z = [tmp_x,tmp_y]
            tmp1 = np.c_[tmp1, tmp_z]
    tmp2 = tmp1[:,1:].T
    return tmp2

def plot_PerCapGDP_PerCapEmi(co2_WB, gdp_WB, pop_WB, countryList):
    histCO2_tmp = get_histCtry0610(co2_WB, countryList)
    histGDP_tmp = get_histCtry0610(gdp_WB, countryList)           #(177, 2)
    histPop_tmp = get_histCtry0610(pop_WB, countryList)
    
    #print (histGDP_tmp)
    
    gdp2014 = np.zeros(177)
    pop2014 = np.zeros(177)
    co22014 = np.zeros(177)
    percapitagdp_2014 = np.zeros(177)
    percapitaco2_2014 = np.zeros(177)
    ci_2014 = np.zeros(177)
    for i in range(177):
        if len(histGDP_tmp[i,1]) != 0 and len(histPop_tmp[i,1]) != 0 and len(histCO2_tmp[i,1]) != 0:
            pop2014[i] = histPop_tmp[i][1].astype(np.float) * (10**-9)
            gdp2014[i] = histGDP_tmp[i][1].astype(np.float) * (10**-12)
            co22014[i] = histCO2_tmp[i][1].astype(np.float) * (10**-6)
            percapitagdp_2014[i] = gdp2014[i] / pop2014[i]
            percapitaco2_2014[i] = co22014[i] / pop2014[i]
            ci_2014[i] = co22014[i] / gdp2014[i]
    
    percapitagdp_copy = np.copy(percapitagdp_2014)
    index = np.arange(177)
    length = len(percapitagdp_copy)   #177
    totco22014 = cdutil.averager(co22014,axis=0,weights='equal',action='sum')
    totgdp2014 = cdutil.averager(gdp2014,axis=0,weights='equal',action='sum')
    totpop2014 = cdutil.averager(pop2014,axis=0,weights='equal',action='sum')

    # order from small to large
    for i in range(1, length, 1):
        j = i - 1
        key = percapitagdp_copy[i]
        key_tmp = index[i]
        while (j >= 0 and percapitagdp_copy[j] > key):
            percapitagdp_copy[j+1] = percapitagdp_copy[j]
            index[j+1] = index[j]
            j = j - 1  
        percapitagdp_copy[j + 1] = key   
        index[j+1] = key_tmp

    width   = pop2014[index] * 10
    co2rank = co22014[index]/totco22014*100
    gdprank = gdp2014[index]/totgdp2014*100
    poprank = pop2014[index]/totpop2014*100
    co2cumu = np.zeros(177)
    gdpcumu = np.zeros(177)
    popcumu = np.zeros(177)
    for i in range(177):
        co2cumu[i] = cdutil.averager(co2rank[:i+1],axis=0,weights='equal',action='sum')
        gdpcumu[i] = cdutil.averager(gdprank[:i+1],axis=0,weights='equal',action='sum')
        popcumu[i] = cdutil.averager(poprank[:i+1],axis=0,weights='equal',action='sum')
    
    # idx = 116
    # print (percapitagdp_copy[idx])
    # print (popcumu[idx])
    # print (co2cumu[idx])
    # stop
    
    popindex = np.zeros(9)
    for i in range(177):
        if popcumu[i] > 10 and popcumu[i-1]<10:
            popindex[0] = i
        if popcumu[i] > 20 and popcumu[i-1]<20:
            popindex[1] = i      
        if popcumu[i] > 30 and popcumu[i-1]<30:
            popindex[2] = i         
        if popcumu[i] > 40 and popcumu[i-1]<40:
            popindex[3] = i         
        if popcumu[i] > 50 and popcumu[i-1]<50:
            popindex[4] = i         
        if popcumu[i] > 60 and popcumu[i-1]<60:
            popindex[5] = i         
        if popcumu[i] > 70 and popcumu[i-1]<70:
            popindex[6] = i         
        if popcumu[i] > 80 and popcumu[i-1]<80:
            popindex[7] = i         
        if popcumu[i] > 90 and popcumu[i-1]<90:
            popindex[8] = i 

    space = 0.2
    x = np.zeros(177)
    x2 = np.zeros(177)
    for i in range(177):
        if i ==0:
            x[i] = 0.5*width[0] + 0.5
            x2[i] = width[0] + 0.5
        else:
            x[i] = 0.5*width[i] + i*space + 0.5 + cdutil.averager(width[:i],axis=0,weights='equal',action='sum')
            x2[i] = width[i] + i*space + 0.5 + cdutil.averager(width[:i],axis=0,weights='equal',action='sum')

    a = (len( percapitagdp_2014[percapitagdp_2014<=10] ))
    b = (len( percapitagdp_2014[(percapitagdp_2014>10)&(percapitagdp_2014<=20)] ))
    c = (len( percapitagdp_2014[(percapitagdp_2014>20)&(percapitagdp_2014<=40)] ))
    d = (len( percapitagdp_2014[(percapitagdp_2014>40)&(percapitagdp_2014<=80)] ))
    e = (len( percapitagdp_2014[(percapitagdp_2014>80)] ))
    
    color_list = a*['black'] + b*['red'] + c*['blue'] + d*['orange'] + e*['green']

    #fig.subplots_adjust(top=1, left=0.0, right=1, hspace=1.0, wspace=0.35)
    ax1 = plt.subplot2grid((1,1),(0,0),rowspan=1, colspan=1)
    ax1v = ax1.twinx()
    ax1.plot(x, np.zeros(len(x))+10, color='grey', linestyle='--', linewidth='0.5')
    ax1.plot(x, np.zeros(len(x))+20, color='grey', linestyle='--', linewidth='0.5')
    ax1.plot(x, np.zeros(len(x))+40, color='grey', linestyle='--', linewidth='0.5')
    ax1.plot(x, np.zeros(len(x))+80, color='grey', linestyle='--', linewidth='0.5')
    ax1.bar(x, np.array(percapitagdp_2014[index]), width, color=color_list, edgecolor='black',linewidth=0.0)
    ax1v.plot(x2, np.array(gdpcumu), c='green')
    plt.scatter(x2[popindex.astype(int)], np.zeros(9)+100, c='black', marker = '+')
    plt.xlim(0, x[-1]+width[-1]*0.5+0.5)
    ax1.set_ylim(0,100)
    ax1v.set_ylim(0,100)
    plt.show()
    # plt.savefig('fig1_panel1.ps',dpi=300)
    plt.close()

    ax1 = plt.subplot2grid((1,1),(0,0),rowspan=1, colspan=1)
    ax1v = ax1.twinx()
    ax1.bar(x, np.array(percapitaco2_2014[index]), width, color=color_list, edgecolor='black',linewidth=0.0)
    ax1v.plot(x2, np.array(co2cumu), c='red')
    plt.xlim(0, x[-1]+width[-1]*0.5+0.5)
    ax1.set_ylim(0,35)
    ax1v.set_ylim(0, 100)
    plt.show()
    # plt.savefig('fig1_panel2.ps',dpi=300)
    plt.close()
