import numpy as np, sys
from scipy.optimize import curve_fit
from scipy import stats

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

def cal_R2(var1,var2):
    tmp1 = np.sum( (var1 - var2)**2 )
    tmp2 = np.sum( (var1 - np.mean(var1))**2  )
    tmp3 = 1. - tmp1/tmp2
    return tmp3

def get_table(CI_na, years_na):
    table_na = np.zeros([len(years_na),4])
    for yr_no in range(len(years_na)): 
        ref_yr = yr_no+years_na[0]
        table_na[yr_no,0] = ref_yr
        def nlm0(x,c0,r):
            yr_tmp = ref_yr
            return c0/(1+r)**(x-yr_tmp)
        popt,pcov=curve_fit(nlm0,years_na,CI_na)
        R2 = cal_R2(CI_na, popt[0]/(1+popt[1])**(years_na-ref_yr)) 
        table_na[yr_no,1] = popt[0]
        table_na[yr_no,2] = popt[1]
        table_na[yr_no,3] = R2
    return table_na

def get_histCtry(var1, countryList, beg, end):
    flag = 0
    for i in range(264):               # total row numbers
        i = i+5
        if var1[i][1] in countryList:
            tmp_x = var1[i][1]
            tmp_y = var1[i][beg:end]
            try:
                convert_y = np.array(tmp_y).astype(float)
            except:
                for idx in range(len(tmp_y)):
                    if tmp_y[idx] == '':
                        tmp_y[idx] = 0.
                convert_y = np.array(tmp_y).astype(float)
            if flag == 0:
                name_array = [tmp_x]
                data_array = convert_y
                flag = 1
            else:
                name_array.append(tmp_x)
                data_array = np.c_[data_array, convert_y]
    return name_array, data_array

# def plot_individual_Cty_trend(pop_WB, gdp_WB, co2_WB, int_WB, countryList):
#     years_WB         = np.array(pop_WB[4][5:-4]).astype(np.int)   # 1961 - 2014
#     namePOP, histPOP = get_histCtry(pop_WB, countryList, 5, -4)
#     nameGDP, histGDP = get_histCtry(gdp_WB, countryList, 5, -4)
#     nameCO2, histCO2 = get_histCtry(co2_WB, countryList, 5, -4)
#     CI_WB            = (histCO2*(10**-6)) / (histGDP*(10**-12))
#     CI_WB_toShow     = CI_WB
#     import matplotlib.pyplot as plt
#     for name_idx in range(177):
#         name = nameCO2[name_idx]
#         if name in Lincome_list:
#             print (name)
#             plt.scatter(np.arange(54), CI_WB_toShow[:, name_idx], s=5)
#             plt.ylim(0, 8)
#             plt.show()
#             plt.clf

def calculate_historical_global(pop_WB, gdp_WB, co2_WB, int_WB, countryList):
    years_WB     = np.array(pop_WB[4][5:-4]).astype(np.int)   # 1961 - 2014
    popGlobal_WB = (10**-9) *  np.array(pop_WB[262][5:-4]).astype(np.float)    # billion pop
    gdpGlobal_WB = (10**-12)*  np.array(gdp_WB[262][5:-4]).astype(np.float)    # trillion 2010 US$
    co2Global_WB = (10**-6) *  np.array(co2_WB[262][5:-4]).astype(np.float)    # Gt CO2
    intGlobal_WB =             np.array(int_WB[262][15:-6]).astype(np.float)   # Energy use 1971-2014
    percapitagdp_WB = gdpGlobal_WB / popGlobal_WB
    CI_WB           = co2Global_WB / gdpGlobal_WB
    table_WB0 = get_table(CI_WB[:-4],     years_WB[:-4] )
    table_WB1 = get_table(CI_WB     ,     years_WB      )      # Use data between 1961-2014
    # table_WB2 = get_table(CI_WB[33:],     years_WB[33:] )      # Use data between 1904-2014
    return years_WB, popGlobal_WB, gdpGlobal_WB, co2Global_WB, intGlobal_WB, percapitagdp_WB, CI_WB, table_WB1



def calculate_historical_cty(pop_WB, gdp_WB, co2_WB, int_WB, countryList):
    years_WB     = np.array(pop_WB[4][5:-4]).astype(np.int)   # 1961 - 2014
    namePOP, histPOP = get_histCtry(pop_WB, countryList, 5, -4)
    nameGDP, histGDP = get_histCtry(gdp_WB, countryList, 5, -4)
    nameCO2, histCO2 = get_histCtry(co2_WB, countryList, 5, -4)
    nameINT, histINT = get_histCtry(int_WB, countryList, 5, -5)
    Lco2, Lgdp, Lene, Lint = np.zeros([54]), np.zeros([54]), np.zeros([54]), np.zeros([54])
    Mco2, Mgdp, Mene, Mint = np.zeros([54]), np.zeros([54]), np.zeros([54]), np.zeros([54])
    Hco2, Hgdp, Hene, Hint = np.zeros([54]), np.zeros([54]), np.zeros([54]), np.zeros([54])
    for i in range(177):
        # ZeroArry = histCO2[:,i] * histGDP[:,i]
        # ZeroArry[ZeroArry!=0] = 1
        # histCO2[:,i] = histCO2[:,i] * ZeroArry
        # histGDP[:,i] = histGDP[:,i] * ZeroArry
        if namePOP[i] in Lincome_list:
            Lco2 = Lco2 + (10**-6) *  histCO2[:,i]    #(in units of Tg or Gt)
            Lgdp = Lgdp + (10**-12)*  histGDP[:,i]
            Lene = Lene + histINT[:,i] * histPOP[:,i] #(in units of kg)
        elif namePOP[i] in Mincome_list:
            Mco2 = Mco2 + (10**-6) *  histCO2[:,i]
            Mgdp = Mgdp + (10**-12)*  histGDP[:,i]
            Mene = Mene + histINT[:,i] * histPOP[:,i]
        elif namePOP[i] in Hincome_list:
            Hco2 = Hco2 + (10**-6) *  histCO2[:,i]
            Hgdp = Hgdp + (10**-12)*  histGDP[:,i]
            Hene = Hene + histINT[:,i] * histPOP[:,i]
    CI_CTY_L, INT_CTY_L, CI_INT_CTY_L  = Lco2/Lgdp, Lco2/Lene*10**12, (Lco2/Lgdp)/(Lco2/Lene*10**12)
    CI_CTY_M, INT_CTY_M, CI_INT_CTY_M  = Mco2/Mgdp, Mco2/Mene*10**12, (Mco2/Mgdp)/(Mco2/Mene*10**12)
    CI_CTY_H, INT_CTY_H, CI_INT_CTY_H  = Hco2/Hgdp, Hco2/Hene*10**12, (Hco2/Hgdp)/(Hco2/Hene*10**12)
    table_ctyL = get_table(CI_CTY_L[-22:], years_WB[-22:])
    table_ctyM = get_table(CI_CTY_M[-22:], years_WB[-22:])
    table_ctyH = get_table(CI_CTY_H[-22:], years_WB[-22:]) 
    return [table_ctyL, table_ctyM, table_ctyH, 
            CI_CTY_L, CI_CTY_M, CI_CTY_H, 
            INT_CTY_L, INT_CTY_M, INT_CTY_H, 
            CI_INT_CTY_L, CI_INT_CTY_M, CI_INT_CTY_H]