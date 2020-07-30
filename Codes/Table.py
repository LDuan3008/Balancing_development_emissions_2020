import numpy as np
from matplotlib import pyplot as plt

Hincome_list = ["ABW", "AND", "ARE", "ATG", "AUS", "AUT", "BEL", "BHR", "BHS", "BMU", "BRB", "BRN", "CAN", "CHE", "CHI", "CHL", "CUW", "CYM",
                "CYP", "CZE", "DEU", "DNK", "ESP", "EST", "FIN", "FRA", "FRO", "GBR", "GIB", "GRC", "GRL", "GUM", "HKG", "HRV", "HUN", "IMN",
                "IRL", "ISL", "ISR", "ITA", "JPN", "KNA", "KOR", "KWT", "LIE", "LTU", "LUX", "LVA", "MAC", "MAF", "MCO", "MLT", "MNP", "NCL",
                "NLD", "NOR", "NZL", "OMN", "PAN", "PLW", "POL", "PRI", "PRT", "PYF", "QAT", "SAU", "SGP", "SMR", "SVK", "SVN", "SWE", "SXM",
                "SYC", "TCA", "TTO", "TWN", "URY", "USA", "VGB", "VIR"]
Mincome_list = ["ALB", "ARG", "ARM", "ASM", "AZE", "BGR", "BIH", "BLR", "BLZ", "BRA", "BWA", "CHN", "COL", "CRI", "CUB", "DMA", "DOM", "DZA", "ECU", "FJI",
                "GAB", "GEO", "GNQ", "GRD", "GTM", "GUY", "IRN", "IRQ", "JAM", "JOR", "KAZ", "LBN", "LBY", "LCA", "LKA", "MDV", "MEX", "MHL", "MKD", "MNE",
                "MUS", "MYS", "NAM", "NRU", "PER", "PRY", "ROU", "RUS", "SRB", "SUR", "THA", "TKM", "TON", "TUR", "TUV", "VCT", "VEN", "WSM", "XKX", "ZAF"]
Lincome_list = ["AFG", "BDI", "BEN", "BFA", "CAF", "COD", "ERI", "ETH", "GIN", "GMB", "GNB", "HTI", "LBR", "MDG", "MLI", "MOZ", "MWI", "NER", 
                "NPL", "PRK", "RWA", "SLE", "SOM", "SSD", "SYR", "TCD", "TGO", "TJK", "TZA", "UGA", "YEM", "AGO", "BGD", "BOL", "BTN", "CIV",
                "CMR", "COG", "COM", "CPV", "DJI", "EGY", "FSM", "GHA", "HND", "IDN", "IND", "KEN", "KGZ", "KHM", "KIR", "LAO", "LSO", "MAR",
                "MDA", "MMR", "MNG", "MRT", "NGA", "NIC", "PAK", "PHL", "PNG", "PSE", "SDN", "SEN", "SLB", "SLV", "STP", "SWZ", "TLS", "TUN",
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

def Fig_YearReachThreshold_Table(percapitagdpSSPs, shreshold_list, interpolatedyearSSP, pop_WB, gdp_WB, countryList):
    case_num = len(shreshold_list)
    output_array = np.zeros([case_num, 5, 177]) + 2100
    for case_idx in range(case_num):
        for ssp_idx in range(5):
            for cty_idx in range(177):
                for time_idx in range(91):
                    if percapitagdpSSPs[ssp_idx,cty_idx,time_idx] >= shreshold_list[case_idx] and interpolatedyearSSP[time_idx]>=2020:
                        output_array[case_idx, ssp_idx, cty_idx] = interpolatedyearSSP[time_idx]
                        break
    aa, bb, ymax, ymin = 0, 0, 2020, 2100
    for i in range(177):
        if countryList[i] in Lincome_list:
            aa = aa + output_array[0, 4, i]
            bb = bb + 1
            if output_array[0, 4, i] > ymax:
                ymax = output_array[0, 4, i]
            if output_array[0, 4, i] < ymin:
                ymin = output_array[0, 4, i]
    print (aa/bb-2020)
    print (ymax-2020, ymin-2020)
    aa = np.array(output_array[:,4].T)
    np.savetxt('value.csv', aa, fmt='%int', delimiter=',')
    np.savetxt('countryList.csv', np.array(countryList), fmt='%str')