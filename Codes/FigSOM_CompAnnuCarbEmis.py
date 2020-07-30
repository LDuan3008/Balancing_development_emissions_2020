import csv, pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compare(original_AnnCO2Emit_gloLevel, adjuated_AnnCO2Emit_gloLevel, countryList):
    year1 = np.array([2015, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
    data_path = '/Users/leiduan/Desktop/File/Research/Paper/Lei/Ongoing/Duan et al. 2019_GDP vs. CO2/Codes/new_data/'
    co2SSPcmip6_fn = 'iamc_db_CO2_SSPcmip6.xlsx'
    co2SSPcmip6    = np.array(pd.read_excel(data_path + co2SSPcmip6_fn, header = None))[1:]
    co2SSP5cmip6   = co2SSPcmip6[8][5:-1]/1000
    co2SSP2cmip6   = co2SSPcmip6[6][5:-1]/1000

    year2 = np.arange(81)+2020
    co2RCP85_fn = 'RCP85_EMISSIONS.xls'
    co2RCP85_al = np.array(pd.read_excel(data_path + co2RCP85_fn, header = None))[293:374, :3]
    co2RCP85 = co2RCP85_al[:, 1] + co2RCP85_al[:, 2]

    year3 = np.arange(91)+2010
    plt.plot(year1, co2SSP5cmip6, color='firebrick')
    plt.plot(year2, co2RCP85*3.67, color='royalblue')
    plt.plot(year3, original_AnnCO2Emit_gloLevel[4], color='grey')
    for idx in range(5):
        plt.plot(year3, adjuated_AnnCO2Emit_gloLevel[idx, 0, 4], color='grey')
    plt.xlim(2020, 2100)
    plt.ylim(0, 180)
    plt.show()
    # plt.savefig('globalscale.ps')
    plt.clf()

    
def compare_reg(original_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_ctyLevel, countryList):
    year1 = np.array([2015, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
    data_path = '/Users/leiduan/Desktop/File/Research/Paper/Lei/Ongoing/Duan et al. 2019_GDP vs. CO2/Codes/new_data/'
    co2SSP5cmip6_fn = 'iamc_db_CO2_SSP5cmip6.xlsx'
    co2SSP5cmip6    = np.array(pd.read_excel(data_path + co2SSP5cmip6_fn, header = None))[1:]
    R5_2OECD_co2SSP5cmip6  = co2SSP5cmip6[9][5:-1]/1000
    R5_2REF_co2SSP5cmip6   = co2SSP5cmip6[10][5:-1]/1000
    R5_2ASIA_co2SSP5cmip6  = co2SSP5cmip6[6][5:-1]/1000
    R5_2MAF_co2SSP5cmip6   = co2SSP5cmip6[8][5:-1]/1000
    R5_2LAM_co2SSP5cmip6   = co2SSP5cmip6[7][5:-1]/1000

    co2SSP2cmip6_fn = 'iamc_db_CO2_SSP2cmip6.xlsx'
    co2SSP2cmip6    = np.array(pd.read_excel(data_path + co2SSP2cmip6_fn, header = None))[1:]
    R5_2OECD_co2SSP2cmip6  = co2SSP2cmip6[12][5:-1]/1000
    R5_2REF_co2SSP2cmip6   = co2SSP2cmip6[13][5:-1]/1000
    R5_2ASIA_co2SSP2cmip6  = co2SSP2cmip6[9][5:-1]/1000
    R5_2MAF_co2SSP2cmip6   = co2SSP2cmip6[11][5:-1]/1000
    R5_2LAM_co2SSP2cmip6   = co2SSP2cmip6[10][5:-1]/1000

    print (R5_2OECD_co2SSP2cmip6)
    print (R5_2ASIA_co2SSP2cmip6)
    print (R5_2LAM_co2SSP2cmip6)

    R5_2OECD = ['ALB', 'AUS', 'AUT', 'BEL', 'BIH', 'BGR', 'CAN', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 'FIN', 'FRA', 'DEU',
                'GRC', 'GUM', 'HUN', 'ISL', 'IRL', 'ITA', 'JPN', 'LVA', 'LTU', 'LUX', 'MLT', 'MNE', 'NLD', 'NZL', 'NOR',
                'POL', 'PRT', 'PRI', 'ROU', 'SRB', 'SVK', 'SVN', 'ESP', 'SWE', 'CHE', 'MKD', 'TUR', 'GBR', 'USA']
    R5_2REF = ['ARM', 'AZE', 'BLR', 'GEO', 'KAZ', 'KGZ', 'MDA', 'RUS', 'TJK', 'TKM', 'UKR', 'UZB']
    R5_2ASIA = ['AFG', 'BGD', 'BTN', 'BRN', 'KHM', 'CHN', 'HKG', 'MAC', 'PRK', 'FJI', 'PYF', 'IND', 'IDN', 'LAO', 'MYS',
                'MDV', 'FSM', 'MNG', 'MMR', 'NPL', 'NCL', 'PAK', 'PNG', 'PHL', 'KOR', 'WSM', 'SGP', 'SLB', 'LKA', 'TWN',
                'THA', 'TLS', 'VUT', 'VNM']
    R5_2MAF = ['DZA', 'AGO', 'BHR', 'BEN', 'BWA', 'BFA', 'BDI', 'CMR', 'CPV', 'CAF', 'TCD', 'COM', 'COG', 'CIV', 'COD',
               'DJI', 'EGY', 'GNQ', 'ERI', 'ETH', 'GAB', 'GMB', 'GHA', 'GIN', 'GNB', 'IRN', 'IRQ', 'ISR', 'JOR', 'KEN',
               'KWT', 'LBN', 'LSO', 'LBR', 'MDG', 'MWI', 'MLI', 'MRT', 'MUS', 'MYT', 'MAR', 'MOZ', 'NAM', 'NER', 'NGA',
               'OMN', 'QAT', 'RWA', 'REU', 'SAU', 'SEN', 'SLE', 'SOM', 'ZAF', 'SSD', 'SDN', 'SYR', 'TGO', 'TUN', 'UGA',
               'ARE', 'TZA', 'ESH', 'YEM', 'ZMB', 'ZWE']
    R5_2LAM = ['ARG', 'ABW', 'BHS', 'BRB', 'BLZ', 'BOL', 'BRA', 'CHL', 'COL', 'CRI', 'CUB', 'DOM', 'ECU', 'SLV', 'GUF',
               'GRD', 'GLP', 'GTM', 'GUY', 'HTI', 'HND', 'JAM', 'MTQ', 'MEX', 'NIC', 'PAN', 'PRY', 'PER', 'SUR', 'TTO',
               'VIR', 'URY', 'VEN']
    year3 = np.arange(91)+2010
    CO2_R5_2OECD_org, CO2_R5_2OECD_adj = np.zeros([5, 91]), np.zeros([5, 2, 5, 91])
    CO2_R5_2REF_org,  CO2_R5_2REF_adj  = np.zeros([5, 91]), np.zeros([5, 2, 5, 91])
    CO2_R5_2ASIA_org, CO2_R5_2ASIA_adj = np.zeros([5, 91]), np.zeros([5, 2, 5, 91])
    CO2_R5_2MAF_org,  CO2_R5_2MAF_adj  = np.zeros([5, 91]), np.zeros([5, 2, 5, 91])
    CO2_R5_2LAM_org,  CO2_R5_2LAM_adj  = np.zeros([5, 91]), np.zeros([5, 2, 5, 91])
    for idx in range(countryList.shape[0]):
        cty_idx = countryList[idx]
        if cty_idx in R5_2OECD: 
            CO2_R5_2OECD_org = CO2_R5_2OECD_org + original_AnnCO2Emit_ctyLevel[:, idx]
            CO2_R5_2OECD_adj = CO2_R5_2OECD_adj + adjuated_AnnCO2Emit_ctyLevel[:, :, :, idx]
        elif cty_idx in R5_2REF:  
            CO2_R5_2REF_org = CO2_R5_2REF_org + original_AnnCO2Emit_ctyLevel[:, idx]
            CO2_R5_2REF_adj = CO2_R5_2REF_adj + adjuated_AnnCO2Emit_ctyLevel[:, :, :, idx]
        elif cty_idx in R5_2ASIA: 
            CO2_R5_2ASIA_org = CO2_R5_2ASIA_org + original_AnnCO2Emit_ctyLevel[:, idx]
            CO2_R5_2ASIA_adj = CO2_R5_2ASIA_adj + adjuated_AnnCO2Emit_ctyLevel[:, :, :, idx]
        elif cty_idx in R5_2MAF:  
            CO2_R5_2MAF_org = CO2_R5_2MAF_org + original_AnnCO2Emit_ctyLevel[:, idx]
            CO2_R5_2MAF_adj = CO2_R5_2MAF_adj + adjuated_AnnCO2Emit_ctyLevel[:, :, :, idx]
        elif cty_idx in R5_2LAM:  
            CO2_R5_2LAM_org = CO2_R5_2LAM_org + original_AnnCO2Emit_ctyLevel[:, idx]
            CO2_R5_2LAM_adj = CO2_R5_2LAM_adj + adjuated_AnnCO2Emit_ctyLevel[:, :, :, idx]
        else:
            print ('not in the list: ', cty_idx)
    plt.plot(year1, R5_2OECD_co2SSP5cmip6, color='firebrick')
    plt.plot(year1, R5_2OECD_co2SSP2cmip6, color='firebrick')
    plt.plot(year3, CO2_R5_2OECD_org[4], color='royalblue')
    for idx in range(5):
        plt.plot(year3, CO2_R5_2OECD_adj[idx, 0, 4], color='grey')
    plt.show()
    plt.clf()
    plt.plot(year1, R5_2REF_co2SSP5cmip6, color='firebrick')
    plt.plot(year1, R5_2REF_co2SSP2cmip6, color='firebrick')
    plt.plot(year3, CO2_R5_2REF_org[4], color='royalblue')
    for idx in range(5):
        plt.plot(year3, CO2_R5_2REF_adj[idx, 0, 4], color='grey')
    plt.show()
    plt.clf()
    plt.plot(year1, R5_2ASIA_co2SSP5cmip6, color='firebrick')
    plt.plot(year1, R5_2ASIA_co2SSP2cmip6, color='firebrick')
    plt.plot(year3, CO2_R5_2ASIA_org[4], color='royalblue')
    for idx in range(5):
        plt.plot(year3, CO2_R5_2ASIA_adj[idx, 0, 4], color='grey')
    plt.show()
    plt.clf()
    plt.plot(year1, R5_2MAF_co2SSP5cmip6, color='firebrick')
    plt.plot(year1, R5_2MAF_co2SSP2cmip6, color='firebrick')
    plt.plot(year3, CO2_R5_2MAF_org[4], color='royalblue')
    for idx in range(5):
        plt.plot(year3, CO2_R5_2MAF_adj[idx, 0, 4], color='grey')
    plt.show()
    plt.clf()
    plt.plot(year1, R5_2LAM_co2SSP5cmip6, color='firebrick')
    plt.plot(year1, R5_2LAM_co2SSP2cmip6, color='firebrick')
    plt.plot(year3, CO2_R5_2LAM_org[4], color='royalblue')
    for idx in range(5):
        plt.plot(year3, CO2_R5_2LAM_adj[idx, 0, 4], color='grey')
    plt.show()
    plt.clf()



def compare_cty(original_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_ctyLevel, countryList):
    year1 = np.array([2015, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
    data_path = '/Users/leiduan/Desktop/File/Research/Paper/Lei/Ongoing/Duan et al. 2019_GDP vs. CO2/Codes/new_data/'
    co2SSPcmip6_fn = 'iamc_db_CO2_SSP5cmip6.xlsx'
    co2SSPcmip6    = np.array(pd.read_excel(data_path + co2SSPcmip6_fn, header = None))[1:]
    co2SSPcmip6_China  = co2SSPcmip6[1][5:-1]/1000
    co2SSPcmip6_India  = co2SSPcmip6[2][5:-1]/1000
    co2SSPcmip6_USA    = co2SSPcmip6[11][5:-1]/1000

    year3 = np.arange(91)+2010
    CO2_China_org, CO2_China_adj = np.zeros([5, 91]), np.zeros([5, 2, 5, 91])
    CO2_India_org, CO2_India_adj = np.zeros([5, 91]), np.zeros([5, 2, 5, 91])
    CO2_USA_org,   CO2_USA_adj   = np.zeros([5, 91]), np.zeros([5, 2, 5, 91])
    for idx in range(countryList.shape[0]):
        cty_idx = countryList[idx]
        if cty_idx in ['CHN', 'HKG', 'MAC']: 
            CO2_China_org = CO2_China_org + original_AnnCO2Emit_ctyLevel[:, idx]
            CO2_China_adj = CO2_China_adj + adjuated_AnnCO2Emit_ctyLevel[:, :, :, idx]
        elif cty_idx == 'IND':  
            CO2_India_org = CO2_India_org + original_AnnCO2Emit_ctyLevel[:, idx]
            CO2_India_adj = CO2_India_adj + adjuated_AnnCO2Emit_ctyLevel[:, :, :, idx]
        elif cty_idx == 'USA': 
            CO2_USA_org = CO2_USA_org + original_AnnCO2Emit_ctyLevel[:, idx]
            CO2_USA_adj = CO2_USA_adj + adjuated_AnnCO2Emit_ctyLevel[:, :, :, idx]

    plt.plot(year1, co2SSPcmip6_China, color='firebrick')
    plt.plot(year3, CO2_China_org[4], color='royalblue')
    for idx in range(5):
        plt.plot(year3, CO2_China_adj[idx, 0, 4], color='grey')
    plt.show()
    plt.clf()

    plt.plot(year1, co2SSPcmip6_India, color='firebrick')
    plt.plot(year3, CO2_India_org[4], color='royalblue')
    for idx in range(5):
        plt.plot(year3, CO2_India_adj[idx, 0, 4], color='grey')
    plt.show()
    plt.clf()

    plt.plot(year1, co2SSPcmip6_USA, color='firebrick')
    plt.plot(year3, CO2_USA_org[4], color='royalblue')
    for idx in range(5):
        plt.plot(year3, CO2_USA_adj[idx, 0, 4], color='grey')
    plt.show()
    plt.clf()

