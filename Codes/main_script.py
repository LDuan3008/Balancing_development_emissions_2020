# %%
import numpy as np
import pickle, sys
from main_script1 import read_in_data
from main_script2 import calculate_historical_global
from main_script2 import calculate_historical_cty
from main_script3_1 import future_projections_SameRate
from main_script3_2 import future_projections_DiffRate

######################################################################################################
# read_in_data
pop_WB, gdp_WB, co2_WB, int_WB, gdpRawSSP, popRawSSP = read_in_data()
countryList = np.unique((gdpRawSSP[1:-1,2]))
[years_WB, popGlobal_WB, gdpGlobal_WB, co2Global_WB, intGlobal_WB, percapitagdp_WB, CI_WB, table_WB] = calculate_historical_global(pop_WB, gdp_WB, co2_WB, int_WB, countryList)
[table_ctyL, table_ctyM, table_ctyH, CI_CTY_L, CI_CTY_M, CI_CTY_H, INT_CTY_L, INT_CTY_M, INT_CTY_H, CI_INT_CTY_L, CI_INT_CTY_M, CI_INT_CTY_H] = calculate_historical_cty(pop_WB, gdp_WB, co2_WB, int_WB, countryList)


""" Calculate numbers in paper
################################################################################################################################################################
shreshold_list, ramprate_list, need_country, table_used = [0, 10, 20, 40, 80], [0, 0.02, 0.08], 1.,  table_WB[-6] 
[original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
 adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
 percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)

# Second paragraph
term1 = (adjuated_CumCO2Emit_ctyLevel[0,1,4,:,-1] - adjuated_CumCO2Emit_ctyLevel[0,1,4,:,9])
term2 = (adjuated_CumCO2Emit_ctyLevel[1,1,4,:,-1] - adjuated_CumCO2Emit_ctyLevel[1,1,4,:,9])
tmp01 = (term1 - term2)*(-1)
print ( tmp01.max(), tmp01.min() )
print ()
print (original_AnnCO2Emit_gloLevel[4,10], original_AnnCO2Emit_gloLevel[4,-1])
print (original_CumCO2Emit_gloLevel[4,-1] - original_CumCO2Emit_gloLevel[4,9] )
print (adjuated_AnnCO2Emit_gloLevel[1,1,4,-1])
tmp11 = adjuated_CumCO2Emit_gloLevel[1,1,4,-1] - adjuated_CumCO2Emit_gloLevel[1,1,4,9]
tmp22 = adjuated_CumCO2Emit_gloLevel[0,1,4,-1] - adjuated_CumCO2Emit_gloLevel[0,1,4,9]
tmp33 = original_CumCO2Emit_gloLevel[4,-1] - original_CumCO2Emit_gloLevel[4,9]
diff3 = tmp22 - tmp33
diff2 = tmp11 - tmp22
print (diff3)
print ()
# Third paragraph
print ( (adjuated_AnnCO2Emit_gloLevel[1,1,4,-1] - adjuated_AnnCO2Emit_gloLevel[0,1,4,-1]))
print (diff2)
print ( (adjuated_AnnCO2Emit_gloLevel[1,1,4,-1] - adjuated_AnnCO2Emit_gloLevel[0,1,4,-1]) / original_AnnCO2Emit_gloLevel[4,-1]*100  )
print ( (adjuated_CumCO2Emit_gloLevel[1,1,4,-1] - adjuated_CumCO2Emit_gloLevel[0,1,4,-1]) / (original_CumCO2Emit_gloLevel[4,-1] - original_CumCO2Emit_gloLevel[4,9]) *100  )
print ( (adjuated_AnnCO2Emit_gloLevel[2,1,4,-1] - adjuated_AnnCO2Emit_gloLevel[0,1,4,-1]) / original_AnnCO2Emit_gloLevel[4,-1]*100  )
print ( (adjuated_CumCO2Emit_gloLevel[2,1,4,-1] - adjuated_CumCO2Emit_gloLevel[0,1,4,-1]) / (original_CumCO2Emit_gloLevel[4,-1]-original_CumCO2Emit_gloLevel[4,9]) *100  )
print ()
# Forth 
warming_org = original_CumCO2Emit_gloLevel[:,-1] - original_CumCO2Emit_gloLevel[:,1] + 515*3.667
warming_red = adjuated_CumCO2Emit_gloLevel[:,:,:,-1] - adjuated_CumCO2Emit_gloLevel[:,:,:,1] + 515*3.667
print ( (warming_red[1, 0, 4] - warming_red[0, 0, 4])*2/3667)
print ( (warming_red[1, 1, 4] - warming_red[0, 1, 4])*2/3667)
print ( (warming_red[1, 2, 4] - warming_red[0, 2, 4])*2/3667)
print ()
print ( (warming_red[1, 1, 4] - warming_red[0, 1, 4])*2/3667)
print ( (warming_red[2, 1, 4] - warming_red[0, 1, 4])*2/3667)
print ( (warming_red[3, 1, 4] - warming_red[0, 1, 4])*2/3667)
print ( (warming_red[4, 1, 4] - warming_red[0, 1, 4])*2/3667)
print ()
print (  warming_red[0, 1, 4]                        *2/3667)  # Abstract
################################################################################################################################################################
# """

""" table S2-S6
################################################################################################################################################################
shreshold_list, ramprate_list, need_country, table_used = [0, 10, 20, 40, 80], [0, 0.01, 0.02, 0.04, 0.08], 0, table_WB[-6]
[original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
 adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
 percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)
# Table S2-S5
from Table import Fig_YearReachThreshold_Table
shreshold_list_for_plot = [10, 20, 40, 80]
Fig_YearReachThreshold_Table(percapitagdpSSPs, shreshold_list_for_plot, interpolatedyearSSP, pop_WB, gdp_WB, countryList)
# Table S6
warming_org = original_CumCO2Emit_gloLevel[4,-1] - original_CumCO2Emit_gloLevel[4,1] + 515*3.667
warming_red = adjuated_CumCO2Emit_gloLevel[:,:,4,-1] - adjuated_CumCO2Emit_gloLevel[:,:,4,1] + 515*3.667
print ( (warming_red[1:] - warming_red[0]) * 2/3667 )
################################################################################################################################################################
# """

""" SOM Figures
################################################################################################################################################################
# from FigSOM_PerCapGDP_PerCapEmi import plot_PerCapGDP_PerCapEmi
# plot_PerCapGDP_PerCapEmi(co2_WB, gdp_WB, pop_WB, countryList)

# from FigSOM_CarIntImp import plt_trends, plot_compare_Kaya_components
# plt_trends(pop_WB, gdp_WB, co2_WB, countryList)
# plot_compare_Kaya_components(pop_WB, gdp_WB, co2_WB, int_WB, countryList)

# from FigSOM_MapsYearToDecarbonization import plot_maps    # need_country = 1
# shreshold_list, ramprate_list, need_country, table_used = [0, 10, 20, 40, 80], [0.01,  0.02], 1, table_WB[-6]
# [original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
#  adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
#  percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)
# plot_maps(original_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_ctyLevel, countryList)

# from FigSOM_CumulativeEmissions import plot_CumEmi    # need_country = 0
# shreshold_list, ramprate_list, need_country, table_used = [0, 10, 20, 40, 80], [0.01,  0.02], 0, table_WB[-6]
# [original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
#  adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
#  percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)
# plot_CumEmi(interpolatedyearSSP, original_CumCO2Emit_gloLevel, adjuated_CumCO2Emit_gloLevel)

# from FigSOM_pie import plot_pie
# shreshold_list, ramprate_list, need_country, table_used = [0, 10, 20, 40, 80], [0.01,  0.02], 0, table_WB[-6]
# [original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
#  adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
#  percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)
# plot_pie(interpolatedyearSSP, adjuated_AnnCO2Emit_gloLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_gloLevel, adjuated_CumCO2Emit_gloLevel, interpolatedpopSSPs, percapitagdpSSPs)

# Newly added, Compare annual CO2 emissions from our estimation with the SSP baseline scenario
# shreshold_list, ramprate_list, need_country, table_used = [0,  10,  20, 40, 80], [0.02, 0.04], 0, table_WB[-6]
# [original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
#  adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
#  percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs
#  ] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)
# year2 = np.arange(91)+2010
# from FigSOM_CompAnnuCarbEmis import compare, compare_reg, compare_cty
# compare(original_AnnCO2Emit_gloLevel, adjuated_AnnCO2Emit_gloLevel, countryList)
# compare_reg(original_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_ctyLevel, countryList)
# compare_cty(original_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_ctyLevel, countryList)
################################################################################################################################################################
# """


"""            #------------------------------------------------------->    figure here
################################################################################################################################################################
shreshold_list = [0, 10, 20, 40, 80]
ramprate_list  = [0.01, 0.02]
need_country   = 1
table_used = table_WB[-6] 

[original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
 adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
 percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs
 ] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)

from Fig_YearReach_BarEmit import Fig_YearReachThreshold
shreshold_list_for_plot = [10, 20, 40, 80]
ramprate_list = [0, 0.02]
Fig_YearReachThreshold(percapitagdpSSPs, shreshold_list_for_plot, interpolatedyearSSP, pop_WB, gdp_WB, countryList)
from Fig_YearReach_BarEmit import plot_cty_CumEmit
plot_cty_CumEmit(original_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_ctyLevel, interpolatedpopSSPs, interpolatedgdpSSPs, percapitagdpSSPs, countryList)
################################################################################################################################################################
#"""


"""            #------------------------------------------------------->    figure here
################################################################################################################################################################
shreshold_list = [0, 10, 20, 40, 80]
ramprate_list  = [0.01, 0.02]
need_country   = 0
table_used = table_WB[-6] 

[original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
 adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
 percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs
 ] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)

# Three figures:
# (1) Time series of the global-scale annual CO2 emissions from 2020;
# (2) Pie plot of percentages of cumulative CO2 emissions in various decarbonization scenarios relative to the NoReduce case between 2020 and 2100;
# (3) Pie plot of percentages of populations at various per-capital GDP levels at year 2020.
from Fig_TimeSeries_Pieplots import Fig_TimeSeries_Pieplots
Fig_TimeSeries_Pieplots(interpolatedyearSSP, interpolatedpopSSPs, percapitagdpSSPs, adjuated_AnnCO2Emit_gloLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_gloLevel, adjuated_CumCO2Emit_gloLevel)
################################################################################################################################################################
#"""


"""            #------------------------------------------------------->    figure here
################################################################################################################################################################
shreshold_list = np.arange(0,82,1)
ramprate_list  = [0, 0.01, 0.02, 0.04, 0.08]
# ramprate_list  = np.arange(0, 0.082, 0.01)
need_country   = 0
table_used = table_WB[-6] 

[original_AnnCO2Emit_ctyLevel, original_AnnCO2Emit_gloLevel, original_CumCO2Emit_ctyLevel, original_CumCO2Emit_gloLevel, 
 adjuated_AnnCO2Emit_ctyLevel, adjuated_AnnCO2Emit_gloLevel, adjuated_CumCO2Emit_ctyLevel, adjuated_CumCO2Emit_gloLevel,
 percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs
 ] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)

# Twp figures: 
# (1) Line plots showing additional warming;
# (2) Contour plots showing total warming.
from Fig_TempChange_lines import Fig_TempChange_lines
Fig_TempChange_lines(shreshold_list, adjuated_CumCO2Emit_gloLevel, original_CumCO2Emit_gloLevel, interpolatedpopSSPs, interpolatedyearSSP, percapitagdpSSPs)
# from Fig_TempChange_lines import plot_contour_plot
# plot_contour_plot(shreshold_list, ramprate_list, adjuated_CumCO2Emit_gloLevel)
################################################################################################################################################################
#"""


"""             #------------------------------------------------------->    figure here
################################################################################################################################################################
shreshold_list = np.array([0,   10,   20,   40])
ramprate_list  = np.array([0.0, 0.01, 0.02    ])
need_country   = 0

first_time = 0
if first_time == 1:
    table_used = table_WB[-6] 
    [original_AnnCO2Emit_ctyLevel_add0, original_AnnCO2Emit_gloLevel_add0, original_CumCO2Emit_ctyLevel_add0, original_CumCO2Emit_gloLevel_add0, 
    adjuated_AnnCO2Emit_ctyLevel_add0, adjuated_AnnCO2Emit_gloLevel_add0, adjuated_CumCO2Emit_ctyLevel_add0, adjuated_CumCO2Emit_gloLevel_add0,
    percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs
    ] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)
    print ('done 0')
    with open('add0.pickle', 'wb') as handle:
        pickle.dump([original_CumCO2Emit_gloLevel_add0,adjuated_CumCO2Emit_gloLevel_add0], handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    table_used = table_ctyL[-6]
    WB_case = table_WB[-6] 
    WB_inia = WB_case[1]
    table_used[1] = WB_inia
    [original_AnnCO2Emit_ctyLevel_add1, original_AnnCO2Emit_gloLevel_add1, original_CumCO2Emit_ctyLevel_add1, original_CumCO2Emit_gloLevel_add1, 
    adjuated_AnnCO2Emit_ctyLevel_add1, adjuated_AnnCO2Emit_gloLevel_add1, adjuated_CumCO2Emit_ctyLevel_add1, adjuated_CumCO2Emit_gloLevel_add1,
    percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs
    ] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)
    print ('done 1')
    with open('add1.pickle', 'wb') as handle:
        pickle.dump([original_CumCO2Emit_gloLevel_add1,adjuated_CumCO2Emit_gloLevel_add1], handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    table_used = table_ctyM[-6]
    WB_case = table_WB[-6] 
    WB_inia = WB_case[1]
    table_used[1] = WB_inia
    [original_AnnCO2Emit_ctyLevel_add2, original_AnnCO2Emit_gloLevel_add2, original_CumCO2Emit_ctyLevel_add2, original_CumCO2Emit_gloLevel_add2, 
    adjuated_AnnCO2Emit_ctyLevel_add2, adjuated_AnnCO2Emit_gloLevel_add2, adjuated_CumCO2Emit_ctyLevel_add2, adjuated_CumCO2Emit_gloLevel_add2,
    percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs
    ] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)
    print ('done 2')
    with open('add2.pickle', 'wb') as handle:
        pickle.dump([original_CumCO2Emit_gloLevel_add2,adjuated_CumCO2Emit_gloLevel_add2], handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    table_used = table_ctyH[-6]
    WB_case = table_WB[-6] 
    WB_inia = WB_case[1]
    table_used[1] = WB_inia
    [original_AnnCO2Emit_ctyLevel_add3, original_AnnCO2Emit_gloLevel_add3, original_CumCO2Emit_ctyLevel_add3, original_CumCO2Emit_gloLevel_add3, 
    adjuated_AnnCO2Emit_ctyLevel_add3, adjuated_AnnCO2Emit_gloLevel_add3, adjuated_CumCO2Emit_ctyLevel_add3, adjuated_CumCO2Emit_gloLevel_add3,
    percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs
    ] = future_projections_SameRate(gdpRawSSP, popRawSSP, countryList, table_used, shreshold_list, ramprate_list, need_country)
    print ('done 3')
    with open('add3.pickle', 'wb') as handle:
        pickle.dump([original_CumCO2Emit_gloLevel_add3,adjuated_CumCO2Emit_gloLevel_add3], handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    table_usedL = table_ctyL[-6]
    table_usedM = table_ctyM[-6]
    table_usedH = table_ctyH[-6]
    [original_AnnCO2Emit_ctyLevel_add4, original_AnnCO2Emit_gloLevel_add4, original_CumCO2Emit_ctyLevel_add4, original_CumCO2Emit_gloLevel_add4, 
    adjuated_AnnCO2Emit_ctyLevel_add4, adjuated_AnnCO2Emit_gloLevel_add4, adjuated_CumCO2Emit_ctyLevel_add4, adjuated_CumCO2Emit_gloLevel_add4,
    percapitagdpSSPs, interpolatedyearSSP, interpolatedgdpSSPs, interpolatedpopSSPs
    ] = future_projections_DiffRate(gdpRawSSP, popRawSSP, countryList, table_usedL, table_usedM, table_usedH, shreshold_list, ramprate_list, need_country)
    print ('done 4')
    with open('add4.pickle', 'wb') as handle:
        pickle.dump([original_CumCO2Emit_gloLevel_add4,adjuated_CumCO2Emit_gloLevel_add4], handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('add0.pickle', 'rb') as handle:
    original_CumCO2Emit_gloLevel_add0,adjuated_CumCO2Emit_gloLevel_add0 = pickle.load(handle)
with open('add1.pickle', 'rb') as handle:
    original_CumCO2Emit_gloLevel_add1,adjuated_CumCO2Emit_gloLevel_add1 = pickle.load(handle)
with open('add2.pickle', 'rb') as handle:
    original_CumCO2Emit_gloLevel_add2,adjuated_CumCO2Emit_gloLevel_add2 = pickle.load(handle)
with open('add3.pickle', 'rb') as handle:
    original_CumCO2Emit_gloLevel_add3,adjuated_CumCO2Emit_gloLevel_add3 = pickle.load(handle)
with open('add4.pickle', 'rb') as handle:
    original_CumCO2Emit_gloLevel_add4,adjuated_CumCO2Emit_gloLevel_add4 = pickle.load(handle)

from Fig_uncertainty_range import Fig_uncertainty_range
Fig_uncertainty_range(original_CumCO2Emit_gloLevel_add0, adjuated_CumCO2Emit_gloLevel_add0,
                      original_CumCO2Emit_gloLevel_add1, adjuated_CumCO2Emit_gloLevel_add1,
                      original_CumCO2Emit_gloLevel_add2, adjuated_CumCO2Emit_gloLevel_add2,
                      original_CumCO2Emit_gloLevel_add3, adjuated_CumCO2Emit_gloLevel_add3,
                      original_CumCO2Emit_gloLevel_add4, adjuated_CumCO2Emit_gloLevel_add4,
                      shreshold_list, ramprate_list)
################################################################################################################################################################
#"""