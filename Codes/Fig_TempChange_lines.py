import numpy as np
from matplotlib import pyplot as plt
import cdms2 as cdms, MV2 as MV

def find_pop_in_shreshold(shreshold_list, interpolatedpopSSPs, interpolatedyearSSP, percapitagdpSSPs):
    year = interpolatedyearSSP[10]
    print (year)
    pop_ssp5_2020 = interpolatedpopSSPs[4, :, 10]
    pcg_ssp5_2020 = percapitagdpSSPs[4, :, 10]
    pop_total  = np.zeros(len(shreshold_list)+1)  #82
    pop_total2 = np.zeros(len(shreshold_list)+1)  #82
    for i in range(177):
        if pcg_ssp5_2020[i] == 0.:
            idx = 0.
        else:
            idx = int(pcg_ssp5_2020[i])+1  
        if idx >= len(shreshold_list):
            idx = len(shreshold_list)
        pop_total[idx] = pop_total[idx] + pop_ssp5_2020[i]
    for i in range(len(shreshold_list)+1):
        pop_total2[i] = np.sum(pop_total[:i+1])/np.sum(pop_total)
    return pop_total2
    

def Fig_TempChange_lines(shreshold_list, cumulco2Emi, cumulco2Emi_org, interpolatedpopSSPs, interpolatedyearSSP, percapitagdpSSPs):
    cumulco2Emi     = cumulco2Emi[:,:,4,-1] - cumulco2Emi[:,:,4,1] + 515*3.667
    cumulco2Emi_org = cumulco2Emi_org[4,-1] - cumulco2Emi_org[4,1] + 515*3.667
    xaxis = np.array(shreshold_list)
    yaxis = np.array(cumulco2Emi * 2. / 3667.  )  # note here is the total warming fro pre-industrial [shreshold, ramprate]
    new_xaxis = find_pop_in_shreshold(shreshold_list, interpolatedpopSSPs, interpolatedyearSSP, percapitagdpSSPs)
    ax1 = plt.subplot2grid((1,1),(0,0),rowspan=1, colspan=1)
    ax1v = ax1.twiny()
    ax1.plot(new_xaxis[:-1], yaxis[:,0] - yaxis[0,0])
    ax1.plot(new_xaxis[:-1], yaxis[:,1] - yaxis[0,1])
    ax1.plot(new_xaxis[:-1], yaxis[:,2] - yaxis[0,2])
    ax1.plot(new_xaxis[:-1], yaxis[:,3] - yaxis[0,3])
    ax1.plot(new_xaxis[:-1], yaxis[:,4] - yaxis[0,4])
    ax1.plot(np.ones(6)*new_xaxis[10], np.r_[ yaxis[10,:]-yaxis[0,:], 0], linestyle='--', color='black')
    ax1.plot(np.ones(6)*new_xaxis[20], np.r_[ yaxis[20,:]-yaxis[0,:], 0], linestyle='--', color='black')
    ax1.plot(np.ones(6)*new_xaxis[40], np.r_[ yaxis[40,:]-yaxis[0,:], 0], linestyle='--', color='black')
    ax1v.plot(new_xaxis[:-1], np.ones(82)*3)
    ax1.set_xlim(0,1)
    ax1v.set_xlim(0,1)
    plt.ylim(0, 3)
    # plt.show()
    plt.savefig('figs3.ps')
    plt.clf()
    

def plot_contour_plot(shreshold_list, ramprate_list, cumulco2Emi):
    print (cumulco2Emi.shape)
    
    axis_shreshold = cdms.createAxis(shreshold_list)
    axis_ramprate  = cdms.createAxis(ramprate_list)
    len1 = len(shreshold_list)
    len2 = len(ramprate_list)
    
    tmp1 = np.zeros([len2,len1])
    sf = 2.0/3667.   # Here we use the relationship that per 1000 GtC carbon emission would produce 2C warming
    
    for i in range(len1):
        for j in range(len2):
            cumulco2Emi2 = cumulco2Emi[i,j,4,-1] - cumulco2Emi[i,j,4,1] + 515*3.667
            tmp1[j,i] = cumulco2Emi2 * sf     
    shre_ramp_cuml1 = MV.array(tmp1); shre_ramp_cuml1.setAxis(1,axis_shreshold); shre_ramp_cuml1.setAxis(0,axis_ramprate)
    
    x, y = np.meshgrid(axis_shreshold, axis_ramprate)
    ax = plt.subplot(111)
    mp = ax.pcolormesh(shreshold_list, ramprate_list, shre_ramp_cuml1, cmap='RdYlGn_r')
    lp = ax.contour(x, y, shre_ramp_cuml1, levels=[1,2,3,4,5,6], colors='black', linestyles='dashed', linewidths=1)
    
    plt.colorbar(mp, ax=ax, extend='max')
    plt.savefig('test3.ps')
    # plt.show()
    plt.clf()