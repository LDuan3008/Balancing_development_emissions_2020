import numpy as np
from scipy.optimize import curve_fit
from scipy import stats
import matplotlib.pyplot as plt

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

def plt_trends(pop_WB, gdp_WB, co2_WB, countryList):
    years_WB     = np.array(pop_WB[4][5:-5]).astype(np.int)   # 1961 - 2014
    new_year     = np.arange(2100-1961)+1962
    new_year2     = np.arange(2100-1993)+1994
    popGlobal_WB = (10**-9) *  np.array(pop_WB[262][5:-5]).astype(np.float)    # billion pop
    gdpGlobal_WB = (10**-12)*  np.array(gdp_WB[262][5:-5]).astype(np.float)    # trillion 2010 US$
    co2Global_WB = (10**-6) *  np.array(co2_WB[262][5:-4]).astype(np.float)    # Gt CO2
    CI_WB1 = co2Global_WB / gdpGlobal_WB
    table_WB1 = get_table(CI_WB1     ,     years_WB      )[-6]
    CI_WB2 = table_WB1[1]/(1+table_WB1[2])**(new_year-table_WB1[0])
    
    years_WB     = np.array(pop_WB[4][5:-5]).astype(np.int)   # 1961 - 2014
    namePOP, histPOP = get_histCtry(pop_WB, countryList, 5, -5)
    nameGDP, histGDP = get_histCtry(gdp_WB, countryList, 5, -5)
    nameCO2, histCO2 = get_histCtry(co2_WB, countryList, 5, -4)
    Lco2, Lgdp = np.zeros([54]), np.zeros([54])
    Mco2, Mgdp = np.zeros([54]), np.zeros([54])
    Hco2, Hgdp = np.zeros([54]), np.zeros([54])
    for i in range(177):
        if namePOP[i] in Lincome_list:
            Lco2 = Lco2 + (10**-6) *  histCO2[:,i]
            Lgdp = Lgdp + (10**-12)*  histGDP[:,i]
        elif namePOP[i] in Mincome_list:
            Mco2 = Mco2 + (10**-6) *  histCO2[:,i]
            Mgdp = Mgdp + (10**-12)*  histGDP[:,i]
        elif namePOP[i] in Hincome_list:
            Hco2 = Hco2 + (10**-6) *  histCO2[:,i]
            Hgdp = Hgdp + (10**-12)*  histGDP[:,i]
    CI_CTY_L1           = Lco2/Lgdp
    CI_CTY_M1           = Mco2/Mgdp
    CI_CTY_H1           = Hco2/Hgdp
    table_ctyL = get_table(CI_CTY_L1[-22:], years_WB[-22:])[-6]
    table_ctyM = get_table(CI_CTY_M1[-22:], years_WB[-22:])[-6]
    table_ctyH = get_table(CI_CTY_H1[-22:], years_WB[-22:])[-6]
    CI_CTY_L2           = table_ctyL[1]/(1+table_ctyL[2])**(new_year2-table_ctyL[0])
    CI_CTY_M2           = table_ctyM[1]/(1+table_ctyM[2])**(new_year2-table_ctyM[0])
    CI_CTY_H2           = table_ctyH[1]/(1+table_ctyH[2])**(new_year2-table_ctyH[0])
    
    plt.scatter(np.arange(len(CI_WB1))+1961, CI_WB1, s=5, c='black')
    plt.scatter(years_WB[:-22], CI_CTY_L1[:-22], s=5, marker='^', alpha=0.3, c='firebrick')
    plt.scatter(years_WB[:-22], CI_CTY_M1[:-22], s=5, marker='^', alpha=0.3, c='royalblue')
    plt.scatter(years_WB[:-22], CI_CTY_H1[:-22], s=5, marker='^', alpha=0.3, c='orange')
    plt.scatter(np.arange(len(CI_CTY_L1[-22:]))+years_WB[-22], CI_CTY_L1[-22:], s=5, c='firebrick')
    plt.scatter(np.arange(len(CI_CTY_M1[-22:]))+years_WB[-22], CI_CTY_M1[-22:], s=5, c='royalblue')
    plt.scatter(np.arange(len(CI_CTY_H1[-22:]))+years_WB[-22], CI_CTY_H1[-22:], s=5, c='orange')
    plt.plot(new_year, CI_WB2, c='black')
    plt.plot(new_year2, CI_CTY_L2, c='firebrick')
    plt.plot(new_year2, CI_CTY_M2, c='royalblue')
    plt.plot(new_year2, CI_CTY_H2, c='orange')
    
    plt.ylim(0, 1.2)
    plt.show()
    # plt.savefig('testFigS2.ps')
    plt.clf()
    

def plot_compare_Kaya_components(pop_WB, gdp_WB, co2_WB, int_WB, countryList):
    years_WB     = np.array(pop_WB[4][5:-5]).astype(np.int)   # 1961 - 2014
    namePOP, histPOP = get_histCtry(pop_WB, countryList, 5, -5)
    nameGDP, histGDP = get_histCtry(gdp_WB, countryList, 5, -5)
    nameCO2, histCO2 = get_histCtry(co2_WB, countryList, 5, -4)
    nameINT, histINT = get_histCtry(int_WB, countryList, 5, -5)
    Lco2, Lgdp, Lene, Lint = np.zeros([54]), np.zeros([54]), np.zeros([54]), np.zeros([54])
    Mco2, Mgdp, Mene, Mint = np.zeros([54]), np.zeros([54]), np.zeros([54]), np.zeros([54])
    Hco2, Hgdp, Hene, Hint = np.zeros([54]), np.zeros([54]), np.zeros([54]), np.zeros([54])
    for i in range(177):
        ZeroArry = histCO2[:,i] * histGDP[:,i] * histINT[:, i]
        ZeroArry[ZeroArry!=0] = 1
        histCO2[:,i] = histCO2[:,i] * ZeroArry
        histGDP[:,i] = histGDP[:,i] * ZeroArry
        histINT[:,i] = histINT[:,i] * ZeroArry
        if namePOP[i] in Lincome_list:
            Lco2 = Lco2 + (10**-6) *  histCO2[:,i]       #(in units of Tg or Gt)
            Lgdp = Lgdp + (10**-12)*  histGDP[:,i]
            Lene = Lene + histINT[:,i] * histPOP[:,i]    #(in units of kg)
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

    num = CI_CTY_L.shape[0]
    plt.plot((np.arange(num)+1961)[-22:], CI_CTY_L[-22:], color='green')
    plt.plot((np.arange(num)+1961)[-22:], CI_CTY_M[-22:], color='royalblue')
    plt.plot((np.arange(num)+1961)[-22:], CI_CTY_H[-22:], color='pink')
    plt.xlim(1993, 2014)
    plt.ylim(0, 1.2)
    plt.show()
    # plt.savefig('p1.ps')
    plt.clf()
    plt.plot((np.arange(num)+1961)[-22:], INT_CTY_L[-22:], color='green')
    plt.plot((np.arange(num)+1961)[-22:], INT_CTY_M[-22:], color='royalblue')
    plt.plot((np.arange(num)+1961)[-22:], INT_CTY_H[-22:], color='pink')
    plt.xlim(1993, 2014)
    plt.ylim(0, 4)
    plt.show()
    # plt.savefig('p2.ps')
    plt.clf()
    plt.plot((np.arange(num)+1961)[-22:], CI_INT_CTY_L[-22:], color='green')
    plt.plot((np.arange(num)+1961)[-22:], CI_INT_CTY_M[-22:], color='royalblue')
    plt.plot((np.arange(num)+1961)[-22:], CI_INT_CTY_H[-22:], color='pink')
    plt.xlim(1993, 2014)
    plt.ylim(0, 0.6)
    plt.show()
    # plt.savefig('p3.ps')
    plt.clf()