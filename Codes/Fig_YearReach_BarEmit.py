import numpy as np
from matplotlib import pyplot as plt

Hincome_list = ["ABW", "AND", "ARE", "ATG", "AUS", "AUT", "BEL", "BHR", "BHS",
                "BMU", "BRB", "BRN", "CAN", "CHE", "CHI", "CHL", "CUW", "CYM",
                "CYP", "CZE", "DEU", "DNK", "ESP", "EST", "FIN", "FRA", "FRO",
                "GBR", "GIB", "GRC", "GRL", "GUM", "HKG", "HRV", "HUN", "IMN",
                "IRL", "ISL", "ISR", "ITA", "JPN", "KNA", "KOR", "KWT", "LIE",
                "LTU", "LUX", "LVA", "MAC", "MAF", "MCO", "MLT", "MNP", "NCL",
                "NLD", "NOR", "NZL", "OMN", "PAN", "PLW", "POL", "PRI", "PRT",
                "PYF", "QAT", "SAU", "SGP", "SMR", "SVK", "SVN", "SWE", "SXM",
                "SYC", "TCA", "TTO", "TWN", "URY", "USA", "VGB", "VIR"]
Mincome_list = ["ALB", "ARG", "ARM", "ASM", "AZE", "BGR", "BIH", "BLR", "BLZ", "BRA",
                "BWA", "CHN", "COL", "CRI", "CUB", "DMA", "DOM", "DZA", "ECU", "FJI",
                "GAB", "GEO", "GNQ", "GRD", "GTM", "GUY", "IRN", "IRQ", "JAM", "JOR",
                "KAZ", "LBN", "LBY", "LCA", "LKA", "MDV", "MEX", "MHL", "MKD", "MNE",
                "MUS", "MYS", "NAM", "NRU", "PER", "PRY", "ROU", "RUS", "SRB", "SUR",
                "THA", "TKM", "TON", "TUR", "TUV", "VCT", "VEN", "WSM", "XKX", "ZAF"]
Lincome_list = ["AFG", "BDI", "BEN", "BFA", "CAF", "COD", "ERI", "ETH", "GIN",
                "GMB", "GNB", "HTI", "LBR", "MDG", "MLI", "MOZ", "MWI", "NER", 
                "NPL", "PRK", "RWA", "SLE", "SOM", "SSD", "SYR", "TCD", "TGO",
                "TJK", "TZA", "UGA", "YEM", "AGO", "BGD", "BOL", "BTN", "CIV",
                "CMR", "COG", "COM", "CPV", "DJI", "EGY", "FSM", "GHA", "HND",
                "IDN", "IND", "KEN", "KGZ", "KHM", "KIR", "LAO", "LSO", "MAR",
                "MDA", "MMR", "MNG", "MRT", "NGA", "NIC", "PAK", "PHL", "PNG",
                "PSE", "SDN", "SEN", "SLB", "SLV", "STP", "SWZ", "TLS", "TUN",
                "UKR", "UZB", "VNM", "VUT", "ZMB", "ZWE"]

def get_2018_pcgdp(pop, gdp, category, countryList, idx):
    flag = 0
    for i in range(264):               # total row numbers
        i = i+5
        if pop[i][1] in countryList and pop[i][1] in category:
            name_cty = pop[i][1]
            pop_cty  = pop[i][idx]
            try:
                convert_pop = float(pop_cty) * (10**-9)
                pcgdp = convert_pop
            except:
                pcgdp = 0.
            if pop[i][1] == "CHN" or pop[i][1] == "ARG":
                print (pop[i][1], pcgdp)
            if flag == 0:
                name_array = [name_cty]
                data_array = [pcgdp]
                flag = 1
            else:
                name_array.append(name_cty)
                data_array.append(pcgdp)
    return np.array(name_array), np.array(data_array)


def new_CTYemissions(original_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_ctyLevel):
    print (original_CumCO2Emit_ctyLevel.shape)
    print (adjuated_CumCO2Emit_ctyLevel.shape)

    idx = [167, 137, 72, 42, 30, 73, 82, 103, 117, 55, 21, 124]
    idx = [124]

    for i in idx:
        plt.plot(np.arange(91)+2010, np.array(original_CumCO2Emit_ctyLevel[4, i, :]), color='black')
        plt.plot(np.arange(91)+2010, np.array(adjuated_CumCO2Emit_ctyLevel[4, 1, 4, i, :]), color='blue')
        plt.plot(np.arange(91)+2010, np.array(adjuated_CumCO2Emit_ctyLevel[3, 1, 4, i, :]), color='green')
        plt.plot(np.arange(91)+2010, np.array(adjuated_CumCO2Emit_ctyLevel[2, 1, 4, i, :]), color='orange')
        plt.plot(np.arange(91)+2010, np.array(adjuated_CumCO2Emit_ctyLevel[1, 1, 4, i, :]), color='purple')
        plt.plot(np.arange(91)+2010, np.array(adjuated_CumCO2Emit_ctyLevel[0, 1, 4, i, :]), color='firebrick')
    plt.xlim(2020, 2100)
    # plt.ylim(0, 30)
    # plt.yscale('log', basey=10)
    plt.savefig('testtest124.ps')
    # plt.show()
    plt.clf()
    stop







def Fig_YearReachThreshold(percapitagdpSSPs, shreshold_list, interpolatedyearSSP, pop_WB, gdp_WB, countryList):
    # calculate time reaching gdp thresholds
    case_num = len(shreshold_list)
    output_array = np.zeros([case_num, 5, 177]) + 2100
    for case_idx in range(case_num):
        for ssp_idx in range(5):
            for cty_idx in range(177):
                for time_idx in range(91):
                    if percapitagdpSSPs[ssp_idx,cty_idx,time_idx] >= shreshold_list[case_idx] and interpolatedyearSSP[time_idx]>=2020:
                        output_array[case_idx, ssp_idx, cty_idx] = interpolatedyearSSP[time_idx]
                        break

    """
    # select countries based on emissions
    num = 4
    nameL, pcgdpL = get_2018_pcgdp(pop_WB, gdp_WB, Lincome_list, countryList, -2)
    nameM, pcgdpM = get_2018_pcgdp(pop_WB, gdp_WB, Mincome_list, countryList, -2)
    nameH, pcgdpH = get_2018_pcgdp(pop_WB, gdp_WB, Hincome_list, countryList, -2)
    max_idxL = np.argpartition(pcgdpL, -num)[-num:]
    max_idxM = np.argpartition(pcgdpM, -num)[-num:]
    max_idxH = np.argpartition(pcgdpH, -num)[-num:]
    selected_ctyL = []
    selected_ctyM = []
    selected_ctyH = []
    for i in range(num):
        selected_ctyL.append(nameL[max_idxL[i]])
        selected_ctyM.append(nameM[max_idxM[i]])
        selected_ctyH.append(nameH[max_idxH[i]])
    print (selected_ctyL)
    print (selected_ctyM)
    print (selected_ctyH)
    stop
    #"""
    
    EU_list = ['GBR', 'FRA', 'DEU', 'ITA', 'NLD', 'BEL', 'LUX', 'DNK', 'IRL', 
               'GRC', 'PRT', 'ESP', 'AUT', 'SWE', 'FIN', 'MLT', 'CYP', 'POL', 
               'HUN', 'CZE', 'SVK', 'SVN', 'EST', 'LVA', 'LTU', 'ROU', 'BGR']
    ssp5EU = np.zeros([27, case_num, 5])
    ssp5EU_2 = np.zeros([27, 91])
    for idx in range(27):
        EUidx = int(np.argwhere(countryList == EU_list[idx] ))
        ssp5EU[idx, :, :] = output_array[:, :, EUidx]
        ssp5EU_2[idx] = percapitagdpSSPs[4, EUidx]
    EU_avg = np.mean(ssp5EU, axis=0)
    EU_avg_2 = np.mean(ssp5EU_2, axis=0)
    
    num = 4
    selected_ctyH = ['USA', 'DEU', 'JPN', 'FRA'] #'GBR', 
    selected_ctyM = ['RUS', 'CHN', 'MEX', 'BRA'] #'TUR', 
    selected_ctyL = ['IDN', 'IND', 'NGA', 'PAK'] #'BGD', 
    
    ssp5H = np.zeros([num, case_num, 5])
    ssp5M = np.zeros([num, case_num, 5])
    ssp5L = np.zeros([num, case_num, 5])
    idx = []
    for i in range(num):
        Hidx = int(np.argwhere(countryList == selected_ctyH[i] ))
        ssp5H[i] = output_array[:, :, Hidx]
        Midx = int(np.argwhere(countryList == selected_ctyM[i] ))
        ssp5M[i] = output_array[:, :, Midx]
        Lidx = int(np.argwhere(countryList == selected_ctyL[i] ))
        ssp5L[i] = output_array[:, :, Lidx]
        idx.append(Hidx); idx.append(Midx); idx.append(Lidx)

    for i in idx:
        plt.plot(np.arange(91)+2010, np.array(percapitagdpSSPs[4, i, :]), color='black')
    # plt.plot(np.arange(91)+2010, np.array(EU_avg_2), color='black')
    plt.plot(np.arange(91)+2010, np.zeros(91)+10, color='firebrick')
    plt.plot(np.arange(91)+2010, np.zeros(91)+20, color='firebrick')
    plt.plot(np.arange(91)+2010, np.zeros(91)+40, color='firebrick')
    plt.plot(np.arange(91)+2010, np.zeros(91)+80, color='firebrick')
    plt.xlim(2020, 2100)
    # plt.ylim(2**2, 200)
    plt.ylim(5, 160)
    plt.yscale('log', basey=10)
    plt.savefig('test_log2_2.ps')
    # plt.show()
    plt.clf()
    stop



    #ssp5 = np.r_[ssp5H, ssp5M, ssp5L]
    ssp5 = np.array(np.r_[ssp5H, ssp5M, ssp5L, EU_avg[None,:,:]])
    print (ssp5.shape)
    plt.barh(np.arange(num*3+1)+1, ssp5[:, 0, 4]-2020,          0.5, color='firebrick',                            alpha=1)
    plt.barh(np.arange(num*3+1)+1, ssp5[:, 1, 4]-ssp5[:, 0, 4], 0.5, color='orange',     left=ssp5[:, 0, 4]-2020,  alpha=1)
    plt.barh(np.arange(num*3+1)+1, ssp5[:, 2, 4]-ssp5[:, 1, 4], 0.5, color='green',      left=ssp5[:, 1, 4]-2020,  alpha=1)
    plt.barh(np.arange(num*3+1)+1, ssp5[:, 3, 4]-ssp5[:, 2, 4], 0.5, color='gray',       left=ssp5[:, 2, 4]-2020,  alpha=1)
    plt.xlim(0,80)
    plt.xticks(np.arange(9)*10, ('2020', '2030', '2040', '2050', '2060', '2070', '2080', '2090', '2100'))
    plt.ylim(14,0)
    plt.yticks(np.arange(15), ('', 'USA', 'DEU', 'JPN', 'FRA', 'RUS', 'CHN', 'MEX', 'BRA', 'IDN', 'IND', 'NGA', 'PAK', 'EU', ''))
    plt.show()
    # plt.savefig('upper.ps')
    plt.clf()







    
    
    
###############################################################################################################################
    
def get_emis(cty_name, countryList, cumulco2Emi_org_select, cumulco2Emi_red_select):
    cty_arg = int(np.argwhere(countryList == cty_name ))
    emissions_org = cumulco2Emi_org_select[cty_arg]
    emissions_red = cumulco2Emi_red_select[:,:,cty_arg]
    return emissions_org, emissions_red
    
def plot_cty_CumEmit(original_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_ctyLevel, interpolatedpopSSPs, interpolatedgdpSSPs, percapitagdpSSPs, countryList):
    cumulco2Emi_org_select = original_CumCO2Emit_ctyLevel[4,:,-1]      - original_CumCO2Emit_ctyLevel[4,:,9]         #(177)  from 2020 to 2100    
    cumulco2Emi_red_select = adjuated_CumCO2Emit_ctyLevel[:,:,4,:,-1]  - adjuated_CumCO2Emit_ctyLevel[:,:,4,:,9]     #(len1,len2,177) from 2020 to 2100
    
    #"""
    ######## get EU data ############################
    EU_list = ['GBR', 'FRA', 'DEU', 'ITA', 'NLD', 'BEL', 'LUX', 'DNK', 'IRL', 
               'GRC', 'PRT', 'ESP', 'AUT', 'SWE', 'FIN', 'MLT', 'CYP', 'POL', 
               'HUN', 'CZE', 'SVK', 'SVN', 'EST', 'LVA', 'LTU', 'ROU', 'BGR']
    eu_emits_org = 0
    eu_emits_red = cumulco2Emi_red_select[:,:,0]*0.
    for eu_idx in range(27):
        arg_idx = int(np.argwhere(countryList == EU_list[eu_idx] ))
        eu_emits_org = eu_emits_org + cumulco2Emi_org_select[arg_idx]
        eu_emits_red = eu_emits_red + cumulco2Emi_red_select[:,:,arg_idx]
    #"""
    
    ######## get other data ############################
    #get_country_list = ['USA', 'FRA', 'DEU', 'JPN', 'RUS', 'CHN', 'MEX', 'BRA', 'IDN', 'IND', 'NGA', 'PAK']
    
    usa_emit_org, usa_emit_red = get_emis('USA', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    deu_emit_org, deu_emit_red = get_emis('DEU', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    jpn_emit_org, jpn_emit_red = get_emis('JPN', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    fra_emit_org, fra_emit_red = get_emis('FRA', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    rus_emit_org, rus_emit_red = get_emis('RUS', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    chn_emit_org, chn_emit_red = get_emis('CHN', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    mex_emit_org, mex_emit_red = get_emis('MEX', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    bra_emit_org, bra_emit_red = get_emis('BRA', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    idn_emit_org, idn_emit_red = get_emis('IDN', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    ind_emit_org, ind_emit_red = get_emis('IND', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    nga_emit_org, nga_emit_red = get_emis('NGA', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    pak_emit_org, pak_emit_red = get_emis('PAK', countryList, cumulco2Emi_org_select, cumulco2Emi_red_select)
    
    country_list_00 = np.array( [usa_emit_red[0,1], deu_emit_red[0,1], jpn_emit_red[0,1], fra_emit_red[0,1], rus_emit_red[0,1], chn_emit_red[0,1], mex_emit_red[0,1], bra_emit_red[0,1], idn_emit_red[0,1], ind_emit_red[0,1], nga_emit_red[0,1], pak_emit_red[0,1], eu_emits_red[0,1] ] )
    country_list_10 = np.array( [usa_emit_red[1,1], deu_emit_red[1,1], jpn_emit_red[1,1], fra_emit_red[1,1], rus_emit_red[1,1], chn_emit_red[1,1], mex_emit_red[1,1], bra_emit_red[1,1], idn_emit_red[1,1], ind_emit_red[1,1], nga_emit_red[1,1], pak_emit_red[1,1], eu_emits_red[1,1] ] )
    country_list_20 = np.array( [usa_emit_red[2,1], deu_emit_red[2,1], jpn_emit_red[2,1], fra_emit_red[2,1], rus_emit_red[2,1], chn_emit_red[2,1], mex_emit_red[2,1], bra_emit_red[2,1], idn_emit_red[2,1], ind_emit_red[2,1], nga_emit_red[2,1], pak_emit_red[2,1], eu_emits_red[2,1] ] )
    country_list_40 = np.array( [usa_emit_red[3,1], deu_emit_red[3,1], jpn_emit_red[3,1], fra_emit_red[3,1], rus_emit_red[3,1], chn_emit_red[3,1], mex_emit_red[3,1], bra_emit_red[3,1], idn_emit_red[3,1], ind_emit_red[3,1], nga_emit_red[3,1], pak_emit_red[3,1], eu_emits_red[3,1] ] )
    country_list_80 = np.array( [usa_emit_red[4,1], deu_emit_red[4,1], jpn_emit_red[4,1], fra_emit_red[4,1], rus_emit_red[4,1], chn_emit_red[4,1], mex_emit_red[4,1], bra_emit_red[4,1], idn_emit_red[4,1], ind_emit_red[4,1], nga_emit_red[4,1], pak_emit_red[4,1], eu_emits_red[4,1] ] )
    country_list_n0 = np.array( [usa_emit_org,      deu_emit_org,      jpn_emit_org,      fra_emit_org,      rus_emit_org,      chn_emit_org,      mex_emit_org,      bra_emit_org,      idn_emit_org,      ind_emit_org,      nga_emit_org,      pak_emit_org     , eu_emits_org      ] )
    
    print (country_list_00)
    print (country_list_10)
    print (country_list_20)
    print (country_list_40)
    print (country_list_80)
    print (country_list_n0)
    stop

    xaxis = np.arange(13)
    width = 0.5
    plt.bar(xaxis, country_list_00, width, color='grey')
    plt.bar(xaxis, country_list_10-country_list_00, width, bottom = country_list_00, color='firebrick')
    plt.bar(xaxis, country_list_20-country_list_10, width, bottom = country_list_10, color='saddlebrown')
    plt.bar(xaxis, country_list_40-country_list_20, width, bottom = country_list_20, color='chocolate')
    plt.bar(xaxis, country_list_80-country_list_40, width, bottom = country_list_40, color='burlywood')
    plt.bar(xaxis, country_list_n0-country_list_80, width, bottom = country_list_80, color='wheat')
    
    #plt.ylim(0,1600)
    plt.xticks(np.arange(13), ('USA', 'DEU', 'JPN', 'FRA', 'RUS', 'CHN', 'MEX', 'BRA', 'IDN', 'IND', 'NGA', 'PAK', 'EU'))
    plt.show()
    # plt.savefig('lower.ps')
    plt.clf()