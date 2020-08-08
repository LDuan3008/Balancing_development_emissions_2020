import numpy as np
import MV2 as MV
import cdms2 as cdms
import vcs
from matplotlib import pyplot as plt

"""
def cal_additional_warming(org, red):
    new_red  = red[:,:,:,-1] - red[:,:,:,1] + 515*3.667  #(threshold, ramprate, ssp)
    #new_org  = org[:,-1]     - org[:,1]     + 515*3.667  #(ssp)
    additional_emissions_compare_to_AllReduce = new_red - new_red[0]
    additional_warming = additional_emissions_compare_to_AllReduce * 2. / 3667.
    return additional_warming
"""

def cal_additional_warming(org, red):
    new_red  = red[:,:,:,-1] - red[:,:,:,1] + 515*3.667  #(threshold, ramprate, ssp)
    #new_org  = org[:,-1]     - org[:,1]     + 515*3.667  #(ssp)
    additional_emissions_compare_to_AllReduce = new_red
    additional_warming = additional_emissions_compare_to_AllReduce * 2. / 3667.
    return additional_warming


def Fig_uncertainty_range(org0, red0, org1, red1, org2, red2, org3, red3, org4, red4, shreshold_list, ramprate_list):    
    add0 = cal_additional_warming(org0, red0)
    add1 = cal_additional_warming(org1, red1)
    add2 = cal_additional_warming(org2, red2)
    add3 = cal_additional_warming(org3, red3)
    add4 = cal_additional_warming(org4, red4)
    
    def get_result_array(idx1, idx2, idx3):
        result_array = [add0[idx1,idx2,idx3],
                        add1[idx1,idx2,idx3],
                        add2[idx1,idx2,idx3],
                        add3[idx1,idx2,idx3],
                        add4[idx1,idx2,idx3]]
        return result_array
    
    def all_SSPs_array(idx1,idx2):
        return np.c_[get_result_array(idx1,idx2,0), np.zeros(5), 
                     get_result_array(idx1,idx2,1), np.zeros(5), 
                     get_result_array(idx1,idx2,2), np.zeros(5),
                     get_result_array(idx1,idx2,3), np.zeros(5), 
                     get_result_array(idx1,idx2,4)]
    
    thr0red1, thr1red1, thr2red1, thr3red1 = all_SSPs_array(0,0), all_SSPs_array(1,0), all_SSPs_array(2,0), all_SSPs_array(3,0)
    thr0red2, thr1red2, thr2red2, thr3red2 = all_SSPs_array(0,1), all_SSPs_array(1,1), all_SSPs_array(2,1), all_SSPs_array(3,1)
    thr0red3, thr1red3, thr2red3, thr3red3 = all_SSPs_array(0,2), all_SSPs_array(1,2), all_SSPs_array(2,2), all_SSPs_array(3,2)
    
    ax1 = plt.subplot(131)
    ax1.boxplot(thr0red1, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='orange'), medianprops=dict(linewidth='0.5'))
    ax1.boxplot(thr1red1, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='firebrick'), medianprops=dict(linewidth='0.5'))
    ax1.boxplot(thr2red1, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='royalblue'), medianprops=dict(linewidth='0.5'))
    ax1.boxplot(thr3red1, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='green'), medianprops=dict(linewidth='0.5'))
    
    ax2 = plt.subplot(132, sharex=ax1, sharey=ax1)
    ax2.boxplot(thr0red2, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='orange'), medianprops=dict(linewidth='0.5'))
    ax2.boxplot(thr1red2, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='firebrick'), medianprops=dict(linewidth='0.5'))
    ax2.boxplot(thr2red2, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='royalblue'), medianprops=dict(linewidth='0.5'))
    ax2.boxplot(thr3red2, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='green'), medianprops=dict(linewidth='0.5'))
    
    ax3 = plt.subplot(133, sharex=ax1, sharey=ax1)
    ax3.boxplot(thr0red3, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='orange'), medianprops=dict(linewidth='0.5'))
    ax3.boxplot(thr1red3, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='firebrick'), medianprops=dict(linewidth='0.5'))
    ax3.boxplot(thr2red3, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='royalblue'), medianprops=dict(linewidth='0.5'))
    ax3.boxplot(thr3red3, patch_artist=True, showfliers=True, showcaps=True, boxprops=dict(facecolor='green'), medianprops=dict(linewidth='0.5'))
    
    plt.xlim(0, 10)
    plt.xticks( np.arange(5)*2+1, ('SSP1', 'SSP2', 'SSP3', 'SSP4', 'SSP5'))
    #plt.show()
    plt.savefig('test_uncert.ps', transparent=True)
    plt.clf()