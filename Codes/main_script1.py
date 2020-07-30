import csv, pandas as pd
import numpy as np

def read_in_data():
    # World Bank Data
    data_path = './'
    popRawHist_fn = 'API_SP.POP.TOTL_DS2_en_csv_v2_41106.csv'
    gdpRawHist_fn = 'API_NY.GDP.MKTP.KD_DS2_en_csv_v2_41054.csv' 
    co2RawHist_fn = 'API_EN.ATM.CO2E.KT_DS2_en_csv_v2_41056.csv'
    # intRawHist_fn = 'API_EN.ATM.CO2E.EG.ZS_DS2_EN_csv_v2_991856.csv'
    intRawHist_fn = 'API_EG.USE.PCAP.KG.OE_DS2_en_csv_v2_989395.csv'
    with open(data_path + popRawHist_fn, 'rU') as popRawHist_f:
        reader_WB1 = csv.reader(popRawHist_f, delimiter=',')
        pop_WB = np.array(list(reader_WB1))
    with open(data_path + gdpRawHist_fn, 'rU') as gdpRawHist_f:
        reader_WB2 = csv.reader(gdpRawHist_f, delimiter=',')
        gdp_WB = np.array(list(reader_WB2))
    with open(data_path + co2RawHist_fn, 'rU') as co2RawHist_f:
        reader_WB3 = csv.reader(co2RawHist_f, delimiter=',')
        co2_WB = np.array(list(reader_WB3))
    with open(data_path + intRawHist_fn, 'rU') as intRawHist_f:
        reader_WB4 = csv.reader(intRawHist_f, delimiter=',')
        int_WB = np.array(list(reader_WB4))
    # SSPs data
    data_path = './'
    gdpRawSSP_fn = 'iamc_db-GDPppp.xlsx'
    popRawSSP_fn = 'iamc_db-Pop.xlsx'
    gdpRawSSP = np.array(pd.read_excel(data_path + gdpRawSSP_fn, header = None))[1:1726]
    popRawSSP = np.array(pd.read_excel(data_path + popRawSSP_fn, header = None))[1:2711]
    return pop_WB, gdp_WB, co2_WB, int_WB, gdpRawSSP, popRawSSP

    