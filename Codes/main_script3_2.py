import numpy as np,cdutil
import scipy.interpolate as itp

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

def selectSSPs(var1, SSP_name, YearsSSP, Model_name, CountryList):
    tmp1 = np.zeros(len(YearsSSP))
    for i in range(len(var1[:,0])):     
        if var1[i,0] == Model_name and var1[i,1] == SSP_name and var1[i,2] in CountryList:
            tmp1 = np.c_[tmp1,var1[i,6:16]]
    tmp2 = tmp1[:,1:].T
    return tmp2 

def interpolate(var_in, YearsSSP):
    yr_org = np.copy(YearsSSP)
    yr_aft = np.arange(2010,2101,1)
    tmp1 = np.zeros([177,91])
    for i in range(177):
         tmp2 = np.array(var_in[i])
         itpfun = itp.interp1d(yr_org,tmp2)
         tmp1[i] = itpfun(yr_aft)
    return tmp1

def future_emi_global(CountryList, year, tableL, tableM, tableH, gdp):
    emi = np.zeros([5,177,91])
    ciL = tableL[1]/(1+tableL[2])**(year-tableL[0])
    ciM = tableM[1]/(1+tableM[2])**(year-tableM[0])
    ciH = tableH[1]/(1+tableH[2])**(year-tableH[0])
    
    for ssp_idx in range(5):
        for cty_idx in range(177):
            if CountryList[cty_idx] in Lincome_list:
                emi[ssp_idx, cty_idx] = gdp[ssp_idx, cty_idx] * ciL
            if CountryList[cty_idx] in Mincome_list:
                emi[ssp_idx, cty_idx] = gdp[ssp_idx, cty_idx] * ciM
            if CountryList[cty_idx] in Hincome_list:
                emi[ssp_idx, cty_idx] = gdp[ssp_idx, cty_idx] * ciH
    return emi


def cal_adjuated_emissions(shreshold, ramprate, co2EmiCtry, percapitagdpSSPs, interpolatedyearSSP, need_country): 
    adjuated_AnnCO2Emit_ctyLevel       = np.copy(co2EmiCtry)                 #(5,177,91)
    percapitagdp_tmp                   = np.copy(percapitagdpSSPs)           #(5,177,91)
    interpolatedyear_tmp               = np.copy(interpolatedyearSSP)        #(91)
    # adjust annual CO2 emissions:
    for ssp_index in range(5):
        for i in range(177):
            for j in range(91):
                if percapitagdp_tmp[ssp_index,i,j] >= shreshold and interpolatedyear_tmp[j] >= 2020:
                    idx = j
                    for k in range(91 - idx):
                        adjuated_AnnCO2Emit_ctyLevel[ssp_index,i,k+idx] = adjuated_AnnCO2Emit_ctyLevel[ssp_index,i,k+idx-1] * (1.-ramprate)
                    break
    # calculate other emissions
    adjuated_AnnCO2Emit_gloLevel = cdutil.averager(adjuated_AnnCO2Emit_ctyLevel,axis=1,weights='equal',action='sum') 
    adjuated_CumCO2Emit_gloLevel = np.zeros([5,91])
    for ssp_index in range(5):
        for i in range(91):
            adjuated_CumCO2Emit_gloLevel[ssp_index,i]  = cdutil.averager(adjuated_AnnCO2Emit_gloLevel[ssp_index,:i+1] ,axis=0,weights='equal',action='sum')
    if need_country == 1:
        adjuated_CumCO2Emit_ctyLevel = np.zeros([5,177,91])
        for ssp_index in range(5):
            for i in range(177):
                for j in range(91):
                    adjuated_CumCO2Emit_ctyLevel[ssp_index,i,j] = cdutil.averager(adjuated_AnnCO2Emit_ctyLevel[ssp_index,i,:j+1], axis=0,weights='equal',action='sum')
    else:
        adjuated_CumCO2Emit_ctyLevel = 0.
    return adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel



############################################################################################################
#### main function starts from here ########################################################################
    ########################################################################################################
def future_projections_DiffRate(gdpRawSSP, popRawSSP, countryList, table_usedL, table_usedM, table_usedH, shreshold_list, ramprate_list, need_country, convert):
    # factor2010gdp2005 = 0.909585947164884
    factor2010gdp2005 = 1.0
    model_name = 'OECD Env-Growth'
    SSP_list = {0:'SSP1', 1:'SSP2', 2:'SSP3', 3:'SSP4', 4:'SSP5'}
    yearsSSP = np.array([2010,2020,2030,2040,2050,2060,2070,2080,2090,2100])
    
    # step1, select data from input files
    gdpSSPs = np.zeros([5,177,10])
    popSSPs = np.zeros([5,177,10])
    for i in range(5):
        gdpSSPs[i] = selectSSPs(gdpRawSSP, SSP_list[i], yearsSSP, model_name, countryList)
        gdpSSPs[i] = gdpSSPs[i] * convert[:, None]
        popSSPs[i] = selectSSPs(popRawSSP, SSP_list[i], yearsSSP, model_name, countryList) 
        
    # step2, interpolate to yearly resolution
    interpolatedyearSSP = np.arange(2010,2101,1)
    interpolatedgdpSSPs = np.zeros([5,177,91])
    interpolatedpopSSPs = np.zeros([5,177,91])
    percapitagdpSSPs    = np.zeros([5,177,91])
    for i in range(5):
        interpolatedgdpSSPs[i] = interpolate(gdpSSPs[i], yearsSSP) * (10**-3) * factor2010gdp2005      
        interpolatedpopSSPs[i] = interpolate(popSSPs[i], yearsSSP) * (10**-3)                          
        percapitagdpSSPs[i]    = interpolatedgdpSSPs[i] / interpolatedpopSSPs[i]
        
        
    # step 3, calculate original future emissions
    original_AnnCO2Emit_ctyLevel = future_emi_global(countryList, interpolatedyearSSP, table_usedL, table_usedM, table_usedH, interpolatedgdpSSPs).astype(np.float)
    # derived from original_AnnCO2Emit_ctyLevel
    original_AnnCO2Emit_gloLevel = cdutil.averager(original_AnnCO2Emit_ctyLevel,axis=1,weights='equal',action='sum')
    original_CumCO2Emit_ctyLevel =  np.zeros([5,177,91])
    for i in range(5):
        for j in range(177):
            for k in range(91):
                original_CumCO2Emit_ctyLevel[i,j,k] = cdutil.averager(original_AnnCO2Emit_ctyLevel[i,j,:k+1] ,axis=0,weights='equal',action='sum')
    original_CumCO2Emit_gloLevel = np.zeros([5,91])
    for i in range(5):
        for j in range(91):
            original_CumCO2Emit_gloLevel[i,j]= cdutil.averager(original_AnnCO2Emit_gloLevel[i,:j+1] ,axis=0,weights='equal',action='sum')
            
    # step 4, calculate adjuated future emissions
    len1 = len(shreshold_list)
    len2 = len(ramprate_list)
    adjuated_AnnCO2Emit_gloLevel = np.zeros([len1,len2,5,91])
    adjuated_AnnCO2Emit_ctyLevel = np.zeros([len1,len2,5,177,91])
    adjuated_CumCO2Emit_gloLevel = np.zeros([len1,len2,5,91])
    adjuated_CumCO2Emit_ctyLevel = np.zeros([len1,len2,5,177,91])
    for ii in range(len1):
        for jj in range(len2):
            [adjuated_AnnCO2Emit_ctyLevel[ii,jj], adjuated_AnnCO2Emit_gloLevel[ii,jj], 
             adjuated_CumCO2Emit_ctyLevel[ii,jj], adjuated_CumCO2Emit_gloLevel[ii,jj]
             ] = cal_adjuated_emissions(shreshold_list[ii], ramprate_list[jj], original_AnnCO2Emit_ctyLevel, percapitagdpSSPs, interpolatedyearSSP, need_country)
    
    return [original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
            adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
            percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs]
    