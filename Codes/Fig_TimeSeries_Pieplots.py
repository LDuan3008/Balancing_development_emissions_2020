import numpy as np
from matplotlib import pyplot as plt

def Fig_TimeSeries_Pieplots(interpolatedyearSSP, interpolatedpopSSPs, percapitagdpSSPs, annualco2Emi, annualco2Emi_org, cumulco2Emi_org, cumulco2Emi):
    
    err = 1
    ssp = 4
    
    plt.stackplot(interpolatedyearSSP[10:],
                  annualco2Emi[0,err,ssp,10:],
                  annualco2Emi[1,err,ssp,10:]-annualco2Emi[0,err,ssp,10:],
                  annualco2Emi[2,err,ssp,10:]-annualco2Emi[1,err,ssp,10:],
                  annualco2Emi[3,err,ssp,10:]-annualco2Emi[2,err,ssp,10:],
                  annualco2Emi[4,err,ssp,10:]-annualco2Emi[3,err,ssp,10:],
                  annualco2Emi_org[ssp,10:]  -annualco2Emi[4,err,ssp,10:])
    
    plt.plot(interpolatedyearSSP[10:],  annualco2Emi_org[ssp,10:],  c="black",   linewidth=1,    alpha=1)
    plt.plot(interpolatedyearSSP[10:],  annualco2Emi[0,err,ssp,10:],  c="black",   linewidth=1,    alpha=1)
    plt.plot(interpolatedyearSSP[10:],  annualco2Emi[1,err,ssp,10:],  c="black",   linewidth=1,    alpha=1)
    plt.plot(interpolatedyearSSP[10:],  annualco2Emi[2,err,ssp,10:],  c="black",   linewidth=1,    alpha=1)
    plt.plot(interpolatedyearSSP[10:],  annualco2Emi[3,err,ssp,10:],  c="black",   linewidth=1,    alpha=1)
    plt.plot(interpolatedyearSSP[10:],  annualco2Emi[4,err,ssp,10:],  c="black",   linewidth=1,    alpha=1)
    plt.ylim(0,180)
    plt.xlim(2020,2100)
    plt.xlabel("yr")
    plt.ylabel("co2Emi")
    plt.legend(loc=2) 
    #plt.show()
    plt.savefig('err_2_ssp_4.ps',dpi=300,bbox_inches='tight',transparent=True)
    plt.close()
    
    select_case_NOC = cumulco2Emi_org[ssp,-1] - cumulco2Emi_org[ssp,9]
    select_case_00  = cumulco2Emi[0,err,ssp,-1] - cumulco2Emi[0,err,ssp,9]
    select_case_10  = cumulco2Emi[1,err,ssp,-1] - cumulco2Emi[1,err,ssp,9]
    select_case_20  = cumulco2Emi[2,err,ssp,-1] - cumulco2Emi[2,err,ssp,9]
    select_case_40  = cumulco2Emi[3,err,ssp,-1] - cumulco2Emi[3,err,ssp,9]
    select_case_80  = cumulco2Emi[4,err,ssp,-1] - cumulco2Emi[4,err,ssp,9]
    
    per_80 = select_case_NOC -select_case_80
    per_40 = select_case_80  -select_case_40
    per_20 = select_case_40  -select_case_20
    per_10 = select_case_20  -select_case_10
    per_00 = select_case_10  -select_case_00
    per_no = select_case_00
    
    pie = [per_00, per_10, per_20, per_40, per_80, per_no]
    explode = (0, 0, 0, 0, 0, 0)
    plt.pie(pie, explode=explode, shadow=False, startangle=90, autopct='%1.3f%%', counterclock=False)
    #plt.show()
    plt.savefig('err_2_ssp_4_pie.ps')
    plt.clf()
    
    
    pop_ssp5_2020 = interpolatedpopSSPs[ssp, :, 10]
    percapgdp = percapitagdpSSPs[ssp, :, 10]
    category = np.zeros(5)
    for i in range(177):
        if percapgdp[i] <= 10:
            category[0] = category[0] + pop_ssp5_2020[i]
        elif percapgdp[i]>10 and percapgdp[i]<=20:
            category[1] = category[1] + pop_ssp5_2020[i]
        elif percapgdp[i]>20 and percapgdp[i]<=40:
            category[2] = category[2] + pop_ssp5_2020[i]
        elif percapgdp[i]>40 and percapgdp[i]<=80:
            category[3] = category[3] + pop_ssp5_2020[i]
        elif percapgdp[i]>80:
            category[4] = category[4] + pop_ssp5_2020[i]
            
    percentage = category / np.sum(pop_ssp5_2020) * 100
    explode = (0, 0, 0, 0, 0)
    plt.pie(percentage, explode=explode, shadow=False, startangle=90, autopct='%1.4f%%', counterclock=False)
    #plt.show()
    plt.savefig('pie_pop_SSPX.ps')
    plt.clf()