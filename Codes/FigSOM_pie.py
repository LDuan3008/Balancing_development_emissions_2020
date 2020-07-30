import numpy as np
from matplotlib import pyplot as plt

def plot_pie(interpolatedyearSSP, annualco2Emi, annualco2Emi_org, cumulco2Emi_org, cumulco2Emi, interpolatedpopSSPs, percapitagdpSSPs):    
    select_case_NOC = cumulco2Emi_org[4,-1] - cumulco2Emi_org[4,9]
    select_case_00  = cumulco2Emi[0,1,4,-1] - cumulco2Emi[0,1,4,9]
    select_case_10  = cumulco2Emi[1,1,4,-1] - cumulco2Emi[1,1,4,9]
    select_case_20  = cumulco2Emi[2,1,4,-1] - cumulco2Emi[2,1,4,9]
    select_case_40  = cumulco2Emi[3,1,4,-1] - cumulco2Emi[3,1,4,9]
    select_case_80  = cumulco2Emi[4,1,4,-1] - cumulco2Emi[4,1,4,9]
    
    per_80 = select_case_NOC -select_case_80
    per_40 = select_case_80  -select_case_40
    per_20 = select_case_40  -select_case_20
    per_10 = select_case_20  -select_case_10
    per_00 = select_case_10  -select_case_00
    #per_no = select_case_00
    
    pie = [per_00, per_10, per_20, per_40, per_80]
    explode = (0, 0, 0, 0, 0)
    plt.pie(pie, explode=explode, shadow=False, startangle=90, autopct='%1.3f%%', counterclock=False)
    plt.show()
    # plt.savefig('pieS5.ps')
    plt.clf()
    
    
    