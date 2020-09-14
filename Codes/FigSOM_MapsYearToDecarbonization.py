import numpy as np
import pygal
import pygal.maps.world
from pygal.style import Style
from matplotlib import pyplot as plt


create_Ctry_list = {'AFG':'af', 'AGO':'ao', 'ALB':'al', 'ARE':'ae', 'ARG':'ar',        \
                    'ARM':'am', 'AUS':'au', 'AUT':'at', 'AZE':'az', 'BDI':'bi', 'BEL':'be', 'BEN':'bj',    \
                    'BFA':'bf', 'BGD':'bd', 'BGR':'bg', 'BHR':'bh', 'BHS':'--', 'BIH':'ba', 'BLR':'by',    \
                    'BLZ':'bz', 'BOL':'bo', 'BRA':'br', 'BRB':'--', 'BRN':'bn', 'BTN':'bt', 'BWA':'bw',    \
                    'CAF':'cf', 'CAN':'ca', 'CHE':'ch', 'CHL':'cl', 'CHN':'cn', 'CIV':'ci', 'CMR':'cm',    \
                    'COD':'cd', 'COG':'cg', 'COL':'co', 'COM':'--', 'CPV':'cv', 'CRI':'cr', 'CUB':'cu',    \
                    'CYP':'cy', 'CZE':'cz', 'DEU':'de', 'DJI':'dj', 'DNK':'dk', 'DOM':'do', 'DZA':'dz',    \
                    'ECU':'ec', 'EGY':'eg', 'ERI':'er', 'ESP':'es', 'EST':'ee', 'ETH':'et', 'FIN':'fi',    \
                    'FJI':'--', 'FRA':'fr', 'GAB':'ga', 'GBR':'gb', 'GEO':'ge', 'GHA':'gh', 'GIN':'gn',    \
                    'GMB':'gm', 'GNB':'gw', 'GNQ':'gq', 'GRC':'gr', 'GTM':'gt', 'GUY':'gy', 'HKG':'hk',    \
                    'HND':'hn', 'HRV':'hr', 'HTI':'ht', 'HUN':'hu', 'IDN':'id', 'IND':'in', 'IRL':'ie',    \
                    'IRN':'ir', 'IRQ':'iq', 'ISL':'is', 'ISR':'il', 'ITA':'it', 'JAM':'jm', 'JOR':'jo',    \
                    'JPN':'jp', 'KAZ':'kz', 'KEN':'ke', 'KGZ':'kg', 'KHM':'kh', 'KOR':'kr', 'KWT':'kw',    \
                    'LAO':'la', 'LBN':'lb', 'LBR':'lr', 'LBY':'ly', 'LKA':'lk', 'LSO':'ls', 'LTU':'lt',    \
                    'LUX':'lu', 'LVA':'lv', 'MAC':'mo', 'MAR':'ma', 'MDA':'md', 'MDG':'mg', 'MDV':'mv',    \
                    'MEX':'mx', 'MKD':'mk', 'MLI':'ml', 'MLT':'mt', 'MMR':'mm', 'MNG':'mn', 'MOZ':'mz',    \
                    'MRT':'mr', 'MUS':'mu', 'MWI':'mw', 'MYS':'my', 'NAM':'na', 'NCL':'--', 'NER':'ne',    \
                    'NGA':'ng', 'NIC':'ni', 'NLD':'nl', 'NOR':'no', 'NPL':'np', 'NZL':'nz', 'OMN':'om',    \
                    'PAK':'pk', 'PAN':'pa', 'PER':'pe', 'PHL':'ph', 'PNG':'pg', 'POL':'pl', 'PRI':'pr',    \
                    'PRT':'pt', 'PRY':'py', 'PSE':'ps', 'PYF':'--', 'QAT':'--', 'ROU':'ro', 'RUS':'ru',    \
                    'RWA':'rw', 'SAU':'sa', 'SDN':'sd', 'SEN':'sn', 'SGP':'sg', 'SLB':'--', 'SLE':'sl',    \
                    'SLV':'sv', 'SOM':'so', 'SRB':'rs', 'SUR':'sr', 'SVK':'sk', 'SVN':'si', 'SWE':'se',    \
                    'SWZ':'sz', 'SYR':'sy', 'TCD':'td', 'TGO':'tg', 'THA':'th', 'TJK':'tj', 'TKM':'tm',    \
                    'TLS':'tl', 'TTO':'--', 'TUN':'tn', 'TUR':'tr', 'TZA':'tz', 'UGA':'ug', 'UKR':'ua',    \
                    'URY':'uy', 'USA':'us', 'UZB':'uz', 'VEN':'ve', 'VNM':'vn', 'VUT':'--', 'WSM':'--',    \
                    'YEM':'ye', 'ZAF':'za', 'ZMB':'zm', 'ZWE':'zw'}



####################################################################################

def plot_Ctrymap_dl_emit(year_decarbon, name, countryList):
    colors_list = ('#b2b2b2',
                   '#C8E7EE', '#BEDAEB', '#B5CEE9', '#ACC2E6', '#A3B6E4', 
                   '#9AAAE1', '#919EDF', '#8791DC', '#7E85DA', '#7579D7',
                   '#6C6DD5', '#6361D2', '#5A55D0', '#5048CD', '#473CCB', 
                   '#3E30C8', '#3524C6', '#2C18C3', '#230CC1', '#1A00BF',
                   '#130477')
                   
    custom_style1 = Style(
            background='white',                     # whole background
            plot_background='white',                # canvas background
            foreground='black',                     # capital color
            foreground_strong='black',              # capital color
            foreground_subtle='black',              # all boundary color
            opacity='1',
            opacity_hover='1',
            #transition='400ms ease-in',
            colors= colors_list
            )
    
    def find_interval(x, interval_num_total, low_b, hig_b, width):
        if x == low_b:
            return 0
        elif x >= hig_b:
            return interval_num_total-1
        else:
            idx = int(x/width)
            return idx+1
    
    low_b = 0.
    hig_b = 400.
    width = 20.
    interval_num_total = int((hig_b-low_b)/width +2) #22
    
    my_list = [ [] for i in range(interval_num_total) ] #0-21
    for i in range(177):
        if create_Ctry_list[countryList[i]] != '--':
            interval_idx = find_interval(year_decarbon[i], interval_num_total, low_b, hig_b, width)
            my_list[interval_idx].append( create_Ctry_list[countryList[i]] )
    
    supra = pygal.maps.world.World(style = custom_style1)
    for i in range(interval_num_total):
        supra.add('',my_list[i])
    # supra.render_to_file(name + '.svg')
    supra.render_to_file(name + '.pdf')
    
    
def plot_maps(cumulco2Emi_country_org, cumulco2Emi, countryList):
    cumulco2Emi_select0 = cumulco2Emi_country_org[4,:,-1]  - cumulco2Emi_country_org[4,:,9]
    cumulco2Emi_select1 = cumulco2Emi[0,1,4,:,-1]          - cumulco2Emi[0,1,4,:,9] #(177)
    cumulco2Emi_select2 = cumulco2Emi[1,1,4,:,-1]          - cumulco2Emi[1,1,4,:,9] #(177)
    cumulco2Emi_select3 = cumulco2Emi[2,1,4,:,-1]          - cumulco2Emi[2,1,4,:,9] #(177)
    cumulco2Emi_select4 = cumulco2Emi[3,1,4,:,-1]          - cumulco2Emi[3,1,4,:,9] #(177)
    cumulco2Emi_select5 = cumulco2Emi[4,1,4,:,-1]          - cumulco2Emi[4,1,4,:,9] #(177)
    
    additions_emissions0 = cumulco2Emi_select0              - cumulco2Emi_select1
    additions_emissions1 = cumulco2Emi_select2              - cumulco2Emi_select1
    additions_emissions2 = cumulco2Emi_select3              - cumulco2Emi_select1
    additions_emissions3 = cumulco2Emi_select4              - cumulco2Emi_select1
    additions_emissions4 = cumulco2Emi_select5              - cumulco2Emi_select1
    
    plot_Ctrymap_dl_emit(cumulco2Emi_select0, 'no_decarb',         countryList)
    plot_Ctrymap_dl_emit(cumulco2Emi_select1, 'all_decarb',        countryList)
    plot_Ctrymap_dl_emit(cumulco2Emi_select2, '10kReduce',         countryList)
    plot_Ctrymap_dl_emit(cumulco2Emi_select3, '20kReduce',         countryList)
    plot_Ctrymap_dl_emit(cumulco2Emi_select4, '40kReduce',         countryList)
    plot_Ctrymap_dl_emit(cumulco2Emi_select5, '80kReduce',         countryList)
    
    plot_Ctrymap_dl_emit(additions_emissions1, 'additions_emissions10k', countryList)
    plot_Ctrymap_dl_emit(additions_emissions2, 'additions_emissions20k', countryList)
    plot_Ctrymap_dl_emit(additions_emissions3, 'additions_emissions40k', countryList)
    plot_Ctrymap_dl_emit(additions_emissions4, 'additions_emissions80k', countryList)
    plot_Ctrymap_dl_emit(additions_emissions0, 'additions_emissionsNoR', countryList)

