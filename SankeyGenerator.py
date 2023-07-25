# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:33:40 2023

@author: jjs78
"""
### IMPORT NECESSARY MODULES ###
import csv
import numpy as np
#from floweaver import *
from ipysankeywidget import SankeyWidget
from ipywidgets import Layout


### SANKEY GENERATION FUNCTION FROM RICK LUPTON ###
#change dimensions of outputted Sankey
layout = Layout(width="1600", height="900")
#define function to generate Sankey
def sankey(margin_top=0, **value):
    """Show SankeyWidget with default values for size and margins"""
    return SankeyWidget(layout=layout,
                        margins=dict(top=margin_top, bottom=40, left=160, right=160),
                        **value)

###DATA GATHERING FUNCTION###
def data(Country,Year):
    '''
    Function to gather data for constructing 
    Sankey diagrams
    
    Inputs: 
        Country - name of country from IEA list
        Year - year between 1960 and 2019
        
    Returns values to be used for construction of
    Sankey diagrams for the given year and country
    
    '''
    #User inputs
    Country=Country
    Year=Year
    
    #set names of flows to be searched in csv (IEA Flow Short Names from World Balance Documentation)
    source=['TES', 'TRANSFER', 'STATDIFF', 'MAINELEC', 'AUTOELEC', 'MAINCHP','AUTOCHP','MAINHEAT','AUTOHEAT','THEAT','TBOILER',
           'TELE','TBLASTFUR','TGASWKS','TCOKEOVS','TPATFUEL','TBKB','TREFINER','TPETCHEM','LIQUEFAC','TNONSPEC','OWNUSE',
           'DISTLOSS','TFC', 'NONENUSE']
    consumption=['TOTIND', 'MINING', 'CONSTRUC', 'MANUFACT', 'IRONSTL', 'CHEMICAL', 'NONFERR', 'NONMET', 'TRANSEQ', 'MACHINE',
                 'FOODPRO', 'PAPERPRO', 'WOODPRO', 'TEXTILES', 'INONSPEC', 'TOTTRANS', 'WORLDAV', 'DOMESAIR', 'ROAD', 'RAIL',
                 'PIPELINE', 'WORLDMAR', 'DOMESNAV', 'TRNONSPE', 'RESIDENT', 'COMMPUB', 'AGRICULT', 'FISHING', 'ONONSPEC']
    
    #set up empty arrays for energy values from IEA data
    IEATES=np.zeros([9,len(source)]) #array for energy supply
    IEATFC=np.zeros([9,29]) #array for energy consumption
    electricity=np.zeros(29) #array for electricity consumption
    heat=np.zeros(29) #array for heat consumption
    
    #search through csv for required data for flows specified above and products as stated below
    f1=open('Balance1.csv') #open IEA world balance .csv file downloaded from OECD iLibrary (split into 5 smaller files for easier storage)
    temp1=csv.reader(f1)
    for row in temp1: #scan through all rows for required data
        try:
            if row[0]=='TJ': #get values in TJ
                if row[3]==Country: #for country as specified
                    if row[8]==Year: #year as specified
                        for x in source: #flow from 'source' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATES[0][source.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATES[1][source.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATES[2][source.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATES[3][source.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATES[4][source.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATES[5][source.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATES[6][source.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATES[7][source.index(x)]=row[10]
                        for x in consumption: #flow from 'consumption' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATFC[0][consumption.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATFC[1][consumption.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATFC[2][consumption.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATFC[3][consumption.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATFC[4][consumption.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATFC[5][consumption.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATFC[6][consumption.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATFC[7][consumption.index(x)]=row[10]
                                elif row[4]=='ELECTR': #product=electricity
                                    electricity[consumption.index(x)]=row[10]
                                elif row[4]=='HEAT': #product=heat
                                    heat[consumption.index(x)]=row[10]
        except ValueError: #to avoid errors where data is not available
            if Country!='World':
                if row[6]=='WORLDAV':
                    pass #pass since there will be only be data when country=world
                elif row[6]=='WORLDMAR':
                    pass #pass since there will be only be data when country=world
                else:
                    print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])
            else:
                print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])
                
    f2=open('Balance2.csv') #open IEA world balance .csv file downloaded from OECD iLibrary
    temp2=csv.reader(f2)
    for row in temp2: #scan through all rows for required data
        try:
            if row[0]=='TJ': #get values in TJ
                if row[3]==Country: #for country as specified
                    if row[8]==Year: #year as specified
                        for x in source: #flow from 'source' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATES[0][source.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATES[1][source.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATES[2][source.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATES[3][source.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATES[4][source.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATES[5][source.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATES[6][source.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATES[7][source.index(x)]=row[10]
                        for x in consumption: #flow from 'consumption' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATFC[0][consumption.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATFC[1][consumption.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATFC[2][consumption.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATFC[3][consumption.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATFC[4][consumption.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATFC[5][consumption.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATFC[6][consumption.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATFC[7][consumption.index(x)]=row[10]
                                elif row[4]=='ELECTR': #product=electricity
                                    electricity[consumption.index(x)]=row[10]
                                elif row[4]=='HEAT': #product=heat
                                    heat[consumption.index(x)]=row[10]
        except ValueError: #to avoid errors where data is not available
            if Country!='World':
                if row[6]=='WORLDAV':
                    pass #pass since there will be only be data when country=world
                elif row[6]=='WORLDMAR':
                    pass #pass since there will be only be data when country=world
                else:
                    print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])
            else:
                print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])
    
    f3=open('Balance3.csv') #open IEA world balance .csv file downloaded from OECD iLibrary
    temp3=csv.reader(f3)
    for row in temp3: #scan through all rows for required data
        try:
            if row[0]=='TJ': #get values in TJ
                if row[3]==Country: #for country as specified
                    if row[8]==Year: #year as specified
                        for x in source: #flow from 'source' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATES[0][source.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATES[1][source.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATES[2][source.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATES[3][source.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATES[4][source.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATES[5][source.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATES[6][source.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATES[7][source.index(x)]=row[10]
                        for x in consumption: #flow from 'consumption' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATFC[0][consumption.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATFC[1][consumption.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATFC[2][consumption.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATFC[3][consumption.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATFC[4][consumption.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATFC[5][consumption.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATFC[6][consumption.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATFC[7][consumption.index(x)]=row[10]
                                elif row[4]=='ELECTR': #product=electricity
                                    electricity[consumption.index(x)]=row[10]
                                elif row[4]=='HEAT': #product=heat
                                    heat[consumption.index(x)]=row[10]
        except ValueError: #to avoid errors where data is not available
            if Country!='World':
                if row[6]=='WORLDAV':
                    pass #pass since there will be only be data when country=world
                elif row[6]=='WORLDMAR':
                    pass #pass since there will be only be data when country=world
                else:
                    print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])
            else:
                print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])

    f4=open('Balance4.csv') #open IEA world balance .csv file downloaded from OECD iLibrary
    temp4=csv.reader(f4)
    for row in temp4: #scan through all rows for required data
        try:
            if row[0]=='TJ': #get values in TJ
                if row[3]==Country: #for country as specified
                    if row[8]==Year: #year as specified
                        for x in source: #flow from 'source' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATES[0][source.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATES[1][source.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATES[2][source.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATES[3][source.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATES[4][source.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATES[5][source.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATES[6][source.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATES[7][source.index(x)]=row[10]
                        for x in consumption: #flow from 'consumption' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATFC[0][consumption.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATFC[1][consumption.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATFC[2][consumption.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATFC[3][consumption.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATFC[4][consumption.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATFC[5][consumption.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATFC[6][consumption.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATFC[7][consumption.index(x)]=row[10]
                                elif row[4]=='ELECTR': #product=electricity
                                    electricity[consumption.index(x)]=row[10]
                                elif row[4]=='HEAT': #product=heat
                                    heat[consumption.index(x)]=row[10]
        except ValueError: #to avoid errors where data is not available
            if Country!='World':
                if row[6]=='WORLDAV':
                    pass #pass since there will be only be data when country=world
                elif row[6]=='WORLDMAR':
                    pass #pass since there will be only be data when country=world
                else:
                    print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])
            else:
                print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])
    
    f5=open('Balance5.csv') #open IEA world balance .csv file downloaded from OECD iLibrary
    temp5=csv.reader(f5)
    for row in temp5: #scan through all rows for required data
        try:
            if row[0]=='TJ': #get values in TJ
                if row[3]==Country: #for country as specified
                    if row[8]==Year: #year as specified
                        for x in source: #flow from 'source' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATES[0][source.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATES[1][source.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATES[2][source.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATES[3][source.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATES[4][source.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATES[5][source.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATES[6][source.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATES[7][source.index(x)]=row[10]
                        for x in consumption: #flow from 'consumption' list
                            if row[6]==x:
                                if row[4]=='MTOTOIL': #product=primary and secondary oil
                                    IEATFC[0][consumption.index(x)]=row[10]
                                elif row[4]=='NATGAS': #product=natural gas
                                    IEATFC[1][consumption.index(x)]=row[10]
                                elif row[4]=='NUCLEAR': #product=nuclear
                                    IEATFC[2][consumption.index(x)]=row[10]
                                elif row[4]=='HYDRO': #product=hydro
                                    IEATFC[3][consumption.index(x)]=row[10]
                                elif row[4]=='GEOTHERM': #product=geothermal
                                    IEATFC[4][consumption.index(x)]=row[10]
                                elif row[4]=='SOLWIND': #product=solar/wind/other
                                    IEATFC[5][consumption.index(x)]=row[10]
                                elif row[4]=='COMRENEW': #product=biofuels and waste
                                    IEATFC[6][consumption.index(x)]=row[10]
                                elif row[4]=='MTOTSOLID': #product=coal, peat and oil shale
                                    IEATFC[7][consumption.index(x)]=row[10]
                                elif row[4]=='ELECTR': #product=electricity
                                    electricity[consumption.index(x)]=row[10]
                                elif row[4]=='HEAT': #product=heat
                                    heat[consumption.index(x)]=row[10]
        except ValueError: #to avoid errors where data is not available
            if Country!='World':
                if row[6]=='WORLDAV':
                    pass #pass since there will be only be data when country=world
                elif row[6]=='WORLDMAR':
                    pass #pass since there will be only be data when country=world
                else:
                    print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])
            else:
                print('The following data was unavailable: \n Product =', row[5], '\n Flow =', row[7])
    
    return IEATES,IEATFC,electricity,heat,Country,Year

###ALLOCATION SANKEY GENERATOR FUNCTION###    
def allocation(IEATES,IEATFC,electricity,heat,Country,Year,Exergy):
    '''
    Function to return an allocation Sankey diagram
    
    Inputs: 
        IEATES - Energy Supply Values from IEA
        IEATFC - Energy Consumption Values from IEA
        electricity - Electricity Consumption values from IEA
        heat - Heat Consumption values from IEA
        Country - name of country from IEA list
        Year - year between 1960 and 2019
        Exergy - Produce Diagram in Exergy or Energy Values
        
    Returns an allocation Sankey diagram for the given 
    year and country
    
    '''
    
    #convert supply to exergy values and combine oil and renewable products (exergy factors from https://doi.org/10.3390/en9090707)
    if Exergy=='Exergy':                          
        exergy=np.array([1.04*IEATES[0],1.03*IEATES[1],0.95*IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],1.13*IEATES[6],1.06*IEATES[7]])
        exergy_h=0.17*heat
    elif Exergy=='Energy':
        exergy=np.array([IEATES[0],IEATES[1],IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],IEATES[6],IEATES[7]])
        exergy_h=heat
    
    #calculate total electricity generation and direct fuel use
    tpes=np.zeros(len(exergy))
    losses=np.zeros(len(exergy))
    tfc=np.zeros(len(exergy))
    nonenergy=np.zeros(len(exergy))
    egeneration=np.zeros(len(exergy))
    hgeneration=np.zeros(len(exergy))
    for i in range (0,len(exergy)):
        tpes[i]=exergy[i][0]
        #combine all losses
        for j in range(1,3):
            losses[i]=losses[i]+exergy[i][j] 
        for j in range(9,23):
            losses[i]=losses[i]+exergy[i][j]
        tfc[i]=exergy[i][23]
        nonenergy[i]=exergy[i][24]
        #combine electriciy and heat generation from electricity, heating and CHP plants
        for j in range(3,5):
            egeneration[i]=egeneration[i]+exergy[i][j]
        for j in range(5,7):
            egeneration[i]=egeneration[i]+0.89*exergy[i][j]
            hgeneration[i]=hgeneration[i]+0.11*exergy[i][j]
        for j in range(7,9):
            hgeneration[i]=hgeneration[i]+exergy[i][j]
    
    dfu_used=tfc-nonenergy #total fuel used directly is total final consumption of fuel - non-energy use
    elec_used=-egeneration-hgeneration #total fuel used for electricity generation is combination of fuels to all plants from above (- sign to yield +ve values)
    
    #losses split proportionally between dfu & electricity generation
    dfu_losses=np.zeros(len(tpes))
    elec_losses=np.zeros(len(tpes))
    for i in range(len(tpes)):
        if tpes[i]+losses[i]==0: #to avoid divide zero errors
            dfu_losses[i]=0
            elec_losses[i]=0
        else: #- signs as losses[i] have -ve values
            dfu_losses[i]=-dfu_used[i]*(losses[i]/(tpes[i]+losses[i])) 
            elec_losses[i]=-elec_used[i]*(losses[i]/(tpes[i]+losses[i]))
    #convert from TJ to PJ
    direct_fuel_use=(dfu_used+dfu_losses)/(10**3)
    electricity_generation=(elec_used+elec_losses)/(10**3)
    
    #convert consumption to exergy values and combine oil and renewable products
    exergycons=np.array([1.04*IEATFC[0],1.03*IEATFC[1],0.95*IEATFC[2],IEATFC[3]+IEATFC[4]+IEATFC[5],1.11*IEATFC[6],1.06*IEATFC[7]])
    
    #calculate direct fuel use energy to industry
    industry=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        industry[i]=exergycons[i][0]
    industry=industry/(10**3)
    
    #scale to include losses
    for i in range(len(dfu_used)):
        if dfu_used[i]!=0:
            industry[i]=industry[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            
    #calculate total electricity (& heat) 
    totelec=electricity[0]+electricity[15]+electricity[24]+electricity[25]+electricity[26]+electricity[27]+electricity[28]
    totheat=exergy_h[0]+exergy_h[15]+exergy_h[24]+exergy_h[25]+exergy_h[26]+exergy_h[27]+exergy_h[28]
    
    if (totelec+totheat)!=0: #to avoid divide zero errors
        totelec_=totelec/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
        totheat_=totheat/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
    else:
        totelec_=0
        totheat_=0
        
    #scale electricity (& heat) flow to industry only
    if totelec!=0:
        elec_ind=(electricity[0]/totelec)*totelec_
    else:
        elec_ind=0
        
    if totheat!=0:
        heat_ind=(exergy_h[0]/totheat)*totheat_
    else:
        heat_ind=0
        
    #calculate energy to electricity from each fuel for industry
    totelecind=np.zeros(len(exergycons))
    totheatind=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecind[i]=(elec_ind/np.sum(electricity_generation))*electricity_generation[i]
            totheatind[i]=(heat_ind/np.sum(electricity_generation))*electricity_generation[i]
            
    #calculate direct use for industrial sub-sectors
    exergyInd=np.zeros((len(exergycons),29))
    for j in range(0,len(exergycons)):
        for i in range(0,29):
            if dfu_used[j]!=0: #to avoid divide zero errors
                exergyInd[j][i]=exergycons[j][i]*direct_fuel_use[j]/(dfu_used[j]/10**3)
                
    steel=np.zeros(len(exergycons))
    aluminium=np.zeros(len(exergycons))
    machinery=np.zeros(len(exergycons))
    mineral=np.zeros(len(exergycons))
    chemical=np.zeros(len(exergycons))
    paper=np.zeros(len(exergycons))
    food=np.zeros(len(exergycons))
    other=np.zeros(len(exergycons))
    
    for i in range(0,len(exergycons)):
        steel[i]=exergyInd[i][4]/(10**3)
        aluminium[i]=exergyInd[i][6]/(10**3)
        machinery[i]=(exergyInd[i][8]+exergyInd[i][9])/(10**3)
        mineral[i]=exergyInd[i][7]/(10**3)
        chemical[i]=exergyInd[i][5]/(10**3)
        paper[i]=(exergyInd[i][11]+exergyInd[i][12])/(10**3)
        food[i]=exergyInd[i][10]/(10**3)
        other[i]=(exergyInd[i][1]+exergyInd[i][2]+exergyInd[i][13]+exergyInd[i][14])/(10**3)
        
    #calculate electricity to industrial sub-sectors  
    if totelec!=0:
        elec_steel=(electricity[4]/totelec)*totelec_
        elec_aluminium=(electricity[6]/totelec)*totelec_
        elec_machinery=((electricity[8]+electricity[9])/totelec)*totelec_
        elec_mineral=(electricity[7]/totelec)*totelec_
        elec_chemical=(electricity[5]/totelec)*totelec_
        elec_paper=((electricity[11]+electricity[12])/totelec)*totelec_
        elec_food=(electricity[10]/totelec)*totelec_
        elec_other=((electricity[1]+electricity[2]+electricity[13]+electricity[14])/totelec)*totelec_
    else:
        elec_steel=0
        elec_aluminium=0
        elec_machinery=0
        elec_mineral=0
        elec_chemical=0
        elec_paper=0
        elec_food=0
        elec_other=0
        
    #calculate heat to industrial sub-sectors  
    if totheat!=0:
        heat_steel=(exergy_h[4]/totheat)*totheat_
        heat_aluminium=(exergy_h[6]/totheat)*totheat_
        heat_machinery=((exergy_h[8]+exergy_h[9])/totheat)*totheat_
        heat_mineral=(exergy_h[7]/totheat)*totheat_
        heat_chemical=(exergy_h[5]/totheat)*totheat_
        heat_paper=((exergy_h[11]+exergy_h[12])/totheat)*totheat_
        heat_food=(exergy_h[10]/totheat)*totheat_
        heat_other=((exergy_h[1]+exergy_h[2]+exergy_h[13]+exergy_h[14])/totheat)*totheat_
    else:
        heat_steel=0
        heat_aluminium=0
        heat_machinery=0
        heat_mineral=0
        heat_chemical=0
        heat_paper=0
        heat_food=0
        heat_other=0
        
    #append electricity and heat values to sub-sector fuel consumption arrays
    steelfull=np.append(steel, [elec_steel, heat_steel])
    aluminiumfull=np.append(aluminium, [elec_aluminium, heat_aluminium])
    machineryfull=np.append(machinery, [elec_machinery, heat_machinery])
    mineralfull=np.append(mineral, [elec_mineral, heat_mineral])
    chemicalfull=np.append(chemical, [elec_chemical, heat_chemical])
    paperfull=np.append(paper, [elec_paper, heat_paper])
    foodfull=np.append(food, [elec_food, heat_food])
    otherfull=np.append(other, [elec_other, heat_other])
    
    #define allocation matrices, based on US industry data - used to assign fuels to passive systems below
    #rows are passive systems, columns are fuels (oil, gas, nuclear, renewables, biomass, coal, electricity, heat))
    steel_mat = np.array([[0.00  , 0.10  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.39  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 1.00  , 1.00  , 0.53  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.03  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#appliance
                         [1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    al_mat = np.array([[0.00  , 0.13  , 1.00  , 0.00  , 0.13  , 0.13  , 0.01  , 0.00  ],#steam
                         [0.25  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.24  , 0.00  ],#driven
                         [0.25  , 0.76  , 0.00  , 0.00  , 0.76  , 0.76  , 0.65  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.03  , 0.00  ],#light
                         [0.00  , 0.09  , 0.00  , 1.00  , 0.09  , 0.09  , 0.04  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.02  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                      ])
    
    mach_mat = np.array([[0.15  , 0.16  , 1.00  , 0.00  , 0.16  , 0.16  , 0.01  , 0.00  ],#steam
                         [0.14  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.49  , 0.00  ],#driven
                         [0.07  , 0.45  , 0.00  , 0.00  , 0.45  , 0.45  , 0.16  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.11  , 0.00  ],#light
                         [0.14  , 0.35  , 0.00  , 1.00  , 0.35  , 0.35  , 0.19  , 1.00  ],#spaceheat
                         [0.00  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.03  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])
    
    min_mat = np.array([[0.00  , 0.03  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.38  , 0.08  , 0.00  , 0.00  , 0.10  , 0.10  , 0.60  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 0.90  , 0.90  , 0.28  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.62  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                       ])
    
    chem_mat = np.array([[0.50  , 0.52  , 1.00  , 0.00  , 0.87  , 0.87  , 0.01  , 0.00  ],#steam
                         [0.00  , 0.04  , 0.00  , 0.00  , 0.00  , 0.00  , 0.63  , 0.00  ],#driven
                         [0.10  , 0.41  , 0.00  , 0.00  , 0.13  , 0.13  , 0.25  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.02  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.40  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                        ])                 
    
    paper_mat = np.array([[0.36  , 0.63  , 1.00  , 0.00  , 0.98  , 0.98  , 0.04  , 0.00  ],#steam
                         [0.04  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.78  , 0.00  ],#driven
                         [0.08  , 0.30  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.06  , 1.00  ],#spaceheat
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.52  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    food_mat = np.array([[0.59  , 0.59  , 1.00  , 0.00  , 0.79  , 0.79  , 0.03  , 0.00  ],#steam
                         [0.00  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.69  , 0.00  ],#driven
                         [0.00  , 0.27  , 0.00  , 0.00  , 0.21  , 0.21  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#light
                         [0.08  , 0.08  , 0.00  , 1.00  , 0.00  , 0.00  , 0.11  , 1.00  ],#spaceheat
                         [0.08  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.25  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])
    
    other_mat = np.array([[0.13  , 0.34  , 1.00  , 0.00  , 1.00  , 1.00  , 0.01  , 0.00  ],#steam
                         [0.13  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.73  , 0.00  ],#driven
                         [0.71  , 0.61  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.06  , 0.00  ],#light
                         [0.00  , 0.04  , 0.00  , 1.00  , 0.00  , 0.00  , 0.09  , 1.00  ],#spaceheat
                         [0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    #import data on share of steel from EAF
    import pandas as pd
    df=pd.read_csv('SteelShares2023.csv')
    try:
        EAF=float(df['EAF'][df['Country'] == Country].values[0])
    except:
        EAF=float(df['EAF'][df['Country'] == 'World'].values[0])
        
    #calculate new allocation matrices for steel, based on share of EAF
    x=(442.01*EAF)/((442.01*EAF)+(4128.05*(1-EAF)))
    z1=0.943*x+0.045*(1-x)
    z2=0.928*(1-x)
    z3=0.057*x+0.027*(1-x)
    gamma=0
        
    if x==1:
        if electricity[4]!=0:
            gammaprime=(0.02*IEATFC[1][4]/electricity[4])*(z1/z3)
            steel_mat[2][6]=0.4+0.6*gammaprime
            steel_mat[1][6]=0.5*(1-gammaprime)
            steel_mat[3][6]=0.04*(1-gammaprime)
            steel_mat[4][6]=0.05*(1-gammaprime)
            steel_mat[5][6]=0.01*(1-gammaprime)
    else:
        if electricity[4]!=0:
            gamma=(IEATFC[7][4]/electricity[4])*(z1/z2)
            steel_mat[2][6]=0.4+0.6*gamma
            steel_mat[1][6]=0.5*(1-gamma)
            steel_mat[3][6]=0.04*(1-gamma)
            steel_mat[4][6]=0.05*(1-gamma)
            steel_mat[5][6]=0.01*(1-gamma)
        if IEATFC[1][4]!=0:
            delta=(IEATFC[7][4]/IEATFC[1][4])*(z3/z2)
            steel_mat[2][1]=0.83+0.17*delta
            steel_mat[0][1]=0.1*(1-delta)
            steel_mat[1][1]=0.01*(1-delta)
            steel_mat[4][1]=0.05*(1-delta)
            steel_mat[5][1]=0.01*(1-delta)
            
    #use matrix multiplication to assign fuel to each passive system
    steel_ps=np.zeros(7)
    al_ps=np.zeros(7)
    mach_ps=np.zeros(7)
    min_ps=np.zeros(7)
    chem_ps=np.zeros(7)
    paper_ps=np.zeros(7)
    food_ps=np.zeros(7)
    other_ps=np.zeros(7)
    for i in range(0,len(steelfull)):
        for j in range(0,7):
            steel_ps[j]=steel_ps[j]+steelfull[i]*steel_mat[j][i]
            al_ps[j]=al_ps[j]+aluminiumfull[i]*al_mat[j][i]
            mach_ps[j]=mach_ps[j]+machineryfull[i]*mach_mat[j][i]
            min_ps[j]=min_ps[j]+mineralfull[i]*min_mat[j][i]
            chem_ps[j]=chem_ps[j]+chemicalfull[i]*chem_mat[j][i]
            paper_ps[j]=paper_ps[j]+paperfull[i]*paper_mat[j][i]
            food_ps[j]=food_ps[j]+foodfull[i]*food_mat[j][i]
            other_ps[j]=other_ps[j]+otherfull[i]*other_mat[j][i]
            
    #define matrices for assigning fuels to conversion devices
    #rows are purposes of converson devices, columns are industries (steel, aluminium, machinery, mineral, chemical, paper, food, other)
    oil_mat = np.array([[1.00, 0.75, 0.64, 1.00, 0.40, 0.56, 0.25, 0.13],#motion
                       [0.00, 0.25, 0.36, 0.00, 0.60, 0.44, 0.67, 0.84],#heat
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.08, 0.03]])#appliance
    
    gas_mat = np.array([[steel_mat[1][1]+steel_mat[6][1], 0.01, 0.02, 0.08, 0.04, 0.02, 0.03, 0.01],#motion
                       [steel_mat[0][1]+steel_mat[2][1]+steel_mat[4][1], 0.98, 0.96, 0.91, 0.95, 0.98, 0.94, 0.99],#heat
                       [steel_mat[3][1], 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [steel_mat[5][1], 0.01, 0.02, 0.01, 0.01, 0.00, 0.03, 0.00]])#appliance
    
    coal_mat = np.array([[0.00, 0.01, 0.02, 0.10, 0.00, 0.02, 0.00, 0.00],#motion
                        [1.00, 0.98, 0.96, 0.90, 1.00, 0.98, 1.00, 1.00],#heat
                        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                        [0.00, 0.01, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00]])#appliance
    
    elec_mat = np.array([[steel_mat[1][6]+steel_mat[6][6], 0.25, 0.50, 0.60, 0.63, 0.78, 0.70, 0.73],#motion
                        [steel_mat[0][6]+steel_mat[2][6]+steel_mat[4][6], 0.70, 0.36, 0.33, 0.31, 0.15, 0.19, 0.19],#heat
                        [steel_mat[3][6], 0.03, 0.11, 0.05, 0.04, 0.05, 0.09, 0.06],#light
                        [steel_mat[5][6], 0.02, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02]])#appliance
    
    #use matrix multiplication to assign energy to each conversion device
    oil_cd=np.zeros(4)
    gas_cd=np.zeros(4)
    biomass_cd=np.zeros(4)
    coal_cd=np.zeros(4)
    elec_cd=np.zeros(4)
    for i in range(0,4):
        oil_cd[i]=oil_mat[i][0]*steelfull[0]+oil_mat[i][1]*aluminiumfull[0]+oil_mat[i][2]*machineryfull[0]+oil_mat[i][3]*mineralfull[0]+oil_mat[i][4]*chemicalfull[0]+oil_mat[i][5]*paperfull[0]+oil_mat[i][6]*foodfull[0]+oil_mat[i][7]*otherfull[0]
        gas_cd[i]=gas_mat[i][0]*steelfull[1]+gas_mat[i][1]*aluminiumfull[1]+gas_mat[i][2]*machineryfull[1]+gas_mat[i][3]*mineralfull[1]+gas_mat[i][4]*chemicalfull[1]+gas_mat[i][5]*paperfull[1]+gas_mat[i][6]*foodfull[1]+gas_mat[i][7]*otherfull[1]
        biomass_cd[i]=coal_mat[i][0]*steelfull[4]+coal_mat[i][1]*aluminiumfull[4]+coal_mat[i][2]*machineryfull[4]+coal_mat[i][3]*mineralfull[4]+coal_mat[i][4]*chemicalfull[4]+coal_mat[i][5]*paperfull[4]+coal_mat[i][6]*foodfull[4]+coal_mat[i][7]*otherfull[4]
        coal_cd[i]=coal_mat[i][0]*steelfull[5]+coal_mat[i][1]*aluminiumfull[5]+coal_mat[i][2]*machineryfull[5]+coal_mat[i][3]*mineralfull[5]+coal_mat[i][4]*chemicalfull[5]+coal_mat[i][5]*paperfull[5]+coal_mat[i][6]*foodfull[5]+coal_mat[i][7]*otherfull[5]
        elec_cd[i]=elec_mat[i][0]*steelfull[6]+elec_mat[i][1]*aluminiumfull[6]+elec_mat[i][2]*machineryfull[6]+elec_mat[i][3]*mineralfull[6]+elec_mat[i][4]*chemicalfull[6]+elec_mat[i][5]*paperfull[6]+elec_mat[i][6]*foodfull[6]+elec_mat[i][7]*otherfull[6]
    
    #assumed that all nuclear, renewable and direct heat contributes to heat
    nuclear_cd=steelfull[2]+aluminiumfull[2]+machineryfull[2]+mineralfull[2]+chemicalfull[2]+paperfull[2]+foodfull[2]+otherfull[2]
    renewable_cd=steelfull[3]+aluminiumfull[3]+machineryfull[3]+mineralfull[3]+chemicalfull[3]+paperfull[3]+foodfull[3]+otherfull[3]
    heat_cd=steelfull[7]+aluminiumfull[7]+machineryfull[7]+mineralfull[7]+chemicalfull[7]+paperfull[7]+foodfull[7]+otherfull[7]
    
    #values for Sankey labels
    DFU='DFU ({:.0f}PJ)'.format(np.sum(industry))
    TEG='TEG ({:.0f}PJ)'.format(np.sum(totelecind)+np.sum(totheatind))
    PrimEng=np.sum(industry)+np.sum(totelecind)+np.sum(totheatind)
    
    #combine passive system values
    steam=steel_ps[0]+al_ps[0]+mach_ps[0]+min_ps[0]+chem_ps[0]+paper_ps[0]+food_ps[0]+other_ps[0]
    driven=steel_ps[1]+al_ps[1]+mach_ps[1]+min_ps[1]+chem_ps[1]+paper_ps[1]+food_ps[1]+other_ps[1]
    furnace=steel_ps[2]+al_ps[2]+mach_ps[2]+min_ps[2]+chem_ps[2]+paper_ps[2]+food_ps[2]+other_ps[2]
    light=steel_ps[3]+al_ps[3]+mach_ps[3]+min_ps[3]+chem_ps[3]+paper_ps[3]+food_ps[3]+other_ps[3]
    spaceheat=steel_ps[4]+al_ps[4]+mach_ps[4]+min_ps[4]+chem_ps[4]+paper_ps[4]+food_ps[4]+other_ps[4]
    appliance=steel_ps[5]+al_ps[5]+mach_ps[5]+min_ps[5]+chem_ps[5]+paper_ps[5]+food_ps[5]+other_ps[5]
    vehicle=steel_ps[6]+al_ps[6]+mach_ps[6]+min_ps[6]+chem_ps[6]+paper_ps[6]+food_ps[6]+other_ps[6]
    
    #Sankey labels
    Motion='Motion ({:.0f}PJ)'.format(driven+vehicle)
    Heat='Heat ({:.0f}PJ)'.format(steam+furnace+spaceheat)
    Other='Other ({:.0f}PJ)'.format(light+appliance)
    
    ##### set up links for Allocation Sankey
    links = [
        #direct fuel use and fuel for electricity generation
        {'source': 'Oil', 'target': DFU, 'value': industry[0], 'type':'A', 'color': 'darkkhaki' },
        {'source': 'Oil', 'target': TEG, 'value': totelecind[0]+totheatind[0], 'type':'A', 'color': 'darkkhaki'},
        {'source': 'Coal', 'target': DFU, 'value': industry[5], 'type':'D', 'color': 'dimgrey'},
        {'source': 'Coal', 'target': TEG, 'value': totelecind[5]+totheatind[5], 'type':'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': DFU, 'value': industry[1], 'type':'C', 'color': 'gold'},
        {'source': 'Gas', 'target': TEG, 'value': totelecind[1]+totheatind[1], 'type':'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': DFU, 'value': industry[4], 'type':'B', 'color': 'green'},
        {'source': 'Biomass', 'target': TEG, 'value': totelecind[4]+totheatind[4], 'type':'B', 'color': 'green'},
        {'source': 'Renewables', 'target': DFU, 'value': industry[3], 'type':'F', 'color': 'dodgerblue'},
        {'source': 'Renewables', 'target': TEG, 'value': totelecind[3]+totheatind[3], 'type':'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': DFU, 'value': industry[2], 'type':'E', 'color': 'purple'},
        {'source': 'Nuclear', 'target': TEG, 'value': totelecind[2]+totheatind[2], 'type':'E', 'color':'purple'},
        
        #fuel and electricity to conversion devices for motion
        {'source': DFU, 'target': 'Engine', 'value': oil_cd[0], 'type':'A', 'color':'darkkhaki'},
        {'source': DFU, 'target': 'Engine', 'value': gas_cd[0], 'type':'C', 'color':'gold'},
        {'source': DFU, 'target': 'Engine', 'value': coal_cd[0], 'type':'D', 'color':'dimgrey'},
        {'source': DFU, 'target': 'Engine', 'value': biomass_cd[0], 'type':'B', 'color':'green'},
        {'source': TEG, 'target': 'Electric Motor', 'value': elec_cd[0], 'type':'H', 'color':'silver'},
        
        #fuel and electricity to conversion devices for heat
        {'source': DFU, 'target': 'Oil Burner', 'value': oil_cd[1]+oil_cd[3], 'type':'A', 'color':'darkkhaki'},
        {'source': DFU, 'target': 'Gas Burner', 'value': gas_cd[1]+gas_cd[3], 'type':'C', 'color':'gold'},
        {'source': DFU, 'target': 'Coal Burner', 'value': coal_cd[1]+coal_cd[3], 'type':'D', 'color':'dimgrey'},
        {'source': DFU, 'target': 'Biomass Burner', 'value': biomass_cd[1]+biomass_cd[3], 'type':'B', 'color':'green'},
        {'source': TEG, 'target': 'Electric Heater', 'value': elec_cd[1], 'type':'H', 'color':'silver'},
        {'source': DFU, 'target': 'Nuclear Heater', 'value': nuclear_cd, 'type':'E', 'color':'purple'},
        {'source': DFU, 'target': 'Renewable Heater', 'value': renewable_cd, 'type':'F', 'color':'dodgerblue'},
        {'source': TEG, 'target': 'Heat Exchanger', 'value': heat_cd, 'type': 'G', 'color': 'red'},
    
        #fuel and electricity to conversion devices for other
        {'source': DFU, 'target': 'Lighting Device', 'value': oil_cd[2], 'type':'A', 'color':'darkkhaki'},
        {'source': DFU, 'target': 'Lighting Device', 'value': gas_cd[2], 'type':'C', 'color':'gold'},
        {'source': DFU, 'target': 'Lighting Device', 'value': coal_cd[2], 'type':'D', 'color':'dimgrey'},
        {'source': DFU, 'target': 'Lighting Device', 'value': biomass_cd[2], 'type':'B', 'color':'green'},
        {'source': TEG, 'target': 'Lighting Device', 'value': elec_cd[2], 'type':'H', 'color':'silver'},
        {'source': TEG, 'target': 'Electronic', 'value': elec_cd[3], 'type':'H', 'color':'silver'},
        
        #energy to provide motion
        {'source': 'Engine', 'target': Motion, 'value': oil_cd[0], 'type':'A', 'color':'darkkhaki'},
        {'source': 'Engine', 'target': Motion, 'value': gas_cd[0], 'type':'C', 'color':'gold'},
        {'source': 'Engine', 'target': Motion, 'value': coal_cd[0], 'type':'D', 'color':'dimgrey'},
        {'source': 'Engine', 'target': Motion, 'value': biomass_cd[0], 'type':'B', 'color':'green'},
        {'source': 'Electric Motor', 'target': Motion, 'value': elec_cd[0], 'type':'H', 'color':'silver'},
        
        #energy to provide heat
        {'source': 'Oil Burner', 'target': Heat, 'value': oil_cd[1], 'type':'A', 'color':'darkkhaki'},
        {'source': 'Gas Burner', 'target': Heat, 'value': gas_cd[1], 'type':'C', 'color':'gold'},
        {'source': 'Coal Burner', 'target': Heat, 'value': coal_cd[1], 'type':'D', 'color':'dimgrey'},
        {'source': 'Biomass Burner', 'target': Heat, 'value': biomass_cd[1], 'type':'B', 'color':'green'},
        {'source': 'Electric Heater', 'target': Heat, 'value': elec_cd[1], 'type':'H', 'color':'silver'},
        {'source': 'Nuclear Heater', 'target': Heat, 'value': nuclear_cd, 'type':'E', 'color':'purple'},
        {'source': 'Renewable Heater', 'target': Heat, 'value': renewable_cd, 'type':'F', 'color':'dodgerblue'},
        {'source': 'Heat Exchanger', 'target': Heat, 'value': heat_cd, 'type':'G', 'color':'red'},
    
        #energy used for other purposes
        {'source': 'Lighting Device', 'target': Other, 'value': oil_cd[2], 'type':'A', 'color':'darkkhaki'},
        {'source': 'Lighting Device', 'target': Other, 'value': gas_cd[2], 'type':'C', 'color':'gold'},
        {'source': 'Lighting Device', 'target': Other, 'value': coal_cd[2], 'type':'D', 'color':'dimgrey'},
        {'source': 'Lighting Device', 'target': Other, 'value': biomass_cd[2], 'type':'B', 'color':'green'},
        {'source': 'Lighting Device', 'target': Other, 'value': elec_cd[2], 'type':'H', 'color':'silver'},
        
        {'source': 'Oil Burner', 'target': Other, 'value': oil_cd[3], 'type':'A', 'color':'darkkhaki'},
        {'source': 'Gas Burner', 'target': Other, 'value': gas_cd[3], 'type':'C', 'color':'gold'},
        {'source': 'Coal Burner', 'target': Other, 'value': coal_cd[3], 'type':'D', 'color':'dimgrey'},
        {'source': 'Biomass Burner', 'target': Other, 'value': biomass_cd[3], 'type':'B', 'color':'green'},
        
        {'source': 'Electronic', 'target': Other, 'value': elec_cd[3], 'type':'H', 'color':'silver'},
        
        #heat, motion and other to passive systems
        {'source': Heat, 'target': 'Steam System', 'value': steam, 'type': 'K', 'color':'indianred'},
        {'source': Heat, 'target': 'Furnace', 'value': furnace, 'type': 'I', 'color':'maroon'},
        {'source': Heat, 'target': 'Heated Space', 'value': spaceheat, 'type': 'J', 'color':'firebrick'},
        {'source': Motion, 'target': 'Driven System', 'value': driven, 'type': 'L', 'color':'lightblue'},
        {'source': Motion, 'target': 'Vehicle', 'value': vehicle, 'type': 'M', 'color':'lightskyblue'},
        {'source': Other, 'target': 'Illuminated Space', 'value': light, 'type': 'O', 'color':'darkolivegreen'},
        {'source': Other, 'target': 'Appliance', 'value': appliance, 'type': 'P', 'color':'olivedrab'},
        
        #passive system to industrial sub-sectors
        {'source': 'Steam System', 'target': 'Steel', 'value': steel_ps[0], 'type':'K', 'color': 'indianred' },
        {'source': 'Driven System', 'target': 'Steel', 'value': steel_ps[1], 'type':'L', 'color': 'lightblue' },
        {'source': 'Furnace', 'target': 'Steel', 'value': steel_ps[2], 'type':'I', 'color': 'maroon' },
        {'source': 'Illuminated Space', 'target': 'Steel', 'value': steel_ps[3], 'type':'O', 'color': 'darkolivegreen' },
        {'source': 'Heated Space', 'target': 'Steel', 'value': steel_ps[4], 'type':'J', 'color': 'firebrick' },
        {'source': 'Appliance', 'target': 'Steel', 'value': steel_ps[5], 'type':'P', 'color': 'olivedrab' },
        {'source': 'Vehicle', 'target': 'Steel', 'value': steel_ps[6], 'type':'M', 'color': 'lightskyblue' },
        
        {'source': 'Steam System', 'target': 'Aluminium', 'value': al_ps[0], 'type':'K', 'color': 'indianred' },
        {'source': 'Driven System', 'target': 'Aluminium', 'value': al_ps[1], 'type':'L', 'color': 'lightblue' },
        {'source': 'Furnace', 'target': 'Aluminium', 'value': al_ps[2], 'type':'I', 'color': 'maroon' },
        {'source': 'Illuminated Space', 'target': 'Aluminium', 'value': al_ps[3], 'type':'O', 'color': 'darkolivegreen' },
        {'source': 'Heated Space', 'target': 'Aluminium', 'value': al_ps[4], 'type':'J', 'color': 'firebrick' },
        {'source': 'Appliance', 'target': 'Aluminium', 'value': al_ps[5], 'type':'P', 'color': 'olivedrab' },
        {'source': 'Vehicle', 'target': 'Aluminium', 'value': al_ps[6], 'type':'M', 'color': 'lightskyblue' },
        
        {'source': 'Steam System', 'target': 'Machinery', 'value': mach_ps[0], 'type':'K', 'color': 'indianred' },
        {'source': 'Driven System', 'target': 'Machinery', 'value': mach_ps[1], 'type':'L', 'color': 'lightblue' },
        {'source': 'Furnace', 'target': 'Machinery', 'value': mach_ps[2], 'type':'I', 'color': 'maroon' },
        {'source': 'Illuminated Space', 'target': 'Machinery', 'value': mach_ps[3], 'type':'O', 'color': 'darkolivegreen' },
        {'source': 'Heated Space', 'target': 'Machinery', 'value': mach_ps[4], 'type':'J', 'color': 'firebrick' },
        {'source': 'Appliance', 'target': 'Machinery', 'value': mach_ps[5], 'type':'P', 'color': 'olivedrab' },
        {'source': 'Vehicle', 'target': 'Machinery', 'value': mach_ps[6], 'type':'M', 'color': 'lightskyblue' },
    
        {'source': 'Steam System', 'target': 'Mineral', 'value': min_ps[0], 'type':'K', 'color': 'indianred' },
        {'source': 'Driven System', 'target': 'Mineral', 'value': min_ps[1], 'type':'L', 'color': 'lightblue' },
        {'source': 'Furnace', 'target': 'Mineral', 'value': min_ps[2], 'type':'I', 'color': 'maroon' },
        {'source': 'Illuminated Space', 'target': 'Mineral', 'value': min_ps[3], 'type':'O', 'color': 'darkolivegreen' },
        {'source': 'Heated Space', 'target': 'Mineral', 'value': min_ps[4], 'type':'J', 'color': 'firebrick' },
        {'source': 'Appliance', 'target': 'Mineral', 'value': min_ps[5], 'type':'P', 'color': 'olivedrab' },
        {'source': 'Vehicle', 'target': 'Mineral', 'value': min_ps[6], 'type':'M', 'color': 'lightskyblue' },
    
        {'source': 'Steam System', 'target': 'Chemical', 'value': chem_ps[0], 'type':'K', 'color': 'indianred' },
        {'source': 'Driven System', 'target': 'Chemical', 'value': chem_ps[1], 'type':'L', 'color': 'lightblue' },
        {'source': 'Furnace', 'target': 'Chemical', 'value': chem_ps[2], 'type':'I', 'color': 'maroon' },
        {'source': 'Illuminated Space', 'target': 'Chemical', 'value': chem_ps[3], 'type':'O', 'color': 'darkolivegreen' },
        {'source': 'Heated Space', 'target': 'Chemical', 'value': chem_ps[4], 'type':'J', 'color': 'firebrick' },
        {'source': 'Appliance', 'target': 'Chemical', 'value': chem_ps[5], 'type':'P', 'color': 'olivedrab' },
        {'source': 'Vehicle', 'target': 'Chemical', 'value': chem_ps[6], 'type':'M', 'color': 'lightblue' },
        
        {'source': 'Steam System', 'target': 'Paper', 'value': paper_ps[0], 'type':'K', 'color': 'indianred' },
        {'source': 'Driven System', 'target': 'Paper', 'value': paper_ps[1], 'type':'L', 'color': 'lightblue' },
        {'source': 'Furnace', 'target': 'Paper', 'value': paper_ps[2], 'type':'I', 'color': 'maroon' },
        {'source': 'Illuminated Space', 'target': 'Paper', 'value': paper_ps[3], 'type':'O', 'color': 'darkolivegreen' },
        {'source': 'Heated Space', 'target': 'Paper', 'value': paper_ps[4], 'type':'J', 'color': 'firebrick' },
        {'source': 'Appliance', 'target': 'Paper', 'value': paper_ps[5], 'type':'P', 'color': 'olivedrab' },
        {'source': 'Vehicle', 'target': 'Paper', 'value': paper_ps[6], 'type':'M', 'color': 'lightskyblue' },
        
        {'source': 'Steam System', 'target': 'Food', 'value': food_ps[0], 'type':'K', 'color': 'indianred' },
        {'source': 'Driven System', 'target': 'Food', 'value': food_ps[1], 'type':'L', 'color': 'lightblue' },
        {'source': 'Furnace', 'target': 'Food', 'value': food_ps[2], 'type':'I', 'color': 'maroon' },
        {'source': 'Illuminated Space', 'target': 'Food', 'value': food_ps[3], 'type':'O', 'color': 'darkolivegreen' },
        {'source': 'Heated Space', 'target': 'Food', 'value': food_ps[4], 'type':'J', 'color': 'firebrick' },
        {'source': 'Appliance', 'target': 'Food', 'value': food_ps[5], 'type':'P', 'color': 'olivedrab' },
        {'source': 'Vehicle', 'target': 'Food', 'value': food_ps[6], 'type':'M', 'color': 'lightskyblue' },
        
        {'source': 'Steam System', 'target': 'Other Industry', 'value': other_ps[0], 'type':'K', 'color': 'indianred' },
        {'source': 'Driven System', 'target': 'Other Industry', 'value': other_ps[1], 'type':'L', 'color': 'lightblue' },
        {'source': 'Furnace', 'target': 'Other Industry', 'value': other_ps[2], 'type':'I', 'color': 'maroon' },
        {'source': 'Illuminated Space', 'target': 'Other Industry', 'value': other_ps[3], 'type':'O', 'color': 'darkolivegreen' },
        {'source': 'Heated Space', 'target': 'Other Industry', 'value': other_ps[4], 'type':'J', 'color': 'firebrick' },
        {'source': 'Appliance', 'target': 'Other Industry', 'value': other_ps[5], 'type':'P', 'color': 'olivedrab' },
        {'source': 'Vehicle', 'target': 'Other Industry', 'value': other_ps[6], 'type':'M', 'color': 'lightskyblue' },    
    ]
    
    #groups for showing total primary energy supply and labelling conversion devices and passive systems
    groups = [
        {'id': 'G', 'title': 'TPE ({:.0f}PJ)'.format(PrimEng), 'nodes': ['Oil', 'Coal', 'Gas', 'Biomass', 'Nuclear', 'Renewables']},
        {'id': 'G', 'title': 'Conversion Devices', 'nodes': ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Lighting Device']},
        {'id': 'G', 'title': 'Passive Systems', 'nodes': ['Steam System', 'Furnace',  'Heated Space', 'Driven System','Illuminated Space', 'Appliance']}
    ]
    
    #set order in which nodes appear
    order = [
        ['Oil', 'Biomass', 'Gas', 'Coal', 'Nuclear', 'Renewables'],
        [DFU, TEG],
        ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Electronic', 'Lighting Device'],
        [Heat, Motion, Other],
        ['Furnace',  'Heated Space', 'Steam System', 'Driven System', 'Vehicle', 'Illuminated Space', 'Appliance'],
        ['Steel', 'Aluminium', 'Machinery', 'Mineral', 'Chemical', 'Paper', 'Food', 'Other Industry']
    
    ]
    
    return sankey(links=links, groups=groups, linkLabelFormat='.0f', linkLabelMinWidth=10, order=order, align_link_types=True).auto_save_png(Country+'_Allocation_Sankey_'+Year+'.png')
   
###EFFICIENCY SANKEY GENERATOR FUNCTION###    
def efficiency(IEATES,IEATFC,electricity,heat,Country,Year,Exergy):
    '''
    Function to return an efficiency Sankey diagram
    
    Inputs: 
        IEATES - Energy Supply Values from IEA
        IEATFC - Energy Consumption Values from IEA
        electricity - Electricity Consumption values from IEA
        heat - Heat Consumption values from IEA
        Country - name of country from IEA list
        Year - year between 1960 and 2019
        Exergy - Produce Diagram in Exergy or Energy Values
        
    Returns an efficiency Sankey diagram for the given 
    year and country and prints the overall efficiency.
    
    '''
    #convert supply to exergy values and combine oil and renewable products (exergy factors from https://doi.org/10.3390/en9090707)
    if Exergy=='Exergy':                          
        exergy=np.array([1.04*IEATES[0],1.03*IEATES[1],0.95*IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],1.13*IEATES[6],1.06*IEATES[7]])
        exergy_h=0.17*heat
    elif Exergy=='Energy':
        exergy=np.array([IEATES[0],IEATES[1],IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],IEATES[6],IEATES[7]])
        exergy_h=heat                          
    
    #calculate total electricity generation and direct fuel use
    tpes=np.zeros(len(exergy))
    losses=np.zeros(len(exergy))
    tfc=np.zeros(len(exergy))
    nonenergy=np.zeros(len(exergy))
    egeneration=np.zeros(len(exergy))
    hgeneration=np.zeros(len(exergy))
    for i in range (0,len(exergy)):
        tpes[i]=exergy[i][0]
        #combine all losses
        for j in range(1,3):
            losses[i]=losses[i]+exergy[i][j] 
        for j in range(9,23):
            losses[i]=losses[i]+exergy[i][j]
        tfc[i]=exergy[i][23]
        nonenergy[i]=exergy[i][24]
        #combine electriciy and heat generation from electricity, heating and CHP plants
        for j in range(3,5):
            egeneration[i]=egeneration[i]+exergy[i][j]
        for j in range(5,7):
            egeneration[i]=egeneration[i]+0.89*exergy[i][j]
            hgeneration[i]=hgeneration[i]+0.11*exergy[i][j]
        for j in range(7,9):
            hgeneration[i]=hgeneration[i]+exergy[i][j]
    
    dfu_used=tfc-nonenergy #total fuel used directly is total final consumption of fuel - non-energy use
    elec_used=-egeneration-hgeneration #total fuel used for electricity generation is combination of fuels to all plants from above (- sign to yield +ve values)
    
    #losses split proportionally between dfu & electricity generation
    dfu_losses=np.zeros(len(tpes))
    elec_losses=np.zeros(len(tpes))
    for i in range(len(tpes)):
        if tpes[i]+losses[i]==0: #to avoid divide zero errors
            dfu_losses[i]=0
            elec_losses[i]=0
        else: #- signs as losses[i] have -ve values
            dfu_losses[i]=-dfu_used[i]*(losses[i]/(tpes[i]+losses[i])) 
            elec_losses[i]=-elec_used[i]*(losses[i]/(tpes[i]+losses[i]))
    #convert from TJ to PJ
    direct_fuel_use=(dfu_used+dfu_losses)/(10**3)
    electricity_generation=(elec_used+elec_losses)/(10**3)
   
    
    #convert consumption to exergy values and combine oil and renewable products
    exergycons=np.array([1.04*IEATFC[0],1.03*IEATFC[1],0.95*IEATFC[2],IEATFC[3]+IEATFC[4]+IEATFC[5],1.11*IEATFC[6],1.06*IEATFC[7]])
    
    #calculate direct fuel use energy to industry
    industry=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        industry[i]=exergycons[i][0]
    industry=industry/(10**3)
    
    #scale to include losses
    for i in range(len(dfu_used)):
        if dfu_used[i]!=0:
            industry[i]=industry[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            
    #calculate total electricity (& heat) 
    totelec=electricity[0]+electricity[15]+electricity[24]+electricity[25]+electricity[26]+electricity[27]+electricity[28]
    totheat=exergy_h[0]+exergy_h[15]+exergy_h[24]+exergy_h[25]+exergy_h[26]+exergy_h[27]+exergy_h[28]
    
    if (totelec+totheat)!=0: #to avoid divide zero errors
        totelec_=totelec/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
        totheat_=totheat/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
    else:
        totelec_=0
        totheat_=0
        
    #scale electricity (& heat) flow to industry only
    if totelec!=0:
        elec_ind=(electricity[0]/totelec)*totelec_
    else:
        elec_ind=0
        
    if totheat!=0:
        heat_ind=(exergy_h[0]/totheat)*totheat_
    else:
        heat_ind=0
        
    #calculate energy to electricity from each fuel for industry
    totelecind=np.zeros(len(exergycons))
    totheatind=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecind[i]=(elec_ind/np.sum(electricity_generation))*electricity_generation[i]
            totheatind[i]=(heat_ind/np.sum(electricity_generation))*electricity_generation[i]
            
    #calculate direct use for industrial sub-sectors
    exergyInd=np.zeros((len(exergycons),29))
    for j in range(0,len(exergycons)):
        for i in range(0,29):
            if dfu_used[j]!=0: #to avoid divide zero errors
                exergyInd[j][i]=exergycons[j][i]*direct_fuel_use[j]/(dfu_used[j]/10**3)
                
    steel=np.zeros(len(exergycons))
    aluminium=np.zeros(len(exergycons))
    machinery=np.zeros(len(exergycons))
    mineral=np.zeros(len(exergycons))
    chemical=np.zeros(len(exergycons))
    paper=np.zeros(len(exergycons))
    food=np.zeros(len(exergycons))
    other=np.zeros(len(exergycons))
    
    for i in range(0,len(exergycons)):
        steel[i]=exergyInd[i][4]/(10**3)
        aluminium[i]=exergyInd[i][6]/(10**3)
        machinery[i]=(exergyInd[i][8]+exergyInd[i][9])/(10**3)
        mineral[i]=exergyInd[i][7]/(10**3)
        chemical[i]=exergyInd[i][5]/(10**3)
        paper[i]=(exergyInd[i][11]+exergyInd[i][12])/(10**3)
        food[i]=exergyInd[i][10]/(10**3)
        other[i]=(exergyInd[i][1]+exergyInd[i][2]+exergyInd[i][13]+exergyInd[i][14])/(10**3)
        
    #calculate electricity to industrial sub-sectors  
    if totelec!=0:
        elec_steel=(electricity[4]/totelec)*totelec_
        elec_aluminium=(electricity[6]/totelec)*totelec_
        elec_machinery=((electricity[8]+electricity[9])/totelec)*totelec_
        elec_mineral=(electricity[7]/totelec)*totelec_
        elec_chemical=(electricity[5]/totelec)*totelec_
        elec_paper=((electricity[11]+electricity[12])/totelec)*totelec_
        elec_food=(electricity[10]/totelec)*totelec_
        elec_other=((electricity[1]+electricity[2]+electricity[13]+electricity[14])/totelec)*totelec_
    else:
        elec_steel=0
        elec_aluminium=0
        elec_machinery=0
        elec_mineral=0
        elec_chemical=0
        elec_paper=0
        elec_food=0
        elec_other=0
        
    #calculate heat to industrial sub-sectors  
    if totheat!=0:
        heat_steel=(exergy_h[4]/totheat)*totheat_
        heat_aluminium=(exergy_h[6]/totheat)*totheat_
        heat_machinery=((exergy_h[8]+exergy_h[9])/totheat)*totheat_
        heat_mineral=(exergy_h[7]/totheat)*totheat_
        heat_chemical=(exergy_h[5]/totheat)*totheat_
        heat_paper=((exergy_h[11]+exergy_h[12])/totheat)*totheat_
        heat_food=(exergy_h[10]/totheat)*totheat_
        heat_other=((exergy_h[1]+exergy_h[2]+exergy_h[13]+exergy_h[14])/totheat)*totheat_
    else:
        heat_steel=0
        heat_aluminium=0
        heat_machinery=0
        heat_mineral=0
        heat_chemical=0
        heat_paper=0
        heat_food=0
        heat_other=0
        
    #append electricity and heat values to sub-sector fuel consumption arrays
    steelfull=np.append(steel, [elec_steel, heat_steel])
    aluminiumfull=np.append(aluminium, [elec_aluminium, heat_aluminium])
    machineryfull=np.append(machinery, [elec_machinery, heat_machinery])
    mineralfull=np.append(mineral, [elec_mineral, heat_mineral])
    chemicalfull=np.append(chemical, [elec_chemical, heat_chemical])
    paperfull=np.append(paper, [elec_paper, heat_paper])
    foodfull=np.append(food, [elec_food, heat_food])
    otherfull=np.append(other, [elec_other, heat_other])
    
    #define allocation matrices, based on US industry data - used to assign fuels to passive systems below
    #rows are passive systems, columns are fuels (oil, gas, nuclear, renewables, biomass, coal, electricity, heat))
    steel_mat = np.array([[0.00  , 0.10  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.39  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 1.00  , 1.00  , 0.53  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.03  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#appliance
                         [1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    al_mat = np.array([[0.00  , 0.13  , 1.00  , 0.00  , 0.13  , 0.13  , 0.01  , 0.00  ],#steam
                         [0.25  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.24  , 0.00  ],#driven
                         [0.25  , 0.76  , 0.00  , 0.00  , 0.76  , 0.76  , 0.65  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.03  , 0.00  ],#light
                         [0.00  , 0.09  , 0.00  , 1.00  , 0.09  , 0.09  , 0.04  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.02  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                      ])
    
    mach_mat = np.array([[0.15  , 0.16  , 1.00  , 0.00  , 0.16  , 0.16  , 0.01  , 0.00  ],#steam
                         [0.14  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.49  , 0.00  ],#driven
                         [0.07  , 0.45  , 0.00  , 0.00  , 0.45  , 0.45  , 0.16  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.11  , 0.00  ],#light
                         [0.14  , 0.35  , 0.00  , 1.00  , 0.35  , 0.35  , 0.19  , 1.00  ],#spaceheat
                         [0.00  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.03  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])
    
    min_mat = np.array([[0.00  , 0.03  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.38  , 0.08  , 0.00  , 0.00  , 0.10  , 0.10  , 0.60  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 0.90  , 0.90  , 0.28  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.62  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                       ])
    
    chem_mat = np.array([[0.50  , 0.52  , 1.00  , 0.00  , 0.87  , 0.87  , 0.01  , 0.00  ],#steam
                         [0.00  , 0.04  , 0.00  , 0.00  , 0.00  , 0.00  , 0.63  , 0.00  ],#driven
                         [0.10  , 0.41  , 0.00  , 0.00  , 0.13  , 0.13  , 0.25  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.02  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.40  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                        ])                 
    
    paper_mat = np.array([[0.36  , 0.63  , 1.00  , 0.00  , 0.98  , 0.98  , 0.04  , 0.00  ],#steam
                         [0.04  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.78  , 0.00  ],#driven
                         [0.08  , 0.30  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.06  , 1.00  ],#spaceheat
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.52  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    food_mat = np.array([[0.59  , 0.59  , 1.00  , 0.00  , 0.79  , 0.79  , 0.03  , 0.00  ],#steam
                         [0.00  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.69  , 0.00  ],#driven
                         [0.00  , 0.27  , 0.00  , 0.00  , 0.21  , 0.21  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#light
                         [0.08  , 0.08  , 0.00  , 1.00  , 0.00  , 0.00  , 0.11  , 1.00  ],#spaceheat
                         [0.08  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.25  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])
    
    other_mat = np.array([[0.13  , 0.34  , 1.00  , 0.00  , 1.00  , 1.00  , 0.01  , 0.00  ],#steam
                         [0.13  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.73  , 0.00  ],#driven
                         [0.71  , 0.61  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.06  , 0.00  ],#light
                         [0.00  , 0.04  , 0.00  , 1.00  , 0.00  , 0.00  , 0.09  , 1.00  ],#spaceheat
                         [0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    #import data on share of steel from EAF
    import pandas as pd
    df=pd.read_csv('SteelShares2023.csv')
    try:
        EAF=float(df['EAF'][df['Country'] == Country].values[0])
    except:
        EAF=float(df['EAF'][df['Country'] == 'World'].values[0])
        
    #calculate new allocation matrices for steel, based on share of EAF
    x=(442.01*EAF)/((442.01*EAF)+(4128.05*(1-EAF)))
    z1=0.943*x+0.045*(1-x)
    z2=0.928*(1-x)
    z3=0.057*x+0.027*(1-x)
    gamma=0
        
    if x==1:
        if electricity[4]!=0:
            gammaprime=(0.02*IEATFC[1][4]/electricity[4])*(z1/z3)
            steel_mat[2][6]=0.4+0.6*gammaprime
            steel_mat[1][6]=0.5*(1-gammaprime)
            steel_mat[3][6]=0.04*(1-gammaprime)
            steel_mat[4][6]=0.05*(1-gammaprime)
            steel_mat[5][6]=0.01*(1-gammaprime)
    else:
        if electricity[4]!=0:
            gamma=(IEATFC[7][4]/electricity[4])*(z1/z2)
            steel_mat[2][6]=0.4+0.6*gamma
            steel_mat[1][6]=0.5*(1-gamma)
            steel_mat[3][6]=0.04*(1-gamma)
            steel_mat[4][6]=0.05*(1-gamma)
            steel_mat[5][6]=0.01*(1-gamma)
        if IEATFC[1][4]!=0:
            delta=(IEATFC[7][4]/IEATFC[1][4])*(z3/z2)
            steel_mat[2][1]=0.83+0.17*delta
            steel_mat[0][1]=0.1*(1-delta)
            steel_mat[1][1]=0.01*(1-delta)
            steel_mat[4][1]=0.05*(1-delta)
            steel_mat[5][1]=0.01*(1-delta)
            
    #use matrix multiplication to assign fuel to each passive system
    steel_ps=np.zeros(7)
    al_ps=np.zeros(7)
    mach_ps=np.zeros(7)
    min_ps=np.zeros(7)
    chem_ps=np.zeros(7)
    paper_ps=np.zeros(7)
    food_ps=np.zeros(7)
    other_ps=np.zeros(7)
    for i in range(0,len(steelfull)):
        for j in range(0,7):
            steel_ps[j]=steel_ps[j]+steelfull[i]*steel_mat[j][i]
            al_ps[j]=al_ps[j]+aluminiumfull[i]*al_mat[j][i]
            mach_ps[j]=mach_ps[j]+machineryfull[i]*mach_mat[j][i]
            min_ps[j]=min_ps[j]+mineralfull[i]*min_mat[j][i]
            chem_ps[j]=chem_ps[j]+chemicalfull[i]*chem_mat[j][i]
            paper_ps[j]=paper_ps[j]+paperfull[i]*paper_mat[j][i]
            food_ps[j]=food_ps[j]+foodfull[i]*food_mat[j][i]
            other_ps[j]=other_ps[j]+otherfull[i]*other_mat[j][i]
            
    #define matrices for assigning fuels to conversion devices
    #rows are purposes of converson devices, columns are industries (steel, aluminium, machinery, mineral, chemical, paper, food, other)
    oil_mat = np.array([[1.00, 0.75, 0.64, 1.00, 0.40, 0.56, 0.25, 0.13],#motion
                       [0.00, 0.25, 0.36, 0.00, 0.60, 0.44, 0.67, 0.84],#heat
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.08, 0.03]])#appliance
    
    gas_mat = np.array([[steel_mat[1][1]+steel_mat[6][1], 0.01, 0.02, 0.08, 0.04, 0.02, 0.03, 0.01],#motion
                       [steel_mat[0][1]+steel_mat[2][1]+steel_mat[4][1], 0.98, 0.96, 0.91, 0.95, 0.98, 0.94, 0.99],#heat
                       [steel_mat[3][1], 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [steel_mat[5][1], 0.01, 0.02, 0.01, 0.01, 0.00, 0.03, 0.00]])#appliance
    
    coal_mat = np.array([[0.00, 0.01, 0.02, 0.10, 0.00, 0.02, 0.00, 0.00],#motion
                        [1.00, 0.98, 0.96, 0.90, 1.00, 0.98, 1.00, 1.00],#heat
                        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                        [0.00, 0.01, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00]])#appliance
    
    elec_mat = np.array([[steel_mat[1][6]+steel_mat[6][6], 0.25, 0.50, 0.60, 0.63, 0.78, 0.70, 0.73],#motion
                        [steel_mat[0][6]+steel_mat[2][6]+steel_mat[4][6], 0.70, 0.36, 0.33, 0.31, 0.15, 0.19, 0.19],#heat
                        [steel_mat[3][6], 0.03, 0.11, 0.05, 0.04, 0.05, 0.09, 0.06],#light
                        [steel_mat[5][6], 0.02, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02]])#appliance
    
    #use matrix multiplication to assign energy to each conversion device
    oil_cd=np.zeros(4)
    gas_cd=np.zeros(4)
    biomass_cd=np.zeros(4)
    coal_cd=np.zeros(4)
    elec_cd=np.zeros(4)
    for i in range(0,4):
        oil_cd[i]=oil_mat[i][0]*steelfull[0]+oil_mat[i][1]*aluminiumfull[0]+oil_mat[i][2]*machineryfull[0]+oil_mat[i][3]*mineralfull[0]+oil_mat[i][4]*chemicalfull[0]+oil_mat[i][5]*paperfull[0]+oil_mat[i][6]*foodfull[0]+oil_mat[i][7]*otherfull[0]
        gas_cd[i]=gas_mat[i][0]*steelfull[1]+gas_mat[i][1]*aluminiumfull[1]+gas_mat[i][2]*machineryfull[1]+gas_mat[i][3]*mineralfull[1]+gas_mat[i][4]*chemicalfull[1]+gas_mat[i][5]*paperfull[1]+gas_mat[i][6]*foodfull[1]+gas_mat[i][7]*otherfull[1]
        biomass_cd[i]=coal_mat[i][0]*steelfull[4]+coal_mat[i][1]*aluminiumfull[4]+coal_mat[i][2]*machineryfull[4]+coal_mat[i][3]*mineralfull[4]+coal_mat[i][4]*chemicalfull[4]+coal_mat[i][5]*paperfull[4]+coal_mat[i][6]*foodfull[4]+coal_mat[i][7]*otherfull[4]
        coal_cd[i]=coal_mat[i][0]*steelfull[5]+coal_mat[i][1]*aluminiumfull[5]+coal_mat[i][2]*machineryfull[5]+coal_mat[i][3]*mineralfull[5]+coal_mat[i][4]*chemicalfull[5]+coal_mat[i][5]*paperfull[5]+coal_mat[i][6]*foodfull[5]+coal_mat[i][7]*otherfull[5]
        elec_cd[i]=elec_mat[i][0]*steelfull[6]+elec_mat[i][1]*aluminiumfull[6]+elec_mat[i][2]*machineryfull[6]+elec_mat[i][3]*mineralfull[6]+elec_mat[i][4]*chemicalfull[6]+elec_mat[i][5]*paperfull[6]+elec_mat[i][6]*foodfull[6]+elec_mat[i][7]*otherfull[6]
    
    #assumed that all nuclear, renewable and direct heat contributes to heat
    heat_cd=steelfull[7]+aluminiumfull[7]+machineryfull[7]+mineralfull[7]+chemicalfull[7]+paperfull[7]+foodfull[7]+otherfull[7]
    
    #values for Sankey labels
    PrimEng=np.sum(industry)+np.sum(totelecind)+np.sum(totheatind)
    
    #calculate losses in fuel transformation
    ind_used=np.zeros(len(industry))
    inddfu_losses=np.zeros(len(industry))
    indelec_used=np.zeros(len(industry))
    indelec_losses=np.zeros(len(industry))
    for i in range(len(industry)):
        if direct_fuel_use[i]!=0: #to avoid divide zero errors
            ind_used[i]=industry[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
            inddfu_losses[i]=industry[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
        if electricity_generation[i]!=0: #to avoid divide zero errors
            indelec_used[i]=(totelecind[i]+totheatind[i])*elec_used[i]/(electricity_generation[i]*1000)
            indelec_losses[i]=(totelecind[i]+totheatind[i])*elec_losses[i]/(electricity_generation[i]*1000)
        ind_losses=indelec_losses+inddfu_losses
            
    #calculate energy to each conversion device
    if np.sum(oil_cd)!=0: #to avoid divide zero errors
        oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
        oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
    else:
        oilburner=0
        oilengine=0
        
    if np.sum(gas_cd)!=0: #to avoid divide zero errors
        gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
        gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
    else:
        gasburner=0
        gasengine=0
    
    nuclearheater=ind_used[2] #in case nuclear is used directly
    renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating
    
    if np.sum(biomass_cd)!=0: #to avoid divide zero errors
        biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
        biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
    else:
        biomassburner=0
        biomassengine=0
        
    if np.sum(coal_cd)!=0: #to avoid divide zero errors
        coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
        coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
    else:
        coalburner=0
        coalengine=0
        
    #calculate losses in electricity generation
    if np.sum(egeneration)!=0: #to avoid divide zero errors
        eleceff=totelec/(-np.sum(egeneration))
    else:
        eleceff=0
    if np.sum(hgeneration)!=0:
        heateff=totheat/(-np.sum(hgeneration))
    else:
        heateff=0
        
    heatex=heateff*heat_cd
    elecmotor=eleceff*elec_cd[1]
    elecheater=eleceff*elec_cd[0]
    lightingdevice=eleceff*elec_cd[2]
    applianceelec=eleceff*elec_cd[3]
    
    eloss=np.sum(indelec_used)-heatex-elecmotor-elecheater-lightingdevice-applianceelec
    
    #create new matrices with all passive systems
    oil_mat2=np.zeros((7,8))
    for i in range(7):
        oil_mat2[i][0]=steel_mat[i][0]
        oil_mat2[i][1]=al_mat[i][0]
        oil_mat2[i][2]=mach_mat[i][0]
        oil_mat2[i][3]=min_mat[i][0]
        oil_mat2[i][4]=chem_mat[i][0]
        oil_mat2[i][5]=paper_mat[i][0]
        oil_mat2[i][6]=food_mat[i][0]
        oil_mat2[i][7]=other_mat[i][0]
        
    gas_mat2=np.zeros((7,8))
    for i in range(7):
        gas_mat2[i][0]=steel_mat[i][1]
        gas_mat2[i][1]=al_mat[i][1]
        gas_mat2[i][2]=mach_mat[i][1]
        gas_mat2[i][3]=min_mat[i][1]
        gas_mat2[i][4]=chem_mat[i][1]
        gas_mat2[i][5]=paper_mat[i][1]
        gas_mat2[i][6]=food_mat[i][1]
        gas_mat2[i][7]=other_mat[i][1]
        
    coal_mat2=np.zeros((7,8))
    for i in range(7):
        coal_mat2[i][0]=steel_mat[i][4]
        coal_mat2[i][1]=al_mat[i][4]
        coal_mat2[i][2]=mach_mat[i][4]
        coal_mat2[i][3]=min_mat[i][4]
        coal_mat2[i][4]=chem_mat[i][4]
        coal_mat2[i][5]=paper_mat[i][4]
        coal_mat2[i][6]=food_mat[i][4]
        coal_mat2[i][7]=other_mat[i][4]
        
    elec_mat2=np.zeros((7,8))#
    for i in range(7):
        elec_mat2[i][0]=steel_mat[i][6]
        elec_mat2[i][1]=al_mat[i][6]
        elec_mat2[i][2]=mach_mat[i][6]
        elec_mat2[i][3]=min_mat[i][6]
        elec_mat2[i][4]=chem_mat[i][6]
        elec_mat2[i][5]=paper_mat[i][6]
        elec_mat2[i][6]=food_mat[i][6]
        elec_mat2[i][7]=other_mat[i][6]
        
    #use matrix multiplication to assign energy to each conversion device
    oil_cd2=np.zeros(7)
    gas_cd2=np.zeros(7)
    biomass_cd2=np.zeros(7)
    coal_cd2=np.zeros(7)
    elec_cd2=np.zeros(7)
    for i in range(0,7):
        oil_cd2[i]=oil_mat2[i][0]*steelfull[0]+oil_mat2[i][1]*aluminiumfull[0]+oil_mat2[i][2]*machineryfull[0]+oil_mat2[i][3]*mineralfull[0]+oil_mat2[i][4]*chemicalfull[0]+oil_mat2[i][5]*paperfull[0]+oil_mat2[i][6]*foodfull[0]+oil_mat2[i][7]*otherfull[0]
        gas_cd2[i]=gas_mat2[i][0]*steelfull[1]+gas_mat2[i][1]*aluminiumfull[1]+gas_mat2[i][2]*machineryfull[1]+gas_mat2[i][3]*mineralfull[1]+gas_mat2[i][4]*chemicalfull[1]+gas_mat2[i][5]*paperfull[1]+gas_mat2[i][6]*foodfull[1]+gas_mat2[i][7]*otherfull[1]
        biomass_cd2[i]=coal_mat2[i][0]*steelfull[4]+coal_mat2[i][1]*aluminiumfull[4]+coal_mat2[i][2]*machineryfull[4]+coal_mat2[i][3]*mineralfull[4]+coal_mat2[i][4]*chemicalfull[4]+coal_mat2[i][5]*paperfull[4]+coal_mat2[i][6]*foodfull[4]+coal_mat2[i][7]*otherfull[4]
        coal_cd2[i]=coal_mat2[i][0]*steelfull[5]+coal_mat2[i][1]*aluminiumfull[5]+coal_mat2[i][2]*machineryfull[5]+coal_mat2[i][3]*mineralfull[5]+coal_mat2[i][4]*chemicalfull[5]+coal_mat2[i][5]*paperfull[5]+coal_mat2[i][6]*foodfull[5]+coal_mat2[i][7]*otherfull[5]
        elec_cd2[i]=elec_mat2[i][0]*steelfull[6]+elec_mat2[i][1]*aluminiumfull[6]+elec_mat2[i][2]*machineryfull[6]+elec_mat2[i][3]*mineralfull[6]+elec_mat2[i][4]*chemicalfull[6]+elec_mat2[i][5]*paperfull[6]+elec_mat2[i][6]*foodfull[6]+elec_mat2[i][7]*otherfull[6]
        
    #calculate energy used
    if Exergy=='Exergy':
        #energy efficiency (from Paoli) x quality factor (from cullen) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average exergy efficiency
            oilburneffex=0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #exergy used
        else:
            oilburnused=0
            
        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average exergy efficiency
            gasburneffex=0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #exergy used
        else:
            gasburnused=0
            
        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average exergy efficiency
            coalburneffex=0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #exergy used
        else:
            coalburnused=0
            
        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average exergy efficiency
            bioburneffex=0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #exergy used
        else:
            biomassburnused=0
        
        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(0.95*dieselengeff*oilengine)+(0.53*turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine
        
        heatexeff=0.87 #heat exchanger efficiency
        heatexused=0.15*heatexeff*heatex #exergy used
        
        elecheateff=1 #electric heater efficiency
        elecheatused=0.3*elecheateff*elecheater #exergy used
        
        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=0.93*elecmotoreff*elecmotor #exergy used
        
        electroneff=0.85 #electronics efficiency
        electronused=0.3*electroneff*applianceelec #exergy used
        
        lighteff=0.13 #lighting device efficiency
        lightused=0.9*lighteff*lightingdevice #exergy used
        
        renheateff=1 #renewable heater efficiency
        renheatused=0.3*renheateff*renheater #exergy used
        
    elif Exergy=='Energy':
        #energy efficiency (from Paoli) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average energy efficiency
            oilburneffex=(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #energy used
        else:
            oilburnused=0
            
        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average energy efficiency
            gasburneffex=(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #energy used
        else:
            gasburnused=0
            
        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average energy efficiency
            coalburneffex=(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #energy used
        else:
            coalburnused=0
            
        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average energy efficiency
            bioburneffex=(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #energy used
        else:
            biomassburnused=0
        
        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(dieselengeff*oilengine)+(turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine
        
        heatexeff=0.87 #heat exchanger efficiency
        heatexused=heatexeff*heatex #energy used
        
        elecheateff=1 #electric heater efficiency
        elecheatused=elecheateff*elecheater #energy used
        
        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=elecmotoreff*elecmotor #energy used
        
        electroneff=0.85 #electronics efficiency
        electronused=electroneff*applianceelec #energy used
        
        lighteff=0.13 #lighting device efficiency
        lightused=lighteff*lightingdevice #energy used
        
        renheateff=1 #renewable heater efficiency
        renheatused=renheateff*renheater #energy used
        
    #calculate energy lost
    oilburnloss=oilburner-oilburnused
    gasburnloss=gasburner-gasburnused
    coalburnloss=coalburner-coalburnused
    biomassburnloss=biomassburner-biomassburnused
    diesloss=(oilengine+coalengine+gasengine+biomassengine)-engused
    heatexloss=heatex-heatexused
    elecheatloss=elecheater-elecheatused
    elecmotorloss=elecmotor-elecmotorused
    electronloss=applianceelec-electronused
    lightloss=lightingdevice-lightused
    renheatloss=renheater-renheatused
    
    #values for Sankey labels
    PrimEngeff=np.sum(ind_used)+np.sum(indelec_used)+np.sum(ind_losses)
    DFUeff='DFU ({:.0f}PJ)'.format(np.sum(ind_used))
    TEGeff='TEG ({:.0f}PJ)'.format(np.sum(indelec_used))
    FuelLoss='Fuel Loss ({:.0f}PJ)'.format(np.sum(ind_losses))
    
    ConvDev=oilburner+gasburner+nuclearheater+renheater+biomassburner+coalburner+oilengine+gasengine+biomassengine+coalengine+elecmotor+elecheater+lightingdevice+applianceelec+heatex
    GenerationLoss='Generation Loss ({:.0f}PJ)'.format(eloss)
    
    Heateff='Heat ({:.0f}PJ)'.format(oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+elecheatused+heatexused+renheatused)
    Motioneff='Motion ({:.0f}PJ)'.format(engused+elecmotorused)
    Othereff='Other ({:.0f}PJ)'.format(electronused+lightused)
    ConversionLoss='Conversion Loss ({:.0f}PJ)'.format(oilburnloss+gasburnloss+coalburnloss+biomassburnloss+elecheatloss+heatexloss+diesloss+elecmotorloss+electronloss+lightloss+renheatloss)
    useful=oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+renheatused+elecheatused+heatexused+engused+elecmotorused+electronused+lightused
    UsefulEnergy='Useful \n Energy \n ({:.0f}PJ)'.format(useful)
    Loss='Loss \n ({:.0f}PJ)'.format(np.sum(ind_losses)+eloss+oilburnloss+gasburnloss+coalburnloss+biomassburnloss+elecheatloss+heatexloss+diesloss+elecmotorloss+electronloss+lightloss+renheatloss)
    
    #set up links for Efficiency Sankey
    linkseff = [
        #direct fuel use
        {'source': 'Oil', 'target': DFUeff, 'value': ind_used[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': DFUeff, 'value': ind_used[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': DFUeff, 'value': ind_used[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': DFUeff, 'value': ind_used[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': DFUeff, 'value': ind_used[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': DFUeff, 'value': ind_used[2], 'type': 'E', 'color': 'purple'},
        
        #fuel for electricity generation
        {'source': 'Oil', 'target': TEGeff, 'value': indelec_used[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': TEGeff, 'value': indelec_used[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': TEGeff, 'value': indelec_used[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': TEGeff, 'value': indelec_used[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': TEGeff, 'value': indelec_used[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': TEGeff, 'value': indelec_used[2], 'type': 'E', 'color': 'purple'},
    
        #fuel transformation losses
        {'source': 'Oil', 'target': FuelLoss, 'value': ind_losses[0], 'type': 'Z', 'color': 'gainsboro' },
        {'source': 'Coal', 'target': FuelLoss, 'value': ind_losses[5], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Gas', 'target': FuelLoss, 'value': ind_losses[1], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Biomass', 'target': FuelLoss, 'value': ind_losses[4], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Renewables', 'target': FuelLoss, 'value': ind_losses[3], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Nuclear', 'target': FuelLoss, 'value': ind_losses[2], 'type': 'Z', 'color': 'gainsboro'},
        
        #direct fuel to conversion devices for heat
        {'source': DFUeff, 'target': 'Oil Burner', 'value': oilburner, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUeff, 'target': 'Coal Burner', 'value': coalburner, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUeff, 'target': 'Gas Burner', 'value': gasburner, 'type': 'C', 'color': 'gold'},
        {'source': DFUeff, 'target': 'Biomass Burner', 'value': biomassburner, 'type': 'B', 'color': 'green'},
        {'source': DFUeff, 'target': 'Renewable Heater', 'value': renheater, 'type': 'F', 'color': 'dodgerblue'},
        {'source': DFUeff, 'target': 'Nuclear Heater', 'value': nuclearheater, 'type': 'E', 'color': 'purple'},
    
        #direct fuel to conversion devices for motion
        {'source': DFUeff, 'target': 'Engine', 'value': oilengine, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUeff, 'target': 'Engine', 'value': coalengine, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUeff, 'target': 'Engine', 'value': gasengine, 'type': 'C', 'color': 'gold'},
        {'source': DFUeff, 'target': 'Engine', 'value': biomassengine, 'type': 'B', 'color': 'green'}, 
        
        #electricity to conversion devices
        {'source': TEGeff, 'target': 'Electric Motor', 'value': elecmotor, 'type': 'H', 'color': 'silver' },
        {'source': TEGeff, 'target': 'Electric Heater', 'value': elecheater, 'type': 'H', 'color': 'silver'},
        {'source': TEGeff, 'target': 'Lighting Device', 'value': lightingdevice, 'type': 'H', 'color': 'silver'},
        {'source': TEGeff, 'target': 'Electronic', 'value': applianceelec, 'type': 'H', 'color': 'silver'},
        {'source': TEGeff, 'target': 'Heat Exchanger', 'value': heatex, 'type': 'G', 'color': 'red'},
        
        #electricity generation losses
        {'source': TEGeff, 'target': GenerationLoss, 'value': eloss, 'type': 'Z', 'color': 'gainsboro'},  
        
        #energy to provide motion
        {'source': 'Engine', 'target': Motioneff, 'value': engused, 'type': 'I', 'color':'lightblue'},
        {'source': 'Electric Motor', 'target': Motioneff, 'value': elecmotorused, 'type': 'I', 'color':'lightblue'},
    
        #energy to provide heat
        {'source': 'Oil Burner', 'target': Heateff, 'value': oilburnused, 'type': 'G', 'color':'red'},
        {'source': 'Gas Burner', 'target': Heateff, 'value': gasburnused, 'type': 'G', 'color':'red'},
        {'source': 'Coal Burner', 'target': Heateff, 'value': coalburnused, 'type': 'G', 'color':'red'},
        {'source': 'Biomass Burner', 'target': Heateff, 'value': biomassburnused, 'type':'G', 'color':'red'},
        {'source': 'Renewable Heater', 'target': Heateff, 'value': renheatused, 'type': 'G', 'color': 'red'},
        {'source': 'Nuclear Heater', 'target': Heateff, 'value': nuclearheater, 'type': 'E', 'color': 'red'},
        {'source': 'Electric Heater', 'target': Heateff, 'value': elecheatused, 'type': 'G', 'color':'red'},
        {'source': 'Heat Exchanger', 'target': Heateff, 'value': heatexused, 'type': 'G', 'color':'red'},
    
        #energy used for other purposes
        {'source': 'Lighting Device', 'target': Othereff, 'value': lightused, 'type': 'J', 'color':'black'},
        {'source': 'Electronic', 'target': Othereff, 'value': electronused, 'type': 'J', 'color':'black'},
        
        #device conversion losses
        {'source': 'Engine', 'target': ConversionLoss, 'value': diesloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Motor', 'target': ConversionLoss, 'value': elecmotorloss, 'type': 'Z', 'color':'gainsboro'},
    
        {'source': 'Oil Burner', 'target': ConversionLoss, 'value': oilburnloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Gas Burner', 'target': ConversionLoss, 'value': gasburnloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Coal Burner', 'target': ConversionLoss, 'value': coalburnloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Biomass Burner', 'target': ConversionLoss, 'value': biomassburnloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Heater', 'target': ConversionLoss, 'value': elecheatloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Heat Exchanger', 'target': ConversionLoss, 'value': heatexloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Renewable Heater', 'target': ConversionLoss, 'value': renheatloss, 'type': 'Z', 'color':'gainsboro'},
    
        {'source': 'Lighting Device', 'target': ConversionLoss, 'value': lightloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electronic', 'target': ConversionLoss, 'value': electronloss, 'type': 'Z', 'color':'gainsboro'},
        
        #energy lost
        {'source': ConversionLoss, 'target': Loss, 'value': oilburnloss+gasburnloss+coalburnloss+biomassburnloss+elecheatloss+heatexloss+diesloss+elecmotorloss+electronloss+lightloss+renheatloss, 'type': 'A', 'color': 'gainsboro'},#
        {'source': GenerationLoss, 'target': Loss, 'value': eloss, 'type': 'Z', 'color': 'gainsboro'},
        {'source': FuelLoss, 'target': Loss, 'value': np.sum(ind_losses), 'type': 'Z', 'color': 'gainsboro'},
    
        #energy used
        {'source': Heateff, 'target': UsefulEnergy, 'value': oilburnused+gasburnused+coalburnused+biomassburnused+elecheatused+heatexused+renheatused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Motioneff, 'target': UsefulEnergy, 'value': engused+elecmotorused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Othereff, 'target': UsefulEnergy, 'value': electronused+lightused, 'type': 'K', 'color': 'whitesmoke'}
    
    ]
    
    #groups for showing total primary energy supply and labelling conversion devices
    groupseff = [
        {'id': 'G', 'title': 'TPE ({:.0f}PJ)'.format(PrimEngeff), 'nodes': ['Oil', 'Coal', 'Gas', 'Biomass', 'Nuclear', 'Renewables']},
        {'id': 'G', 'title': 'Conversion Devices ({:.0f}PJ)'.format(ConvDev), 'nodes': ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Lighting Device']},
    ]
    
    #set order in which nodes appear
    ordereff = [
        [['Oil', 'Biomass', 'Gas', 'Coal', 'Nuclear', 'Renewables']],
        [DFUeff, TEGeff, FuelLoss],
        ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Electronic', 'Lighting Device', GenerationLoss],
        [[Heateff, Motioneff, Othereff, ConversionLoss]],
        [UsefulEnergy, Loss]
    
    ]
    
    eff=useful/PrimEng
    print('The Total', Exergy, 'Efficiency of the industrial sector in', Country,  'is {:.0f}%'.format(eff*100))
    
    return sankey(links=linkseff, groups=groupseff, linkLabelFormat='.0f', linkLabelMinWidth=10, order=ordereff, align_link_types=True).auto_save_png(Country+'_Efficiency_Sankey_'+Year+'.png')

###EFFICIENCY VALUES FUNCTION###
def efficiencyvalues(IEATES,IEATFC,electricity,heat,Country,Year,Exergy):
    '''
    Function to return efficiency values
    
    Inputs: 
        IEATES - Energy Supply Values from IEA
        IEATFC - Energy Consumption Values from IEA
        electricity - Electricity Consumption values from IEA
        heat - Heat Consumption values from IEA
        Country - name of country from IEA list
        Year - year between 1960 and 2019
        Exergy - Produce Diagram in Exergy or Energy Values
        
    Returns values for the efficiency of each stage of energy transfer,
    as well as the compound efficiency of each device.
    
    '''
    #convert supply to exergy values and combine oil and renewable products (exergy factors from https://doi.org/10.3390/en9090707)
    if Exergy=='Exergy':                          
        exergy=np.array([1.04*IEATES[0],1.03*IEATES[1],0.95*IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],1.13*IEATES[6],1.06*IEATES[7]])
        exergy_h=0.17*heat
    elif Exergy=='Energy':
        exergy=np.array([IEATES[0],IEATES[1],IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],IEATES[6],IEATES[7]])
        exergy_h=heat                          
    
    #calculate total electricity generation and direct fuel use
    tpes=np.zeros(len(exergy))
    losses=np.zeros(len(exergy))
    tfc=np.zeros(len(exergy))
    nonenergy=np.zeros(len(exergy))
    egeneration=np.zeros(len(exergy))
    hgeneration=np.zeros(len(exergy))
    for i in range (0,len(exergy)):
        tpes[i]=exergy[i][0]
        #combine all losses
        for j in range(1,3):
            losses[i]=losses[i]+exergy[i][j] 
        for j in range(9,23):
            losses[i]=losses[i]+exergy[i][j]
        tfc[i]=exergy[i][23]
        nonenergy[i]=exergy[i][24]
        #combine electriciy and heat generation from electricity, heating and CHP plants
        for j in range(3,5):
            egeneration[i]=egeneration[i]+exergy[i][j]
        for j in range(5,7):
            egeneration[i]=egeneration[i]+0.89*exergy[i][j]
            hgeneration[i]=hgeneration[i]+0.11*exergy[i][j]
        for j in range(7,9):
            hgeneration[i]=hgeneration[i]+exergy[i][j]
    
    dfu_used=tfc-nonenergy #total fuel used directly is total final consumption of fuel - non-energy use
    elec_used=-egeneration-hgeneration #total fuel used for electricity generation is combination of fuels to all plants from above (- sign to yield +ve values)
    
    #losses split proportionally between dfu & electricity generation
    dfu_losses=np.zeros(len(tpes))
    elec_losses=np.zeros(len(tpes))
    for i in range(len(tpes)):
        if tpes[i]+losses[i]==0: #to avoid divide zero errors
            dfu_losses[i]=0
            elec_losses[i]=0
        else: #- signs as losses[i] have -ve values
            dfu_losses[i]=-dfu_used[i]*(losses[i]/(tpes[i]+losses[i])) 
            elec_losses[i]=-elec_used[i]*(losses[i]/(tpes[i]+losses[i]))
    #convert from TJ to PJ
    direct_fuel_use=(dfu_used+dfu_losses)/(10**3)
    electricity_generation=(elec_used+elec_losses)/(10**3)
   
    
    #convert consumption to exergy values and combine oil and renewable products
    exergycons=np.array([1.04*IEATFC[0],1.03*IEATFC[1],0.95*IEATFC[2],IEATFC[3]+IEATFC[4]+IEATFC[5],1.11*IEATFC[6],1.06*IEATFC[7]])
    
    #calculate direct fuel use energy to industry
    industry=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        industry[i]=exergycons[i][0]
    industry=industry/(10**3)
    
    #scale to include losses
    for i in range(len(dfu_used)):
        if dfu_used[i]!=0:
            industry[i]=industry[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            
    #calculate total electricity (& heat) 
    totelec=electricity[0]+electricity[15]+electricity[24]+electricity[25]+electricity[26]+electricity[27]+electricity[28]
    totheat=exergy_h[0]+exergy_h[15]+exergy_h[24]+exergy_h[25]+exergy_h[26]+exergy_h[27]+exergy_h[28]
    
    if (totelec+totheat)!=0: #to avoid divide zero errors
        totelec_=totelec/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
        totheat_=totheat/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
    else:
        totelec_=0
        totheat_=0
        
    #scale electricity (& heat) flow to industry only
    if totelec!=0:
        elec_ind=(electricity[0]/totelec)*totelec_
    else:
        elec_ind=0
        
    if totheat!=0:
        heat_ind=(exergy_h[0]/totheat)*totheat_
    else:
        heat_ind=0
        
    #calculate energy to electricity from each fuel for industry
    totelecind=np.zeros(len(exergycons))
    totheatind=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecind[i]=(elec_ind/np.sum(electricity_generation))*electricity_generation[i]
            totheatind[i]=(heat_ind/np.sum(electricity_generation))*electricity_generation[i]
            
    #calculate direct use for industrial sub-sectors
    exergyInd=np.zeros((len(exergycons),29))
    for j in range(0,len(exergycons)):
        for i in range(0,29):
            if dfu_used[j]!=0: #to avoid divide zero errors
                exergyInd[j][i]=exergycons[j][i]*direct_fuel_use[j]/(dfu_used[j]/10**3)
                
    steel=np.zeros(len(exergycons))
    aluminium=np.zeros(len(exergycons))
    machinery=np.zeros(len(exergycons))
    mineral=np.zeros(len(exergycons))
    chemical=np.zeros(len(exergycons))
    paper=np.zeros(len(exergycons))
    food=np.zeros(len(exergycons))
    other=np.zeros(len(exergycons))
    
    for i in range(0,len(exergycons)):
        steel[i]=exergyInd[i][4]/(10**3)
        aluminium[i]=exergyInd[i][6]/(10**3)
        machinery[i]=(exergyInd[i][8]+exergyInd[i][9])/(10**3)
        mineral[i]=exergyInd[i][7]/(10**3)
        chemical[i]=exergyInd[i][5]/(10**3)
        paper[i]=(exergyInd[i][11]+exergyInd[i][12])/(10**3)
        food[i]=exergyInd[i][10]/(10**3)
        other[i]=(exergyInd[i][1]+exergyInd[i][2]+exergyInd[i][13]+exergyInd[i][14])/(10**3)
        
    #calculate electricity to industrial sub-sectors  
    if totelec!=0:
        elec_steel=(electricity[4]/totelec)*totelec_
        elec_aluminium=(electricity[6]/totelec)*totelec_
        elec_machinery=((electricity[8]+electricity[9])/totelec)*totelec_
        elec_mineral=(electricity[7]/totelec)*totelec_
        elec_chemical=(electricity[5]/totelec)*totelec_
        elec_paper=((electricity[11]+electricity[12])/totelec)*totelec_
        elec_food=(electricity[10]/totelec)*totelec_
        elec_other=((electricity[1]+electricity[2]+electricity[13]+electricity[14])/totelec)*totelec_
    else:
        elec_steel=0
        elec_aluminium=0
        elec_machinery=0
        elec_mineral=0
        elec_chemical=0
        elec_paper=0
        elec_food=0
        elec_other=0
        
    #calculate heat to industrial sub-sectors  
    if totheat!=0:
        heat_steel=(exergy_h[4]/totheat)*totheat_
        heat_aluminium=(exergy_h[6]/totheat)*totheat_
        heat_machinery=((exergy_h[8]+exergy_h[9])/totheat)*totheat_
        heat_mineral=(exergy_h[7]/totheat)*totheat_
        heat_chemical=(exergy_h[5]/totheat)*totheat_
        heat_paper=((exergy_h[11]+exergy_h[12])/totheat)*totheat_
        heat_food=(exergy_h[10]/totheat)*totheat_
        heat_other=((exergy_h[1]+exergy_h[2]+exergy_h[13]+exergy_h[14])/totheat)*totheat_
    else:
        heat_steel=0
        heat_aluminium=0
        heat_machinery=0
        heat_mineral=0
        heat_chemical=0
        heat_paper=0
        heat_food=0
        heat_other=0
        
    #append electricity and heat values to sub-sector fuel consumption arrays
    steelfull=np.append(steel, [elec_steel, heat_steel])
    aluminiumfull=np.append(aluminium, [elec_aluminium, heat_aluminium])
    machineryfull=np.append(machinery, [elec_machinery, heat_machinery])
    mineralfull=np.append(mineral, [elec_mineral, heat_mineral])
    chemicalfull=np.append(chemical, [elec_chemical, heat_chemical])
    paperfull=np.append(paper, [elec_paper, heat_paper])
    foodfull=np.append(food, [elec_food, heat_food])
    otherfull=np.append(other, [elec_other, heat_other])
    
    #define allocation matrices, based on US industry data - used to assign fuels to passive systems below
    #rows are passive systems, columns are fuels (oil, gas, nuclear, renewables, biomass, coal, electricity, heat))
    steel_mat = np.array([[0.00  , 0.10  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.39  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 1.00  , 1.00  , 0.53  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.03  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#appliance
                         [1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    al_mat = np.array([[0.00  , 0.13  , 1.00  , 0.00  , 0.13  , 0.13  , 0.01  , 0.00  ],#steam
                         [0.25  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.24  , 0.00  ],#driven
                         [0.25  , 0.76  , 0.00  , 0.00  , 0.76  , 0.76  , 0.65  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.03  , 0.00  ],#light
                         [0.00  , 0.09  , 0.00  , 1.00  , 0.09  , 0.09  , 0.04  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.02  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                      ])
    
    mach_mat = np.array([[0.15  , 0.16  , 1.00  , 0.00  , 0.16  , 0.16  , 0.01  , 0.00  ],#steam
                         [0.14  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.49  , 0.00  ],#driven
                         [0.07  , 0.45  , 0.00  , 0.00  , 0.45  , 0.45  , 0.16  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.11  , 0.00  ],#light
                         [0.14  , 0.35  , 0.00  , 1.00  , 0.35  , 0.35  , 0.19  , 1.00  ],#spaceheat
                         [0.00  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.03  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])
    
    min_mat = np.array([[0.00  , 0.03  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.38  , 0.08  , 0.00  , 0.00  , 0.10  , 0.10  , 0.60  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 0.90  , 0.90  , 0.28  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.62  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                       ])
    
    chem_mat = np.array([[0.50  , 0.52  , 1.00  , 0.00  , 0.87  , 0.87  , 0.01  , 0.00  ],#steam
                         [0.00  , 0.04  , 0.00  , 0.00  , 0.00  , 0.00  , 0.63  , 0.00  ],#driven
                         [0.10  , 0.41  , 0.00  , 0.00  , 0.13  , 0.13  , 0.25  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.02  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.40  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                        ])                 
    
    paper_mat = np.array([[0.36  , 0.63  , 1.00  , 0.00  , 0.98  , 0.98  , 0.04  , 0.00  ],#steam
                         [0.04  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.78  , 0.00  ],#driven
                         [0.08  , 0.30  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.06  , 1.00  ],#spaceheat
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.52  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    food_mat = np.array([[0.59  , 0.59  , 1.00  , 0.00  , 0.79  , 0.79  , 0.03  , 0.00  ],#steam
                         [0.00  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.69  , 0.00  ],#driven
                         [0.00  , 0.27  , 0.00  , 0.00  , 0.21  , 0.21  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#light
                         [0.08  , 0.08  , 0.00  , 1.00  , 0.00  , 0.00  , 0.11  , 1.00  ],#spaceheat
                         [0.08  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.25  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])
    
    other_mat = np.array([[0.13  , 0.34  , 1.00  , 0.00  , 1.00  , 1.00  , 0.01  , 0.00  ],#steam
                         [0.13  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.73  , 0.00  ],#driven
                         [0.71  , 0.61  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.06  , 0.00  ],#light
                         [0.00  , 0.04  , 0.00  , 1.00  , 0.00  , 0.00  , 0.09  , 1.00  ],#spaceheat
                         [0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    #import data on share of steel from EAF
    import pandas as pd
    df=pd.read_csv('SteelShares2023.csv')
    try:
        EAF=float(df['EAF'][df['Country'] == Country].values[0])
    except:
        EAF=float(df['EAF'][df['Country'] == 'World'].values[0])
        
    #calculate new allocation matrices for steel, based on share of EAF
    x=(442.01*EAF)/((442.01*EAF)+(4128.05*(1-EAF)))
    z1=0.943*x+0.045*(1-x)
    z2=0.928*(1-x)
    z3=0.057*x+0.027*(1-x)
    gamma=0
        
    if x==1:
        if electricity[4]!=0:
            gammaprime=(0.02*IEATFC[1][4]/electricity[4])*(z1/z3)
            steel_mat[2][6]=0.4+0.6*gammaprime
            steel_mat[1][6]=0.5*(1-gammaprime)
            steel_mat[3][6]=0.04*(1-gammaprime)
            steel_mat[4][6]=0.05*(1-gammaprime)
            steel_mat[5][6]=0.01*(1-gammaprime)
    else:
        if electricity[4]!=0:
            gamma=(IEATFC[7][4]/electricity[4])*(z1/z2)
            steel_mat[2][6]=0.4+0.6*gamma
            steel_mat[1][6]=0.5*(1-gamma)
            steel_mat[3][6]=0.04*(1-gamma)
            steel_mat[4][6]=0.05*(1-gamma)
            steel_mat[5][6]=0.01*(1-gamma)
        if IEATFC[1][4]!=0:
            delta=(IEATFC[7][4]/IEATFC[1][4])*(z3/z2)
            steel_mat[2][1]=0.83+0.17*delta
            steel_mat[0][1]=0.1*(1-delta)
            steel_mat[1][1]=0.01*(1-delta)
            steel_mat[4][1]=0.05*(1-delta)
            steel_mat[5][1]=0.01*(1-delta)
            
    #use matrix multiplication to assign fuel to each passive system
    steel_ps=np.zeros(7)
    al_ps=np.zeros(7)
    mach_ps=np.zeros(7)
    min_ps=np.zeros(7)
    chem_ps=np.zeros(7)
    paper_ps=np.zeros(7)
    food_ps=np.zeros(7)
    other_ps=np.zeros(7)
    for i in range(0,len(steelfull)):
        for j in range(0,7):
            steel_ps[j]=steel_ps[j]+steelfull[i]*steel_mat[j][i]
            al_ps[j]=al_ps[j]+aluminiumfull[i]*al_mat[j][i]
            mach_ps[j]=mach_ps[j]+machineryfull[i]*mach_mat[j][i]
            min_ps[j]=min_ps[j]+mineralfull[i]*min_mat[j][i]
            chem_ps[j]=chem_ps[j]+chemicalfull[i]*chem_mat[j][i]
            paper_ps[j]=paper_ps[j]+paperfull[i]*paper_mat[j][i]
            food_ps[j]=food_ps[j]+foodfull[i]*food_mat[j][i]
            other_ps[j]=other_ps[j]+otherfull[i]*other_mat[j][i]
            
    #define matrices for assigning fuels to conversion devices
    #rows are purposes of converson devices, columns are industries (steel, aluminium, machinery, mineral, chemical, paper, food, other)
    oil_mat = np.array([[1.00, 0.75, 0.64, 1.00, 0.40, 0.56, 0.25, 0.13],#motion
                       [0.00, 0.25, 0.36, 0.00, 0.60, 0.44, 0.67, 0.84],#heat
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.08, 0.03]])#appliance
    
    gas_mat = np.array([[steel_mat[1][1]+steel_mat[6][1], 0.01, 0.02, 0.08, 0.04, 0.02, 0.03, 0.01],#motion
                       [steel_mat[0][1]+steel_mat[2][1]+steel_mat[4][1], 0.98, 0.96, 0.91, 0.95, 0.98, 0.94, 0.99],#heat
                       [steel_mat[3][1], 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [steel_mat[5][1], 0.01, 0.02, 0.01, 0.01, 0.00, 0.03, 0.00]])#appliance
    
    coal_mat = np.array([[0.00, 0.01, 0.02, 0.10, 0.00, 0.02, 0.00, 0.00],#motion
                        [1.00, 0.98, 0.96, 0.90, 1.00, 0.98, 1.00, 1.00],#heat
                        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                        [0.00, 0.01, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00]])#appliance
    
    elec_mat = np.array([[steel_mat[1][6]+steel_mat[6][6], 0.25, 0.50, 0.60, 0.63, 0.78, 0.70, 0.73],#motion
                        [steel_mat[0][6]+steel_mat[2][6]+steel_mat[4][6], 0.70, 0.36, 0.33, 0.31, 0.15, 0.19, 0.19],#heat
                        [steel_mat[3][6], 0.03, 0.11, 0.05, 0.04, 0.05, 0.09, 0.06],#light
                        [steel_mat[5][6], 0.02, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02]])#appliance
    
    #use matrix multiplication to assign energy to each conversion device
    oil_cd=np.zeros(4)
    gas_cd=np.zeros(4)
    biomass_cd=np.zeros(4)
    coal_cd=np.zeros(4)
    elec_cd=np.zeros(4)
    for i in range(0,4):
        oil_cd[i]=oil_mat[i][0]*steelfull[0]+oil_mat[i][1]*aluminiumfull[0]+oil_mat[i][2]*machineryfull[0]+oil_mat[i][3]*mineralfull[0]+oil_mat[i][4]*chemicalfull[0]+oil_mat[i][5]*paperfull[0]+oil_mat[i][6]*foodfull[0]+oil_mat[i][7]*otherfull[0]
        gas_cd[i]=gas_mat[i][0]*steelfull[1]+gas_mat[i][1]*aluminiumfull[1]+gas_mat[i][2]*machineryfull[1]+gas_mat[i][3]*mineralfull[1]+gas_mat[i][4]*chemicalfull[1]+gas_mat[i][5]*paperfull[1]+gas_mat[i][6]*foodfull[1]+gas_mat[i][7]*otherfull[1]
        biomass_cd[i]=coal_mat[i][0]*steelfull[4]+coal_mat[i][1]*aluminiumfull[4]+coal_mat[i][2]*machineryfull[4]+coal_mat[i][3]*mineralfull[4]+coal_mat[i][4]*chemicalfull[4]+coal_mat[i][5]*paperfull[4]+coal_mat[i][6]*foodfull[4]+coal_mat[i][7]*otherfull[4]
        coal_cd[i]=coal_mat[i][0]*steelfull[5]+coal_mat[i][1]*aluminiumfull[5]+coal_mat[i][2]*machineryfull[5]+coal_mat[i][3]*mineralfull[5]+coal_mat[i][4]*chemicalfull[5]+coal_mat[i][5]*paperfull[5]+coal_mat[i][6]*foodfull[5]+coal_mat[i][7]*otherfull[5]
        elec_cd[i]=elec_mat[i][0]*steelfull[6]+elec_mat[i][1]*aluminiumfull[6]+elec_mat[i][2]*machineryfull[6]+elec_mat[i][3]*mineralfull[6]+elec_mat[i][4]*chemicalfull[6]+elec_mat[i][5]*paperfull[6]+elec_mat[i][6]*foodfull[6]+elec_mat[i][7]*otherfull[6]
    
    #assumed that all nuclear, renewable and direct heat contributes to heat
    heat_cd=steelfull[7]+aluminiumfull[7]+machineryfull[7]+mineralfull[7]+chemicalfull[7]+paperfull[7]+foodfull[7]+otherfull[7]
    
    #values for Sankey labels
    PrimEng=np.sum(industry)+np.sum(totelecind)+np.sum(totheatind)
    
    #calculate losses in fuel transformation
    ind_used=np.zeros(len(industry))
    inddfu_losses=np.zeros(len(industry))
    indelec_used=np.zeros(len(industry))
    indelec_losses=np.zeros(len(industry))
    for i in range(len(industry)):
        if direct_fuel_use[i]!=0: #to avoid divide zero errors
            ind_used[i]=industry[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
            inddfu_losses[i]=industry[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
        if electricity_generation[i]!=0: #to avoid divide zero errors
            indelec_used[i]=(totelecind[i]+totheatind[i])*elec_used[i]/(electricity_generation[i]*1000)
            indelec_losses[i]=(totelecind[i]+totheatind[i])*elec_losses[i]/(electricity_generation[i]*1000)
        ind_losses=indelec_losses+inddfu_losses
            
    #calculate energy to each conversion device
    if np.sum(oil_cd)!=0: #to avoid divide zero errors
        oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
        oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
    else:
        oilburner=0
        oilengine=0
        
    if np.sum(gas_cd)!=0: #to avoid divide zero errors
        gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
        gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
    else:
        gasburner=0
        gasengine=0
    
    nuclearheater=ind_used[2] #in case nuclear is used directly
    renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating
    
    if np.sum(biomass_cd)!=0: #to avoid divide zero errors
        biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
        biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
    else:
        biomassburner=0
        biomassengine=0
        
    if np.sum(coal_cd)!=0: #to avoid divide zero errors
        coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
        coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
    else:
        coalburner=0
        coalengine=0
        
    #calculate losses in electricity generation
    if np.sum(egeneration)!=0: #to avoid divide zero errors
        eleceff=totelec/(-np.sum(egeneration))
    else:
        eleceff=0
    if np.sum(hgeneration)!=0:
        heateff=totheat/(-np.sum(hgeneration))
    else:
        heateff=0
    
    heatex=heateff*heat_cd
    elecmotor=eleceff*elec_cd[1]
    elecheater=eleceff*elec_cd[0]
    lightingdevice=eleceff*elec_cd[2]
    applianceelec=eleceff*elec_cd[3]
    
    #create new matrices with all passive systems
    oil_mat2=np.zeros((7,8))
    for i in range(7):
        oil_mat2[i][0]=steel_mat[i][0]
        oil_mat2[i][1]=al_mat[i][0]
        oil_mat2[i][2]=mach_mat[i][0]
        oil_mat2[i][3]=min_mat[i][0]
        oil_mat2[i][4]=chem_mat[i][0]
        oil_mat2[i][5]=paper_mat[i][0]
        oil_mat2[i][6]=food_mat[i][0]
        oil_mat2[i][7]=other_mat[i][0]
        
    gas_mat2=np.zeros((7,8))
    for i in range(7):
        gas_mat2[i][0]=steel_mat[i][1]
        gas_mat2[i][1]=al_mat[i][1]
        gas_mat2[i][2]=mach_mat[i][1]
        gas_mat2[i][3]=min_mat[i][1]
        gas_mat2[i][4]=chem_mat[i][1]
        gas_mat2[i][5]=paper_mat[i][1]
        gas_mat2[i][6]=food_mat[i][1]
        gas_mat2[i][7]=other_mat[i][1]
        
    coal_mat2=np.zeros((7,8))
    for i in range(7):
        coal_mat2[i][0]=steel_mat[i][4]
        coal_mat2[i][1]=al_mat[i][4]
        coal_mat2[i][2]=mach_mat[i][4]
        coal_mat2[i][3]=min_mat[i][4]
        coal_mat2[i][4]=chem_mat[i][4]
        coal_mat2[i][5]=paper_mat[i][4]
        coal_mat2[i][6]=food_mat[i][4]
        coal_mat2[i][7]=other_mat[i][4]
        
    elec_mat2=np.zeros((7,8))#
    for i in range(7):
        elec_mat2[i][0]=steel_mat[i][6]
        elec_mat2[i][1]=al_mat[i][6]
        elec_mat2[i][2]=mach_mat[i][6]
        elec_mat2[i][3]=min_mat[i][6]
        elec_mat2[i][4]=chem_mat[i][6]
        elec_mat2[i][5]=paper_mat[i][6]
        elec_mat2[i][6]=food_mat[i][6]
        elec_mat2[i][7]=other_mat[i][6]
        
    #use matrix multiplication to assign energy to each conversion device
    oil_cd2=np.zeros(7)
    gas_cd2=np.zeros(7)
    biomass_cd2=np.zeros(7)
    coal_cd2=np.zeros(7)
    elec_cd2=np.zeros(7)
    for i in range(0,7):
        oil_cd2[i]=oil_mat2[i][0]*steelfull[0]+oil_mat2[i][1]*aluminiumfull[0]+oil_mat2[i][2]*machineryfull[0]+oil_mat2[i][3]*mineralfull[0]+oil_mat2[i][4]*chemicalfull[0]+oil_mat2[i][5]*paperfull[0]+oil_mat2[i][6]*foodfull[0]+oil_mat2[i][7]*otherfull[0]
        gas_cd2[i]=gas_mat2[i][0]*steelfull[1]+gas_mat2[i][1]*aluminiumfull[1]+gas_mat2[i][2]*machineryfull[1]+gas_mat2[i][3]*mineralfull[1]+gas_mat2[i][4]*chemicalfull[1]+gas_mat2[i][5]*paperfull[1]+gas_mat2[i][6]*foodfull[1]+gas_mat2[i][7]*otherfull[1]
        biomass_cd2[i]=coal_mat2[i][0]*steelfull[4]+coal_mat2[i][1]*aluminiumfull[4]+coal_mat2[i][2]*machineryfull[4]+coal_mat2[i][3]*mineralfull[4]+coal_mat2[i][4]*chemicalfull[4]+coal_mat2[i][5]*paperfull[4]+coal_mat2[i][6]*foodfull[4]+coal_mat2[i][7]*otherfull[4]
        coal_cd2[i]=coal_mat2[i][0]*steelfull[5]+coal_mat2[i][1]*aluminiumfull[5]+coal_mat2[i][2]*machineryfull[5]+coal_mat2[i][3]*mineralfull[5]+coal_mat2[i][4]*chemicalfull[5]+coal_mat2[i][5]*paperfull[5]+coal_mat2[i][6]*foodfull[5]+coal_mat2[i][7]*otherfull[5]
        elec_cd2[i]=elec_mat2[i][0]*steelfull[6]+elec_mat2[i][1]*aluminiumfull[6]+elec_mat2[i][2]*machineryfull[6]+elec_mat2[i][3]*mineralfull[6]+elec_mat2[i][4]*chemicalfull[6]+elec_mat2[i][5]*paperfull[6]+elec_mat2[i][6]*foodfull[6]+elec_mat2[i][7]*otherfull[6]
        
    #calculate energy used
    if Exergy=='Exergy':
        #energy efficiency (from Paoli) x quality factor (from cullen) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average exergy efficiency
            oilburneffex=0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #exergy used
        else:
            oilburnused=0
            
        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average exergy efficiency
            gasburneffex=0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #exergy used
        else:
            gasburnused=0
            
        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average exergy efficiency
            coalburneffex=0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #exergy used
        else:
            coalburnused=0
            
        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average exergy efficiency
            bioburneffex=0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #exergy used
        else:
            biomassburnused=0
        
        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(0.95*dieselengeff*oilengine)+(0.53*turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine
        
        heatexeff=0.87 #heat exchanger efficiency
        heatexused=0.15*heatexeff*heatex #exergy used
        
        elecheateff=1 #electric heater efficiency
        elecheatused=0.3*elecheateff*elecheater #exergy used
        
        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=0.93*elecmotoreff*elecmotor #exergy used
        
        electroneff=0.85 #electronics efficiency
        electronused=0.3*electroneff*applianceelec #exergy used
        
        lighteff=0.13 #lighting device efficiency
        lightused=0.9*lighteff*lightingdevice #exergy used
        
        renheateff=1 #renewable heater efficiency
        renheatused=0.3*renheateff*renheater #exergy used
        
    elif Exergy=='Energy':
        #energy efficiency (from Paoli) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average energy efficiency
            oilburneffex=(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #energy used
        else:
            oilburnused=0
            
        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average energy efficiency
            gasburneffex=(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #energy used
        else:
            gasburnused=0
            
        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average energy efficiency
            coalburneffex=(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #energy used
        else:
            coalburnused=0
            
        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average energy efficiency
            bioburneffex=(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #energy used
        else:
            biomassburnused=0
        
        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(dieselengeff*oilengine)+(turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine
        
        heatexeff=0.87 #heat exchanger efficiency
        heatexused=heatexeff*heatex #energy used
        
        elecheateff=1 #electric heater efficiency
        elecheatused=elecheateff*elecheater #energy used
        
        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=elecmotoreff*elecmotor #energy used
        
        electroneff=0.85 #electronics efficiency
        electronused=electroneff*applianceelec #energy used
        
        lighteff=0.13 #lighting device efficiency
        lightused=lighteff*lightingdevice #energy used
        
        renheateff=1 #renewable heater efficiency
        renheatused=renheateff*renheater #energy used
    
    #Useful Energy
    useful=oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+renheatused+elecheatused+heatexused+engused+elecmotorused+electronused+lightused

    
    #calculate a number of efficiency values
    fueleff=np.zeros(6)
    for i in range(6):
        if (ind_losses[i]+ind_used[i]+indelec_used[i])!=0: #to avoid divide zero errors
            fueleff[i]=(ind_used[i]+indelec_used[i])/(ind_losses[i]+ind_used[i]+indelec_used[i])
    if (np.sum(ind_losses)+np.sum(ind_used)+np.sum(indelec_used))!=0: #to avoid divide zero errors
        totfueleff=(np.sum(ind_used)+np.sum(indelec_used))/(np.sum(ind_losses)+np.sum(ind_used)+np.sum(indelec_used))
    if np.sum(indelec_used)!=0: #to avoid divide zero errors
        elecfeff=(np.sum(fueleff*indelec_used))/(np.sum(indelec_used))
    if (oilengine+coalengine+gasengine+biomassengine)!=0: #to avoid divide zero errors
        engfeff=(fueleff[0]*oilengine+fueleff[1]*gasengine+fueleff[4]*biomassengine+fueleff[5]*coalengine)/((oilengine+coalengine+gasengine+biomassengine))
    
    if (np.sum(elec_cd)+heat_cd)!=0: #to avoid divide zero erros
        if ((np.sum(elec_cd)/(np.sum(elec_cd)+heat_cd))*np.sum(indelec_used))!=0: #to avoid divide zero erros
            eleceff=(elecmotor+elecheater+applianceelec+lightingdevice)/((np.sum(elec_cd)/(np.sum(elec_cd)+heat_cd))*np.sum(indelec_used))
        if ((heat_cd/(np.sum(elec_cd)+heat_cd))*np.sum(indelec_used))!=0: #to avoid divide zero erros
            heateff=heatex/((heat_cd/(np.sum(elec_cd)+heat_cd))*np.sum(indelec_used))
    if np.sum(indelec_used)!=0: #to avoid divide zero erros
        alleleceff=(heatex+elecmotor+elecheater+applianceelec+lightingdevice)/(np.sum(indelec_used))
    
    if oilburner!=0: #to avoid divide zero errors
        oilburnefficiency=oilburnused/oilburner
    if gasburner!=0: #to avoid divide zero errors
        gasburnefficiency=gasburnused/gasburner
    if biomassburner!=0: #to avoid divide zero errors
        biomassburnefficiency=biomassburnused/biomassburner
    if coalburner!=0: #to avoid divide zero errors
        coalburnefficiency=coalburnused/coalburner
    if (oilengine+coalengine+oilengine+biomassengine)!=0: #to avoid divide zero errors
        dieselengefficiency=engused/(oilengine+coalengine+oilengine+biomassengine)
    if heatex!=0: #to avoid divide zero errors
        heatexefficiency=heatexused/heatex
    if elecheater!=0: #to avoid divide zero errors
        elecheatefficiency=elecheatused/elecheater
    if elecmotor!=0: #to avoid divide zero errors
        elecmotorefficiency=elecmotorused/elecmotor
    if applianceelec!=0: #to avoid divide zero errors
        electronefficiency=electronused/applianceelec
    if lightingdevice!=0: #to avoid divide zero errors
        lightefficiency=lightused/lightingdevice
    if renheater!=0: #to avoid divide zero errors
        renheatefficiency=renheatused/renheater
    
    try:
        oilburneffcomp=fueleff[0]*oilburnefficiency
    except:
        pass
    try:
        gasburneffcomp=fueleff[1]*gasburnefficiency
    except:
        pass
    try:
        coalburneffcomp=fueleff[5]*coalburnefficiency
    except:
        pass
    try:
        biomassburneffcomp=fueleff[4]*biomassburnefficiency
    except:
        pass
    try:
        dieselengeffcomp=engfeff*dieselengefficiency
    except:
        pass
    try:
        heatexeffcomp=totfueleff*heateff*heatexefficiency
    except:
        pass
    try:
        elecheateffcomp=totfueleff*eleceff*elecheatefficiency
    except:
        pass
    try:
        elecmotoreffcomp=totfueleff*eleceff*elecmotorefficiency
    except:
        pass
    try:
        electroneffcomp=totfueleff*eleceff*electronefficiency
    except:
        pass
    try:
        lighteffcomp=totfueleff*eleceff*lightefficiency
    except:
        pass
    try:
        renheateffcomp=fueleff[3]*renheatefficiency
    except:
        pass

    if PrimEng!=0: #to avoid divide zero errors
        eff=useful/PrimEng
        
    try:
        print('The Efficiency of Oil Transformation is {:.0f}%'.format(fueleff[0]*100))
    except:
        pass
    try:
        print('The Efficiency of Gas Transformation is {:.0f}%'.format(fueleff[1]*100))
    except:
        pass
    try:
        print('The Efficiency of Nuclear Transformation is {:.0f}%'.format(fueleff[2]*100))
    except:
        pass
    try:
        print('The Efficiency of Renewable Transformation is {:.0f}%'.format(fueleff[3]*100))
    except:
        pass
    try:
        print('The Efficiency of Biomass Transformation is {:.0f}%'.format(fueleff[4]*100))
    except:
        pass
    try:
        print('The Efficiency of Coal Transformation is {:.0f}%'.format(fueleff[5]*100))
    except:
        pass
    try:
        print('The Efficiency of Fuel Transformation for Electricity Generation is {:.0f}%'.format(elecfeff*100))
    except:
        pass
    try:
        print('The Efficiency of Fuel Transformation for Engines is {:.0f}%'.format(engfeff*100))
    except:
        pass
    try:
        print('The Total Efficiency of Fuel Transformation is {:.0f}%'.format(totfueleff*100))
    except:
        pass
    
    try:
        print('The Efficiency of Electricity Production in', Country, 'is {0:.0f}%'.format(eleceff*100))
    except:
        pass
    try:
        print('The Efficiency of Heat Production in', Country, 'is {0:.0f}% '.format(heateff*100))
    except:
        pass
    try:
        print('The Average Efficiency of both Heat and Electricity Production in', Country, 'is {0:.0f}%'.format(alleleceff*100))
    except:
        pass
    
    try:
        print('The Efficiency of Oil Burner is {:.0f}%'.format(oilburnefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Biomass Burner is {:.0f}%'.format(biomassburnefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Gas Burner is {:.0f}%'.format(gasburnefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Coal Burner is {:.0f}%'.format(coalburnefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Heat Exchanger is {:.0f}%'.format(heatexefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Electric Heater is {:.0f}%'.format(elecheatefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Renewable Heater is {:.0f}%'.format(renheatefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Engine is {:.0f}%'.format(dieselengefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Electric Motor is {:.0f}%'.format(elecmotorefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Electronic is {:.0f}%'.format(electronefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Lighting Device is {:.0f}%'.format(lightefficiency*100))
    except:
        pass
    
    try:
        print('The Compound Efficiency of Oil Burner is {:.0f}%'.format(oilburneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Biomass Burner is {:.0f}%'.format(biomassburneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Gas Burner is {:.0f}%'.format(gasburneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Coal Burner is {:.0f}%'.format(coalburneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Heat Exchanger is {:.0f}%'.format(heatexeffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Electric Heater is {:.0f}%'.format(elecheateffcomp*100))#
    except:
        pass
    try:
        print('The Compound Efficiency of Renewable Heater is {:.0f}%'.format(renheateffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Engine is {:.0f}%'.format(dieselengeffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Electric Motor is {:.0f}%'.format(elecmotoreffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Electronic is {:.0f}%'.format(electroneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Lighting Device is {:.0f}%'.format(lighteffcomp*100))
    except:
        pass
    
    try:
        print('The Total', Exergy, 'Efficiency of the industrial sector in', Country,  'is {:.0f}%'.format(eff*100))
    except:
        pass
    return

###CHANGING DEVICE EFFICIENCY SANKEY GENERATOR FUNCTION###
def change(IEATES,IEATFC,electricity,heat,Country,Year,Exergy,Device,Value):
    '''
    Function to return a Sankey Diagram with altered
    engineering device efficiency
    
    Inputs: 
        IEATES - Energy Supply Values from IEA
        IEATFC - Energy Consumption Values from IEA
        electricity - Electricity Consumption values from IEA
        heat - Heat Consumption values from IEA
        Country - name of country from IEA list
        Year - year between 1960 and 2019
        Exergy - Produce Diagram in Exergy or Energy Values
        Device - name of engineering device for which
                the efficiency is to be altered
        Value - new value of engineering device efficiency
        
    Returns a Sankey diagram for the given year and country 
    with the new device efficiency taken into account (and 
    prints the new overall efficiency, the change in overall
    efficiency and the change in primary energy demand)
    
    '''
    #convert supply to exergy values and combine oil and renewable products (exergy factors from https://doi.org/10.3390/en9090707)                          
    if Exergy=='Exergy':                          
        exergy=np.array([1.04*IEATES[0],1.03*IEATES[1],0.95*IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],1.13*IEATES[6],1.06*IEATES[7]])
        exergy_h=0.17*heat
    elif Exergy=='Energy':
        exergy=np.array([IEATES[0],IEATES[1],IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],IEATES[6],IEATES[7]])
        exergy_h=heat    
    
    #calculate total electricity generation and direct fuel use
    tpes=np.zeros(len(exergy))
    losses=np.zeros(len(exergy))
    tfc=np.zeros(len(exergy))
    nonenergy=np.zeros(len(exergy))
    egeneration=np.zeros(len(exergy))
    hgeneration=np.zeros(len(exergy))
    for i in range (0,len(exergy)):
        tpes[i]=exergy[i][0]
        #combine all losses
        for j in range(1,3):
            losses[i]=losses[i]+exergy[i][j] 
        for j in range(9,23):
            losses[i]=losses[i]+exergy[i][j]
        tfc[i]=exergy[i][23]
        nonenergy[i]=exergy[i][24]
        #combine electriciy and heat generation from electricity, heating and CHP plants
        for j in range(3,5):
            egeneration[i]=egeneration[i]+exergy[i][j]
        for j in range(5,7):
            egeneration[i]=egeneration[i]+0.89*exergy[i][j]
            hgeneration[i]=hgeneration[i]+0.11*exergy[i][j]
        for j in range(7,9):
            hgeneration[i]=hgeneration[i]+exergy[i][j]
    
    dfu_used=tfc-nonenergy #total fuel used directly is total final consumption of fuel - non-energy use
    elec_used=-egeneration-hgeneration #total fuel used for electricity generation is combination of fuels to all plants from above (- sign to yield +ve values)
    
    #losses split proportionally between dfu & electricity generation
    dfu_losses=np.zeros(len(tpes))
    elec_losses=np.zeros(len(tpes))
    for i in range(len(tpes)):
        if tpes[i]+losses[i]==0: #to avoid divide zero errors
            dfu_losses[i]=0
            elec_losses[i]=0
        else: #- signs as losses[i] have -ve values
            dfu_losses[i]=-dfu_used[i]*(losses[i]/(tpes[i]+losses[i])) 
            elec_losses[i]=-elec_used[i]*(losses[i]/(tpes[i]+losses[i]))
    #convert from TJ to PJ
    direct_fuel_use=(dfu_used+dfu_losses)/(10**3)
    electricity_generation=(elec_used+elec_losses)/(10**3)
    
    #convert consumption to exergy values and combine oil and renewable products
    exergycons=np.array([1.04*IEATFC[0],1.03*IEATFC[1],0.95*IEATFC[2],IEATFC[3]+IEATFC[4]+IEATFC[5],1.11*IEATFC[6],1.06*IEATFC[7]])
    
    #calculate direct fuel use energy to industry
    industry=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        industry[i]=exergycons[i][0]
    industry=industry/(10**3)
    
    #scale to include losses
    for i in range(len(dfu_used)):
        if dfu_used[i]!=0:
            industry[i]=industry[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            
    #calculate total electricity (& heat) 
    totelec=electricity[0]+electricity[15]+electricity[24]+electricity[25]+electricity[26]+electricity[27]+electricity[28]
    totheat=exergy_h[0]+exergy_h[15]+exergy_h[24]+exergy_h[25]+exergy_h[26]+exergy_h[27]+exergy_h[28]
    
    if (totelec+totheat)!=0: #to avoid divide zero errors
        totelec_=totelec/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
        totheat_=totheat/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
    else:
        totelec_=0
        totheat_=0
        
    #scale electricity (& heat) flow to industry only
    if totelec!=0:
        elec_ind=(electricity[0]/totelec)*totelec_
    else:
        elec_ind=0
        
    if totheat!=0:
        heat_ind=(exergy_h[0]/totheat)*totheat_
    else:
        heat_ind=0
        
    #calculate energy to electricity from each fuel for industry
    totelecind=np.zeros(len(exergycons))
    totheatind=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecind[i]=(elec_ind/np.sum(electricity_generation))*electricity_generation[i]
            totheatind[i]=(heat_ind/np.sum(electricity_generation))*electricity_generation[i]
            
    #calculate direct use for industrial sub-sectors
    exergyInd=np.zeros((len(exergycons),29))
    for j in range(0,len(exergycons)):
        for i in range(0,29):
            if dfu_used[j]!=0: #to avoid divide zero errors
                exergyInd[j][i]=exergycons[j][i]*direct_fuel_use[j]/(dfu_used[j]/10**3)
                
    steel=np.zeros(len(exergycons))
    aluminium=np.zeros(len(exergycons))
    machinery=np.zeros(len(exergycons))
    mineral=np.zeros(len(exergycons))
    chemical=np.zeros(len(exergycons))
    paper=np.zeros(len(exergycons))
    food=np.zeros(len(exergycons))
    other=np.zeros(len(exergycons))
    
    for i in range(0,len(exergycons)):
        steel[i]=exergyInd[i][4]/(10**3)
        aluminium[i]=exergyInd[i][6]/(10**3)
        machinery[i]=(exergyInd[i][8]+exergyInd[i][9])/(10**3)
        mineral[i]=exergyInd[i][7]/(10**3)
        chemical[i]=exergyInd[i][5]/(10**3)
        paper[i]=(exergyInd[i][11]+exergyInd[i][12])/(10**3)
        food[i]=exergyInd[i][10]/(10**3)
        other[i]=(exergyInd[i][1]+exergyInd[i][2]+exergyInd[i][13]+exergyInd[i][14])/(10**3)
        
    #calculate electricity to industrial sub-sectors  
    if totelec!=0:
        elec_steel=(electricity[4]/totelec)*totelec_
        elec_aluminium=(electricity[6]/totelec)*totelec_
        elec_machinery=((electricity[8]+electricity[9])/totelec)*totelec_
        elec_mineral=(electricity[7]/totelec)*totelec_
        elec_chemical=(electricity[5]/totelec)*totelec_
        elec_paper=((electricity[11]+electricity[12])/totelec)*totelec_
        elec_food=(electricity[10]/totelec)*totelec_
        elec_other=((electricity[1]+electricity[2]+electricity[13]+electricity[14])/totelec)*totelec_
    else:
        elec_steel=0
        elec_aluminium=0
        elec_machinery=0
        elec_mineral=0
        elec_chemical=0
        elec_paper=0
        elec_food=0
        elec_other=0
        
    #calculate heat to industrial sub-sectors  
    if totheat!=0:
        heat_steel=(exergy_h[4]/totheat)*totheat_
        heat_aluminium=(exergy_h[6]/totheat)*totheat_
        heat_machinery=((exergy_h[8]+exergy_h[9])/totheat)*totheat_
        heat_mineral=(exergy_h[7]/totheat)*totheat_
        heat_chemical=(exergy_h[5]/totheat)*totheat_
        heat_paper=((exergy_h[11]+exergy_h[12])/totheat)*totheat_
        heat_food=(exergy_h[10]/totheat)*totheat_
        heat_other=((exergy_h[1]+exergy_h[2]+exergy_h[13]+exergy_h[14])/totheat)*totheat_
    else:
        heat_steel=0
        heat_aluminium=0
        heat_machinery=0
        heat_mineral=0
        heat_chemical=0
        heat_paper=0
        heat_food=0
        heat_other=0
        
    #append electricity and heat values to sub-sector fuel consumption arrays
    steelfull=np.append(steel, [elec_steel, heat_steel])
    aluminiumfull=np.append(aluminium, [elec_aluminium, heat_aluminium])
    machineryfull=np.append(machinery, [elec_machinery, heat_machinery])
    mineralfull=np.append(mineral, [elec_mineral, heat_mineral])
    chemicalfull=np.append(chemical, [elec_chemical, heat_chemical])
    paperfull=np.append(paper, [elec_paper, heat_paper])
    foodfull=np.append(food, [elec_food, heat_food])
    otherfull=np.append(other, [elec_other, heat_other])
    
    #define allocation matrices, based on US industry data - used to assign fuels to passive systems below
    #rows are passive systems, columns are fuels (oil, gas, nuclear, renewables, biomass, coal, electricity, heat))
    steel_mat = np.array([[0.00  , 0.10  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.39  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 1.00  , 1.00  , 0.53  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.03  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#appliance
                         [1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    al_mat = np.array([[0.00  , 0.13  , 1.00  , 0.00  , 0.13  , 0.13  , 0.01  , 0.00  ],#steam
                         [0.25  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.24  , 0.00  ],#driven
                         [0.25  , 0.76  , 0.00  , 0.00  , 0.76  , 0.76  , 0.65  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.03  , 0.00  ],#light
                         [0.00  , 0.09  , 0.00  , 1.00  , 0.09  , 0.09  , 0.04  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.02  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                      ])
    
    mach_mat = np.array([[0.15  , 0.16  , 1.00  , 0.00  , 0.16  , 0.16  , 0.01  , 0.00  ],#steam
                         [0.14  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.49  , 0.00  ],#driven
                         [0.07  , 0.45  , 0.00  , 0.00  , 0.45  , 0.45  , 0.16  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.11  , 0.00  ],#light
                         [0.14  , 0.35  , 0.00  , 1.00  , 0.35  , 0.35  , 0.19  , 1.00  ],#spaceheat
                         [0.00  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.03  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])
    
    min_mat = np.array([[0.00  , 0.03  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.38  , 0.08  , 0.00  , 0.00  , 0.10  , 0.10  , 0.60  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 0.90  , 0.90  , 0.28  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.62  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                       ])
    
    chem_mat = np.array([[0.50  , 0.52  , 1.00  , 0.00  , 0.87  , 0.87  , 0.01  , 0.00  ],#steam
                         [0.00  , 0.04  , 0.00  , 0.00  , 0.00  , 0.00  , 0.63  , 0.00  ],#driven
                         [0.10  , 0.41  , 0.00  , 0.00  , 0.13  , 0.13  , 0.25  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.02  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.40  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                        ])                 
    
    paper_mat = np.array([[0.36  , 0.63  , 1.00  , 0.00  , 0.98  , 0.98  , 0.04  , 0.00  ],#steam
                         [0.04  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.78  , 0.00  ],#driven
                         [0.08  , 0.30  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.06  , 1.00  ],#spaceheat
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.52  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    food_mat = np.array([[0.59  , 0.59  , 1.00  , 0.00  , 0.79  , 0.79  , 0.03  , 0.00  ],#steam
                         [0.00  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.69  , 0.00  ],#driven
                         [0.00  , 0.27  , 0.00  , 0.00  , 0.21  , 0.21  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#light
                         [0.08  , 0.08  , 0.00  , 1.00  , 0.00  , 0.00  , 0.11  , 1.00  ],#spaceheat
                         [0.08  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.25  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])
    
    other_mat = np.array([[0.13  , 0.34  , 1.00  , 0.00  , 1.00  , 1.00  , 0.01  , 0.00  ],#steam
                         [0.13  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.73  , 0.00  ],#driven
                         [0.71  , 0.61  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.06  , 0.00  ],#light
                         [0.00  , 0.04  , 0.00  , 1.00  , 0.00  , 0.00  , 0.09  , 1.00  ],#spaceheat
                         [0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])
    
    #import data on share of steel from EAF
    import pandas as pd
    df=pd.read_csv('SteelShares2023.csv')
    try:
        EAF=float(df['EAF'][df['Country'] == Country].values[0])
    except:
        EAF=float(df['EAF'][df['Country'] == 'World'].values[0])
        
    #calculate new allocation matrices for steel, based on share of EAF
    x=(442.01*EAF)/((442.01*EAF)+(4128.05*(1-EAF)))
    z1=0.943*x+0.045*(1-x)
    z2=0.928*(1-x)
    z3=0.057*x+0.027*(1-x)
    gamma=0
        
    if x==1:
        if electricity[4]!=0:
            gammaprime=(0.02*IEATFC[1][4]/electricity[4])*(z1/z3)
            steel_mat[2][6]=0.4+0.6*gammaprime
            steel_mat[1][6]=0.5*(1-gammaprime)
            steel_mat[3][6]=0.04*(1-gammaprime)
            steel_mat[4][6]=0.05*(1-gammaprime)
            steel_mat[5][6]=0.01*(1-gammaprime)
    else:
        if electricity[4]!=0:
            gamma=(IEATFC[7][4]/electricity[4])*(z1/z2)
            steel_mat[2][6]=0.4+0.6*gamma
            steel_mat[1][6]=0.5*(1-gamma)
            steel_mat[3][6]=0.04*(1-gamma)
            steel_mat[4][6]=0.05*(1-gamma)
            steel_mat[5][6]=0.01*(1-gamma)
        if IEATFC[1][4]!=0:
            delta=(IEATFC[7][4]/IEATFC[1][4])*(z3/z2)
            steel_mat[2][1]=0.83+0.17*delta
            steel_mat[0][1]=0.1*(1-delta)
            steel_mat[1][1]=0.01*(1-delta)
            steel_mat[4][1]=0.05*(1-delta)
            steel_mat[5][1]=0.01*(1-delta)
            
    #use matrix multiplication to assign fuel to each passive system
    steel_ps=np.zeros(7)
    al_ps=np.zeros(7)
    mach_ps=np.zeros(7)
    min_ps=np.zeros(7)
    chem_ps=np.zeros(7)
    paper_ps=np.zeros(7)
    food_ps=np.zeros(7)
    other_ps=np.zeros(7)
    for i in range(0,len(steelfull)):
        for j in range(0,7):
            steel_ps[j]=steel_ps[j]+steelfull[i]*steel_mat[j][i]
            al_ps[j]=al_ps[j]+aluminiumfull[i]*al_mat[j][i]
            mach_ps[j]=mach_ps[j]+machineryfull[i]*mach_mat[j][i]
            min_ps[j]=min_ps[j]+mineralfull[i]*min_mat[j][i]
            chem_ps[j]=chem_ps[j]+chemicalfull[i]*chem_mat[j][i]
            paper_ps[j]=paper_ps[j]+paperfull[i]*paper_mat[j][i]
            food_ps[j]=food_ps[j]+foodfull[i]*food_mat[j][i]
            other_ps[j]=other_ps[j]+otherfull[i]*other_mat[j][i]
            
    #define matrices for assigning fuels to conversion devices
    #rows are purposes of converson devices, columns are industries (steel, aluminium, machinery, mineral, chemical, paper, food, other)
    oil_mat = np.array([[1.00, 0.75, 0.64, 1.00, 0.40, 0.56, 0.25, 0.13],#motion
                       [0.00, 0.25, 0.36, 0.00, 0.60, 0.44, 0.67, 0.84],#heat
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.08, 0.03]])#appliance
    
    gas_mat = np.array([[steel_mat[1][1]+steel_mat[6][1], 0.01, 0.02, 0.08, 0.04, 0.02, 0.03, 0.01],#motion
                       [steel_mat[0][1]+steel_mat[2][1]+steel_mat[4][1], 0.98, 0.96, 0.91, 0.95, 0.98, 0.94, 0.99],#heat
                       [steel_mat[3][1], 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [steel_mat[5][1], 0.01, 0.02, 0.01, 0.01, 0.00, 0.03, 0.00]])#appliance
    
    coal_mat = np.array([[0.00, 0.01, 0.02, 0.10, 0.00, 0.02, 0.00, 0.00],#motion
                        [1.00, 0.98, 0.96, 0.90, 1.00, 0.98, 1.00, 1.00],#heat
                        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                        [0.00, 0.01, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00]])#appliance
    
    elec_mat = np.array([[steel_mat[1][6]+steel_mat[6][6], 0.25, 0.50, 0.60, 0.63, 0.78, 0.70, 0.73],#motion
                        [steel_mat[0][6]+steel_mat[2][6]+steel_mat[4][6], 0.70, 0.36, 0.33, 0.31, 0.15, 0.19, 0.19],#heat
                        [steel_mat[3][6], 0.03, 0.11, 0.05, 0.04, 0.05, 0.09, 0.06],#light
                        [steel_mat[5][6], 0.02, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02]])#appliance
    
    #use matrix multiplication to assign energy to each conversion device
    oil_cd=np.zeros(4)
    gas_cd=np.zeros(4)
    biomass_cd=np.zeros(4)
    coal_cd=np.zeros(4)
    elec_cd=np.zeros(4)
    for i in range(0,4):
        oil_cd[i]=oil_mat[i][0]*steelfull[0]+oil_mat[i][1]*aluminiumfull[0]+oil_mat[i][2]*machineryfull[0]+oil_mat[i][3]*mineralfull[0]+oil_mat[i][4]*chemicalfull[0]+oil_mat[i][5]*paperfull[0]+oil_mat[i][6]*foodfull[0]+oil_mat[i][7]*otherfull[0]
        gas_cd[i]=gas_mat[i][0]*steelfull[1]+gas_mat[i][1]*aluminiumfull[1]+gas_mat[i][2]*machineryfull[1]+gas_mat[i][3]*mineralfull[1]+gas_mat[i][4]*chemicalfull[1]+gas_mat[i][5]*paperfull[1]+gas_mat[i][6]*foodfull[1]+gas_mat[i][7]*otherfull[1]
        biomass_cd[i]=coal_mat[i][0]*steelfull[4]+coal_mat[i][1]*aluminiumfull[4]+coal_mat[i][2]*machineryfull[4]+coal_mat[i][3]*mineralfull[4]+coal_mat[i][4]*chemicalfull[4]+coal_mat[i][5]*paperfull[4]+coal_mat[i][6]*foodfull[4]+coal_mat[i][7]*otherfull[4]
        coal_cd[i]=coal_mat[i][0]*steelfull[5]+coal_mat[i][1]*aluminiumfull[5]+coal_mat[i][2]*machineryfull[5]+coal_mat[i][3]*mineralfull[5]+coal_mat[i][4]*chemicalfull[5]+coal_mat[i][5]*paperfull[5]+coal_mat[i][6]*foodfull[5]+coal_mat[i][7]*otherfull[5]
        elec_cd[i]=elec_mat[i][0]*steelfull[6]+elec_mat[i][1]*aluminiumfull[6]+elec_mat[i][2]*machineryfull[6]+elec_mat[i][3]*mineralfull[6]+elec_mat[i][4]*chemicalfull[6]+elec_mat[i][5]*paperfull[6]+elec_mat[i][6]*foodfull[6]+elec_mat[i][7]*otherfull[6]
    
    #assumed that all direct heat contributes to heat
    heat_cd=steelfull[7]+aluminiumfull[7]+machineryfull[7]+mineralfull[7]+chemicalfull[7]+paperfull[7]+foodfull[7]+otherfull[7]
    
    
    ###INITIAL EFFICIENCY###
    #calculate losses in fuel transformation
    ind_used=np.zeros(len(industry))
    inddfu_losses=np.zeros(len(industry))
    indelec_used=np.zeros(len(industry))
    indelec_losses=np.zeros(len(industry))
    for i in range(len(industry)):
        if direct_fuel_use[i]!=0: #to avoid divide zero errors
            ind_used[i]=industry[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
            inddfu_losses[i]=industry[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
        if electricity_generation[i]!=0: #to avoid divide zero errors
            indelec_used[i]=(totelecind[i]+totheatind[i])*elec_used[i]/(electricity_generation[i]*1000)
            indelec_losses[i]=(totelecind[i]+totheatind[i])*elec_losses[i]/(electricity_generation[i]*1000)
        ind_losses=indelec_losses+inddfu_losses
    
    InitialPE=np.sum(ind_used)+np.sum(indelec_used)+np.sum(ind_losses) #for comparison purposes
    #calculate energy to each conversion device
    if np.sum(oil_cd)!=0: #to avoid divide zero errors
        oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
        oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
    else:
        oilburner=0
        oilengine=0
        
    if np.sum(gas_cd)!=0: #to avoid divide zero errors
        gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
        gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
    else:
        gasburner=0
        gasengine=0
    
    nuclearheater=ind_used[2] #in case nuclear is used directly
    renheater=ind_used[3] #direct use of renewables only for solar heating
    
    if np.sum(biomass_cd)!=0: #to avoid divide zero errors
        biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
        biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
    else:
        biomassburner=0
        biomassengine=0
        
    if np.sum(coal_cd)!=0: #to avoid divide zero errors
        coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
        coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
    else:
        coalburner=0
        coalengine=0
        
    #calculate losses in electricity generation
    if np.sum(egeneration)!=0: #to avoid divide zero errors
        eleceff=totelec/(-np.sum(egeneration))
    else:
        eleceff=0
    if np.sum(hgeneration)!=0:
        heateff=totheat/(-np.sum(hgeneration))
    else:
        heateff=0
    
    #useful energy to electricity and heat powered devices
    heatex=heateff*heat_cd
    elecmotor=eleceff*elec_cd[1]
    elecheater=eleceff*elec_cd[0]
    lightingdevice=eleceff*elec_cd[2]
    applianceelec=eleceff*elec_cd[3]
    
    #create new matrices with all passive systems
    oil_mat2=np.zeros((7,8))
    for i in range(7):
        oil_mat2[i][0]=steel_mat[i][0]
        oil_mat2[i][1]=al_mat[i][0]
        oil_mat2[i][2]=mach_mat[i][0]
        oil_mat2[i][3]=min_mat[i][0]
        oil_mat2[i][4]=chem_mat[i][0]
        oil_mat2[i][5]=paper_mat[i][0]
        oil_mat2[i][6]=food_mat[i][0]
        oil_mat2[i][7]=other_mat[i][0]
        
    gas_mat2=np.zeros((7,8))
    for i in range(7):
        gas_mat2[i][0]=steel_mat[i][1]
        gas_mat2[i][1]=al_mat[i][1]
        gas_mat2[i][2]=mach_mat[i][1]
        gas_mat2[i][3]=min_mat[i][1]
        gas_mat2[i][4]=chem_mat[i][1]
        gas_mat2[i][5]=paper_mat[i][1]
        gas_mat2[i][6]=food_mat[i][1]
        gas_mat2[i][7]=other_mat[i][1]
        
    coal_mat2=np.zeros((7,8))
    for i in range(7):
        coal_mat2[i][0]=steel_mat[i][4]
        coal_mat2[i][1]=al_mat[i][4]
        coal_mat2[i][2]=mach_mat[i][4]
        coal_mat2[i][3]=min_mat[i][4]
        coal_mat2[i][4]=chem_mat[i][4]
        coal_mat2[i][5]=paper_mat[i][4]
        coal_mat2[i][6]=food_mat[i][4]
        coal_mat2[i][7]=other_mat[i][4]
        
    elec_mat2=np.zeros((7,8))#
    for i in range(7):
        elec_mat2[i][0]=steel_mat[i][6]
        elec_mat2[i][1]=al_mat[i][6]
        elec_mat2[i][2]=mach_mat[i][6]
        elec_mat2[i][3]=min_mat[i][6]
        elec_mat2[i][4]=chem_mat[i][6]
        elec_mat2[i][5]=paper_mat[i][6]
        elec_mat2[i][6]=food_mat[i][6]
        elec_mat2[i][7]=other_mat[i][6]
        
    #use matrix multiplication to assign energy to each conversion device
    oil_cd2=np.zeros(7)
    gas_cd2=np.zeros(7)
    biomass_cd2=np.zeros(7)
    coal_cd2=np.zeros(7)
    elec_cd2=np.zeros(7)
    for i in range(0,7):
        oil_cd2[i]=oil_mat2[i][0]*steelfull[0]+oil_mat2[i][1]*aluminiumfull[0]+oil_mat2[i][2]*machineryfull[0]+oil_mat2[i][3]*mineralfull[0]+oil_mat2[i][4]*chemicalfull[0]+oil_mat2[i][5]*paperfull[0]+oil_mat2[i][6]*foodfull[0]+oil_mat2[i][7]*otherfull[0]
        gas_cd2[i]=gas_mat2[i][0]*steelfull[1]+gas_mat2[i][1]*aluminiumfull[1]+gas_mat2[i][2]*machineryfull[1]+gas_mat2[i][3]*mineralfull[1]+gas_mat2[i][4]*chemicalfull[1]+gas_mat2[i][5]*paperfull[1]+gas_mat2[i][6]*foodfull[1]+gas_mat2[i][7]*otherfull[1]
        biomass_cd2[i]=coal_mat2[i][0]*steelfull[4]+coal_mat2[i][1]*aluminiumfull[4]+coal_mat2[i][2]*machineryfull[4]+coal_mat2[i][3]*mineralfull[4]+coal_mat2[i][4]*chemicalfull[4]+coal_mat2[i][5]*paperfull[4]+coal_mat2[i][6]*foodfull[4]+coal_mat2[i][7]*otherfull[4]
        coal_cd2[i]=coal_mat2[i][0]*steelfull[5]+coal_mat2[i][1]*aluminiumfull[5]+coal_mat2[i][2]*machineryfull[5]+coal_mat2[i][3]*mineralfull[5]+coal_mat2[i][4]*chemicalfull[5]+coal_mat2[i][5]*paperfull[5]+coal_mat2[i][6]*foodfull[5]+coal_mat2[i][7]*otherfull[5]
        elec_cd2[i]=elec_mat2[i][0]*steelfull[6]+elec_mat2[i][1]*aluminiumfull[6]+elec_mat2[i][2]*machineryfull[6]+elec_mat2[i][3]*mineralfull[6]+elec_mat2[i][4]*chemicalfull[6]+elec_mat2[i][5]*paperfull[6]+elec_mat2[i][6]*foodfull[6]+elec_mat2[i][7]*otherfull[6]
        
    #calculate energy used
    if Exergy=='Exergy':
        #energy efficiency (from Paoli) x quality factor (from cullen) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average exergy efficiency
            oilburneffex=0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #exergy used
        else:
            oilburnused=0
            
        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average exergy efficiency
            gasburneffex=0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #exergy used
        else:
            gasburnused=0
            
        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average exergy efficiency
            coalburneffex=0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #exergy used
        else:
            coalburnused=0
            
        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average exergy efficiency
            bioburneffex=0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #exergy used
        else:
            biomassburnused=0
        
        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(0.95*dieselengeff*oilengine)+(0.53*turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine
        
        heatexeff=0.87 #heat exchanger efficiency
        heatexused=0.15*heatexeff*heatex #exergy used
        
        elecheateff=1 #electric heater efficiency
        elecheatused=0.3*elecheateff*elecheater #exergy used
        
        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=0.93*elecmotoreff*elecmotor #exergy used
        
        electroneff=0.85 #electronics efficiency
        electronused=0.3*electroneff*applianceelec #exergy used
        
        lighteff=0.13 #lighting device efficiency
        lightused=0.9*lighteff*lightingdevice #exergy used
        
        renheateff=1 #renewable heater efficiency
        renheatused=0.3*renheateff*renheater #exergy used
        
    elif Exergy=='Energy':
        #energy efficiency (from Paoli) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average energy efficiency
            oilburneffex=(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #energy used
        else:
            oilburnused=0
            
        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average energy efficiency
            gasburneffex=(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #energy used
        else:
            gasburnused=0
            
        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average energy efficiency
            coalburneffex=(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #energy used
        else:
            coalburnused=0
            
        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average energy efficiency
            bioburneffex=(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #energy used
        else:
            biomassburnused=0
        
        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(dieselengeff*oilengine)+(turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine
        
        heatexeff=0.87 #heat exchanger efficiency
        heatexused=heatexeff*heatex #energy used
        
        elecheateff=1 #electric heater efficiency
        elecheatused=elecheateff*elecheater #energy used
        
        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=elecmotoreff*elecmotor #energy used
        
        electroneff=0.85 #electronics efficiency
        electronused=electroneff*applianceelec #energy used
        
        lighteff=0.13 #lighting device efficiency
        lightused=lighteff*lightingdevice #energy used
        
        renheateff=1 #renewable heater efficiency
        renheatused=renheateff*renheater #energy used
    
    Heateff='Heat ({:.0f}PJ)'.format(oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+elecheatused+heatexused+renheatused)
    Motioneff='Motion ({:.0f}PJ)'.format(engused+elecmotorused)
    Othereff='Other ({:.0f}PJ)'.format(electronused+lightused)
    
    ###NEW EFFICIENCY###
    #user inputs new device efficiency in %
    value=float(Value)/100
    #for given device change value for that device whilst keeping others the same
    if Exergy=='Exergy':
        if Device=='Oil Burner':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/(0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + value*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Oil Boiler':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/(0.25*(value*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Burner':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/(0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + value*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Boiler':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/(0.21*(value*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/(0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + value*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/(0.31*(value*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/(0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + value*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/(0.2*(value*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Diesel Engine':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=(engused-(0.53*turbeff*(gasengine+coalengine+biomassengine)))/(0.95*value)
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Turbine':
            turbine=(engused-(0.95*dieselengeff*oilengine))/(0.53*value)
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            if (gasengine+coalengine+biomassengine)!=0:
                gasenginenew=turbine/(gasengine+coalengine+biomassengine)*gasengine
                coalenginenew=turbine/(gasengine+coalengine+biomassengine)*coalengine
                biomassenginenew=turbine/(gasengine+coalengine+biomassengine)*biomassengine
            else:
                gasenginenew=0
                coalenginenew=0
                biomassenginenew=0
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Heat Exchanger':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatexused/(0.15*value)
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheatused/(0.3*value)
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Motor':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotorused/(0.93*value)
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electronic':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=electronused/(0.3*value)
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Lighting Device':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightused/(0.9*value)
            renheaternew=renheater
        if Device=='Renewable Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheatused/(0.3*value)
    if Exergy=='Energy':
        if Device=='Oil Burner':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/((oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + value*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Oil Boiler':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/((value*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Burner':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/((gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + value*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Boiler':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/((value*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/((coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + value*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/((value*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/((bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + value*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/((value*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Diesel Engine':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=(engused-(turbeff*(gasengine+coalengine+biomassengine)))/(value)
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Turbine':
            turbine=(engused-(dieselengeff*oilengine))/(value)
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            if (gasengine+coalengine+biomassengine)!=0:
                gasenginenew=turbine/(gasengine+coalengine+biomassengine)*gasengine
                coalenginenew=turbine/(gasengine+coalengine+biomassengine)*coalengine
                biomassenginenew=turbine/(gasengine+coalengine+biomassengine)*biomassengine
            else:
                gasenginenew=0
                coalenginenew=0
                biomassenginenew=0
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Heat Exchanger':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatexused/(value)
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheatused/(value)
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Motor':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotorused/(value)
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electronic':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=electronused/(value)
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Lighting Device':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightused/(value)
            renheaternew=renheater
        if Device=='Renewable Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheatused/(value)        
        

    #calculate energy lost
    oilburnlossnew=oilburnernew-oilburnused
    gasburnlossnew=gasburnernew-gasburnused
    coalburnlossnew=coalburnernew-coalburnused
    biomassburnlossnew=biomassburnernew-biomassburnused
    dieslossnew=(oilenginenew+coalenginenew+gasenginenew+biomassenginenew)-engused
    heatexlossnew=heatexnew-heatexused
    elecheatlossnew=elecheaternew-elecheatused
    elecmotorlossnew=elecmotornew-elecmotorused
    electronlossnew=applianceelecnew-electronused
    lightlossnew=lightingdevicenew-lightused
    renheatlossnew=renheaternew-renheatused
    
    #efficiencies from original Efficiency Sankey required for subsequent calculations
    fueleff=np.zeros(6)
    for i in range(6):
        if (ind_losses[i]+ind_used[i]+indelec_used[i])!=0: #to avoid divide zero errors
            fueleff[i]=(ind_used[i]+indelec_used[i])/(ind_losses[i]+ind_used[i]+indelec_used[i])
        else:
            fueleff[i]=0
    if np.sum(indelec_used)!=0:
        alleleceff=(heatex+elecmotor+elecheater+applianceelec+lightingdevice)/(np.sum(indelec_used))
    else:
        alleleceff=0
    
    if alleleceff!=0:
        elossnew=(1/alleleceff-1)*(elecmotornew+elecheaternew+applianceelecnew+lightingdevicenew+heatexnew) #new electricity loss, based on same electricity efficiency as previously
    else:
        elossnew=0
    #calculate new primary energy values, based on new final energy demand
    ind_usednew=np.zeros(6)
    indelec_usednew=np.zeros(6)  
    ind_lossesnew=np.zeros(6)  
    ind_usednew[0]=oilenginenew+oilburnernew
    ind_usednew[1]=gasenginenew+gasburnernew
    ind_usednew[2]=nuclearheater
    ind_usednew[3]=renheaternew
    ind_usednew[4]=biomassenginenew+biomassburnernew
    ind_usednew[5]=coalenginenew+coalburnernew
    for i in range(6):
        if np.sum(indelec_used)!=0:
            indelec_usednew[i]=(indelec_used[i]/np.sum(indelec_used))*(elossnew+elecmotornew+elecheaternew+applianceelecnew+lightingdevicenew+heatexnew)
        else:
            indelec_usednew[i]=0
        if fueleff[i]!=0:
            ind_lossesnew[i]=(indelec_usednew[i]+ind_usednew[i])*(1/fueleff[i]-1) #using same fuel transformation efficiency as previously
        else:
            ind_lossesnew[i]=0
    #values for Sankey labels
    PrimEngnew=np.sum(indelec_usednew)+np.sum(ind_lossesnew)+np.sum(ind_usednew)

    DFUnew='DFU ({:.0f}PJ)'.format(np.sum(ind_usednew))
    TEGnew='TEG ({:.0f}PJ)'.format(np.sum(indelec_usednew))
    FuelLossnew='Fuel Loss ({:.0f}PJ)'.format(np.sum(ind_lossesnew))

    ConvDevnew=oilburnernew+gasburnernew+nuclearheater+renheaternew+biomassburnernew+coalburnernew+oilenginenew+gasenginenew+biomassenginenew+coalenginenew+elecmotornew+elecheaternew+lightingdevicenew+applianceelecnew+heatexnew
    GenerationLossnew='Generation Loss ({:.0f}PJ)'.format(elossnew)

    ConversionLossnew='Conversion Loss ({:.0f}PJ)'.format(oilburnlossnew+gasburnlossnew+coalburnlossnew+biomassburnlossnew+elecheatlossnew+heatexlossnew+dieslossnew+elecmotorlossnew+electronlossnew+lightlossnew+renheatlossnew)
    useful=oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+renheatused+elecheatused+heatexused+engused+elecmotorused+electronused+lightused
    UsefulEnergy='Useful \n Energy \n ({:.0f}PJ)'.format(useful)
    Lossnew='Loss \n ({:.0f}PJ)'.format(np.sum(ind_lossesnew)+elossnew+oilburnlossnew+gasburnlossnew+coalburnlossnew+biomassburnlossnew+elecheatlossnew+heatexlossnew+dieslossnew+elecmotorlossnew+electronlossnew+lightlossnew+renheatlossnew)
    
    #set up links for Industry Sankey
    links_changed = [
        #direct fuel use
        {'source': 'Oil', 'target': DFUnew, 'value': ind_usednew[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': DFUnew, 'value': ind_usednew[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': DFUnew, 'value': ind_usednew[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': DFUnew, 'value': ind_usednew[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': DFUnew, 'value': ind_usednew[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': DFUnew, 'value': ind_usednew[2], 'type': 'E', 'color': 'purple'},

        #fuel for electricity generation
        {'source': 'Oil', 'target': TEGnew, 'value': indelec_usednew[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': TEGnew, 'value': indelec_usednew[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': TEGnew, 'value': indelec_usednew[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': TEGnew, 'value': indelec_usednew[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': TEGnew, 'value': indelec_usednew[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': TEGnew, 'value': indelec_usednew[2], 'type': 'E', 'color': 'purple'},

        #fuel transformation losses
        {'source': 'Oil', 'target': FuelLossnew, 'value': ind_lossesnew[0], 'type': 'Z', 'color': 'gainsboro' },
        {'source': 'Coal', 'target': FuelLossnew, 'value': ind_lossesnew[5], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Gas', 'target': FuelLossnew, 'value': ind_lossesnew[1], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Biomass', 'target': FuelLossnew, 'value': ind_lossesnew[4], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Renewables', 'target': FuelLossnew, 'value': ind_lossesnew[3], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Nuclear', 'target': FuelLossnew, 'value': ind_lossesnew[2], 'type': 'Z', 'color': 'gainsboro'},

        #direct fuel to conversion devices for heat
        {'source': DFUnew, 'target': 'Oil Burner', 'value': oilburnernew, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUnew, 'target': 'Coal Burner', 'value': coalburnernew, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUnew, 'target': 'Gas Burner', 'value': gasburnernew, 'type': 'C', 'color': 'gold'},
        {'source': DFUnew, 'target': 'Biomass Burner', 'value': biomassburnernew, 'type': 'B', 'color': 'green'},
        {'source': DFUnew, 'target': 'Renewable Heater', 'value': renheaternew, 'type': 'F', 'color': 'dodgerblue'},
        {'source': DFUnew, 'target': 'Nuclear Heater', 'value': nuclearheater, 'type': 'E', 'color': 'purple'},

        #direct fuel to conversion devices for motion
        {'source': DFUnew, 'target': 'Engine', 'value': oilenginenew, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUnew, 'target': 'Engine', 'value': coalenginenew, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUnew, 'target': 'Engine', 'value': gasenginenew, 'type': 'C', 'color': 'gold'},
        {'source': DFUnew, 'target': 'Engine', 'value': biomassenginenew, 'type': 'B', 'color': 'green'}, 

        #electricity to conversion devices
        {'source': TEGnew, 'target': 'Electric Motor', 'value': elecmotornew, 'type': 'H', 'color': 'silver' },
        {'source': TEGnew, 'target': 'Electric Heater', 'value': elecheaternew, 'type': 'H', 'color': 'silver'},
        {'source': TEGnew, 'target': 'Lighting Device', 'value': lightingdevicenew, 'type': 'H', 'color': 'silver'},
        {'source': TEGnew, 'target': 'Electronic', 'value': applianceelecnew, 'type': 'H', 'color': 'silver'},
        {'source': TEGnew, 'target': 'Heat Exchanger', 'value': heatexnew, 'type': 'G', 'color': 'red'},

        #electricity generation losses
        {'source': TEGnew, 'target': GenerationLossnew, 'value': elossnew, 'type': 'Z', 'color': 'gainsboro'},  

        #energy to provide motion
        {'source': 'Engine', 'target': Motioneff, 'value': engused, 'type': 'I', 'color':'lightblue'},
        {'source': 'Electric Motor', 'target': Motioneff, 'value': elecmotorused, 'type': 'I', 'color':'lightblue'},

        #energy to provide heat
        {'source': 'Oil Burner', 'target': Heateff, 'value': oilburnused, 'type': 'G', 'color':'red'},
        {'source': 'Gas Burner', 'target': Heateff, 'value': gasburnused, 'type': 'G', 'color':'red'},
        {'source': 'Coal Burner', 'target': Heateff, 'value': coalburnused, 'type': 'G', 'color':'red'},
        {'source': 'Biomass Burner', 'target': Heateff, 'value': biomassburnused, 'type':'G', 'color':'red'},
        {'source': 'Renewable Heater', 'target': Heateff, 'value': renheatused, 'type': 'G', 'color': 'red'},
        {'source': 'Nuclear Heater', 'target': Heateff, 'value': nuclearheater, 'type': 'E', 'color': 'red'},
        {'source': 'Electric Heater', 'target': Heateff, 'value': elecheatused, 'type': 'G', 'color':'red'},
        {'source': 'Heat Exchanger', 'target': Heateff, 'value': heatexused, 'type': 'G', 'color':'red'},

        #energy used for other purposes
        {'source': 'Lighting Device', 'target': Othereff, 'value': lightused, 'type': 'J', 'color':'black'},
        {'source': 'Electronic', 'target': Othereff, 'value': electronused, 'type': 'J', 'color':'black'},

        #device conversion losses
        {'source': 'Engine', 'target': ConversionLossnew, 'value': dieslossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Motor', 'target': ConversionLossnew, 'value': elecmotorlossnew, 'type': 'Z', 'color':'gainsboro'},

        {'source': 'Oil Burner', 'target': ConversionLossnew, 'value': oilburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Gas Burner', 'target': ConversionLossnew, 'value': gasburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Coal Burner', 'target': ConversionLossnew, 'value': coalburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Biomass Burner', 'target': ConversionLossnew, 'value': biomassburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Heater', 'target': ConversionLossnew, 'value': elecheatlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Heat Exchanger', 'target': ConversionLossnew, 'value': heatexlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Renewable Heater', 'target': ConversionLossnew, 'value': renheatlossnew, 'type': 'Z', 'color':'gainsboro'},

        {'source': 'Lighting Device', 'target': ConversionLossnew, 'value': lightlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electronic', 'target': ConversionLossnew, 'value': electronlossnew, 'type': 'Z', 'color':'gainsboro'},

        #energy lost
        {'source': ConversionLossnew, 'target': Lossnew, 'value': oilburnlossnew+gasburnlossnew+coalburnlossnew+biomassburnlossnew+elecheatlossnew+heatexlossnew+dieslossnew+elecmotorlossnew+electronlossnew+lightlossnew+renheatlossnew, 'type': 'A', 'color': 'gainsboro'},#
        {'source': GenerationLossnew, 'target': Lossnew, 'value': elossnew, 'type': 'Z', 'color': 'gainsboro'},
        {'source': FuelLossnew, 'target': Lossnew, 'value': np.sum(ind_lossesnew), 'type': 'Z', 'color': 'gainsboro'},

        #energy used
        {'source': Heateff, 'target': UsefulEnergy, 'value': oilburnused+gasburnused+coalburnused+biomassburnused+elecheatused+heatexused+renheatused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Motioneff, 'target': UsefulEnergy, 'value': engused+elecmotorused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Othereff, 'target': UsefulEnergy, 'value': electronused+lightused, 'type': 'K', 'color': 'whitesmoke'}

    ]

    #groups for showing total primary energy supply and labelling conversion devices
    groups_changed = [
        {'id': 'G', 'title': 'TPE ({:.0f}PJ)'.format(PrimEngnew), 'nodes': ['Oil', 'Coal', 'Gas', 'Biomass', 'Nuclear', 'Renewables']},
        {'id': 'G', 'title': 'Conversion Devices ({:.0f}PJ)'.format(ConvDevnew), 'nodes': ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Lighting Device']},
    ]

    #set order in which nodes appear
    order_changed = [
        [['Oil', 'Biomass', 'Gas', 'Coal', 'Nuclear', 'Renewables']],
        [DFUnew, TEGnew, FuelLossnew],
        ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Electronic', 'Lighting Device', GenerationLossnew],
        [[Heateff, Motioneff, Othereff, ConversionLossnew]],
        [UsefulEnergy, Lossnew]

    ]
    neweff=useful/PrimEngnew
    print('The Total', Exergy, 'Efficiency of the industrial sector in', Country,  'is {:.0f}%'.format(neweff*100))
    print('The Energy Savings are {:.1f} PJ'.format((InitialPE-PrimEngnew)))
    eff=useful/InitialPE #initial efficiency
    print('The Efficiency Improvements are {:.3f}%'.format((neweff-eff)*100))
    return sankey(links=links_changed, groups=groups_changed, linkLabelFormat='.0f', linkLabelMinWidth=10, order=order_changed, align_link_types=True).auto_save_png(Country+'_Efficiency_Sankey_'+Year+Device+'Efficiency'+Value+'.png')

###SECTOR EFFICIENCY SANKEY GENERATOR FUNCTION ###
def sector(IEATES,IEATFC,electricity,heat,Country,Year,Exergy,Sector): 

    '''
    Function to return a Sankey Diagram for a given
    industrial subsector
    
    Inputs: 
        IEATES - Energy Supply Values from IEA
        IEATFC - Energy Consumption Values from IEA
        electricity - Electricity Consumption values from IEA
        heat - Heat Consumption values from IEA
        Country - name of country from IEA list
        Year - year between 1960 and 2019
        Exergy - Produce Diagram in Exergy or Energy Values
        Sector - Sector for which the diagram will be produced
        
    Returns a Sankey diagram for the given year and country 
   for the specified subsector and prints the overall efficiency
   of that subsector
    
    '''
    
    #convert supply to exergy values and combine oil and renewable products (exergy factors from https://doi.org/10.3390/en9090707)
    if Exergy=='Exergy':                          
        exergy=np.array([1.04*IEATES[0],1.03*IEATES[1],0.95*IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],1.13*IEATES[6],1.06*IEATES[7]])
        exergy_h=0.17*heat
    elif Exergy=='Energy':
        exergy=np.array([IEATES[0],IEATES[1],IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],IEATES[6],IEATES[7]])
        exergy_h=heat                          

    #calculate total electricity generation and direct fuel use
    tpes=np.zeros(len(exergy))
    losses=np.zeros(len(exergy))
    tfc=np.zeros(len(exergy))
    nonenergy=np.zeros(len(exergy))
    egeneration=np.zeros(len(exergy))
    hgeneration=np.zeros(len(exergy))
    for i in range (0,len(exergy)):
        tpes[i]=exergy[i][0]
        #combine all losses
        for j in range(1,3):
            losses[i]=losses[i]+exergy[i][j] 
        for j in range(9,23):
            losses[i]=losses[i]+exergy[i][j]
        tfc[i]=exergy[i][23]
        nonenergy[i]=exergy[i][24]
        #combine electriciy and heat generation from electricity, heating and CHP plants
        for j in range(3,5):
            egeneration[i]=egeneration[i]+exergy[i][j]
        for j in range(5,7):
            egeneration[i]=egeneration[i]+0.89*exergy[i][j]
            hgeneration[i]=hgeneration[i]+0.11*exergy[i][j]
        for j in range(7,9):
            hgeneration[i]=hgeneration[i]+exergy[i][j]

    dfu_used=tfc-nonenergy #total fuel used directly is total final consumption of fuel - non-energy use
    elec_used=-egeneration-hgeneration #total fuel used for electricity generation is combination of fuels to all plants from above (- sign to yield +ve values)

    #losses split proportionally between dfu & electricity generation
    dfu_losses=np.zeros(len(tpes))
    elec_losses=np.zeros(len(tpes))
    for i in range(len(tpes)):
        if tpes[i]+losses[i]==0: #to avoid divide zero errors
            dfu_losses[i]=0
            elec_losses[i]=0
        else: #- signs as losses[i] have -ve values
            dfu_losses[i]=-dfu_used[i]*(losses[i]/(tpes[i]+losses[i])) 
            elec_losses[i]=-elec_used[i]*(losses[i]/(tpes[i]+losses[i]))
    #convert from TJ to PJ
    direct_fuel_use=(dfu_used+dfu_losses)/(10**3)
    electricity_generation=(elec_used+elec_losses)/(10**3)

    #convert consumption to exergy values and combine oil and renewable products
    exergycons=np.array([1.04*IEATFC[0],1.03*IEATFC[1],0.95*IEATFC[2],IEATFC[3]+IEATFC[4]+IEATFC[5],1.11*IEATFC[6],1.06*IEATFC[7]])


    #calculate total electricity (& heat) 
    totelec=electricity[0]+electricity[15]+electricity[24]+electricity[25]+electricity[26]+electricity[27]+electricity[28]
    totheat=exergy_h[0]+exergy_h[15]+exergy_h[24]+exergy_h[25]+exergy_h[26]+exergy_h[27]+exergy_h[28]

    if (totelec+totheat)!=0: #to avoid divide zero errors
        totelec_=totelec/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
        totheat_=totheat/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
    else:
        totelec_=0
        totheat_=0

    #calculate direct fuel use energy to steel
    steel=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        steel[i]=exergycons[i][4]
    steel=steel/(10**3)

    #calculate direct fuel use energy to aluminium
    aluminium=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        aluminium[i]=exergycons[i][6]
    aluminium=aluminium/(10**3)

    #calculate direct fuel use energy to machinery
    machinery=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        machinery[i]=exergycons[i][8]+exergycons[i][9]
    machinery=machinery/(10**3)

    #calculate direct fuel use energy to mineral
    mineral=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        mineral[i]=exergycons[i][7]
    mineral=mineral/(10**3)

    #calculate direct fuel use energy to chemical
    chemical=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        chemical[i]=exergycons[i][5]
    chemical=chemical/(10**3)

    #calculate direct fuel use energy to paper
    paper=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        paper[i]=exergycons[i][11]+exergycons[i][12]
    paper=paper/(10**3)

    #calculate direct fuel use energy to food
    food=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        food[i]=exergycons[i][10]
    food=food/(10**3)

    #calculate direct fuel use energy to other
    other=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        other[i]=exergycons[i][1]+exergycons[i][2]+exergycons[i][13]+exergycons[i][14]
    other=other/(10**3)

    #scale to include losses
    for i in range(len(dfu_used)):
        if dfu_used[i]!=0:
            steel[i]=steel[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            aluminium[i]=aluminium[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            machinery[i]=machinery[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            mineral[i]=mineral[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            chemical[i]=chemical[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            paper[i]=paper[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            food[i]=food[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            other[i]=other[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))

    #scale electricity (& heat) flow to each subsector
    if totelec!=0:
        elec_steel=(electricity[4]/totelec)*totelec_
        elec_aluminium=(electricity[6]/totelec)*totelec_
        elec_machinery=((electricity[8]+electricity[9])/totelec)*totelec_
        elec_mineral=(electricity[7]/totelec)*totelec_
        elec_chemical=(electricity[5]/totelec)*totelec_
        elec_paper=((electricity[11]+electricity[12])/totelec)*totelec_
        elec_food=(electricity[10]/totelec)*totelec_
        elec_other=((electricity[1]+electricity[2]+electricity[13]+electricity[14])/totelec)*totelec_
    else:
        elec_steel=0
        elec_steel=0
        elec_aluminium=0
        elec_machinery=0
        elec_mineral=0
        elec_chemical=0
        elec_paper=0
        elec_food=0
        elec_other=0

    if totheat!=0:
        heat_steel=(exergy_h[4]/totheat)*totheat_
        heat_aluminium=(exergy_h[6]/totheat)*totheat_
        heat_machinery=((exergy_h[8]+exergy_h[9])/totheat)*totheat_
        heat_mineral=(exergy_h[7]/totheat)*totheat_
        heat_chemical=(exergy_h[5]/totheat)*totheat_
        heat_paper=((exergy_h[11]+exergy_h[12])/totheat)*totheat_
        heat_food=(exergy_h[10]/totheat)*totheat_
        heat_other=((exergy_h[1]+exergy_h[2]+exergy_h[13]+exergy_h[14])/totheat)*totheat_
    else:
        heat_steel=0
        heat_steel=0
        heat_aluminium=0
        heat_machinery=0
        heat_mineral=0
        heat_chemical=0
        heat_paper=0
        heat_food=0
        heat_other=0

    #calculate energy to electricity from each fuel for steel
    totelecsteel=np.zeros(len(exergycons))
    totheatsteel=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecsteel[i]=(elec_steel/np.sum(electricity_generation))*electricity_generation[i]
            totheatsteel[i]=(heat_steel/np.sum(electricity_generation))*electricity_generation[i]

    #caluminiumculate energy to electricity from each fuel for aluminium
    totelecaluminium=np.zeros(len(exergycons))
    totheataluminium=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecaluminium[i]=(elec_aluminium/np.sum(electricity_generation))*electricity_generation[i]
            totheataluminium[i]=(heat_aluminium/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for machinery
    totelecmachinery=np.zeros(len(exergycons))
    totheatmachinery=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecmachinery[i]=(elec_machinery/np.sum(electricity_generation))*electricity_generation[i]
            totheatmachinery[i]=(heat_machinery/np.sum(electricity_generation))*electricity_generation[i]

            #calculate energy to electricity from each fuel for mineral
    totelecmineral=np.zeros(len(exergycons))
    totheatmineral=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecmineral[i]=(elec_mineral/np.sum(electricity_generation))*electricity_generation[i]
            totheatmineral[i]=(heat_mineral/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for chemical
    totelecchemical=np.zeros(len(exergycons))
    totheatchemical=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecchemical[i]=(elec_chemical/np.sum(electricity_generation))*electricity_generation[i]
            totheatchemical[i]=(heat_chemical/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for paper
    totelecpaper=np.zeros(len(exergycons))
    totheatpaper=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecpaper[i]=(elec_paper/np.sum(electricity_generation))*electricity_generation[i]
            totheatpaper[i]=(heat_paper/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for food
    totelecfood=np.zeros(len(exergycons))
    totheatfood=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecfood[i]=(elec_food/np.sum(electricity_generation))*electricity_generation[i]
            totheatfood[i]=(heat_food/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for other
    totelecother=np.zeros(len(exergycons))
    totheatother=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecother[i]=(elec_other/np.sum(electricity_generation))*electricity_generation[i]
            totheatother[i]=(heat_other/np.sum(electricity_generation))*electricity_generation[i]



    #append electricity and heat values to sub-sector fuel consumption arrays
    steelfull=np.append(steel, [elec_steel, heat_steel])
    aluminiumfull=np.append(aluminium, [elec_aluminium, heat_aluminium])
    machineryfull=np.append(machinery, [elec_machinery, heat_machinery])
    mineralfull=np.append(mineral, [elec_mineral, heat_mineral])
    chemicalfull=np.append(chemical, [elec_chemical, heat_chemical])
    paperfull=np.append(paper, [elec_paper, heat_paper])
    foodfull=np.append(food, [elec_food, heat_food])
    otherfull=np.append(other, [elec_other, heat_other])

    #define allocation matrices, based on US steel data - used to assign fuels to passive systems below
    #rows are passive systems, columns are fuels (oil, gas, nuclear, renewables, biomass, coal, electricity, heat))
    steel_mat = np.array([[0.00  , 0.10  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.39  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 1.00  , 1.00  , 0.53  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.03  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#appliance
                         [1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    al_mat = np.array([[0.00  , 0.13  , 1.00  , 0.00  , 0.13  , 0.13  , 0.01  , 0.00  ],#steam
                         [0.25  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.24  , 0.00  ],#driven
                         [0.25  , 0.76  , 0.00  , 0.00  , 0.76  , 0.76  , 0.65  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.03  , 0.00  ],#light
                         [0.00  , 0.09  , 0.00  , 1.00  , 0.09  , 0.09  , 0.04  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.02  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                      ])

    mach_mat = np.array([[0.15  , 0.16  , 1.00  , 0.00  , 0.16  , 0.16  , 0.01  , 0.00  ],#steam
                         [0.14  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.49  , 0.00  ],#driven
                         [0.07  , 0.45  , 0.00  , 0.00  , 0.45  , 0.45  , 0.16  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.11  , 0.00  ],#light
                         [0.14  , 0.35  , 0.00  , 1.00  , 0.35  , 0.35  , 0.19  , 1.00  ],#spaceheat
                         [0.00  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.03  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])

    min_mat = np.array([[0.00  , 0.03  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.38  , 0.08  , 0.00  , 0.00  , 0.10  , 0.10  , 0.60  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 0.90  , 0.90  , 0.28  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.62  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                       ])

    chem_mat = np.array([[0.50  , 0.52  , 1.00  , 0.00  , 0.87  , 0.87  , 0.01  , 0.00  ],#steam
                         [0.00  , 0.04  , 0.00  , 0.00  , 0.00  , 0.00  , 0.63  , 0.00  ],#driven
                         [0.10  , 0.41  , 0.00  , 0.00  , 0.13  , 0.13  , 0.25  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.02  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.40  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                        ])                 

    paper_mat = np.array([[0.36  , 0.63  , 1.00  , 0.00  , 0.98  , 0.98  , 0.04  , 0.00  ],#steam
                         [0.04  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.78  , 0.00  ],#driven
                         [0.08  , 0.30  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.06  , 1.00  ],#spaceheat
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.52  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    food_mat = np.array([[0.59  , 0.59  , 1.00  , 0.00  , 0.79  , 0.79  , 0.03  , 0.00  ],#steam
                         [0.00  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.69  , 0.00  ],#driven
                         [0.00  , 0.27  , 0.00  , 0.00  , 0.21  , 0.21  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#light
                         [0.08  , 0.08  , 0.00  , 1.00  , 0.00  , 0.00  , 0.11  , 1.00  ],#spaceheat
                         [0.08  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.25  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])

    other_mat = np.array([[0.13  , 0.34  , 1.00  , 0.00  , 1.00  , 1.00  , 0.01  , 0.00  ],#steam
                         [0.13  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.73  , 0.00  ],#driven
                         [0.71  , 0.61  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.06  , 0.00  ],#light
                         [0.00  , 0.04  , 0.00  , 1.00  , 0.00  , 0.00  , 0.09  , 1.00  ],#spaceheat
                         [0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    #import data on share of steel from EAF
    import pandas as pd
    df=pd.read_csv('SteelShares2023.csv')
    try:
        EAF=float(df['EAF'][df['Country'] == Country].values[0])
    except:
        EAF=float(df['EAF'][df['Country'] == 'World'].values[0])

    #calculate new allocation matrices for steel, based on share of EAF
    x=(442.01*EAF)/((442.01*EAF)+(4128.05*(1-EAF)))
    z1=0.943*x+0.045*(1-x)
    z2=0.928*(1-x)
    z3=0.057*x+0.027*(1-x)
    gamma=0

    if x==1:
        if electricity[4]!=0:
            gammaprime=(0.02*IEATFC[1][4]/electricity[4])*(z1/z3)
            steel_mat[2][6]=0.4+0.6*gammaprime
            steel_mat[1][6]=0.5*(1-gammaprime)
            steel_mat[3][6]=0.04*(1-gammaprime)
            steel_mat[4][6]=0.05*(1-gammaprime)
            steel_mat[5][6]=0.01*(1-gammaprime)
    else:
        if electricity[4]!=0:
            gamma=(IEATFC[7][4]/electricity[4])*(z1/z2)
            steel_mat[2][6]=0.4+0.6*gamma
            steel_mat[1][6]=0.5*(1-gamma)
            steel_mat[3][6]=0.04*(1-gamma)
            steel_mat[4][6]=0.05*(1-gamma)
            steel_mat[5][6]=0.01*(1-gamma)
        if IEATFC[1][4]!=0:
            delta=(IEATFC[7][4]/IEATFC[1][4])*(z3/z2)
            steel_mat[2][1]=0.83+0.17*delta
            steel_mat[0][1]=0.1*(1-delta)
            steel_mat[1][1]=0.01*(1-delta)
            steel_mat[4][1]=0.05*(1-delta)
            steel_mat[5][1]=0.01*(1-delta)

    #use matrix multiplication to assign fuel to each passive system
    steel_ps=np.zeros(7)
    al_ps=np.zeros(7)
    mach_ps=np.zeros(7)
    min_ps=np.zeros(7)
    chem_ps=np.zeros(7)
    paper_ps=np.zeros(7)
    food_ps=np.zeros(7)
    other_ps=np.zeros(7)
    for i in range(0,len(steelfull)):
        for j in range(0,7):
            steel_ps[j]=steel_ps[j]+steelfull[i]*steel_mat[j][i]
            al_ps[j]=al_ps[j]+aluminiumfull[i]*al_mat[j][i]
            mach_ps[j]=mach_ps[j]+machineryfull[i]*mach_mat[j][i]
            min_ps[j]=min_ps[j]+mineralfull[i]*min_mat[j][i]
            chem_ps[j]=chem_ps[j]+chemicalfull[i]*chem_mat[j][i]
            paper_ps[j]=paper_ps[j]+paperfull[i]*paper_mat[j][i]
            food_ps[j]=food_ps[j]+foodfull[i]*food_mat[j][i]
            other_ps[j]=other_ps[j]+otherfull[i]*other_mat[j][i]

    #define matrices for assigning fuels to conversion devices
    #rows are purposes of converson devices, columns are industries (steel, aluminium, machinery, mineral, chemical, paper, food, other)
    oil_mat = np.array([[1.00, 0.75, 0.64, 1.00, 0.40, 0.56, 0.25, 0.13],#motion
                       [0.00, 0.25, 0.36, 0.00, 0.60, 0.44, 0.67, 0.84],#heat
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.08, 0.03]])#appliance

    gas_mat = np.array([[steel_mat[1][1]+steel_mat[6][1], 0.01, 0.02, 0.08, 0.04, 0.02, 0.03, 0.01],#motion
                       [steel_mat[0][1]+steel_mat[2][1]+steel_mat[4][1], 0.98, 0.96, 0.91, 0.95, 0.98, 0.94, 0.99],#heat
                       [steel_mat[3][1], 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [steel_mat[5][1], 0.01, 0.02, 0.01, 0.01, 0.00, 0.03, 0.00]])#appliance

    coal_mat = np.array([[0.00, 0.01, 0.02, 0.10, 0.00, 0.02, 0.00, 0.00],#motion
                        [1.00, 0.98, 0.96, 0.90, 1.00, 0.98, 1.00, 1.00],#heat
                        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                        [0.00, 0.01, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00]])#appliance

    elec_mat = np.array([[steel_mat[1][6]+steel_mat[6][6], 0.25, 0.50, 0.60, 0.63, 0.78, 0.70, 0.73],#motion
                        [steel_mat[0][6]+steel_mat[2][6]+steel_mat[4][6], 0.70, 0.36, 0.33, 0.31, 0.15, 0.19, 0.19],#heat
                        [steel_mat[3][6], 0.03, 0.11, 0.05, 0.04, 0.05, 0.09, 0.06],#light
                        [steel_mat[5][6], 0.02, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02]])#appliance

    #create new matrices with all passive systems
    oil_mat2=np.zeros((7,8))
    for i in range(7):
        oil_mat2[i][0]=steel_mat[i][0]
        oil_mat2[i][1]=al_mat[i][0]
        oil_mat2[i][2]=mach_mat[i][0]
        oil_mat2[i][3]=min_mat[i][0]
        oil_mat2[i][4]=chem_mat[i][0]
        oil_mat2[i][5]=paper_mat[i][0]
        oil_mat2[i][6]=food_mat[i][0]
        oil_mat2[i][7]=other_mat[i][0]

    gas_mat2=np.zeros((7,8))
    for i in range(7):
        gas_mat2[i][0]=steel_mat[i][1]
        gas_mat2[i][1]=al_mat[i][1]
        gas_mat2[i][2]=mach_mat[i][1]
        gas_mat2[i][3]=min_mat[i][1]
        gas_mat2[i][4]=chem_mat[i][1]
        gas_mat2[i][5]=paper_mat[i][1]
        gas_mat2[i][6]=food_mat[i][1]
        gas_mat2[i][7]=other_mat[i][1]

    coal_mat2=np.zeros((7,8))
    for i in range(7):
        coal_mat2[i][0]=steel_mat[i][4]
        coal_mat2[i][1]=al_mat[i][4]
        coal_mat2[i][2]=mach_mat[i][4]
        coal_mat2[i][3]=min_mat[i][4]
        coal_mat2[i][4]=chem_mat[i][4]
        coal_mat2[i][5]=paper_mat[i][4]
        coal_mat2[i][6]=food_mat[i][4]
        coal_mat2[i][7]=other_mat[i][4]

    elec_mat2=np.zeros((7,8))#
    for i in range(7):
        elec_mat2[i][0]=steel_mat[i][6]
        elec_mat2[i][1]=al_mat[i][6]
        elec_mat2[i][2]=mach_mat[i][6]
        elec_mat2[i][3]=min_mat[i][6]
        elec_mat2[i][4]=chem_mat[i][6]
        elec_mat2[i][5]=paper_mat[i][6]
        elec_mat2[i][6]=food_mat[i][6]
        elec_mat2[i][7]=other_mat[i][6]

    if Sector=='Steel':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][0]*steelfull[0]
            gas_cd[i]=gas_mat[i][0]*steelfull[1]
            biomass_cd[i]=coal_mat[i][0]*steelfull[4]
            coal_cd[i]=coal_mat[i][0]*steelfull[5]
            elec_cd[i]=elec_mat[i][0]*steelfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=steelfull[7]

        #values for Sankey labels
        PrimEng=np.sum(steel)+np.sum(totelecsteel)+np.sum(totheatsteel)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(steel))
        inddfu_losses=np.zeros(len(steel))
        indelec_used=np.zeros(len(steel))
        indelec_losses=np.zeros(len(steel))
        for i in range(len(steel)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=steel[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=steel[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecsteel[i]+totheatsteel[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecsteel[i]+totheatsteel[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        eloss=np.sum(indelec_used)-heatex-elecmotor-elecheater-lightingdevice-applianceelec

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][0]*steelfull[0]
            gas_cd2[i]=gas_mat2[i][0]*steelfull[1]
            biomass_cd2[i]=coal_mat2[i][0]*steelfull[4]
            coal_cd2[i]=coal_mat2[i][0]*steelfull[5]
            elec_cd2[i]=elec_mat2[i][0]*steelfull[6]

    if Sector=='Aluminium':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][1]*aluminiumfull[0]
            gas_cd[i]=gas_mat[i][1]*aluminiumfull[1]
            biomass_cd[i]=coal_mat[i][1]*aluminiumfull[4]
            coal_cd[i]=coal_mat[i][1]*aluminiumfull[5]
            elec_cd[i]=elec_mat[i][1]*aluminiumfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=aluminiumfull[7]

        #values for Sankey labels
        PrimEng=np.sum(aluminium)+np.sum(totelecaluminium)+np.sum(totheataluminium)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(aluminium))
        inddfu_losses=np.zeros(len(aluminium))
        indelec_used=np.zeros(len(aluminium))
        indelec_losses=np.zeros(len(aluminium))
        for i in range(len(aluminium)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=aluminium[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=aluminium[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecaluminium[i]+totheataluminium[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecaluminium[i]+totheataluminium[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        eloss=np.sum(indelec_used)-heatex-elecmotor-elecheater-lightingdevice-applianceelec

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][1]*aluminiumfull[0]
            gas_cd2[i]=gas_mat2[i][1]*aluminiumfull[1]
            biomass_cd2[i]=coal_mat2[i][1]*aluminiumfull[4]
            coal_cd2[i]=coal_mat2[i][1]*aluminiumfull[5]
            elec_cd2[i]=elec_mat2[i][1]*aluminiumfull[6]

    if Sector=='Machinery':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][2]*machineryfull[0]
            gas_cd[i]=gas_mat[i][2]*machineryfull[1]
            biomass_cd[i]=coal_mat[i][2]*machineryfull[4]
            coal_cd[i]=coal_mat[i][2]*machineryfull[5]
            elec_cd[i]=elec_mat[i][2]*machineryfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=machineryfull[7]

        #values for Sankey labels
        PrimEng=np.sum(machinery)+np.sum(totelecmachinery)+np.sum(totheatmachinery)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(machinery))
        inddfu_losses=np.zeros(len(machinery))
        indelec_used=np.zeros(len(machinery))
        indelec_losses=np.zeros(len(machinery))
        for i in range(len(machinery)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=machinery[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=machinery[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecmachinery[i]+totheatmachinery[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecmachinery[i]+totheatmachinery[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        eloss=np.sum(indelec_used)-heatex-elecmotor-elecheater-lightingdevice-applianceelec

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][2]*machineryfull[0]
            gas_cd2[i]=gas_mat2[i][2]*machineryfull[1]
            biomass_cd2[i]=coal_mat2[i][2]*machineryfull[4]
            coal_cd2[i]=coal_mat2[i][2]*machineryfull[5]
            elec_cd2[i]=elec_mat2[i][2]*machineryfull[6]

    if Sector=='Mineral':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][3]*mineralfull[0]
            gas_cd[i]=gas_mat[i][3]*mineralfull[1]
            biomass_cd[i]=coal_mat[i][3]*mineralfull[4]
            coal_cd[i]=coal_mat[i][3]*mineralfull[5]
            elec_cd[i]=elec_mat[i][3]*mineralfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=mineralfull[7]

        #values for Sankey labels
        PrimEng=np.sum(mineral)+np.sum(totelecmineral)+np.sum(totheatmineral)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(mineral))
        inddfu_losses=np.zeros(len(mineral))
        indelec_used=np.zeros(len(mineral))
        indelec_losses=np.zeros(len(mineral))
        for i in range(len(mineral)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=mineral[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=mineral[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecmineral[i]+totheatmineral[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecmineral[i]+totheatmineral[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        eloss=np.sum(indelec_used)-heatex-elecmotor-elecheater-lightingdevice-applianceelec

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][3]*mineralfull[0]
            gas_cd2[i]=gas_mat2[i][3]*mineralfull[1]
            biomass_cd2[i]=coal_mat2[i][3]*mineralfull[4]
            coal_cd2[i]=coal_mat2[i][3]*mineralfull[5]
            elec_cd2[i]=elec_mat2[i][3]*mineralfull[6]

    if Sector=='Chemical':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][4]*chemicalfull[0]
            gas_cd[i]=gas_mat[i][4]*chemicalfull[1]
            biomass_cd[i]=coal_mat[i][4]*chemicalfull[4]
            coal_cd[i]=coal_mat[i][4]*chemicalfull[5]
            elec_cd[i]=elec_mat[i][4]*chemicalfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=chemicalfull[7]

        #values for Sankey labels
        PrimEng=np.sum(chemical)+np.sum(totelecchemical)+np.sum(totheatchemical)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(chemical))
        inddfu_losses=np.zeros(len(chemical))
        indelec_used=np.zeros(len(chemical))
        indelec_losses=np.zeros(len(chemical))
        for i in range(len(chemical)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=chemical[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=chemical[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecchemical[i]+totheatchemical[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecchemical[i]+totheatchemical[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        eloss=np.sum(indelec_used)-heatex-elecmotor-elecheater-lightingdevice-applianceelec

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][4]*chemicalfull[0]
            gas_cd2[i]=gas_mat2[i][4]*chemicalfull[1]
            biomass_cd2[i]=coal_mat2[i][4]*chemicalfull[4]
            coal_cd2[i]=coal_mat2[i][4]*chemicalfull[5]
            elec_cd2[i]=elec_mat2[i][4]*chemicalfull[6]

    if Sector=='Paper':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][5]*paperfull[0]
            gas_cd[i]=gas_mat[i][5]*paperfull[1]
            biomass_cd[i]=coal_mat[i][5]*paperfull[4]
            coal_cd[i]=coal_mat[i][5]*paperfull[5]
            elec_cd[i]=elec_mat[i][5]*paperfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=paperfull[7]

        #values for Sankey labels
        PrimEng=np.sum(paper)+np.sum(totelecpaper)+np.sum(totheatpaper)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(paper))
        inddfu_losses=np.zeros(len(paper))
        indelec_used=np.zeros(len(paper))
        indelec_losses=np.zeros(len(paper))
        for i in range(len(paper)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=paper[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=paper[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecpaper[i]+totheatpaper[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecpaper[i]+totheatpaper[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        eloss=np.sum(indelec_used)-heatex-elecmotor-elecheater-lightingdevice-applianceelec

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][5]*paperfull[0]
            gas_cd2[i]=gas_mat2[i][5]*paperfull[1]
            biomass_cd2[i]=coal_mat2[i][5]*paperfull[4]
            coal_cd2[i]=coal_mat2[i][5]*paperfull[5]
            elec_cd2[i]=elec_mat2[i][5]*paperfull[6]

    if Sector=='Food':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][6]*foodfull[0]
            gas_cd[i]=gas_mat[i][6]*foodfull[1]
            biomass_cd[i]=coal_mat[i][6]*foodfull[4]
            coal_cd[i]=coal_mat[i][6]*foodfull[5]
            elec_cd[i]=elec_mat[i][6]*foodfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=foodfull[7]

        #values for Sankey labels
        PrimEng=np.sum(food)+np.sum(totelecfood)+np.sum(totheatfood)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(food))
        inddfu_losses=np.zeros(len(food))
        indelec_used=np.zeros(len(food))
        indelec_losses=np.zeros(len(food))
        for i in range(len(food)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=food[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=food[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecfood[i]+totheatfood[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecfood[i]+totheatfood[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        eloss=np.sum(indelec_used)-heatex-elecmotor-elecheater-lightingdevice-applianceelec

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][6]*foodfull[0]
            gas_cd2[i]=gas_mat2[i][6]*foodfull[1]
            biomass_cd2[i]=coal_mat2[i][6]*foodfull[4]
            coal_cd2[i]=coal_mat2[i][6]*foodfull[5]
            elec_cd2[i]=elec_mat2[i][6]*foodfull[6]

    if Sector=='Other':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][7]*otherfull[0]
            gas_cd[i]=gas_mat[i][7]*otherfull[1]
            biomass_cd[i]=coal_mat[i][7]*otherfull[4]
            coal_cd[i]=coal_mat[i][7]*otherfull[5]
            elec_cd[i]=elec_mat[i][7]*otherfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=otherfull[7]

        #values for Sankey labels
        PrimEng=np.sum(other)+np.sum(totelecother)+np.sum(totheatother)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(other))
        inddfu_losses=np.zeros(len(other))
        indelec_used=np.zeros(len(other))
        indelec_losses=np.zeros(len(other))
        for i in range(len(other)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=other[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=other[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecother[i]+totheatother[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecother[i]+totheatother[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        eloss=np.sum(indelec_used)-heatex-elecmotor-elecheater-lightingdevice-applianceelec

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][7]*otherfull[0]
            gas_cd2[i]=gas_mat2[i][7]*otherfull[1]
            biomass_cd2[i]=coal_mat2[i][7]*otherfull[4]
            coal_cd2[i]=coal_mat2[i][7]*otherfull[5]
            elec_cd2[i]=elec_mat2[i][7]*otherfull[6]

    #calculate energy used
    if Exergy=='Exergy':
        #energy efficiency (from Paoli) x quality factor (from cullen) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average exergy efficiency
            oilburneffex=0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #exergy used
        else:
            oilburnused=0

        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average exergy efficiency
            gasburneffex=0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #exergy used
        else:
            gasburnused=0

        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average exergy efficiency
            coalburneffex=0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #exergy used
        else:
            coalburnused=0

        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average exergy efficiency
            bioburneffex=0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #exergy used
        else:
            biomassburnused=0

        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(0.95*dieselengeff*oilengine)+(0.53*turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine

        heatexeff=0.87 #heat exchanger efficiency
        heatexused=0.15*heatexeff*heatex #exergy used

        elecheateff=1 #electric heater efficiency
        elecheatused=0.3*elecheateff*elecheater #exergy used

        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=0.93*elecmotoreff*elecmotor #exergy used

        electroneff=0.85 #electronics efficiency
        electronused=0.3*electroneff*applianceelec #exergy used

        lighteff=0.13 #lighting device efficiency
        lightused=0.9*lighteff*lightingdevice #exergy used

        renheateff=1 #renewable heater efficiency
        renheatused=0.3*renheateff*renheater #exergy used

    elif Exergy=='Energy':
        #energy efficiency (from Paoli) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average energy efficiency
            oilburneffex=(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #energy used
        else:
            oilburnused=0

        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average energy efficiency
            gasburneffex=(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #energy used
        else:
            gasburnused=0

        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average energy efficiency
            coalburneffex=(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #energy used
        else:
            coalburnused=0

        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average energy efficiency
            bioburneffex=(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #energy used
        else:
            biomassburnused=0

        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(dieselengeff*oilengine)+(turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine

        heatexeff=0.87 #heat exchanger efficiency
        heatexused=heatexeff*heatex #energy used

        elecheateff=1 #electric heater efficiency
        elecheatused=elecheateff*elecheater #energy used

        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=elecmotoreff*elecmotor #energy used

        electroneff=0.85 #electronics efficiency
        electronused=electroneff*applianceelec #energy used

        lighteff=0.13 #lighting device efficiency
        lightused=lighteff*lightingdevice #energy used

        renheateff=1 #renewable heater efficiency
        renheatused=renheateff*renheater #energy used

    #calculate energy lost
    oilburnloss=oilburner-oilburnused
    gasburnloss=gasburner-gasburnused
    coalburnloss=coalburner-coalburnused
    biomassburnloss=biomassburner-biomassburnused
    diesloss=(oilengine+coalengine+gasengine+biomassengine)-engused
    heatexloss=heatex-heatexused
    elecheatloss=elecheater-elecheatused
    elecmotorloss=elecmotor-elecmotorused
    electronloss=applianceelec-electronused
    lightloss=lightingdevice-lightused
    renheatloss=renheater-renheatused

    #values for Sankey labels
    PrimEngeff=np.sum(ind_used)+np.sum(indelec_used)+np.sum(ind_losses)
    DFUeff='DFU ({:.0f}PJ)'.format(np.sum(ind_used))
    TEGeff='TEG ({:.0f}PJ)'.format(np.sum(indelec_used))
    FuelLoss='Fuel Loss ({:.0f}PJ)'.format(np.sum(ind_losses))

    ConvDev=oilburner+gasburner+nuclearheater+renheater+biomassburner+coalburner+oilengine+gasengine+biomassengine+coalengine+elecmotor+elecheater+lightingdevice+applianceelec+heatex
    GenerationLoss='Generation Loss ({:.0f}PJ)'.format(eloss)

    Heateff='Heat ({:.0f}PJ)'.format(oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+elecheatused+heatexused+renheatused)
    Motioneff='Motion ({:.0f}PJ)'.format(engused+elecmotorused)
    Othereff='Other ({:.0f}PJ)'.format(electronused+lightused)
    ConversionLoss='Conversion Loss ({:.0f}PJ)'.format(oilburnloss+gasburnloss+coalburnloss+biomassburnloss+elecheatloss+heatexloss+diesloss+elecmotorloss+electronloss+lightloss+renheatloss)
    useful=oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+renheatused+elecheatused+heatexused+engused+elecmotorused+electronused+lightused
    UsefulEnergy='Useful \n Energy \n ({:.0f}PJ)'.format(useful)
    Loss='Loss \n ({:.0f}PJ)'.format(np.sum(ind_losses)+eloss+oilburnloss+gasburnloss+coalburnloss+biomassburnloss+elecheatloss+heatexloss+diesloss+elecmotorloss+electronloss+lightloss+renheatloss)

    #set up links for Efficiency Sankey
    linkseff = [
        #direct fuel use
        {'source': 'Oil', 'target': DFUeff, 'value': ind_used[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': DFUeff, 'value': ind_used[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': DFUeff, 'value': ind_used[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': DFUeff, 'value': ind_used[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': DFUeff, 'value': ind_used[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': DFUeff, 'value': ind_used[2], 'type': 'E', 'color': 'purple'},

        #fuel for electricity generation
        {'source': 'Oil', 'target': TEGeff, 'value': indelec_used[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': TEGeff, 'value': indelec_used[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': TEGeff, 'value': indelec_used[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': TEGeff, 'value': indelec_used[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': TEGeff, 'value': indelec_used[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': TEGeff, 'value': indelec_used[2], 'type': 'E', 'color': 'purple'},

        #fuel transformation losses
        {'source': 'Oil', 'target': FuelLoss, 'value': ind_losses[0], 'type': 'Z', 'color': 'gainsboro' },
        {'source': 'Coal', 'target': FuelLoss, 'value': ind_losses[5], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Gas', 'target': FuelLoss, 'value': ind_losses[1], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Biomass', 'target': FuelLoss, 'value': ind_losses[4], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Renewables', 'target': FuelLoss, 'value': ind_losses[3], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Nuclear', 'target': FuelLoss, 'value': ind_losses[2], 'type': 'Z', 'color': 'gainsboro'},

        #direct fuel to conversion devices for heat
        {'source': DFUeff, 'target': 'Oil Burner', 'value': oilburner, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUeff, 'target': 'Coal Burner', 'value': coalburner, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUeff, 'target': 'Gas Burner', 'value': gasburner, 'type': 'C', 'color': 'gold'},
        {'source': DFUeff, 'target': 'Biomass Burner', 'value': biomassburner, 'type': 'B', 'color': 'green'},
        {'source': DFUeff, 'target': 'Renewable Heater', 'value': renheater, 'type': 'F', 'color': 'dodgerblue'},
        {'source': DFUeff, 'target': 'Nuclear Heater', 'value': nuclearheater, 'type': 'E', 'color': 'purple'},

        #direct fuel to conversion devices for motion
        {'source': DFUeff, 'target': 'Engine', 'value': oilengine, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUeff, 'target': 'Engine', 'value': coalengine, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUeff, 'target': 'Engine', 'value': gasengine, 'type': 'C', 'color': 'gold'},
        {'source': DFUeff, 'target': 'Engine', 'value': biomassengine, 'type': 'B', 'color': 'green'}, 

        #electricity to conversion devices
        {'source': TEGeff, 'target': 'Electric Motor', 'value': elecmotor, 'type': 'H', 'color': 'silver' },
        {'source': TEGeff, 'target': 'Electric Heater', 'value': elecheater, 'type': 'H', 'color': 'silver'},
        {'source': TEGeff, 'target': 'Lighting Device', 'value': lightingdevice, 'type': 'H', 'color': 'silver'},
        {'source': TEGeff, 'target': 'Electronic', 'value': applianceelec, 'type': 'H', 'color': 'silver'},
        {'source': TEGeff, 'target': 'Heat Exchanger', 'value': heatex, 'type': 'G', 'color': 'red'},

        #electricity generation losses
        {'source': TEGeff, 'target': GenerationLoss, 'value': eloss, 'type': 'Z', 'color': 'gainsboro'},  

        #energy to provide motion
        {'source': 'Engine', 'target': Motioneff, 'value': engused, 'type': 'I', 'color':'lightblue'},
        {'source': 'Electric Motor', 'target': Motioneff, 'value': elecmotorused, 'type': 'I', 'color':'lightblue'},

        #energy to provide heat
        {'source': 'Oil Burner', 'target': Heateff, 'value': oilburnused, 'type': 'G', 'color':'red'},
        {'source': 'Gas Burner', 'target': Heateff, 'value': gasburnused, 'type': 'G', 'color':'red'},
        {'source': 'Coal Burner', 'target': Heateff, 'value': coalburnused, 'type': 'G', 'color':'red'},
        {'source': 'Biomass Burner', 'target': Heateff, 'value': biomassburnused, 'type':'G', 'color':'red'},
        {'source': 'Renewable Heater', 'target': Heateff, 'value': renheatused, 'type': 'G', 'color': 'red'},
        {'source': 'Nuclear Heater', 'target': Heateff, 'value': nuclearheater, 'type': 'G', 'color': 'red'},
        {'source': 'Electric Heater', 'target': Heateff, 'value': elecheatused, 'type': 'GGG', 'color':'red'}, #ignore different types here, just for aesthetics to ensure links appear in right order
        {'source': 'Heat Exchanger', 'target': Heateff, 'value': heatexused, 'type': 'GG', 'color':'red'},

        #energy used for other purposes
        {'source': 'Lighting Device', 'target': Othereff, 'value': lightused, 'type': 'J', 'color':'black'},
        {'source': 'Electronic', 'target': Othereff, 'value': electronused, 'type': 'J', 'color':'black'},

        #device conversion losses
        {'source': 'Engine', 'target': ConversionLoss, 'value': diesloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Motor', 'target': ConversionLoss, 'value': elecmotorloss, 'type': 'Z', 'color':'gainsboro'},

        {'source': 'Oil Burner', 'target': ConversionLoss, 'value': oilburnloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Gas Burner', 'target': ConversionLoss, 'value': gasburnloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Coal Burner', 'target': ConversionLoss, 'value': coalburnloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Biomass Burner', 'target': ConversionLoss, 'value': biomassburnloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Heater', 'target': ConversionLoss, 'value': elecheatloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Heat Exchanger', 'target': ConversionLoss, 'value': heatexloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Renewable Heater', 'target': ConversionLoss, 'value': renheatloss, 'type': 'Z', 'color':'gainsboro'},

        {'source': 'Lighting Device', 'target': ConversionLoss, 'value': lightloss, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electronic', 'target': ConversionLoss, 'value': electronloss, 'type': 'Z', 'color':'gainsboro'},

        #energy lost
        {'source': ConversionLoss, 'target': Loss, 'value': oilburnloss+gasburnloss+coalburnloss+biomassburnloss+elecheatloss+heatexloss+diesloss+elecmotorloss+electronloss+lightloss+renheatloss, 'type': 'A', 'color': 'gainsboro'},#
        {'source': GenerationLoss, 'target': Loss, 'value': eloss, 'type': 'Z', 'color': 'gainsboro'},
        {'source': FuelLoss, 'target': Loss, 'value': np.sum(ind_losses), 'type': 'Z', 'color': 'gainsboro'},

        #energy used
        {'source': Heateff, 'target': UsefulEnergy, 'value': oilburnused+gasburnused+coalburnused+biomassburnused+elecheatused+heatexused+renheatused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Motioneff, 'target': UsefulEnergy, 'value': engused+elecmotorused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Othereff, 'target': UsefulEnergy, 'value': electronused+lightused, 'type': 'K', 'color': 'whitesmoke'}

    ]

    #groups for showing total primary energy supply and labelling conversion devices
    groupseff = [
        {'id': 'G', 'title': 'TPE ({:.0f}PJ)'.format(PrimEngeff), 'nodes': ['Oil', 'Coal', 'Gas', 'Biomass', 'Nuclear', 'Renewables']},
        {'id': 'G', 'title': 'Conversion Devices ({:.0f}PJ)'.format(ConvDev), 'nodes': ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Lighting Device']},
    ]

    #set order in which nodes appear
    ordereff = [
        [['Oil', 'Biomass', 'Gas', 'Coal', 'Nuclear', 'Renewables']],
        [DFUeff, TEGeff, FuelLoss],
        ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Electronic', 'Lighting Device', GenerationLoss],
        [[Heateff, Motioneff, Othereff, ConversionLoss]],
        [UsefulEnergy, Loss]

    ]
    eff=useful/PrimEng
    print('The Total', Exergy, 'Efficiency of the', Sector, 'sector in', Country,  'is {:.0f}%'.format(eff*100))
    return sankey(links=linkseff, groups=groupseff, linkLabelFormat='.0f', linkLabelMinWidth=10, order=ordereff, align_link_types=True).auto_save_png(Country+Sector+'_Efficiency_Sankey_'+Year+'.png')

###SECTOR EFFICIENCY VALUES FUNCTION ###
def sectorvalues(IEATES,IEATFC,electricity,heat,Country,Year,Exergy,Sector): 
    '''
    Function to return efficiency values
    
    Inputs: 
        IEATES - Energy Supply Values from IEA
        IEATFC - Energy Consumption Values from IEA
        electricity - Electricity Consumption values from IEA
        heat - Heat Consumption values from IEA
        Country - name of country from IEA list
        Year - year between 1960 and 2019
        Exergy - Produce Diagram in Exergy or Energy Values
        Sector - Sector for which the values will be produced
        
    Returns values for the efficiency of each stage of energy transfer,
    as well as the compound efficiency of each device.
    
    '''
    
    #convert supply to exergy values and combine oil and renewable products (exergy factors from https://doi.org/10.3390/en9090707)
    if Exergy=='Exergy':                          
        exergy=np.array([1.04*IEATES[0],1.03*IEATES[1],0.95*IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],1.13*IEATES[6],1.06*IEATES[7]])
        exergy_h=0.17*heat
    elif Exergy=='Energy':
        exergy=np.array([IEATES[0],IEATES[1],IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],IEATES[6],IEATES[7]])
        exergy_h=heat                          

    #calculate total electricity generation and direct fuel use
    tpes=np.zeros(len(exergy))
    losses=np.zeros(len(exergy))
    tfc=np.zeros(len(exergy))
    nonenergy=np.zeros(len(exergy))
    egeneration=np.zeros(len(exergy))
    hgeneration=np.zeros(len(exergy))
    for i in range (0,len(exergy)):
        tpes[i]=exergy[i][0]
        #combine all losses
        for j in range(1,3):
            losses[i]=losses[i]+exergy[i][j] 
        for j in range(9,23):
            losses[i]=losses[i]+exergy[i][j]
        tfc[i]=exergy[i][23]
        nonenergy[i]=exergy[i][24]
        #combine electriciy and heat generation from electricity, heating and CHP plants
        for j in range(3,5):
            egeneration[i]=egeneration[i]+exergy[i][j]
        for j in range(5,7):
            egeneration[i]=egeneration[i]+0.89*exergy[i][j]
            hgeneration[i]=hgeneration[i]+0.11*exergy[i][j]
        for j in range(7,9):
            hgeneration[i]=hgeneration[i]+exergy[i][j]

    dfu_used=tfc-nonenergy #total fuel used directly is total final consumption of fuel - non-energy use
    elec_used=-egeneration-hgeneration #total fuel used for electricity generation is combination of fuels to all plants from above (- sign to yield +ve values)

    #losses split proportionally between dfu & electricity generation
    dfu_losses=np.zeros(len(tpes))
    elec_losses=np.zeros(len(tpes))
    for i in range(len(tpes)):
        if tpes[i]+losses[i]==0: #to avoid divide zero errors
            dfu_losses[i]=0
            elec_losses[i]=0
        else: #- signs as losses[i] have -ve values
            dfu_losses[i]=-dfu_used[i]*(losses[i]/(tpes[i]+losses[i])) 
            elec_losses[i]=-elec_used[i]*(losses[i]/(tpes[i]+losses[i]))
    #convert from TJ to PJ
    direct_fuel_use=(dfu_used+dfu_losses)/(10**3)
    electricity_generation=(elec_used+elec_losses)/(10**3)

    #convert consumption to exergy values and combine oil and renewable products
    exergycons=np.array([1.04*IEATFC[0],1.03*IEATFC[1],0.95*IEATFC[2],IEATFC[3]+IEATFC[4]+IEATFC[5],1.11*IEATFC[6],1.06*IEATFC[7]])


    #calculate total electricity (& heat) 
    totelec=electricity[0]+electricity[15]+electricity[24]+electricity[25]+electricity[26]+electricity[27]+electricity[28]
    totheat=exergy_h[0]+exergy_h[15]+exergy_h[24]+exergy_h[25]+exergy_h[26]+exergy_h[27]+exergy_h[28]

    if (totelec+totheat)!=0: #to avoid divide zero errors
        totelec_=totelec/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
        totheat_=totheat/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
    else:
        totelec_=0
        totheat_=0

    #calculate direct fuel use energy to steel
    steel=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        steel[i]=exergycons[i][4]
    steel=steel/(10**3)

    #calculate direct fuel use energy to aluminium
    aluminium=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        aluminium[i]=exergycons[i][6]
    aluminium=aluminium/(10**3)

    #calculate direct fuel use energy to machinery
    machinery=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        machinery[i]=exergycons[i][8]+exergycons[i][9]
    machinery=machinery/(10**3)

    #calculate direct fuel use energy to mineral
    mineral=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        mineral[i]=exergycons[i][7]
    mineral=mineral/(10**3)

    #calculate direct fuel use energy to chemical
    chemical=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        chemical[i]=exergycons[i][5]
    chemical=chemical/(10**3)

    #calculate direct fuel use energy to paper
    paper=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        paper[i]=exergycons[i][11]+exergycons[i][12]
    paper=paper/(10**3)

    #calculate direct fuel use energy to food
    food=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        food[i]=exergycons[i][10]
    food=food/(10**3)

    #calculate direct fuel use energy to other
    other=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        other[i]=exergycons[i][1]+exergycons[i][2]+exergycons[i][13]+exergycons[i][14]
    other=other/(10**3)

    #scale to include losses
    for i in range(len(dfu_used)):
        if dfu_used[i]!=0:
            steel[i]=steel[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            aluminium[i]=aluminium[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            machinery[i]=machinery[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            mineral[i]=mineral[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            chemical[i]=chemical[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            paper[i]=paper[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            food[i]=food[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            other[i]=other[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))

    #scale electricity (& heat) flow to each subsector
    if totelec!=0:
        elec_steel=(electricity[4]/totelec)*totelec_
        elec_aluminium=(electricity[6]/totelec)*totelec_
        elec_machinery=((electricity[8]+electricity[9])/totelec)*totelec_
        elec_mineral=(electricity[7]/totelec)*totelec_
        elec_chemical=(electricity[5]/totelec)*totelec_
        elec_paper=((electricity[11]+electricity[12])/totelec)*totelec_
        elec_food=(electricity[10]/totelec)*totelec_
        elec_other=((electricity[1]+electricity[2]+electricity[13]+electricity[14])/totelec)*totelec_
    else:
        elec_steel=0
        elec_steel=0
        elec_aluminium=0
        elec_machinery=0
        elec_mineral=0
        elec_chemical=0
        elec_paper=0
        elec_food=0
        elec_other=0

    if totheat!=0:
        heat_steel=(exergy_h[4]/totheat)*totheat_
        heat_aluminium=(exergy_h[6]/totheat)*totheat_
        heat_machinery=((exergy_h[8]+exergy_h[9])/totheat)*totheat_
        heat_mineral=(exergy_h[7]/totheat)*totheat_
        heat_chemical=(exergy_h[5]/totheat)*totheat_
        heat_paper=((exergy_h[11]+exergy_h[12])/totheat)*totheat_
        heat_food=(exergy_h[10]/totheat)*totheat_
        heat_other=((exergy_h[1]+exergy_h[2]+exergy_h[13]+exergy_h[14])/totheat)*totheat_
    else:
        heat_steel=0
        heat_steel=0
        heat_aluminium=0
        heat_machinery=0
        heat_mineral=0
        heat_chemical=0
        heat_paper=0
        heat_food=0
        heat_other=0

    #calculate energy to electricity from each fuel for steel
    totelecsteel=np.zeros(len(exergycons))
    totheatsteel=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecsteel[i]=(elec_steel/np.sum(electricity_generation))*electricity_generation[i]
            totheatsteel[i]=(heat_steel/np.sum(electricity_generation))*electricity_generation[i]

    #caluminiumculate energy to electricity from each fuel for aluminium
    totelecaluminium=np.zeros(len(exergycons))
    totheataluminium=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecaluminium[i]=(elec_aluminium/np.sum(electricity_generation))*electricity_generation[i]
            totheataluminium[i]=(heat_aluminium/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for machinery
    totelecmachinery=np.zeros(len(exergycons))
    totheatmachinery=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecmachinery[i]=(elec_machinery/np.sum(electricity_generation))*electricity_generation[i]
            totheatmachinery[i]=(heat_machinery/np.sum(electricity_generation))*electricity_generation[i]

            #calculate energy to electricity from each fuel for mineral
    totelecmineral=np.zeros(len(exergycons))
    totheatmineral=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecmineral[i]=(elec_mineral/np.sum(electricity_generation))*electricity_generation[i]
            totheatmineral[i]=(heat_mineral/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for chemical
    totelecchemical=np.zeros(len(exergycons))
    totheatchemical=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecchemical[i]=(elec_chemical/np.sum(electricity_generation))*electricity_generation[i]
            totheatchemical[i]=(heat_chemical/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for paper
    totelecpaper=np.zeros(len(exergycons))
    totheatpaper=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecpaper[i]=(elec_paper/np.sum(electricity_generation))*electricity_generation[i]
            totheatpaper[i]=(heat_paper/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for food
    totelecfood=np.zeros(len(exergycons))
    totheatfood=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecfood[i]=(elec_food/np.sum(electricity_generation))*electricity_generation[i]
            totheatfood[i]=(heat_food/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for other
    totelecother=np.zeros(len(exergycons))
    totheatother=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecother[i]=(elec_other/np.sum(electricity_generation))*electricity_generation[i]
            totheatother[i]=(heat_other/np.sum(electricity_generation))*electricity_generation[i]



    #append electricity and heat values to sub-sector fuel consumption arrays
    steelfull=np.append(steel, [elec_steel, heat_steel])
    aluminiumfull=np.append(aluminium, [elec_aluminium, heat_aluminium])
    machineryfull=np.append(machinery, [elec_machinery, heat_machinery])
    mineralfull=np.append(mineral, [elec_mineral, heat_mineral])
    chemicalfull=np.append(chemical, [elec_chemical, heat_chemical])
    paperfull=np.append(paper, [elec_paper, heat_paper])
    foodfull=np.append(food, [elec_food, heat_food])
    otherfull=np.append(other, [elec_other, heat_other])

    #define allocation matrices, based on US steel data - used to assign fuels to passive systems below
    #rows are passive systems, columns are fuels (oil, gas, nuclear, renewables, biomass, coal, electricity, heat))
    steel_mat = np.array([[0.00  , 0.10  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.39  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 1.00  , 1.00  , 0.53  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.03  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#appliance
                         [1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    al_mat = np.array([[0.00  , 0.13  , 1.00  , 0.00  , 0.13  , 0.13  , 0.01  , 0.00  ],#steam
                         [0.25  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.24  , 0.00  ],#driven
                         [0.25  , 0.76  , 0.00  , 0.00  , 0.76  , 0.76  , 0.65  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.03  , 0.00  ],#light
                         [0.00  , 0.09  , 0.00  , 1.00  , 0.09  , 0.09  , 0.04  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.02  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                      ])

    mach_mat = np.array([[0.15  , 0.16  , 1.00  , 0.00  , 0.16  , 0.16  , 0.01  , 0.00  ],#steam
                         [0.14  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.49  , 0.00  ],#driven
                         [0.07  , 0.45  , 0.00  , 0.00  , 0.45  , 0.45  , 0.16  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.11  , 0.00  ],#light
                         [0.14  , 0.35  , 0.00  , 1.00  , 0.35  , 0.35  , 0.19  , 1.00  ],#spaceheat
                         [0.00  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.03  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])

    min_mat = np.array([[0.00  , 0.03  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.38  , 0.08  , 0.00  , 0.00  , 0.10  , 0.10  , 0.60  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 0.90  , 0.90  , 0.28  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.62  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                       ])

    chem_mat = np.array([[0.50  , 0.52  , 1.00  , 0.00  , 0.87  , 0.87  , 0.01  , 0.00  ],#steam
                         [0.00  , 0.04  , 0.00  , 0.00  , 0.00  , 0.00  , 0.63  , 0.00  ],#driven
                         [0.10  , 0.41  , 0.00  , 0.00  , 0.13  , 0.13  , 0.25  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.02  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.40  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                        ])                 

    paper_mat = np.array([[0.36  , 0.63  , 1.00  , 0.00  , 0.98  , 0.98  , 0.04  , 0.00  ],#steam
                         [0.04  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.78  , 0.00  ],#driven
                         [0.08  , 0.30  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.06  , 1.00  ],#spaceheat
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.52  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    food_mat = np.array([[0.59  , 0.59  , 1.00  , 0.00  , 0.79  , 0.79  , 0.03  , 0.00  ],#steam
                         [0.00  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.69  , 0.00  ],#driven
                         [0.00  , 0.27  , 0.00  , 0.00  , 0.21  , 0.21  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#light
                         [0.08  , 0.08  , 0.00  , 1.00  , 0.00  , 0.00  , 0.11  , 1.00  ],#spaceheat
                         [0.08  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.25  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])

    other_mat = np.array([[0.13  , 0.34  , 1.00  , 0.00  , 1.00  , 1.00  , 0.01  , 0.00  ],#steam
                         [0.13  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.73  , 0.00  ],#driven
                         [0.71  , 0.61  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.06  , 0.00  ],#light
                         [0.00  , 0.04  , 0.00  , 1.00  , 0.00  , 0.00  , 0.09  , 1.00  ],#spaceheat
                         [0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    #import data on share of steel from EAF
    import pandas as pd
    df=pd.read_csv('SteelShares2023.csv')
    try:
        EAF=float(df['EAF'][df['Country'] == Country].values[0])
    except:
        EAF=float(df['EAF'][df['Country'] == 'World'].values[0])

    #calculate new allocation matrices for steel, based on share of EAF
    x=(442.01*EAF)/((442.01*EAF)+(4128.05*(1-EAF)))
    z1=0.943*x+0.045*(1-x)
    z2=0.928*(1-x)
    z3=0.057*x+0.027*(1-x)
    gamma=0

    if x==1:
        if electricity[4]!=0:
            gammaprime=(0.02*IEATFC[1][4]/electricity[4])*(z1/z3)
            steel_mat[2][6]=0.4+0.6*gammaprime
            steel_mat[1][6]=0.5*(1-gammaprime)
            steel_mat[3][6]=0.04*(1-gammaprime)
            steel_mat[4][6]=0.05*(1-gammaprime)
            steel_mat[5][6]=0.01*(1-gammaprime)
    else:
        if electricity[4]!=0:
            gamma=(IEATFC[7][4]/electricity[4])*(z1/z2)
            steel_mat[2][6]=0.4+0.6*gamma
            steel_mat[1][6]=0.5*(1-gamma)
            steel_mat[3][6]=0.04*(1-gamma)
            steel_mat[4][6]=0.05*(1-gamma)
            steel_mat[5][6]=0.01*(1-gamma)
        if IEATFC[1][4]!=0:
            delta=(IEATFC[7][4]/IEATFC[1][4])*(z3/z2)
            steel_mat[2][1]=0.83+0.17*delta
            steel_mat[0][1]=0.1*(1-delta)
            steel_mat[1][1]=0.01*(1-delta)
            steel_mat[4][1]=0.05*(1-delta)
            steel_mat[5][1]=0.01*(1-delta)

    #use matrix multiplication to assign fuel to each passive system
    steel_ps=np.zeros(7)
    al_ps=np.zeros(7)
    mach_ps=np.zeros(7)
    min_ps=np.zeros(7)
    chem_ps=np.zeros(7)
    paper_ps=np.zeros(7)
    food_ps=np.zeros(7)
    other_ps=np.zeros(7)
    for i in range(0,len(steelfull)):
        for j in range(0,7):
            steel_ps[j]=steel_ps[j]+steelfull[i]*steel_mat[j][i]
            al_ps[j]=al_ps[j]+aluminiumfull[i]*al_mat[j][i]
            mach_ps[j]=mach_ps[j]+machineryfull[i]*mach_mat[j][i]
            min_ps[j]=min_ps[j]+mineralfull[i]*min_mat[j][i]
            chem_ps[j]=chem_ps[j]+chemicalfull[i]*chem_mat[j][i]
            paper_ps[j]=paper_ps[j]+paperfull[i]*paper_mat[j][i]
            food_ps[j]=food_ps[j]+foodfull[i]*food_mat[j][i]
            other_ps[j]=other_ps[j]+otherfull[i]*other_mat[j][i]

    #define matrices for assigning fuels to conversion devices
    #rows are purposes of converson devices, columns are industries (steel, aluminium, machinery, mineral, chemical, paper, food, other)
    oil_mat = np.array([[1.00, 0.75, 0.64, 1.00, 0.40, 0.56, 0.25, 0.13],#motion
                       [0.00, 0.25, 0.36, 0.00, 0.60, 0.44, 0.67, 0.84],#heat
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.08, 0.03]])#appliance

    gas_mat = np.array([[steel_mat[1][1]+steel_mat[6][1], 0.01, 0.02, 0.08, 0.04, 0.02, 0.03, 0.01],#motion
                       [steel_mat[0][1]+steel_mat[2][1]+steel_mat[4][1], 0.98, 0.96, 0.91, 0.95, 0.98, 0.94, 0.99],#heat
                       [steel_mat[3][1], 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [steel_mat[5][1], 0.01, 0.02, 0.01, 0.01, 0.00, 0.03, 0.00]])#appliance

    coal_mat = np.array([[0.00, 0.01, 0.02, 0.10, 0.00, 0.02, 0.00, 0.00],#motion
                        [1.00, 0.98, 0.96, 0.90, 1.00, 0.98, 1.00, 1.00],#heat
                        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                        [0.00, 0.01, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00]])#appliance

    elec_mat = np.array([[steel_mat[1][6]+steel_mat[6][6], 0.25, 0.50, 0.60, 0.63, 0.78, 0.70, 0.73],#motion
                        [steel_mat[0][6]+steel_mat[2][6]+steel_mat[4][6], 0.70, 0.36, 0.33, 0.31, 0.15, 0.19, 0.19],#heat
                        [steel_mat[3][6], 0.03, 0.11, 0.05, 0.04, 0.05, 0.09, 0.06],#light
                        [steel_mat[5][6], 0.02, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02]])#appliance

    #create new matrices with all passive systems
    oil_mat2=np.zeros((7,8))
    for i in range(7):
        oil_mat2[i][0]=steel_mat[i][0]
        oil_mat2[i][1]=al_mat[i][0]
        oil_mat2[i][2]=mach_mat[i][0]
        oil_mat2[i][3]=min_mat[i][0]
        oil_mat2[i][4]=chem_mat[i][0]
        oil_mat2[i][5]=paper_mat[i][0]
        oil_mat2[i][6]=food_mat[i][0]
        oil_mat2[i][7]=other_mat[i][0]

    gas_mat2=np.zeros((7,8))
    for i in range(7):
        gas_mat2[i][0]=steel_mat[i][1]
        gas_mat2[i][1]=al_mat[i][1]
        gas_mat2[i][2]=mach_mat[i][1]
        gas_mat2[i][3]=min_mat[i][1]
        gas_mat2[i][4]=chem_mat[i][1]
        gas_mat2[i][5]=paper_mat[i][1]
        gas_mat2[i][6]=food_mat[i][1]
        gas_mat2[i][7]=other_mat[i][1]

    coal_mat2=np.zeros((7,8))
    for i in range(7):
        coal_mat2[i][0]=steel_mat[i][4]
        coal_mat2[i][1]=al_mat[i][4]
        coal_mat2[i][2]=mach_mat[i][4]
        coal_mat2[i][3]=min_mat[i][4]
        coal_mat2[i][4]=chem_mat[i][4]
        coal_mat2[i][5]=paper_mat[i][4]
        coal_mat2[i][6]=food_mat[i][4]
        coal_mat2[i][7]=other_mat[i][4]

    elec_mat2=np.zeros((7,8))#
    for i in range(7):
        elec_mat2[i][0]=steel_mat[i][6]
        elec_mat2[i][1]=al_mat[i][6]
        elec_mat2[i][2]=mach_mat[i][6]
        elec_mat2[i][3]=min_mat[i][6]
        elec_mat2[i][4]=chem_mat[i][6]
        elec_mat2[i][5]=paper_mat[i][6]
        elec_mat2[i][6]=food_mat[i][6]
        elec_mat2[i][7]=other_mat[i][6]

    if Sector=='Steel':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][0]*steelfull[0]
            gas_cd[i]=gas_mat[i][0]*steelfull[1]
            biomass_cd[i]=coal_mat[i][0]*steelfull[4]
            coal_cd[i]=coal_mat[i][0]*steelfull[5]
            elec_cd[i]=elec_mat[i][0]*steelfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=steelfull[7]

        #values for Sankey labels
        PrimEng=np.sum(steel)+np.sum(totelecsteel)+np.sum(totheatsteel)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(steel))
        inddfu_losses=np.zeros(len(steel))
        indelec_used=np.zeros(len(steel))
        indelec_losses=np.zeros(len(steel))
        for i in range(len(steel)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=steel[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=steel[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecsteel[i]+totheatsteel[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecsteel[i]+totheatsteel[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][0]*steelfull[0]
            gas_cd2[i]=gas_mat2[i][0]*steelfull[1]
            biomass_cd2[i]=coal_mat2[i][0]*steelfull[4]
            coal_cd2[i]=coal_mat2[i][0]*steelfull[5]
            elec_cd2[i]=elec_mat2[i][0]*steelfull[6]

    if Sector=='Aluminium':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][1]*aluminiumfull[0]
            gas_cd[i]=gas_mat[i][1]*aluminiumfull[1]
            biomass_cd[i]=coal_mat[i][1]*aluminiumfull[4]
            coal_cd[i]=coal_mat[i][1]*aluminiumfull[5]
            elec_cd[i]=elec_mat[i][1]*aluminiumfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=aluminiumfull[7]

        #values for Sankey labels
        PrimEng=np.sum(aluminium)+np.sum(totelecaluminium)+np.sum(totheataluminium)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(aluminium))
        inddfu_losses=np.zeros(len(aluminium))
        indelec_used=np.zeros(len(aluminium))
        indelec_losses=np.zeros(len(aluminium))
        for i in range(len(aluminium)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=aluminium[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=aluminium[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecaluminium[i]+totheataluminium[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecaluminium[i]+totheataluminium[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][1]*aluminiumfull[0]
            gas_cd2[i]=gas_mat2[i][1]*aluminiumfull[1]
            biomass_cd2[i]=coal_mat2[i][1]*aluminiumfull[4]
            coal_cd2[i]=coal_mat2[i][1]*aluminiumfull[5]
            elec_cd2[i]=elec_mat2[i][1]*aluminiumfull[6]

    if Sector=='Machinery':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][2]*machineryfull[0]
            gas_cd[i]=gas_mat[i][2]*machineryfull[1]
            biomass_cd[i]=coal_mat[i][2]*machineryfull[4]
            coal_cd[i]=coal_mat[i][2]*machineryfull[5]
            elec_cd[i]=elec_mat[i][2]*machineryfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=machineryfull[7]

        #values for Sankey labels
        PrimEng=np.sum(machinery)+np.sum(totelecmachinery)+np.sum(totheatmachinery)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(machinery))
        inddfu_losses=np.zeros(len(machinery))
        indelec_used=np.zeros(len(machinery))
        indelec_losses=np.zeros(len(machinery))
        for i in range(len(machinery)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=machinery[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=machinery[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecmachinery[i]+totheatmachinery[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecmachinery[i]+totheatmachinery[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][2]*machineryfull[0]
            gas_cd2[i]=gas_mat2[i][2]*machineryfull[1]
            biomass_cd2[i]=coal_mat2[i][2]*machineryfull[4]
            coal_cd2[i]=coal_mat2[i][2]*machineryfull[5]
            elec_cd2[i]=elec_mat2[i][2]*machineryfull[6]

    if Sector=='Mineral':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][3]*mineralfull[0]
            gas_cd[i]=gas_mat[i][3]*mineralfull[1]
            biomass_cd[i]=coal_mat[i][3]*mineralfull[4]
            coal_cd[i]=coal_mat[i][3]*mineralfull[5]
            elec_cd[i]=elec_mat[i][3]*mineralfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=mineralfull[7]

        #values for Sankey labels
        PrimEng=np.sum(mineral)+np.sum(totelecmineral)+np.sum(totheatmineral)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(mineral))
        inddfu_losses=np.zeros(len(mineral))
        indelec_used=np.zeros(len(mineral))
        indelec_losses=np.zeros(len(mineral))
        for i in range(len(mineral)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=mineral[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=mineral[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecmineral[i]+totheatmineral[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecmineral[i]+totheatmineral[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][3]*mineralfull[0]
            gas_cd2[i]=gas_mat2[i][3]*mineralfull[1]
            biomass_cd2[i]=coal_mat2[i][3]*mineralfull[4]
            coal_cd2[i]=coal_mat2[i][3]*mineralfull[5]
            elec_cd2[i]=elec_mat2[i][3]*mineralfull[6]

    if Sector=='Chemical':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][4]*chemicalfull[0]
            gas_cd[i]=gas_mat[i][4]*chemicalfull[1]
            biomass_cd[i]=coal_mat[i][4]*chemicalfull[4]
            coal_cd[i]=coal_mat[i][4]*chemicalfull[5]
            elec_cd[i]=elec_mat[i][4]*chemicalfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=chemicalfull[7]

        #values for Sankey labels
        PrimEng=np.sum(chemical)+np.sum(totelecchemical)+np.sum(totheatchemical)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(chemical))
        inddfu_losses=np.zeros(len(chemical))
        indelec_used=np.zeros(len(chemical))
        indelec_losses=np.zeros(len(chemical))
        for i in range(len(chemical)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=chemical[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=chemical[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecchemical[i]+totheatchemical[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecchemical[i]+totheatchemical[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][4]*chemicalfull[0]
            gas_cd2[i]=gas_mat2[i][4]*chemicalfull[1]
            biomass_cd2[i]=coal_mat2[i][4]*chemicalfull[4]
            coal_cd2[i]=coal_mat2[i][4]*chemicalfull[5]
            elec_cd2[i]=elec_mat2[i][4]*chemicalfull[6]

    if Sector=='Paper':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][5]*paperfull[0]
            gas_cd[i]=gas_mat[i][5]*paperfull[1]
            biomass_cd[i]=coal_mat[i][5]*paperfull[4]
            coal_cd[i]=coal_mat[i][5]*paperfull[5]
            elec_cd[i]=elec_mat[i][5]*paperfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=paperfull[7]

        #values for Sankey labels
        PrimEng=np.sum(paper)+np.sum(totelecpaper)+np.sum(totheatpaper)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(paper))
        inddfu_losses=np.zeros(len(paper))
        indelec_used=np.zeros(len(paper))
        indelec_losses=np.zeros(len(paper))
        for i in range(len(paper)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=paper[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=paper[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecpaper[i]+totheatpaper[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecpaper[i]+totheatpaper[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][5]*paperfull[0]
            gas_cd2[i]=gas_mat2[i][5]*paperfull[1]
            biomass_cd2[i]=coal_mat2[i][5]*paperfull[4]
            coal_cd2[i]=coal_mat2[i][5]*paperfull[5]
            elec_cd2[i]=elec_mat2[i][5]*paperfull[6]

    if Sector=='Food':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][6]*foodfull[0]
            gas_cd[i]=gas_mat[i][6]*foodfull[1]
            biomass_cd[i]=coal_mat[i][6]*foodfull[4]
            coal_cd[i]=coal_mat[i][6]*foodfull[5]
            elec_cd[i]=elec_mat[i][6]*foodfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=foodfull[7]

        #values for Sankey labels
        PrimEng=np.sum(food)+np.sum(totelecfood)+np.sum(totheatfood)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(food))
        inddfu_losses=np.zeros(len(food))
        indelec_used=np.zeros(len(food))
        indelec_losses=np.zeros(len(food))
        for i in range(len(food)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=food[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=food[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecfood[i]+totheatfood[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecfood[i]+totheatfood[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][6]*foodfull[0]
            gas_cd2[i]=gas_mat2[i][6]*foodfull[1]
            biomass_cd2[i]=coal_mat2[i][6]*foodfull[4]
            coal_cd2[i]=coal_mat2[i][6]*foodfull[5]
            elec_cd2[i]=elec_mat2[i][6]*foodfull[6]

    if Sector=='Other':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][7]*otherfull[0]
            gas_cd[i]=gas_mat[i][7]*otherfull[1]
            biomass_cd[i]=coal_mat[i][7]*otherfull[4]
            coal_cd[i]=coal_mat[i][7]*otherfull[5]
            elec_cd[i]=elec_mat[i][7]*otherfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=otherfull[7]

        #values for Sankey labels
        PrimEng=np.sum(other)+np.sum(totelecother)+np.sum(totheatother)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(other))
        inddfu_losses=np.zeros(len(other))
        indelec_used=np.zeros(len(other))
        indelec_losses=np.zeros(len(other))
        for i in range(len(other)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=other[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=other[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecother[i]+totheatother[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecother[i]+totheatother[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][7]*otherfull[0]
            gas_cd2[i]=gas_mat2[i][7]*otherfull[1]
            biomass_cd2[i]=coal_mat2[i][7]*otherfull[4]
            coal_cd2[i]=coal_mat2[i][7]*otherfull[5]
            elec_cd2[i]=elec_mat2[i][7]*otherfull[6]

    #calculate energy used
    if Exergy=='Exergy':
        #energy efficiency (from Paoli) x quality factor (from cullen) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average exergy efficiency
            oilburneffex=0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #exergy used
        else:
            oilburnused=0

        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average exergy efficiency
            gasburneffex=0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #exergy used
        else:
            gasburnused=0

        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average exergy efficiency
            coalburneffex=0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #exergy used
        else:
            coalburnused=0

        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average exergy efficiency
            bioburneffex=0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #exergy used
        else:
            biomassburnused=0

        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(0.95*dieselengeff*oilengine)+(0.53*turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine

        heatexeff=0.87 #heat exchanger efficiency
        heatexused=0.15*heatexeff*heatex #exergy used

        elecheateff=1 #electric heater efficiency
        elecheatused=0.3*elecheateff*elecheater #exergy used

        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=0.93*elecmotoreff*elecmotor #exergy used

        electroneff=0.85 #electronics efficiency
        electronused=0.3*electroneff*applianceelec #exergy used

        lighteff=0.13 #lighting device efficiency
        lightused=0.9*lighteff*lightingdevice #exergy used

        renheateff=1 #renewable heater efficiency
        renheatused=0.3*renheateff*renheater #exergy used

    elif Exergy=='Energy':
        #energy efficiency (from Paoli) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average energy efficiency
            oilburneffex=(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #energy used
        else:
            oilburnused=0

        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average energy efficiency
            gasburneffex=(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #energy used
        else:
            gasburnused=0

        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average energy efficiency
            coalburneffex=(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #energy used
        else:
            coalburnused=0

        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average energy efficiency
            bioburneffex=(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #energy used
        else:
            biomassburnused=0

        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(dieselengeff*oilengine)+(turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine

        heatexeff=0.87 #heat exchanger efficiency
        heatexused=heatexeff*heatex #energy used

        elecheateff=1 #electric heater efficiency
        elecheatused=elecheateff*elecheater #energy used

        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=elecmotoreff*elecmotor #energy used

        electroneff=0.85 #electronics efficiency
        electronused=electroneff*applianceelec #energy used

        lighteff=0.13 #lighting device efficiency
        lightused=lighteff*lightingdevice #energy used

        renheateff=1 #renewable heater efficiency
        renheatused=renheateff*renheater #energy used

    #values for Sankey labels

    useful=oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+renheatused+elecheatused+heatexused+engused+elecmotorused+electronused+lightused

    #calculate a number of efficiency values
    fueleff=np.zeros(6)
    for i in range(6):
        if (ind_losses[i]+ind_used[i]+indelec_used[i])!=0: #to avoid divide zero errors
            fueleff[i]=(ind_used[i]+indelec_used[i])/(ind_losses[i]+ind_used[i]+indelec_used[i])
    if (np.sum(ind_losses)+np.sum(ind_used)+np.sum(indelec_used))!=0: #to avoid divide zero errors
        totfueleff=(np.sum(ind_used)+np.sum(indelec_used))/(np.sum(ind_losses)+np.sum(ind_used)+np.sum(indelec_used))
    if np.sum(indelec_used)!=0: #to avoid divide zero errors
        elecfeff=(np.sum(fueleff*indelec_used))/(np.sum(indelec_used))
    if (oilengine+coalengine+gasengine+biomassengine)!=0: #to avoid divide zero errors
        engfeff=(fueleff[0]*oilengine+fueleff[1]*gasengine+fueleff[4]*biomassengine+fueleff[5]*coalengine)/((oilengine+coalengine+gasengine+biomassengine))
    
    if (np.sum(elec_cd)+heat_cd)!=0: #to avoid divide zero erros
        if ((np.sum(elec_cd)/(np.sum(elec_cd)+heat_cd))*np.sum(indelec_used))!=0: #to avoid divide zero erros
            eleceff=(elecmotor+elecheater+applianceelec+lightingdevice)/((np.sum(elec_cd)/(np.sum(elec_cd)+heat_cd))*np.sum(indelec_used))
        if ((heat_cd/(np.sum(elec_cd)+heat_cd))*np.sum(indelec_used))!=0: #to avoid divide zero erros
            heateff=heatex/((heat_cd/(np.sum(elec_cd)+heat_cd))*np.sum(indelec_used))
    if np.sum(indelec_used)!=0: #to avoid divide zero erros
        alleleceff=(heatex+elecmotor+elecheater+applianceelec+lightingdevice)/(np.sum(indelec_used))
    
    if oilburner!=0: #to avoid divide zero errors
        oilburnefficiency=oilburnused/oilburner
    if gasburner!=0: #to avoid divide zero errors
        gasburnefficiency=gasburnused/gasburner
    if biomassburner!=0: #to avoid divide zero errors
        biomassburnefficiency=biomassburnused/biomassburner
    if coalburner!=0: #to avoid divide zero errors
        coalburnefficiency=coalburnused/coalburner
    if (oilengine+coalengine+oilengine+biomassengine)!=0: #to avoid divide zero errors
        dieselengefficiency=engused/(oilengine+coalengine+oilengine+biomassengine)
    if heatex!=0: #to avoid divide zero errors
        heatexefficiency=heatexused/heatex
    if elecheater!=0: #to avoid divide zero errors
        elecheatefficiency=elecheatused/elecheater
    if elecmotor!=0: #to avoid divide zero errors
        elecmotorefficiency=elecmotorused/elecmotor
    if applianceelec!=0: #to avoid divide zero errors
        electronefficiency=electronused/applianceelec
    if lightingdevice!=0: #to avoid divide zero errors
        lightefficiency=lightused/lightingdevice
    if renheater!=0: #to avoid divide zero errors
        renheatefficiency=renheatused/renheater
    
    try:
        oilburneffcomp=fueleff[0]*oilburnefficiency
    except:
        pass
    try:
        gasburneffcomp=fueleff[1]*gasburnefficiency
    except:
        pass
    try:
        coalburneffcomp=fueleff[5]*coalburnefficiency
    except:
        pass
    try:
        biomassburneffcomp=fueleff[4]*biomassburnefficiency
    except:
        pass
    try:
        dieselengeffcomp=engfeff*dieselengefficiency
    except:
        pass
    try:
        heatexeffcomp=totfueleff*heateff*heatexefficiency
    except:
        pass
    try:
        elecheateffcomp=totfueleff*eleceff*elecheatefficiency
    except:
        pass
    try:
        elecmotoreffcomp=totfueleff*eleceff*elecmotorefficiency
    except:
        pass
    try:
        electroneffcomp=totfueleff*eleceff*electronefficiency
    except:
        pass
    try:
        lighteffcomp=totfueleff*eleceff*lightefficiency
    except:
        pass
    try:
        renheateffcomp=fueleff[3]*renheatefficiency
    except:
        pass

    if PrimEng!=0: #to avoid divide zero errors
        eff=useful/PrimEng
        
    try:
        print('The Efficiency of Oil Transformation is {:.0f}%'.format(fueleff[0]*100))
    except:
        pass
    try:
        print('The Efficiency of Gas Transformation is {:.0f}%'.format(fueleff[1]*100))
    except:
        pass
    try:
        print('The Efficiency of Nuclear Transformation is {:.0f}%'.format(fueleff[2]*100))
    except:
        pass
    try:
        print('The Efficiency of Renewable Transformation is {:.0f}%'.format(fueleff[3]*100))
    except:
        pass
    try:
        print('The Efficiency of Biomass Transformation is {:.0f}%'.format(fueleff[4]*100))
    except:
        pass
    try:
        print('The Efficiency of Coal Transformation is {:.0f}%'.format(fueleff[5]*100))
    except:
        pass
    try:
        print('The Efficiency of Fuel Transformation for Electricity Generation is {:.0f}%'.format(elecfeff*100))
    except:
        pass
    try:
        print('The Efficiency of Fuel Transformation for Engines is {:.0f}%'.format(engfeff*100))
    except:
        pass
    try:
        print('The Total Efficiency of Fuel Transformation is {:.0f}%'.format(totfueleff*100))
    except:
        pass
    
    try:
        print('The Efficiency of Electricity Production in', Country, 'is {0:.0f}%'.format(eleceff*100))
    except:
        pass
    try:
        print('The Efficiency of Heat Production in', Country, 'is {0:.0f}% '.format(heateff*100))
    except:
        pass
    try:
        print('The Average Efficiency of both Heat and Electricity Production in', Country, 'is {0:.0f}%'.format(alleleceff*100))
    except:
        pass
    
    try:
        print('The Efficiency of Oil Burner is {:.0f}%'.format(oilburnefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Biomass Burner is {:.0f}%'.format(biomassburnefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Gas Burner is {:.0f}%'.format(gasburnefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Coal Burner is {:.0f}%'.format(coalburnefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Heat Exchanger is {:.0f}%'.format(heatexefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Electric Heater is {:.0f}%'.format(elecheatefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Renewable Heater is {:.0f}%'.format(renheatefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Engine is {:.0f}%'.format(dieselengefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Electric Motor is {:.0f}%'.format(elecmotorefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Electronic is {:.0f}%'.format(electronefficiency*100))
    except:
        pass
    try:
        print('The Efficiency of Lighting Device is {:.0f}%'.format(lightefficiency*100))
    except:
        pass
    
    try:
        print('The Compound Efficiency of Oil Burner is {:.0f}%'.format(oilburneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Biomass Burner is {:.0f}%'.format(biomassburneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Gas Burner is {:.0f}%'.format(gasburneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Coal Burner is {:.0f}%'.format(coalburneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Heat Exchanger is {:.0f}%'.format(heatexeffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Electric Heater is {:.0f}%'.format(elecheateffcomp*100))#
    except:
        pass
    try:
        print('The Compound Efficiency of Renewable Heater is {:.0f}%'.format(renheateffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Engine is {:.0f}%'.format(dieselengeffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Electric Motor is {:.0f}%'.format(elecmotoreffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Electronic is {:.0f}%'.format(electroneffcomp*100))
    except:
        pass
    try:
        print('The Compound Efficiency of Lighting Device is {:.0f}%'.format(lighteffcomp*100))
    except:
        pass
    
    try:
        print('The Total', Exergy, 'Efficiency of the industrial sector in', Country,  'is {:.0f}%'.format(eff*100))
    except:
        pass
    return

###SECTOR CHANGING DEVICE EFFICIENCY SANKEY GENERATOR FUNCTION ###
def sectorchange(IEATES,IEATFC,electricity,heat,Country,Year,Exergy,Sector,Device,Value):
    '''
    Function to return a Sankey Diagram with altered
    engineering device efficiency for a given sector
    
    Inputs: 
        IEATES - Energy Supply Values from IEA
        IEATFC - Energy Consumption Values from IEA
        electricity - Electricity Consumption values from IEA
        heat - Heat Consumption values from IEA
        Country - name of country from IEA list
        Year - year between 1960 and 2019
        Exergy - Produce Diagram in Exergy or Energy Values
        Sector - Sector for which the diagram will be produced
        Device - name of engineering device for which
                the efficiency is to be altered
        Value - new value of engineering device efficiency
        
    Returns a Sankey diagram for the given year, country
    and sector with the new device efficiency taken into
    account (and prints the new overall efficiency, the 
    change in overall efficiency and the change in primary
    energy demand)
    
    '''
    #convert supply to exergy values and combine oil and renewable products (exergy factors from https://doi.org/10.3390/en9090707)
    if Exergy=='Exergy':                          
        exergy=np.array([1.04*IEATES[0],1.03*IEATES[1],0.95*IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],1.13*IEATES[6],1.06*IEATES[7]])
        exergy_h=0.17*heat
    elif Exergy=='Energy':
        exergy=np.array([IEATES[0],IEATES[1],IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],IEATES[6],IEATES[7]])
        exergy_h=heat                          

    #calculate total electricity generation and direct fuel use
    tpes=np.zeros(len(exergy))
    losses=np.zeros(len(exergy))
    tfc=np.zeros(len(exergy))
    nonenergy=np.zeros(len(exergy))
    egeneration=np.zeros(len(exergy))
    hgeneration=np.zeros(len(exergy))
    for i in range (0,len(exergy)):
        tpes[i]=exergy[i][0]
        #combine all losses
        for j in range(1,3):
            losses[i]=losses[i]+exergy[i][j] 
        for j in range(9,23):
            losses[i]=losses[i]+exergy[i][j]
        tfc[i]=exergy[i][23]
        nonenergy[i]=exergy[i][24]
        #combine electriciy and heat generation from electricity, heating and CHP plants
        for j in range(3,5):
            egeneration[i]=egeneration[i]+exergy[i][j]
        for j in range(5,7):
            egeneration[i]=egeneration[i]+0.89*exergy[i][j]
            hgeneration[i]=hgeneration[i]+0.11*exergy[i][j]
        for j in range(7,9):
            hgeneration[i]=hgeneration[i]+exergy[i][j]

    dfu_used=tfc-nonenergy #total fuel used directly is total final consumption of fuel - non-energy use
    elec_used=-egeneration-hgeneration #total fuel used for electricity generation is combination of fuels to all plants from above (- sign to yield +ve values)

    #losses split proportionally between dfu & electricity generation
    dfu_losses=np.zeros(len(tpes))
    elec_losses=np.zeros(len(tpes))
    for i in range(len(tpes)):
        if tpes[i]+losses[i]==0: #to avoid divide zero errors
            dfu_losses[i]=0
            elec_losses[i]=0
        else: #- signs as losses[i] have -ve values
            dfu_losses[i]=-dfu_used[i]*(losses[i]/(tpes[i]+losses[i])) 
            elec_losses[i]=-elec_used[i]*(losses[i]/(tpes[i]+losses[i]))
    #convert from TJ to PJ
    direct_fuel_use=(dfu_used+dfu_losses)/(10**3)
    electricity_generation=(elec_used+elec_losses)/(10**3)

    #convert consumption to exergy values and combine oil and renewable products
    exergycons=np.array([1.04*IEATFC[0],1.03*IEATFC[1],0.95*IEATFC[2],IEATFC[3]+IEATFC[4]+IEATFC[5],1.11*IEATFC[6],1.06*IEATFC[7]])


    #calculate total electricity (& heat) 
    totelec=electricity[0]+electricity[15]+electricity[24]+electricity[25]+electricity[26]+electricity[27]+electricity[28]
    totheat=exergy_h[0]+exergy_h[15]+exergy_h[24]+exergy_h[25]+exergy_h[26]+exergy_h[27]+exergy_h[28]

    if (totelec+totheat)!=0: #to avoid divide zero errors
        totelec_=totelec/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
        totheat_=totheat/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
    else:
        totelec_=0
        totheat_=0

    #calculate direct fuel use energy to steel
    steel=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        steel[i]=exergycons[i][4]
    steel=steel/(10**3)

    #calculate direct fuel use energy to aluminium
    aluminium=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        aluminium[i]=exergycons[i][6]
    aluminium=aluminium/(10**3)

    #calculate direct fuel use energy to machinery
    machinery=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        machinery[i]=exergycons[i][8]+exergycons[i][9]
    machinery=machinery/(10**3)

    #calculate direct fuel use energy to mineral
    mineral=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        mineral[i]=exergycons[i][7]
    mineral=mineral/(10**3)

    #calculate direct fuel use energy to chemical
    chemical=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        chemical[i]=exergycons[i][5]
    chemical=chemical/(10**3)

    #calculate direct fuel use energy to paper
    paper=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        paper[i]=exergycons[i][11]+exergycons[i][12]
    paper=paper/(10**3)

    #calculate direct fuel use energy to food
    food=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        food[i]=exergycons[i][10]
    food=food/(10**3)

    #calculate direct fuel use energy to other
    other=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        other[i]=exergycons[i][1]+exergycons[i][2]+exergycons[i][13]+exergycons[i][14]
    other=other/(10**3)

    #scale to include losses
    for i in range(len(dfu_used)):
        if dfu_used[i]!=0:
            steel[i]=steel[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            aluminium[i]=aluminium[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            machinery[i]=machinery[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            mineral[i]=mineral[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            chemical[i]=chemical[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            paper[i]=paper[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            food[i]=food[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            other[i]=other[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))

    #scale electricity (& heat) flow to each subsector
    if totelec!=0:
        elec_steel=(electricity[4]/totelec)*totelec_
        elec_aluminium=(electricity[6]/totelec)*totelec_
        elec_machinery=((electricity[8]+electricity[9])/totelec)*totelec_
        elec_mineral=(electricity[7]/totelec)*totelec_
        elec_chemical=(electricity[5]/totelec)*totelec_
        elec_paper=((electricity[11]+electricity[12])/totelec)*totelec_
        elec_food=(electricity[10]/totelec)*totelec_
        elec_other=((electricity[1]+electricity[2]+electricity[13]+electricity[14])/totelec)*totelec_
    else:
        elec_steel=0
        elec_steel=0
        elec_aluminium=0
        elec_machinery=0
        elec_mineral=0
        elec_chemical=0
        elec_paper=0
        elec_food=0
        elec_other=0

    if totheat!=0:
        heat_steel=(exergy_h[4]/totheat)*totheat_
        heat_aluminium=(exergy_h[6]/totheat)*totheat_
        heat_machinery=((exergy_h[8]+exergy_h[9])/totheat)*totheat_
        heat_mineral=(exergy_h[7]/totheat)*totheat_
        heat_chemical=(exergy_h[5]/totheat)*totheat_
        heat_paper=((exergy_h[11]+exergy_h[12])/totheat)*totheat_
        heat_food=(exergy_h[10]/totheat)*totheat_
        heat_other=((exergy_h[1]+exergy_h[2]+exergy_h[13]+exergy_h[14])/totheat)*totheat_
    else:
        heat_steel=0
        heat_steel=0
        heat_aluminium=0
        heat_machinery=0
        heat_mineral=0
        heat_chemical=0
        heat_paper=0
        heat_food=0
        heat_other=0

    #calculate energy to electricity from each fuel for steel
    totelecsteel=np.zeros(len(exergycons))
    totheatsteel=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecsteel[i]=(elec_steel/np.sum(electricity_generation))*electricity_generation[i]
            totheatsteel[i]=(heat_steel/np.sum(electricity_generation))*electricity_generation[i]

    #caluminiumculate energy to electricity from each fuel for aluminium
    totelecaluminium=np.zeros(len(exergycons))
    totheataluminium=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecaluminium[i]=(elec_aluminium/np.sum(electricity_generation))*electricity_generation[i]
            totheataluminium[i]=(heat_aluminium/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for machinery
    totelecmachinery=np.zeros(len(exergycons))
    totheatmachinery=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecmachinery[i]=(elec_machinery/np.sum(electricity_generation))*electricity_generation[i]
            totheatmachinery[i]=(heat_machinery/np.sum(electricity_generation))*electricity_generation[i]

            #calculate energy to electricity from each fuel for mineral
    totelecmineral=np.zeros(len(exergycons))
    totheatmineral=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecmineral[i]=(elec_mineral/np.sum(electricity_generation))*electricity_generation[i]
            totheatmineral[i]=(heat_mineral/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for chemical
    totelecchemical=np.zeros(len(exergycons))
    totheatchemical=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecchemical[i]=(elec_chemical/np.sum(electricity_generation))*electricity_generation[i]
            totheatchemical[i]=(heat_chemical/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for paper
    totelecpaper=np.zeros(len(exergycons))
    totheatpaper=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecpaper[i]=(elec_paper/np.sum(electricity_generation))*electricity_generation[i]
            totheatpaper[i]=(heat_paper/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for food
    totelecfood=np.zeros(len(exergycons))
    totheatfood=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecfood[i]=(elec_food/np.sum(electricity_generation))*electricity_generation[i]
            totheatfood[i]=(heat_food/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for other
    totelecother=np.zeros(len(exergycons))
    totheatother=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecother[i]=(elec_other/np.sum(electricity_generation))*electricity_generation[i]
            totheatother[i]=(heat_other/np.sum(electricity_generation))*electricity_generation[i]



    #append electricity and heat values to sub-sector fuel consumption arrays
    steelfull=np.append(steel, [elec_steel, heat_steel])
    aluminiumfull=np.append(aluminium, [elec_aluminium, heat_aluminium])
    machineryfull=np.append(machinery, [elec_machinery, heat_machinery])
    mineralfull=np.append(mineral, [elec_mineral, heat_mineral])
    chemicalfull=np.append(chemical, [elec_chemical, heat_chemical])
    paperfull=np.append(paper, [elec_paper, heat_paper])
    foodfull=np.append(food, [elec_food, heat_food])
    otherfull=np.append(other, [elec_other, heat_other])

    #define allocation matrices, based on US steel data - used to assign fuels to passive systems below
    #rows are passive systems, columns are fuels (oil, gas, nuclear, renewables, biomass, coal, electricity, heat))
    steel_mat = np.array([[0.00  , 0.10  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.39  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 1.00  , 1.00  , 0.53  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.03  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#appliance
                         [1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    al_mat = np.array([[0.00  , 0.13  , 1.00  , 0.00  , 0.13  , 0.13  , 0.01  , 0.00  ],#steam
                         [0.25  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.24  , 0.00  ],#driven
                         [0.25  , 0.76  , 0.00  , 0.00  , 0.76  , 0.76  , 0.65  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.03  , 0.00  ],#light
                         [0.00  , 0.09  , 0.00  , 1.00  , 0.09  , 0.09  , 0.04  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.02  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                      ])

    mach_mat = np.array([[0.15  , 0.16  , 1.00  , 0.00  , 0.16  , 0.16  , 0.01  , 0.00  ],#steam
                         [0.14  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.49  , 0.00  ],#driven
                         [0.07  , 0.45  , 0.00  , 0.00  , 0.45  , 0.45  , 0.16  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.11  , 0.00  ],#light
                         [0.14  , 0.35  , 0.00  , 1.00  , 0.35  , 0.35  , 0.19  , 1.00  ],#spaceheat
                         [0.00  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.03  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])

    min_mat = np.array([[0.00  , 0.03  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.38  , 0.08  , 0.00  , 0.00  , 0.10  , 0.10  , 0.60  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 0.90  , 0.90  , 0.28  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.62  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                       ])

    chem_mat = np.array([[0.50  , 0.52  , 1.00  , 0.00  , 0.87  , 0.87  , 0.01  , 0.00  ],#steam
                         [0.00  , 0.04  , 0.00  , 0.00  , 0.00  , 0.00  , 0.63  , 0.00  ],#driven
                         [0.10  , 0.41  , 0.00  , 0.00  , 0.13  , 0.13  , 0.25  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.02  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.40  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                        ])                 

    paper_mat = np.array([[0.36  , 0.63  , 1.00  , 0.00  , 0.98  , 0.98  , 0.04  , 0.00  ],#steam
                         [0.04  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.78  , 0.00  ],#driven
                         [0.08  , 0.30  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.06  , 1.00  ],#spaceheat
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.52  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    food_mat = np.array([[0.59  , 0.59  , 1.00  , 0.00  , 0.79  , 0.79  , 0.03  , 0.00  ],#steam
                         [0.00  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.69  , 0.00  ],#driven
                         [0.00  , 0.27  , 0.00  , 0.00  , 0.21  , 0.21  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#light
                         [0.08  , 0.08  , 0.00  , 1.00  , 0.00  , 0.00  , 0.11  , 1.00  ],#spaceheat
                         [0.08  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.25  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])

    other_mat = np.array([[0.13  , 0.34  , 1.00  , 0.00  , 1.00  , 1.00  , 0.01  , 0.00  ],#steam
                         [0.13  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.73  , 0.00  ],#driven
                         [0.71  , 0.61  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.06  , 0.00  ],#light
                         [0.00  , 0.04  , 0.00  , 1.00  , 0.00  , 0.00  , 0.09  , 1.00  ],#spaceheat
                         [0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    #import data on share of steel from EAF
    import pandas as pd
    df=pd.read_csv('SteelShares2023.csv')
    try:
        EAF=float(df['EAF'][df['Country'] == Country].values[0])
    except:
        EAF=float(df['EAF'][df['Country'] == 'World'].values[0])

    #calculate new allocation matrices for steel, based on share of EAF
    x=(442.01*EAF)/((442.01*EAF)+(4128.05*(1-EAF)))
    z1=0.943*x+0.045*(1-x)
    z2=0.928*(1-x)
    z3=0.057*x+0.027*(1-x)
    gamma=0

    if x==1:
        if electricity[4]!=0:
            gammaprime=(0.02*IEATFC[1][4]/electricity[4])*(z1/z3)
            steel_mat[2][6]=0.4+0.6*gammaprime
            steel_mat[1][6]=0.5*(1-gammaprime)
            steel_mat[3][6]=0.04*(1-gammaprime)
            steel_mat[4][6]=0.05*(1-gammaprime)
            steel_mat[5][6]=0.01*(1-gammaprime)
    else:
        if electricity[4]!=0:
            gamma=(IEATFC[7][4]/electricity[4])*(z1/z2)
            steel_mat[2][6]=0.4+0.6*gamma
            steel_mat[1][6]=0.5*(1-gamma)
            steel_mat[3][6]=0.04*(1-gamma)
            steel_mat[4][6]=0.05*(1-gamma)
            steel_mat[5][6]=0.01*(1-gamma)
        if IEATFC[1][4]!=0:
            delta=(IEATFC[7][4]/IEATFC[1][4])*(z3/z2)
            steel_mat[2][1]=0.83+0.17*delta
            steel_mat[0][1]=0.1*(1-delta)
            steel_mat[1][1]=0.01*(1-delta)
            steel_mat[4][1]=0.05*(1-delta)
            steel_mat[5][1]=0.01*(1-delta)

    #use matrix multiplication to assign fuel to each passive system
    steel_ps=np.zeros(7)
    al_ps=np.zeros(7)
    mach_ps=np.zeros(7)
    min_ps=np.zeros(7)
    chem_ps=np.zeros(7)
    paper_ps=np.zeros(7)
    food_ps=np.zeros(7)
    other_ps=np.zeros(7)
    for i in range(0,len(steelfull)):
        for j in range(0,7):
            steel_ps[j]=steel_ps[j]+steelfull[i]*steel_mat[j][i]
            al_ps[j]=al_ps[j]+aluminiumfull[i]*al_mat[j][i]
            mach_ps[j]=mach_ps[j]+machineryfull[i]*mach_mat[j][i]
            min_ps[j]=min_ps[j]+mineralfull[i]*min_mat[j][i]
            chem_ps[j]=chem_ps[j]+chemicalfull[i]*chem_mat[j][i]
            paper_ps[j]=paper_ps[j]+paperfull[i]*paper_mat[j][i]
            food_ps[j]=food_ps[j]+foodfull[i]*food_mat[j][i]
            other_ps[j]=other_ps[j]+otherfull[i]*other_mat[j][i]

    #define matrices for assigning fuels to conversion devices
    #rows are purposes of converson devices, columns are industries (steel, aluminium, machinery, mineral, chemical, paper, food, other)
    oil_mat = np.array([[1.00, 0.75, 0.64, 1.00, 0.40, 0.56, 0.25, 0.13],#motion
                       [0.00, 0.25, 0.36, 0.00, 0.60, 0.44, 0.67, 0.84],#heat
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.08, 0.03]])#appliance

    gas_mat = np.array([[steel_mat[1][1]+steel_mat[6][1], 0.01, 0.02, 0.08, 0.04, 0.02, 0.03, 0.01],#motion
                       [steel_mat[0][1]+steel_mat[2][1]+steel_mat[4][1], 0.98, 0.96, 0.91, 0.95, 0.98, 0.94, 0.99],#heat
                       [steel_mat[3][1], 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [steel_mat[5][1], 0.01, 0.02, 0.01, 0.01, 0.00, 0.03, 0.00]])#appliance

    coal_mat = np.array([[0.00, 0.01, 0.02, 0.10, 0.00, 0.02, 0.00, 0.00],#motion
                        [1.00, 0.98, 0.96, 0.90, 1.00, 0.98, 1.00, 1.00],#heat
                        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                        [0.00, 0.01, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00]])#appliance

    elec_mat = np.array([[steel_mat[1][6]+steel_mat[6][6], 0.25, 0.50, 0.60, 0.63, 0.78, 0.70, 0.73],#motion
                        [steel_mat[0][6]+steel_mat[2][6]+steel_mat[4][6], 0.70, 0.36, 0.33, 0.31, 0.15, 0.19, 0.19],#heat
                        [steel_mat[3][6], 0.03, 0.11, 0.05, 0.04, 0.05, 0.09, 0.06],#light
                        [steel_mat[5][6], 0.02, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02]])#appliance

    #create new matrices with all passive systems
    oil_mat2=np.zeros((7,8))
    for i in range(7):
        oil_mat2[i][0]=steel_mat[i][0]
        oil_mat2[i][1]=al_mat[i][0]
        oil_mat2[i][2]=mach_mat[i][0]
        oil_mat2[i][3]=min_mat[i][0]
        oil_mat2[i][4]=chem_mat[i][0]
        oil_mat2[i][5]=paper_mat[i][0]
        oil_mat2[i][6]=food_mat[i][0]
        oil_mat2[i][7]=other_mat[i][0]

    gas_mat2=np.zeros((7,8))
    for i in range(7):
        gas_mat2[i][0]=steel_mat[i][1]
        gas_mat2[i][1]=al_mat[i][1]
        gas_mat2[i][2]=mach_mat[i][1]
        gas_mat2[i][3]=min_mat[i][1]
        gas_mat2[i][4]=chem_mat[i][1]
        gas_mat2[i][5]=paper_mat[i][1]
        gas_mat2[i][6]=food_mat[i][1]
        gas_mat2[i][7]=other_mat[i][1]

    coal_mat2=np.zeros((7,8))
    for i in range(7):
        coal_mat2[i][0]=steel_mat[i][4]
        coal_mat2[i][1]=al_mat[i][4]
        coal_mat2[i][2]=mach_mat[i][4]
        coal_mat2[i][3]=min_mat[i][4]
        coal_mat2[i][4]=chem_mat[i][4]
        coal_mat2[i][5]=paper_mat[i][4]
        coal_mat2[i][6]=food_mat[i][4]
        coal_mat2[i][7]=other_mat[i][4]

    elec_mat2=np.zeros((7,8))#
    for i in range(7):
        elec_mat2[i][0]=steel_mat[i][6]
        elec_mat2[i][1]=al_mat[i][6]
        elec_mat2[i][2]=mach_mat[i][6]
        elec_mat2[i][3]=min_mat[i][6]
        elec_mat2[i][4]=chem_mat[i][6]
        elec_mat2[i][5]=paper_mat[i][6]
        elec_mat2[i][6]=food_mat[i][6]
        elec_mat2[i][7]=other_mat[i][6]

    if Sector=='Steel':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][0]*steelfull[0]
            gas_cd[i]=gas_mat[i][0]*steelfull[1]
            biomass_cd[i]=coal_mat[i][0]*steelfull[4]
            coal_cd[i]=coal_mat[i][0]*steelfull[5]
            elec_cd[i]=elec_mat[i][0]*steelfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=steelfull[7]

        #values for Sankey labels
        PrimEng=np.sum(steel)+np.sum(totelecsteel)+np.sum(totheatsteel)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(steel))
        inddfu_losses=np.zeros(len(steel))
        indelec_used=np.zeros(len(steel))
        indelec_losses=np.zeros(len(steel))
        for i in range(len(steel)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=steel[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=steel[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecsteel[i]+totheatsteel[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecsteel[i]+totheatsteel[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][0]*steelfull[0]
            gas_cd2[i]=gas_mat2[i][0]*steelfull[1]
            biomass_cd2[i]=coal_mat2[i][0]*steelfull[4]
            coal_cd2[i]=coal_mat2[i][0]*steelfull[5]
            elec_cd2[i]=elec_mat2[i][0]*steelfull[6]

    if Sector=='Aluminium':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][1]*aluminiumfull[0]
            gas_cd[i]=gas_mat[i][1]*aluminiumfull[1]
            biomass_cd[i]=coal_mat[i][1]*aluminiumfull[4]
            coal_cd[i]=coal_mat[i][1]*aluminiumfull[5]
            elec_cd[i]=elec_mat[i][1]*aluminiumfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=aluminiumfull[7]

        #values for Sankey labels
        PrimEng=np.sum(aluminium)+np.sum(totelecaluminium)+np.sum(totheataluminium)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(aluminium))
        inddfu_losses=np.zeros(len(aluminium))
        indelec_used=np.zeros(len(aluminium))
        indelec_losses=np.zeros(len(aluminium))
        for i in range(len(aluminium)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=aluminium[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=aluminium[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecaluminium[i]+totheataluminium[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecaluminium[i]+totheataluminium[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][1]*aluminiumfull[0]
            gas_cd2[i]=gas_mat2[i][1]*aluminiumfull[1]
            biomass_cd2[i]=coal_mat2[i][1]*aluminiumfull[4]
            coal_cd2[i]=coal_mat2[i][1]*aluminiumfull[5]
            elec_cd2[i]=elec_mat2[i][1]*aluminiumfull[6]

    if Sector=='Machinery':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][2]*machineryfull[0]
            gas_cd[i]=gas_mat[i][2]*machineryfull[1]
            biomass_cd[i]=coal_mat[i][2]*machineryfull[4]
            coal_cd[i]=coal_mat[i][2]*machineryfull[5]
            elec_cd[i]=elec_mat[i][2]*machineryfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=machineryfull[7]

        #values for Sankey labels
        PrimEng=np.sum(machinery)+np.sum(totelecmachinery)+np.sum(totheatmachinery)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(machinery))
        inddfu_losses=np.zeros(len(machinery))
        indelec_used=np.zeros(len(machinery))
        indelec_losses=np.zeros(len(machinery))
        for i in range(len(machinery)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=machinery[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=machinery[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecmachinery[i]+totheatmachinery[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecmachinery[i]+totheatmachinery[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][2]*machineryfull[0]
            gas_cd2[i]=gas_mat2[i][2]*machineryfull[1]
            biomass_cd2[i]=coal_mat2[i][2]*machineryfull[4]
            coal_cd2[i]=coal_mat2[i][2]*machineryfull[5]
            elec_cd2[i]=elec_mat2[i][2]*machineryfull[6]

    if Sector=='Mineral':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][3]*mineralfull[0]
            gas_cd[i]=gas_mat[i][3]*mineralfull[1]
            biomass_cd[i]=coal_mat[i][3]*mineralfull[4]
            coal_cd[i]=coal_mat[i][3]*mineralfull[5]
            elec_cd[i]=elec_mat[i][3]*mineralfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=mineralfull[7]

        #values for Sankey labels
        PrimEng=np.sum(mineral)+np.sum(totelecmineral)+np.sum(totheatmineral)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(mineral))
        inddfu_losses=np.zeros(len(mineral))
        indelec_used=np.zeros(len(mineral))
        indelec_losses=np.zeros(len(mineral))
        for i in range(len(mineral)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=mineral[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=mineral[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecmineral[i]+totheatmineral[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecmineral[i]+totheatmineral[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][3]*mineralfull[0]
            gas_cd2[i]=gas_mat2[i][3]*mineralfull[1]
            biomass_cd2[i]=coal_mat2[i][3]*mineralfull[4]
            coal_cd2[i]=coal_mat2[i][3]*mineralfull[5]
            elec_cd2[i]=elec_mat2[i][3]*mineralfull[6]

    if Sector=='Chemical':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][4]*chemicalfull[0]
            gas_cd[i]=gas_mat[i][4]*chemicalfull[1]
            biomass_cd[i]=coal_mat[i][4]*chemicalfull[4]
            coal_cd[i]=coal_mat[i][4]*chemicalfull[5]
            elec_cd[i]=elec_mat[i][4]*chemicalfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=chemicalfull[7]

        #values for Sankey labels
        PrimEng=np.sum(chemical)+np.sum(totelecchemical)+np.sum(totheatchemical)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(chemical))
        inddfu_losses=np.zeros(len(chemical))
        indelec_used=np.zeros(len(chemical))
        indelec_losses=np.zeros(len(chemical))
        for i in range(len(chemical)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=chemical[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=chemical[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecchemical[i]+totheatchemical[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecchemical[i]+totheatchemical[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][4]*chemicalfull[0]
            gas_cd2[i]=gas_mat2[i][4]*chemicalfull[1]
            biomass_cd2[i]=coal_mat2[i][4]*chemicalfull[4]
            coal_cd2[i]=coal_mat2[i][4]*chemicalfull[5]
            elec_cd2[i]=elec_mat2[i][4]*chemicalfull[6]

    if Sector=='Paper':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][5]*paperfull[0]
            gas_cd[i]=gas_mat[i][5]*paperfull[1]
            biomass_cd[i]=coal_mat[i][5]*paperfull[4]
            coal_cd[i]=coal_mat[i][5]*paperfull[5]
            elec_cd[i]=elec_mat[i][5]*paperfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=paperfull[7]

        #values for Sankey labels
        PrimEng=np.sum(paper)+np.sum(totelecpaper)+np.sum(totheatpaper)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(paper))
        inddfu_losses=np.zeros(len(paper))
        indelec_used=np.zeros(len(paper))
        indelec_losses=np.zeros(len(paper))
        for i in range(len(paper)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=paper[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=paper[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecpaper[i]+totheatpaper[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecpaper[i]+totheatpaper[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][5]*paperfull[0]
            gas_cd2[i]=gas_mat2[i][5]*paperfull[1]
            biomass_cd2[i]=coal_mat2[i][5]*paperfull[4]
            coal_cd2[i]=coal_mat2[i][5]*paperfull[5]
            elec_cd2[i]=elec_mat2[i][5]*paperfull[6]

    if Sector=='Food':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][6]*foodfull[0]
            gas_cd[i]=gas_mat[i][6]*foodfull[1]
            biomass_cd[i]=coal_mat[i][6]*foodfull[4]
            coal_cd[i]=coal_mat[i][6]*foodfull[5]
            elec_cd[i]=elec_mat[i][6]*foodfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=foodfull[7]

        #values for Sankey labels
        PrimEng=np.sum(food)+np.sum(totelecfood)+np.sum(totheatfood)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(food))
        inddfu_losses=np.zeros(len(food))
        indelec_used=np.zeros(len(food))
        indelec_losses=np.zeros(len(food))
        for i in range(len(food)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=food[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=food[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecfood[i]+totheatfood[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecfood[i]+totheatfood[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][6]*foodfull[0]
            gas_cd2[i]=gas_mat2[i][6]*foodfull[1]
            biomass_cd2[i]=coal_mat2[i][6]*foodfull[4]
            coal_cd2[i]=coal_mat2[i][6]*foodfull[5]
            elec_cd2[i]=elec_mat2[i][6]*foodfull[6]

    if Sector=='Other':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][7]*otherfull[0]
            gas_cd[i]=gas_mat[i][7]*otherfull[1]
            biomass_cd[i]=coal_mat[i][7]*otherfull[4]
            coal_cd[i]=coal_mat[i][7]*otherfull[5]
            elec_cd[i]=elec_mat[i][7]*otherfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=otherfull[7]

        #values for Sankey labels
        PrimEng=np.sum(other)+np.sum(totelecother)+np.sum(totheatother)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(other))
        inddfu_losses=np.zeros(len(other))
        indelec_used=np.zeros(len(other))
        indelec_losses=np.zeros(len(other))
        for i in range(len(other)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=other[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=other[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecother[i]+totheatother[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecother[i]+totheatother[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][7]*otherfull[0]
            gas_cd2[i]=gas_mat2[i][7]*otherfull[1]
            biomass_cd2[i]=coal_mat2[i][7]*otherfull[4]
            coal_cd2[i]=coal_mat2[i][7]*otherfull[5]
            elec_cd2[i]=elec_mat2[i][7]*otherfull[6]

    #calculate energy used
    if Exergy=='Exergy':
        #energy efficiency (from Paoli) x quality factor (from cullen) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average exergy efficiency
            oilburneffex=0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #exergy used
        else:
            oilburnused=0

        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average exergy efficiency
            gasburneffex=0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #exergy used
        else:
            gasburnused=0

        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average exergy efficiency
            coalburneffex=0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #exergy used
        else:
            coalburnused=0

        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average exergy efficiency
            bioburneffex=0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #exergy used
        else:
            biomassburnused=0

        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(0.95*dieselengeff*oilengine)+(0.53*turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine

        heatexeff=0.87 #heat exchanger efficiency
        heatexused=0.15*heatexeff*heatex #exergy used

        elecheateff=1 #electric heater efficiency
        elecheatused=0.3*elecheateff*elecheater #exergy used

        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=0.93*elecmotoreff*elecmotor #exergy used

        electroneff=0.85 #electronics efficiency
        electronused=0.3*electroneff*applianceelec #exergy used

        lighteff=0.13 #lighting device efficiency
        lightused=0.9*lighteff*lightingdevice #exergy used

        renheateff=1 #renewable heater efficiency
        renheatused=0.3*renheateff*renheater #exergy used

    elif Exergy=='Energy':
        #energy efficiency (from Paoli) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average energy efficiency
            oilburneffex=(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #energy used
        else:
            oilburnused=0

        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average energy efficiency
            gasburneffex=(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #energy used
        else:
            gasburnused=0

        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average energy efficiency
            coalburneffex=(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #energy used
        else:
            coalburnused=0

        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average energy efficiency
            bioburneffex=(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #energy used
        else:
            biomassburnused=0

        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(dieselengeff*oilengine)+(turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine

        heatexeff=0.87 #heat exchanger efficiency
        heatexused=heatexeff*heatex #energy used

        elecheateff=1 #electric heater efficiency
        elecheatused=elecheateff*elecheater #energy used

        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=elecmotoreff*elecmotor #energy used

        electroneff=0.85 #electronics efficiency
        electronused=electroneff*applianceelec #energy used

        lighteff=0.13 #lighting device efficiency
        lightused=lighteff*lightingdevice #energy used

        renheateff=1 #renewable heater efficiency
        renheatused=renheateff*renheater #energy used
        
        
    Heateff='Heat ({:.0f}PJ)'.format(oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+elecheatused+heatexused+renheatused)
    Motioneff='Motion ({:.0f}PJ)'.format(engused+elecmotorused)
    Othereff='Other ({:.0f}PJ)'.format(electronused+lightused)

    ###NEW EFFICIENCY###
    #user inputs new device efficiency in %
    value=float(Value)/100
    #for given device change value for that device whilst keeping others the same
    if Exergy=='Exergy':
        if Device=='Oil Burner':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/(0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + value*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Oil Boiler':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/(0.25*(value*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Burner':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/(0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + value*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Boiler':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/(0.21*(value*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/(0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + value*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/(0.31*(value*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/(0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + value*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/(0.2*(value*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Diesel Engine':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=(engused-(0.53*turbeff*(gasengine+coalengine+biomassengine)))/(0.95*value)
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Turbine':
            turbine=(engused-(0.95*dieselengeff*oilengine))/(0.53*value)
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            if (gasengine+coalengine+biomassengine)!=0:
                gasenginenew=turbine/(gasengine+coalengine+biomassengine)*gasengine
                coalenginenew=turbine/(gasengine+coalengine+biomassengine)*coalengine
                biomassenginenew=turbine/(gasengine+coalengine+biomassengine)*biomassengine
            else:
                gasenginenew=0
                coalenginenew=0
                biomassenginenew=0
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Heat Exchanger':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatexused/(0.15*value)
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheatused/(0.3*value)
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Motor':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotorused/(0.93*value)
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electronic':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=electronused/(0.3*value)
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Lighting Device':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightused/(0.9*value)
            renheaternew=renheater
        if Device=='Renewable Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheatused/(0.3*value)
    if Exergy=='Energy':
        if Device=='Oil Burner':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/((oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + value*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Oil Boiler':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/((value*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Burner':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/((gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + value*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Boiler':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/((value*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/((coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + value*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/((value*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/((bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + value*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/((value*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Diesel Engine':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=(engused-(turbeff*(gasengine+coalengine+biomassengine)))/(value)
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Turbine':
            turbine=(engused-(dieselengeff*oilengine))/(value)
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            if (gasengine+coalengine+biomassengine)!=0:
                gasenginenew=turbine/(gasengine+coalengine+biomassengine)*gasengine
                coalenginenew=turbine/(gasengine+coalengine+biomassengine)*coalengine
                biomassenginenew=turbine/(gasengine+coalengine+biomassengine)*biomassengine
            else:
                gasenginenew=0
                coalenginenew=0
                biomassenginenew=0
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Heat Exchanger':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatexused/(value)
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheatused/(value)
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Motor':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotorused/(value)
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electronic':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=electronused/(value)
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Lighting Device':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightused/(value)
            renheaternew=renheater
        if Device=='Renewable Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheatused/(value)        

    #calculate energy lost
    oilburnlossnew=oilburnernew-oilburnused
    gasburnlossnew=gasburnernew-gasburnused
    coalburnlossnew=coalburnernew-coalburnused
    biomassburnlossnew=biomassburnernew-biomassburnused
    dieslossnew=(oilenginenew+coalenginenew+gasenginenew+biomassenginenew)-engused
    heatexlossnew=heatexnew-heatexused
    elecheatlossnew=elecheaternew-elecheatused
    elecmotorlossnew=elecmotornew-elecmotorused
    electronlossnew=applianceelecnew-electronused
    lightlossnew=lightingdevicenew-lightused
    renheatlossnew=renheaternew-renheatused
    
    #efficiencies from original Efficiency Sankey required for subsequent calculations
    fueleff=np.zeros(6)
    for i in range(6):
        if (ind_losses[i]+ind_used[i]+indelec_used[i])!=0: #to avoid divide zero errors
            fueleff[i]=(ind_used[i]+indelec_used[i])/(ind_losses[i]+ind_used[i]+indelec_used[i])
        else:
            fueleff[i]=0
    if np.sum(indelec_used)!=0:
        alleleceff=(heatex+elecmotor+elecheater+applianceelec+lightingdevice)/(np.sum(indelec_used))
    else:
        alleleceff=0
    
    
    if alleleceff!=0:
        elossnew=(1/alleleceff-1)*(elecmotornew+elecheaternew+applianceelecnew+lightingdevicenew+heatexnew) #new electricity loss, based on same electricity efficiency as previously
    else:
        elossnew=0
        
    #calculate new primary energy values, based on new final energy demand
    ind_usednew=np.zeros(6)
    indelec_usednew=np.zeros(6)  
    ind_lossesnew=np.zeros(6)  
    ind_usednew[0]=oilenginenew+oilburnernew
    ind_usednew[1]=gasenginenew+gasburnernew
    ind_usednew[2]=nuclearheater
    ind_usednew[3]=renheaternew
    ind_usednew[4]=biomassenginenew+biomassburnernew
    ind_usednew[5]=coalenginenew+coalburnernew
    for i in range(6):
        if np.sum(indelec_used)!=0:
            indelec_usednew[i]=(indelec_used[i]/np.sum(indelec_used))*(elossnew+elecmotornew+elecheaternew+applianceelecnew+lightingdevicenew+heatexnew)
        else:
            indelec_usednew[i]=0
        if fueleff[i]!=0:
            ind_lossesnew[i]=(indelec_usednew[i]+ind_usednew[i])*(1/fueleff[i]-1) #using same fuel transformation efficiency as previously
        else:
            ind_lossesnew[i]=0
            
    #values for Sankey labels
    PrimEngnew=np.sum(indelec_usednew)+np.sum(ind_lossesnew)+np.sum(ind_usednew)

    DFUnew='DFU ({:.0f}PJ)'.format(np.sum(ind_usednew))
    TEGnew='TEG ({:.0f}PJ)'.format(np.sum(indelec_usednew))
    FuelLossnew='Fuel Loss ({:.0f}PJ)'.format(np.sum(ind_lossesnew))

    ConvDevnew=oilburnernew+gasburnernew+nuclearheater+renheaternew+biomassburnernew+coalburnernew+oilenginenew+gasenginenew+biomassenginenew+coalenginenew+elecmotornew+elecheaternew+lightingdevicenew+applianceelecnew+heatexnew
    GenerationLossnew='Generation Loss ({:.0f}PJ)'.format(elossnew)

    ConversionLossnew='Conversion Loss ({:.0f}PJ)'.format(oilburnlossnew+gasburnlossnew+coalburnlossnew+biomassburnlossnew+elecheatlossnew+heatexlossnew+dieslossnew+elecmotorlossnew+electronlossnew+lightlossnew+renheatlossnew)
    useful=oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+renheatused+elecheatused+heatexused+engused+elecmotorused+electronused+lightused
    UsefulEnergy='Useful \n Energy \n ({:.0f}PJ)'.format(useful)
    Lossnew='Loss \n ({:.0f}PJ)'.format(np.sum(ind_lossesnew)+elossnew+oilburnlossnew+gasburnlossnew+coalburnlossnew+biomassburnlossnew+elecheatlossnew+heatexlossnew+dieslossnew+elecmotorlossnew+electronlossnew+lightlossnew+renheatlossnew)
    
    #set up links for Industry Sankey
    links_changed = [
        #direct fuel use
        {'source': 'Oil', 'target': DFUnew, 'value': ind_usednew[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': DFUnew, 'value': ind_usednew[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': DFUnew, 'value': ind_usednew[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': DFUnew, 'value': ind_usednew[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': DFUnew, 'value': ind_usednew[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': DFUnew, 'value': ind_usednew[2], 'type': 'E', 'color': 'purple'},

        #fuel for electricity generation
        {'source': 'Oil', 'target': TEGnew, 'value': indelec_usednew[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': TEGnew, 'value': indelec_usednew[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': TEGnew, 'value': indelec_usednew[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': TEGnew, 'value': indelec_usednew[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': TEGnew, 'value': indelec_usednew[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': TEGnew, 'value': indelec_usednew[2], 'type': 'E', 'color': 'purple'},

        #fuel transformation losses
        {'source': 'Oil', 'target': FuelLossnew, 'value': ind_lossesnew[0], 'type': 'Z', 'color': 'gainsboro' },
        {'source': 'Coal', 'target': FuelLossnew, 'value': ind_lossesnew[5], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Gas', 'target': FuelLossnew, 'value': ind_lossesnew[1], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Biomass', 'target': FuelLossnew, 'value': ind_lossesnew[4], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Renewables', 'target': FuelLossnew, 'value': ind_lossesnew[3], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Nuclear', 'target': FuelLossnew, 'value': ind_lossesnew[2], 'type': 'Z', 'color': 'gainsboro'},

        #direct fuel to conversion devices for heat
        {'source': DFUnew, 'target': 'Oil Burner', 'value': oilburnernew, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUnew, 'target': 'Coal Burner', 'value': coalburnernew, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUnew, 'target': 'Gas Burner', 'value': gasburnernew, 'type': 'C', 'color': 'gold'},
        {'source': DFUnew, 'target': 'Biomass Burner', 'value': biomassburnernew, 'type': 'B', 'color': 'green'},
        {'source': DFUnew, 'target': 'Renewable Heater', 'value': renheaternew, 'type': 'F', 'color': 'dodgerblue'},
        {'source': DFUnew, 'target': 'Nuclear Heater', 'value': nuclearheater, 'type': 'E', 'color': 'purple'},

        #direct fuel to conversion devices for motion
        {'source': DFUnew, 'target': 'Engine', 'value': oilenginenew, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUnew, 'target': 'Engine', 'value': coalenginenew, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUnew, 'target': 'Engine', 'value': gasenginenew, 'type': 'C', 'color': 'gold'},
        {'source': DFUnew, 'target': 'Engine', 'value': biomassenginenew, 'type': 'B', 'color': 'green'}, 

        #electricity to conversion devices
        {'source': TEGnew, 'target': 'Electric Motor', 'value': elecmotornew, 'type': 'H', 'color': 'silver' },
        {'source': TEGnew, 'target': 'Electric Heater', 'value': elecheaternew, 'type': 'H', 'color': 'silver'},
        {'source': TEGnew, 'target': 'Lighting Device', 'value': lightingdevicenew, 'type': 'H', 'color': 'silver'},
        {'source': TEGnew, 'target': 'Electronic', 'value': applianceelecnew, 'type': 'H', 'color': 'silver'},
        {'source': TEGnew, 'target': 'Heat Exchanger', 'value': heatexnew, 'type': 'G', 'color': 'red'},

        #electricity generation losses
        {'source': TEGnew, 'target': GenerationLossnew, 'value': elossnew, 'type': 'Z', 'color': 'gainsboro'},  

        #energy to provide motion
        {'source': 'Engine', 'target': Motioneff, 'value': engused, 'type': 'I', 'color':'lightblue'},
        {'source': 'Electric Motor', 'target': Motioneff, 'value': elecmotorused, 'type': 'I', 'color':'lightblue'},

        #energy to provide heat
        {'source': 'Oil Burner', 'target': Heateff, 'value': oilburnused, 'type': 'G', 'color':'red'},
        {'source': 'Gas Burner', 'target': Heateff, 'value': gasburnused, 'type': 'G', 'color':'red'},
        {'source': 'Coal Burner', 'target': Heateff, 'value': coalburnused, 'type': 'G', 'color':'red'},
        {'source': 'Biomass Burner', 'target': Heateff, 'value': biomassburnused, 'type':'G', 'color':'red'},
        {'source': 'Renewable Heater', 'target': Heateff, 'value': renheatused, 'type': 'G', 'color': 'red'},
        {'source': 'Nuclear Heater', 'target': Heateff, 'value': nuclearheater, 'type': 'E', 'color': 'red'},
        {'source': 'Electric Heater', 'target': Heateff, 'value': elecheatused, 'type': 'G', 'color':'red'},
        {'source': 'Heat Exchanger', 'target': Heateff, 'value': heatexused, 'type': 'G', 'color':'red'},

        #energy used for other purposes
        {'source': 'Lighting Device', 'target': Othereff, 'value': lightused, 'type': 'J', 'color':'black'},
        {'source': 'Electronic', 'target': Othereff, 'value': electronused, 'type': 'J', 'color':'black'},

        #device conversion losses
        {'source': 'Engine', 'target': ConversionLossnew, 'value': dieslossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Motor', 'target': ConversionLossnew, 'value': elecmotorlossnew, 'type': 'Z', 'color':'gainsboro'},

        {'source': 'Oil Burner', 'target': ConversionLossnew, 'value': oilburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Gas Burner', 'target': ConversionLossnew, 'value': gasburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Coal Burner', 'target': ConversionLossnew, 'value': coalburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Biomass Burner', 'target': ConversionLossnew, 'value': biomassburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Heater', 'target': ConversionLossnew, 'value': elecheatlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Heat Exchanger', 'target': ConversionLossnew, 'value': heatexlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Renewable Heater', 'target': ConversionLossnew, 'value': renheatlossnew, 'type': 'Z', 'color':'gainsboro'},

        {'source': 'Lighting Device', 'target': ConversionLossnew, 'value': lightlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electronic', 'target': ConversionLossnew, 'value': electronlossnew, 'type': 'Z', 'color':'gainsboro'},

        #energy lost
        {'source': ConversionLossnew, 'target': Lossnew, 'value': oilburnlossnew+gasburnlossnew+coalburnlossnew+biomassburnlossnew+elecheatlossnew+heatexlossnew+dieslossnew+elecmotorlossnew+electronlossnew+lightlossnew+renheatlossnew, 'type': 'A', 'color': 'gainsboro'},#
        {'source': GenerationLossnew, 'target': Lossnew, 'value': elossnew, 'type': 'Z', 'color': 'gainsboro'},
        {'source': FuelLossnew, 'target': Lossnew, 'value': np.sum(ind_lossesnew), 'type': 'Z', 'color': 'gainsboro'},

        #energy used
        {'source': Heateff, 'target': UsefulEnergy, 'value': oilburnused+gasburnused+coalburnused+biomassburnused+elecheatused+heatexused+renheatused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Motioneff, 'target': UsefulEnergy, 'value': engused+elecmotorused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Othereff, 'target': UsefulEnergy, 'value': electronused+lightused, 'type': 'K', 'color': 'whitesmoke'}

    ]

    #groups for showing total primary energy supply and labelling conversion devices
    groups_changed = [
        {'id': 'G', 'title': 'TPE ({:.0f}PJ)'.format(PrimEngnew), 'nodes': ['Oil', 'Coal', 'Gas', 'Biomass', 'Nuclear', 'Renewables']},
        {'id': 'G', 'title': 'Conversion Devices ({:.0f}PJ)'.format(ConvDevnew), 'nodes': ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Lighting Device']},
    ]

    #set order in which nodes appear
    order_changed = [
        [['Oil', 'Biomass', 'Gas', 'Coal', 'Nuclear', 'Renewables']],
        [DFUnew, TEGnew, FuelLossnew],
        ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Electronic', 'Lighting Device', GenerationLossnew],
        [[Heateff, Motioneff, Othereff, ConversionLossnew]],
        [UsefulEnergy, Lossnew]

    ]
    neweff=useful/PrimEngnew
    print('The Total Efficiency of the', Sector, ' sector in', Country,  'is {:.0f}%'.format(neweff*100))
    print('The Energy Savings are {:.1f} PJ'.format((PrimEng-PrimEngnew)))
    eff=useful/PrimEng #initial efficiency
    print('The Efficiency Improvements are {:.3f}%'.format((neweff-eff)*100))
    return sankey(links=links_changed, groups=groups_changed, linkLabelFormat='.0f', linkLabelMinWidth=10, order=order_changed, align_link_types=True).auto_save_png(Country+Sector+'_Efficiency_Sankey_'+Year+Device+'Efficiency'+Value+'.png')

    '''
    Function to return a Sankey Diagram with altered
    engineering device efficiency for a given sector
    
    Inputs: 
        IEATES - Energy Supply Values from IEA
        IEATFC - Energy Consumption Values from IEA
        electricity - Electricity Consumption values from IEA
        heat - Heat Consumption values from IEA
        Country - name of country from IEA list
        Year - year between 1960 and 2019
        Exergy - Produce Diagram in Exergy or Energy Values
        Sector - Sector for which the diagram will be produced
        Device - name of engineering device for which
                the efficiency is to be altered
        Value - new value of engineering device efficiency
        
    Returns a Sankey diagram for the given year, country
    and sector with the new device efficiency taken into
    account (and prints the new overall efficiency, the 
    change in overall efficiency and the change in primary
    energy demand)
    
    '''
    #convert supply to exergy values and combine oil and renewable products (exergy factors from https://doi.org/10.3390/en9090707)
    if Exergy=='Exergy':                          
        exergy=np.array([1.04*IEATES[0],1.03*IEATES[1],0.95*IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],1.13*IEATES[6],1.06*IEATES[7]])
        exergy_h=0.17*heat
    elif Exergy=='Energy':
        exergy=np.array([IEATES[0],IEATES[1],IEATES[2],IEATES[3]+IEATES[4]+IEATES[5],IEATES[6],IEATES[7]])
        exergy_h=heat                          

    #calculate total electricity generation and direct fuel use
    tpes=np.zeros(len(exergy))
    losses=np.zeros(len(exergy))
    tfc=np.zeros(len(exergy))
    nonenergy=np.zeros(len(exergy))
    egeneration=np.zeros(len(exergy))
    hgeneration=np.zeros(len(exergy))
    for i in range (0,len(exergy)):
        tpes[i]=exergy[i][0]
        #combine all losses
        for j in range(1,3):
            losses[i]=losses[i]+exergy[i][j] 
        for j in range(9,23):
            losses[i]=losses[i]+exergy[i][j]
        tfc[i]=exergy[i][23]
        nonenergy[i]=exergy[i][24]
        #combine electriciy and heat generation from electricity, heating and CHP plants
        for j in range(3,5):
            egeneration[i]=egeneration[i]+exergy[i][j]
        for j in range(5,7):
            egeneration[i]=egeneration[i]+0.89*exergy[i][j]
            hgeneration[i]=hgeneration[i]+0.11*exergy[i][j]
        for j in range(7,9):
            hgeneration[i]=hgeneration[i]+exergy[i][j]

    dfu_used=tfc-nonenergy #total fuel used directly is total final consumption of fuel - non-energy use
    elec_used=-egeneration-hgeneration #total fuel used for electricity generation is combination of fuels to all plants from above (- sign to yield +ve values)

    #losses split proportionally between dfu & electricity generation
    dfu_losses=np.zeros(len(tpes))
    elec_losses=np.zeros(len(tpes))
    for i in range(len(tpes)):
        if tpes[i]+losses[i]==0: #to avoid divide zero errors
            dfu_losses[i]=0
            elec_losses[i]=0
        else: #- signs as losses[i] have -ve values
            dfu_losses[i]=-dfu_used[i]*(losses[i]/(tpes[i]+losses[i])) 
            elec_losses[i]=-elec_used[i]*(losses[i]/(tpes[i]+losses[i]))
    #convert from TJ to PJ
    direct_fuel_use=(dfu_used+dfu_losses)/(10**3)
    electricity_generation=(elec_used+elec_losses)/(10**3)

    #convert consumption to exergy values and combine oil and renewable products
    exergycons=np.array([1.04*IEATFC[0],1.03*IEATFC[1],0.95*IEATFC[2],IEATFC[3]+IEATFC[4]+IEATFC[5],1.11*IEATFC[6],1.06*IEATFC[7]])


    #calculate total electricity (& heat) 
    totelec=electricity[0]+electricity[15]+electricity[24]+electricity[25]+electricity[26]+electricity[27]+electricity[28]
    totheat=exergy_h[0]+exergy_h[15]+exergy_h[24]+exergy_h[25]+exergy_h[26]+exergy_h[27]+exergy_h[28]

    if (totelec+totheat)!=0: #to avoid divide zero errors
        totelec_=totelec/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
        totheat_=totheat/(totelec+totheat)*np.sum(electricity_generation) #scale to include losses in allocation
    else:
        totelec_=0
        totheat_=0

    #calculate direct fuel use energy to steel
    steel=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        steel[i]=exergycons[i][4]
    steel=steel/(10**3)

    #calculate direct fuel use energy to aluminium
    aluminium=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        aluminium[i]=exergycons[i][6]
    aluminium=aluminium/(10**3)

    #calculate direct fuel use energy to machinery
    machinery=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        machinery[i]=exergycons[i][8]+exergycons[i][9]
    machinery=machinery/(10**3)

    #calculate direct fuel use energy to mineral
    mineral=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        mineral[i]=exergycons[i][7]
    mineral=mineral/(10**3)

    #calculate direct fuel use energy to chemical
    chemical=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        chemical[i]=exergycons[i][5]
    chemical=chemical/(10**3)

    #calculate direct fuel use energy to paper
    paper=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        paper[i]=exergycons[i][11]+exergycons[i][12]
    paper=paper/(10**3)

    #calculate direct fuel use energy to food
    food=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        food[i]=exergycons[i][10]
    food=food/(10**3)

    #calculate direct fuel use energy to other
    other=np.zeros(len(exergycons))
    for i in range (0,len(exergycons)):
        other[i]=exergycons[i][1]+exergycons[i][2]+exergycons[i][13]+exergycons[i][14]
    other=other/(10**3)

    #scale to include losses
    for i in range(len(dfu_used)):
        if dfu_used[i]!=0:
            steel[i]=steel[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            aluminium[i]=aluminium[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            machinery[i]=machinery[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            mineral[i]=mineral[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            chemical[i]=chemical[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            paper[i]=paper[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            food[i]=food[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))
            other[i]=other[i]*direct_fuel_use[i]/(dfu_used[i]/(10**3))

    #scale electricity (& heat) flow to each subsector
    if totelec!=0:
        elec_steel=(electricity[4]/totelec)*totelec_
        elec_aluminium=(electricity[6]/totelec)*totelec_
        elec_machinery=((electricity[8]+electricity[9])/totelec)*totelec_
        elec_mineral=(electricity[7]/totelec)*totelec_
        elec_chemical=(electricity[5]/totelec)*totelec_
        elec_paper=((electricity[11]+electricity[12])/totelec)*totelec_
        elec_food=(electricity[10]/totelec)*totelec_
        elec_other=((electricity[1]+electricity[2]+electricity[13]+electricity[14])/totelec)*totelec_
    else:
        elec_steel=0
        elec_steel=0
        elec_aluminium=0
        elec_machinery=0
        elec_mineral=0
        elec_chemical=0
        elec_paper=0
        elec_food=0
        elec_other=0

    if totheat!=0:
        heat_steel=(exergy_h[4]/totheat)*totheat_
        heat_aluminium=(exergy_h[6]/totheat)*totheat_
        heat_machinery=((exergy_h[8]+exergy_h[9])/totheat)*totheat_
        heat_mineral=(exergy_h[7]/totheat)*totheat_
        heat_chemical=(exergy_h[5]/totheat)*totheat_
        heat_paper=((exergy_h[11]+exergy_h[12])/totheat)*totheat_
        heat_food=(exergy_h[10]/totheat)*totheat_
        heat_other=((exergy_h[1]+exergy_h[2]+exergy_h[13]+exergy_h[14])/totheat)*totheat_
    else:
        heat_steel=0
        heat_steel=0
        heat_aluminium=0
        heat_machinery=0
        heat_mineral=0
        heat_chemical=0
        heat_paper=0
        heat_food=0
        heat_other=0

    #calculate energy to electricity from each fuel for steel
    totelecsteel=np.zeros(len(exergycons))
    totheatsteel=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecsteel[i]=(elec_steel/np.sum(electricity_generation))*electricity_generation[i]
            totheatsteel[i]=(heat_steel/np.sum(electricity_generation))*electricity_generation[i]

    #caluminiumculate energy to electricity from each fuel for aluminium
    totelecaluminium=np.zeros(len(exergycons))
    totheataluminium=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecaluminium[i]=(elec_aluminium/np.sum(electricity_generation))*electricity_generation[i]
            totheataluminium[i]=(heat_aluminium/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for machinery
    totelecmachinery=np.zeros(len(exergycons))
    totheatmachinery=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecmachinery[i]=(elec_machinery/np.sum(electricity_generation))*electricity_generation[i]
            totheatmachinery[i]=(heat_machinery/np.sum(electricity_generation))*electricity_generation[i]

            #calculate energy to electricity from each fuel for mineral
    totelecmineral=np.zeros(len(exergycons))
    totheatmineral=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecmineral[i]=(elec_mineral/np.sum(electricity_generation))*electricity_generation[i]
            totheatmineral[i]=(heat_mineral/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for chemical
    totelecchemical=np.zeros(len(exergycons))
    totheatchemical=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecchemical[i]=(elec_chemical/np.sum(electricity_generation))*electricity_generation[i]
            totheatchemical[i]=(heat_chemical/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for paper
    totelecpaper=np.zeros(len(exergycons))
    totheatpaper=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecpaper[i]=(elec_paper/np.sum(electricity_generation))*electricity_generation[i]
            totheatpaper[i]=(heat_paper/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for food
    totelecfood=np.zeros(len(exergycons))
    totheatfood=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecfood[i]=(elec_food/np.sum(electricity_generation))*electricity_generation[i]
            totheatfood[i]=(heat_food/np.sum(electricity_generation))*electricity_generation[i]

    #calculate energy to electricity from each fuel for other
    totelecother=np.zeros(len(exergycons))
    totheatother=np.zeros(len(exergycons))
    if np.sum(electricity_generation)!=0: #to avoid divide zero errors
        for i in range(len(exergycons)):
            totelecother[i]=(elec_other/np.sum(electricity_generation))*electricity_generation[i]
            totheatother[i]=(heat_other/np.sum(electricity_generation))*electricity_generation[i]



    #append electricity and heat values to sub-sector fuel consumption arrays
    steelfull=np.append(steel, [elec_steel, heat_steel])
    aluminiumfull=np.append(aluminium, [elec_aluminium, heat_aluminium])
    machineryfull=np.append(machinery, [elec_machinery, heat_machinery])
    mineralfull=np.append(mineral, [elec_mineral, heat_mineral])
    chemicalfull=np.append(chemical, [elec_chemical, heat_chemical])
    paperfull=np.append(paper, [elec_paper, heat_paper])
    foodfull=np.append(food, [elec_food, heat_food])
    otherfull=np.append(other, [elec_other, heat_other])

    #define allocation matrices, based on US steel data - used to assign fuels to passive systems below
    #rows are passive systems, columns are fuels (oil, gas, nuclear, renewables, biomass, coal, electricity, heat))
    steel_mat = np.array([[0.00  , 0.10  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.39  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 1.00  , 1.00  , 0.53  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.03  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#appliance
                         [1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    al_mat = np.array([[0.00  , 0.13  , 1.00  , 0.00  , 0.13  , 0.13  , 0.01  , 0.00  ],#steam
                         [0.25  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.24  , 0.00  ],#driven
                         [0.25  , 0.76  , 0.00  , 0.00  , 0.76  , 0.76  , 0.65  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.03  , 0.00  ],#light
                         [0.00  , 0.09  , 0.00  , 1.00  , 0.09  , 0.09  , 0.04  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.01  , 0.01  , 0.02  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                      ])

    mach_mat = np.array([[0.15  , 0.16  , 1.00  , 0.00  , 0.16  , 0.16  , 0.01  , 0.00  ],#steam
                         [0.14  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.49  , 0.00  ],#driven
                         [0.07  , 0.45  , 0.00  , 0.00  , 0.45  , 0.45  , 0.16  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.11  , 0.00  ],#light
                         [0.14  , 0.35  , 0.00  , 1.00  , 0.35  , 0.35  , 0.19  , 1.00  ],#spaceheat
                         [0.00  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.03  , 0.00  ],#appliance
                         [0.50  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])

    min_mat = np.array([[0.00  , 0.03  , 1.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#steam
                         [0.38  , 0.08  , 0.00  , 0.00  , 0.10  , 0.10  , 0.60  , 0.00  ],#driven
                         [0.00  , 0.83  , 0.00  , 0.00  , 0.90  , 0.90  , 0.28  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.62  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                       ])

    chem_mat = np.array([[0.50  , 0.52  , 1.00  , 0.00  , 0.87  , 0.87  , 0.01  , 0.00  ],#steam
                         [0.00  , 0.04  , 0.00  , 0.00  , 0.00  , 0.00  , 0.63  , 0.00  ],#driven
                         [0.10  , 0.41  , 0.00  , 0.00  , 0.13  , 0.13  , 0.25  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.04  , 0.00  ],#light
                         [0.00  , 0.02  , 0.00  , 1.00  , 0.00  , 0.00  , 0.05  , 1.00  ],#spaceheat
                         [0.00  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.40  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                        ])                 

    paper_mat = np.array([[0.36  , 0.63  , 1.00  , 0.00  , 0.98  , 0.98  , 0.04  , 0.00  ],#steam
                         [0.04  , 0.02  , 0.00  , 0.00  , 0.02  , 0.02  , 0.78  , 0.00  ],#driven
                         [0.08  , 0.30  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.05  , 0.00  ],#light
                         [0.00  , 0.05  , 0.00  , 1.00  , 0.00  , 0.00  , 0.06  , 1.00  ],#spaceheat
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.52  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    food_mat = np.array([[0.59  , 0.59  , 1.00  , 0.00  , 0.79  , 0.79  , 0.03  , 0.00  ],#steam
                         [0.00  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.69  , 0.00  ],#driven
                         [0.00  , 0.27  , 0.00  , 0.00  , 0.21  , 0.21  , 0.05  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#light
                         [0.08  , 0.08  , 0.00  , 1.00  , 0.00  , 0.00  , 0.11  , 1.00  ],#spaceheat
                         [0.08  , 0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.25  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.01  , 0.00  ],#vehicle
                        ])

    other_mat = np.array([[0.13  , 0.34  , 1.00  , 0.00  , 1.00  , 1.00  , 0.01  , 0.00  ],#steam
                         [0.13  , 0.01  , 0.00  , 0.00  , 0.00  , 0.00  , 0.73  , 0.00  ],#driven
                         [0.71  , 0.61  , 0.00  , 0.00  , 0.00  , 0.00  , 0.09  , 0.00  ],#furnace
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.06  , 0.00  ],#light
                         [0.00  , 0.04  , 0.00  , 1.00  , 0.00  , 0.00  , 0.09  , 1.00  ],#spaceheat
                         [0.03  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.02  , 0.00  ],#appliance
                         [0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  , 0.00  ],#vehicle
                         ])

    #import data on share of steel from EAF
    import pandas as pd
    df=pd.read_csv('SteelShares2023.csv')
    try:
        EAF=float(df['EAF'][df['Country'] == Country].values[0])
    except:
        EAF=float(df['EAF'][df['Country'] == 'World'].values[0])

    #calculate new allocation matrices for steel, based on share of EAF
    x=(442.01*EAF)/((442.01*EAF)+(4128.05*(1-EAF)))
    z1=0.943*x+0.045*(1-x)
    z2=0.928*(1-x)
    z3=0.057*x+0.027*(1-x)
    gamma=0

    if x==1:
        if electricity[4]!=0:
            gammaprime=(0.02*IEATFC[1][4]/electricity[4])*(z1/z3)
            steel_mat[2][6]=0.4+0.6*gammaprime
            steel_mat[1][6]=0.5*(1-gammaprime)
            steel_mat[3][6]=0.04*(1-gammaprime)
            steel_mat[4][6]=0.05*(1-gammaprime)
            steel_mat[5][6]=0.01*(1-gammaprime)
    else:
        if electricity[4]!=0:
            gamma=(IEATFC[7][4]/electricity[4])*(z1/z2)
            steel_mat[2][6]=0.4+0.6*gamma
            steel_mat[1][6]=0.5*(1-gamma)
            steel_mat[3][6]=0.04*(1-gamma)
            steel_mat[4][6]=0.05*(1-gamma)
            steel_mat[5][6]=0.01*(1-gamma)
        if IEATFC[1][4]!=0:
            delta=(IEATFC[7][4]/IEATFC[1][4])*(z3/z2)
            steel_mat[2][1]=0.83+0.17*delta
            steel_mat[0][1]=0.1*(1-delta)
            steel_mat[1][1]=0.01*(1-delta)
            steel_mat[4][1]=0.05*(1-delta)
            steel_mat[5][1]=0.01*(1-delta)

    #use matrix multiplication to assign fuel to each passive system
    steel_ps=np.zeros(7)
    al_ps=np.zeros(7)
    mach_ps=np.zeros(7)
    min_ps=np.zeros(7)
    chem_ps=np.zeros(7)
    paper_ps=np.zeros(7)
    food_ps=np.zeros(7)
    other_ps=np.zeros(7)
    for i in range(0,len(steelfull)):
        for j in range(0,7):
            steel_ps[j]=steel_ps[j]+steelfull[i]*steel_mat[j][i]
            al_ps[j]=al_ps[j]+aluminiumfull[i]*al_mat[j][i]
            mach_ps[j]=mach_ps[j]+machineryfull[i]*mach_mat[j][i]
            min_ps[j]=min_ps[j]+mineralfull[i]*min_mat[j][i]
            chem_ps[j]=chem_ps[j]+chemicalfull[i]*chem_mat[j][i]
            paper_ps[j]=paper_ps[j]+paperfull[i]*paper_mat[j][i]
            food_ps[j]=food_ps[j]+foodfull[i]*food_mat[j][i]
            other_ps[j]=other_ps[j]+otherfull[i]*other_mat[j][i]

    #define matrices for assigning fuels to conversion devices
    #rows are purposes of converson devices, columns are industries (steel, aluminium, machinery, mineral, chemical, paper, food, other)
    oil_mat = np.array([[1.00, 0.75, 0.64, 1.00, 0.40, 0.56, 0.25, 0.13],#motion
                       [0.00, 0.25, 0.36, 0.00, 0.60, 0.44, 0.67, 0.84],#heat
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.08, 0.03]])#appliance

    gas_mat = np.array([[steel_mat[1][1]+steel_mat[6][1], 0.01, 0.02, 0.08, 0.04, 0.02, 0.03, 0.01],#motion
                       [steel_mat[0][1]+steel_mat[2][1]+steel_mat[4][1], 0.98, 0.96, 0.91, 0.95, 0.98, 0.94, 0.99],#heat
                       [steel_mat[3][1], 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                       [steel_mat[5][1], 0.01, 0.02, 0.01, 0.01, 0.00, 0.03, 0.00]])#appliance

    coal_mat = np.array([[0.00, 0.01, 0.02, 0.10, 0.00, 0.02, 0.00, 0.00],#motion
                        [1.00, 0.98, 0.96, 0.90, 1.00, 0.98, 1.00, 1.00],#heat
                        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],#light
                        [0.00, 0.01, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00]])#appliance

    elec_mat = np.array([[steel_mat[1][6]+steel_mat[6][6], 0.25, 0.50, 0.60, 0.63, 0.78, 0.70, 0.73],#motion
                        [steel_mat[0][6]+steel_mat[2][6]+steel_mat[4][6], 0.70, 0.36, 0.33, 0.31, 0.15, 0.19, 0.19],#heat
                        [steel_mat[3][6], 0.03, 0.11, 0.05, 0.04, 0.05, 0.09, 0.06],#light
                        [steel_mat[5][6], 0.02, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02]])#appliance

    #create new matrices with all passive systems
    oil_mat2=np.zeros((7,8))
    for i in range(7):
        oil_mat2[i][0]=steel_mat[i][0]
        oil_mat2[i][1]=al_mat[i][0]
        oil_mat2[i][2]=mach_mat[i][0]
        oil_mat2[i][3]=min_mat[i][0]
        oil_mat2[i][4]=chem_mat[i][0]
        oil_mat2[i][5]=paper_mat[i][0]
        oil_mat2[i][6]=food_mat[i][0]
        oil_mat2[i][7]=other_mat[i][0]

    gas_mat2=np.zeros((7,8))
    for i in range(7):
        gas_mat2[i][0]=steel_mat[i][1]
        gas_mat2[i][1]=al_mat[i][1]
        gas_mat2[i][2]=mach_mat[i][1]
        gas_mat2[i][3]=min_mat[i][1]
        gas_mat2[i][4]=chem_mat[i][1]
        gas_mat2[i][5]=paper_mat[i][1]
        gas_mat2[i][6]=food_mat[i][1]
        gas_mat2[i][7]=other_mat[i][1]

    coal_mat2=np.zeros((7,8))
    for i in range(7):
        coal_mat2[i][0]=steel_mat[i][4]
        coal_mat2[i][1]=al_mat[i][4]
        coal_mat2[i][2]=mach_mat[i][4]
        coal_mat2[i][3]=min_mat[i][4]
        coal_mat2[i][4]=chem_mat[i][4]
        coal_mat2[i][5]=paper_mat[i][4]
        coal_mat2[i][6]=food_mat[i][4]
        coal_mat2[i][7]=other_mat[i][4]

    elec_mat2=np.zeros((7,8))#
    for i in range(7):
        elec_mat2[i][0]=steel_mat[i][6]
        elec_mat2[i][1]=al_mat[i][6]
        elec_mat2[i][2]=mach_mat[i][6]
        elec_mat2[i][3]=min_mat[i][6]
        elec_mat2[i][4]=chem_mat[i][6]
        elec_mat2[i][5]=paper_mat[i][6]
        elec_mat2[i][6]=food_mat[i][6]
        elec_mat2[i][7]=other_mat[i][6]

    if Sector=='Steel':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][0]*steelfull[0]
            gas_cd[i]=gas_mat[i][0]*steelfull[1]
            biomass_cd[i]=coal_mat[i][0]*steelfull[4]
            coal_cd[i]=coal_mat[i][0]*steelfull[5]
            elec_cd[i]=elec_mat[i][0]*steelfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=steelfull[7]

        #values for Sankey labels
        PrimEng=np.sum(steel)+np.sum(totelecsteel)+np.sum(totheatsteel)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(steel))
        inddfu_losses=np.zeros(len(steel))
        indelec_used=np.zeros(len(steel))
        indelec_losses=np.zeros(len(steel))
        for i in range(len(steel)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=steel[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=steel[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecsteel[i]+totheatsteel[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecsteel[i]+totheatsteel[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][0]*steelfull[0]
            gas_cd2[i]=gas_mat2[i][0]*steelfull[1]
            biomass_cd2[i]=coal_mat2[i][0]*steelfull[4]
            coal_cd2[i]=coal_mat2[i][0]*steelfull[5]
            elec_cd2[i]=elec_mat2[i][0]*steelfull[6]

    if Sector=='Aluminium':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][1]*aluminiumfull[0]
            gas_cd[i]=gas_mat[i][1]*aluminiumfull[1]
            biomass_cd[i]=coal_mat[i][1]*aluminiumfull[4]
            coal_cd[i]=coal_mat[i][1]*aluminiumfull[5]
            elec_cd[i]=elec_mat[i][1]*aluminiumfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=aluminiumfull[7]

        #values for Sankey labels
        PrimEng=np.sum(aluminium)+np.sum(totelecaluminium)+np.sum(totheataluminium)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(aluminium))
        inddfu_losses=np.zeros(len(aluminium))
        indelec_used=np.zeros(len(aluminium))
        indelec_losses=np.zeros(len(aluminium))
        for i in range(len(aluminium)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=aluminium[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=aluminium[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecaluminium[i]+totheataluminium[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecaluminium[i]+totheataluminium[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][1]*aluminiumfull[0]
            gas_cd2[i]=gas_mat2[i][1]*aluminiumfull[1]
            biomass_cd2[i]=coal_mat2[i][1]*aluminiumfull[4]
            coal_cd2[i]=coal_mat2[i][1]*aluminiumfull[5]
            elec_cd2[i]=elec_mat2[i][1]*aluminiumfull[6]

    if Sector=='Machinery':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][2]*machineryfull[0]
            gas_cd[i]=gas_mat[i][2]*machineryfull[1]
            biomass_cd[i]=coal_mat[i][2]*machineryfull[4]
            coal_cd[i]=coal_mat[i][2]*machineryfull[5]
            elec_cd[i]=elec_mat[i][2]*machineryfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=machineryfull[7]

        #values for Sankey labels
        PrimEng=np.sum(machinery)+np.sum(totelecmachinery)+np.sum(totheatmachinery)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(machinery))
        inddfu_losses=np.zeros(len(machinery))
        indelec_used=np.zeros(len(machinery))
        indelec_losses=np.zeros(len(machinery))
        for i in range(len(machinery)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=machinery[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=machinery[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecmachinery[i]+totheatmachinery[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecmachinery[i]+totheatmachinery[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][2]*machineryfull[0]
            gas_cd2[i]=gas_mat2[i][2]*machineryfull[1]
            biomass_cd2[i]=coal_mat2[i][2]*machineryfull[4]
            coal_cd2[i]=coal_mat2[i][2]*machineryfull[5]
            elec_cd2[i]=elec_mat2[i][2]*machineryfull[6]

    if Sector=='Mineral':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][3]*mineralfull[0]
            gas_cd[i]=gas_mat[i][3]*mineralfull[1]
            biomass_cd[i]=coal_mat[i][3]*mineralfull[4]
            coal_cd[i]=coal_mat[i][3]*mineralfull[5]
            elec_cd[i]=elec_mat[i][3]*mineralfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=mineralfull[7]

        #values for Sankey labels
        PrimEng=np.sum(mineral)+np.sum(totelecmineral)+np.sum(totheatmineral)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(mineral))
        inddfu_losses=np.zeros(len(mineral))
        indelec_used=np.zeros(len(mineral))
        indelec_losses=np.zeros(len(mineral))
        for i in range(len(mineral)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=mineral[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=mineral[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecmineral[i]+totheatmineral[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecmineral[i]+totheatmineral[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][3]*mineralfull[0]
            gas_cd2[i]=gas_mat2[i][3]*mineralfull[1]
            biomass_cd2[i]=coal_mat2[i][3]*mineralfull[4]
            coal_cd2[i]=coal_mat2[i][3]*mineralfull[5]
            elec_cd2[i]=elec_mat2[i][3]*mineralfull[6]

    if Sector=='Chemical':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][4]*chemicalfull[0]
            gas_cd[i]=gas_mat[i][4]*chemicalfull[1]
            biomass_cd[i]=coal_mat[i][4]*chemicalfull[4]
            coal_cd[i]=coal_mat[i][4]*chemicalfull[5]
            elec_cd[i]=elec_mat[i][4]*chemicalfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=chemicalfull[7]

        #values for Sankey labels
        PrimEng=np.sum(chemical)+np.sum(totelecchemical)+np.sum(totheatchemical)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(chemical))
        inddfu_losses=np.zeros(len(chemical))
        indelec_used=np.zeros(len(chemical))
        indelec_losses=np.zeros(len(chemical))
        for i in range(len(chemical)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=chemical[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=chemical[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecchemical[i]+totheatchemical[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecchemical[i]+totheatchemical[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][4]*chemicalfull[0]
            gas_cd2[i]=gas_mat2[i][4]*chemicalfull[1]
            biomass_cd2[i]=coal_mat2[i][4]*chemicalfull[4]
            coal_cd2[i]=coal_mat2[i][4]*chemicalfull[5]
            elec_cd2[i]=elec_mat2[i][4]*chemicalfull[6]

    if Sector=='Paper':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][5]*paperfull[0]
            gas_cd[i]=gas_mat[i][5]*paperfull[1]
            biomass_cd[i]=coal_mat[i][5]*paperfull[4]
            coal_cd[i]=coal_mat[i][5]*paperfull[5]
            elec_cd[i]=elec_mat[i][5]*paperfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=paperfull[7]

        #values for Sankey labels
        PrimEng=np.sum(paper)+np.sum(totelecpaper)+np.sum(totheatpaper)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(paper))
        inddfu_losses=np.zeros(len(paper))
        indelec_used=np.zeros(len(paper))
        indelec_losses=np.zeros(len(paper))
        for i in range(len(paper)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=paper[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=paper[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecpaper[i]+totheatpaper[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecpaper[i]+totheatpaper[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][5]*paperfull[0]
            gas_cd2[i]=gas_mat2[i][5]*paperfull[1]
            biomass_cd2[i]=coal_mat2[i][5]*paperfull[4]
            coal_cd2[i]=coal_mat2[i][5]*paperfull[5]
            elec_cd2[i]=elec_mat2[i][5]*paperfull[6]

    if Sector=='Food':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][6]*foodfull[0]
            gas_cd[i]=gas_mat[i][6]*foodfull[1]
            biomass_cd[i]=coal_mat[i][6]*foodfull[4]
            coal_cd[i]=coal_mat[i][6]*foodfull[5]
            elec_cd[i]=elec_mat[i][6]*foodfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=foodfull[7]

        #values for Sankey labels
        PrimEng=np.sum(food)+np.sum(totelecfood)+np.sum(totheatfood)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(food))
        inddfu_losses=np.zeros(len(food))
        indelec_used=np.zeros(len(food))
        indelec_losses=np.zeros(len(food))
        for i in range(len(food)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=food[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=food[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecfood[i]+totheatfood[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecfood[i]+totheatfood[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][6]*foodfull[0]
            gas_cd2[i]=gas_mat2[i][6]*foodfull[1]
            biomass_cd2[i]=coal_mat2[i][6]*foodfull[4]
            coal_cd2[i]=coal_mat2[i][6]*foodfull[5]
            elec_cd2[i]=elec_mat2[i][6]*foodfull[6]

    if Sector=='Other':
        #use matrix multiplication to assign energy to each conversion device
        oil_cd=np.zeros(4)
        gas_cd=np.zeros(4)
        biomass_cd=np.zeros(4)
        coal_cd=np.zeros(4)
        elec_cd=np.zeros(4)
        for i in range(0,4):
            oil_cd[i]=oil_mat[i][7]*otherfull[0]
            gas_cd[i]=gas_mat[i][7]*otherfull[1]
            biomass_cd[i]=coal_mat[i][7]*otherfull[4]
            coal_cd[i]=coal_mat[i][7]*otherfull[5]
            elec_cd[i]=elec_mat[i][7]*otherfull[6]

        #assumed that all nuclear, renewable and direct heat contributes to heat
        heat_cd=otherfull[7]

        #values for Sankey labels
        PrimEng=np.sum(other)+np.sum(totelecother)+np.sum(totheatother)

        #calculate losses in fuel transformation
        ind_used=np.zeros(len(other))
        inddfu_losses=np.zeros(len(other))
        indelec_used=np.zeros(len(other))
        indelec_losses=np.zeros(len(other))
        for i in range(len(other)):
            if direct_fuel_use[i]!=0: #to avoid divide zero errors
                ind_used[i]=other[i]*dfu_used[i]/(direct_fuel_use[i]*1000)
                inddfu_losses[i]=other[i]*dfu_losses[i]/(direct_fuel_use[i]*1000)
            if electricity_generation[i]!=0: #to avoid divide zero errors
                indelec_used[i]=(totelecother[i]+totheatother[i])*elec_used[i]/(electricity_generation[i]*1000)
                indelec_losses[i]=(totelecother[i]+totheatother[i])*elec_losses[i]/(electricity_generation[i]*1000)
            ind_losses=indelec_losses+inddfu_losses

        #calculate energy to each conversion device
        if np.sum(oil_cd)!=0: #to avoid divide zero errors
            oilburner=((oil_cd[1]+oil_cd[3])/np.sum(oil_cd))*ind_used[0] #energy to oil burner is oil used for heat and appliances (burners for heating etc.)
            oilengine=((oil_cd[0])/np.sum(oil_cd))*ind_used[0] #energy to oil engine is oil used for motion
        else:
            oilburner=0
            oilengine=0

        if np.sum(gas_cd)!=0: #to avoid divide zero errors
            gasburner=((gas_cd[1]+gas_cd[3])/np.sum(gas_cd))*ind_used[1] #energy to gas burner is gas used for heat and appliances (burners for heating etc.)
            gasengine=((gas_cd[0])/np.sum(gas_cd))*ind_used[1] #energy to gas engine is gas used for motion
        else:
            gasburner=0
            gasengine=0

        nuclearheater=ind_used[2] #in case nuclear is used directly
        renheater=ind_used[3] #direct use of renewables only for solar/geothermal heating

        if np.sum(biomass_cd)!=0: #to avoid divide zero errors
            biomassburner=((biomass_cd[1]+biomass_cd[3])/np.sum(biomass_cd))*ind_used[4] #energy to biomass burner is biomass used for heat and appliances (burners for heating etc.)
            biomassengine=((biomass_cd[0])/np.sum(biomass_cd))*ind_used[4] #energy to biomass engine is biomass used for motion
        else:
            biomassburner=0
            biomassengine=0

        if np.sum(coal_cd)!=0: #to avoid divide zero errors
            coalburner=((coal_cd[1]+coal_cd[3])/np.sum(coal_cd))*ind_used[5] #energy to coal burner is coal used for heat and appliances (burners for heating etc.)
            coalengine=((coal_cd[0])/np.sum(coal_cd))*ind_used[5] #energy to coal engine is coal used for motion
        else:
            coalburner=0
            coalengine=0

        #calculate losses in electricity generation
        if np.sum(egeneration)!=0: #to avoid divide zero errors
            eleceff=totelec/(-np.sum(egeneration))
        else:
            eleceff=0
        if np.sum(hgeneration)!=0:
            heateff=totheat/(-np.sum(hgeneration))
        else:
            heateff=0

        heatex=heateff*heat_cd
        elecmotor=eleceff*elec_cd[1]
        elecheater=eleceff*elec_cd[0]
        lightingdevice=eleceff*elec_cd[2]
        applianceelec=eleceff*elec_cd[3]

        #use matrix multiplication to assign energy to each conversion device
        oil_cd2=np.zeros(7)
        gas_cd2=np.zeros(7)
        biomass_cd2=np.zeros(7)
        coal_cd2=np.zeros(7)
        elec_cd2=np.zeros(7)
        for i in range(0,7):
            oil_cd2[i]=oil_mat2[i][7]*otherfull[0]
            gas_cd2[i]=gas_mat2[i][7]*otherfull[1]
            biomass_cd2[i]=coal_mat2[i][7]*otherfull[4]
            coal_cd2[i]=coal_mat2[i][7]*otherfull[5]
            elec_cd2[i]=elec_mat2[i][7]*otherfull[6]

    #calculate energy used
    if Exergy=='Exergy':
        #energy efficiency (from Paoli) x quality factor (from cullen) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average exergy efficiency
            oilburneffex=0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #exergy used
        else:
            oilburnused=0

        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average exergy efficiency
            gasburneffex=0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #exergy used
        else:
            gasburnused=0

        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average exergy efficiency
            coalburneffex=0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #exergy used
        else:
            coalburnused=0

        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average exergy efficiency
            bioburneffex=0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #exergy used
        else:
            biomassburnused=0

        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(0.95*dieselengeff*oilengine)+(0.53*turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine

        heatexeff=0.87 #heat exchanger efficiency
        heatexused=0.15*heatexeff*heatex #exergy used

        elecheateff=1 #electric heater efficiency
        elecheatused=0.3*elecheateff*elecheater #exergy used

        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=0.93*elecmotoreff*elecmotor #exergy used

        electroneff=0.85 #electronics efficiency
        electronused=0.3*electroneff*applianceelec #exergy used

        lighteff=0.13 #lighting device efficiency
        lightused=0.9*lighteff*lightingdevice #exergy used

        renheateff=1 #renewable heater efficiency
        renheatused=0.3*renheateff*renheater #exergy used

    elif Exergy=='Energy':
        #energy efficiency (from Paoli) x total energy to device (from above)
        #burners split proportionally between boilers (for space heat and steam) and burners (for furnaces)
        if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
            oilburneff=1 #burner efficiency 
            oilboileff=0.89 #boiler efficiency
            #average energy efficiency
            oilburneffex=(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]))
            oilburnused=oilburneffex*oilburner #energy used
        else:
            oilburnused=0

        if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
            gasburneff=1 #burner efficiency
            gasboileff=0.89 #boiler efficiency
            #average energy efficiency
            gasburneffex=(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]))
            gasburnused=gasburneffex*gasburner #energy used
        else:
            gasburnused=0

        if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
            coalburneff=1 #burner efficiency
            coalboileff=0.85 #boiler efficiency
            #average energy efficiency
            coalburneffex=(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]))
            coalburnused=coalburneffex*coalburner #energy used
        else:
            coalburnused=0

        if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
            bioburneff=1 #burner efficiency
            bioboileff=0.7 #boiler efficiency
            #average energy efficiency
            bioburneffex=(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]))
            biomassburnused=bioburneffex*biomassburner #energy used
        else:
            biomassburnused=0

        dieselengeff=0.39 #diesel engine efficiency
        turbeff=0.35 #gas turbine efficiency
        engused=(dieselengeff*oilengine)+(turbeff*(gasengine+coalengine+biomassengine)) #split between efficiency of diesel engine and that of gas/steam engine

        heatexeff=0.87 #heat exchanger efficiency
        heatexused=heatexeff*heatex #energy used

        elecheateff=1 #electric heater efficiency
        elecheatused=elecheateff*elecheater #energy used

        elecmotoreff=0.87 #electric motor efficiency
        elecmotorused=elecmotoreff*elecmotor #energy used

        electroneff=0.85 #electronics efficiency
        electronused=electroneff*applianceelec #energy used

        lighteff=0.13 #lighting device efficiency
        lightused=lighteff*lightingdevice #energy used

        renheateff=1 #renewable heater efficiency
        renheatused=renheateff*renheater #energy used
        
        
    Heateff='Heat ({:.0f}PJ)'.format(oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+elecheatused+heatexused+renheatused)
    Motioneff='Motion ({:.0f}PJ)'.format(engused+elecmotorused)
    Othereff='Other ({:.0f}PJ)'.format(electronused+lightused)

    ###NEW EFFICIENCY###
    #user inputs new device efficiency in %
    value=float(Value)/100
    #for given device change value for that device whilst keeping others the same
    if Exergy=='Exergy':
        if Device=='Oil Burner':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/(0.25*(oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + value*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Oil Boiler':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/(0.25*(value*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Burner':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/(0.21*(gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + value*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Boiler':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/(0.21*(value*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/(0.31*(coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + value*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/(0.31*(value*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/(0.2*(bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + value*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/(0.2*(value*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Diesel Engine':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=(engused-(0.53*turbeff*(gasengine+coalengine+biomassengine)))/(0.95*value)
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Turbine':
            turbine=(engused-(0.95*dieselengeff*oilengine))/(0.53*value)
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            if (gasengine+coalengine+biomassengine)!=0:
                gasenginenew=turbine/(gasengine+coalengine+biomassengine)*gasengine
                coalenginenew=turbine/(gasengine+coalengine+biomassengine)*coalengine
                biomassenginenew=turbine/(gasengine+coalengine+biomassengine)*biomassengine
            else:
                gasenginenew=0
                coalenginenew=0
                biomassenginenew=0
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Heat Exchanger':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatexused/(0.15*value)
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheatused/(0.3*value)
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Motor':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotorused/(0.93*value)
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electronic':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=electronused/(0.3*value)
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Lighting Device':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightused/(0.9*value)
            renheaternew=renheater
        if Device=='Renewable Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheatused/(0.3*value)
    if Exergy=='Energy':
        if Device=='Oil Burner':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/((oilboileff*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + value*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Oil Boiler':
            if (oil_cd2[0]+oil_cd2[2]+oil_cd2[4])!=0:
                oilburnernew=oilburnused/((value*(oil_cd2[0]+oil_cd2[4])/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4]) + oilburneff*oil_cd2[2]/(oil_cd2[0]+oil_cd2[2]+oil_cd2[4])))
            else:
                oilburnernew=0
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Burner':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/((gasboileff*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + value*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Boiler':
            oilburnernew=oilburner
            if (gas_cd2[0]+gas_cd2[2]+gas_cd2[4])!=0:
                gasburnernew=gasburnused/((value*(gas_cd2[0]+gas_cd2[4])/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4]) + gasburneff*gas_cd2[2]/(gas_cd2[0]+gas_cd2[2]+gas_cd2[4])))
            else:
                gasburnernew=0
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/((coalboileff*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + value*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Coal Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            if (coal_cd2[0]+coal_cd2[2]+coal_cd2[4])!=0:
                coalburnernew=coalburnused/((value*(coal_cd2[0]+coal_cd2[4])/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4]) + coalburneff*coal_cd2[2]/(coal_cd2[0]+coal_cd2[2]+coal_cd2[4])))
            else:
                coalburnernew=0
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Burner':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/((bioboileff*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + value*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Biomass Boiler':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            if (biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])!=0:
                biomassburnernew=biomassburnused/((value*(biomass_cd2[0]+biomass_cd2[4])/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4]) + bioburneff*biomass_cd2[2]/(biomass_cd2[0]+biomass_cd2[2]+biomass_cd2[4])))
            else:
                biomassburnernew=0
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Diesel Engine':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=(engused-(turbeff*(gasengine+coalengine+biomassengine)))/(value)
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Gas Turbine':
            turbine=(engused-(dieselengeff*oilengine))/(value)
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            if (gasengine+coalengine+biomassengine)!=0:
                gasenginenew=turbine/(gasengine+coalengine+biomassengine)*gasengine
                coalenginenew=turbine/(gasengine+coalengine+biomassengine)*coalengine
                biomassenginenew=turbine/(gasengine+coalengine+biomassengine)*biomassengine
            else:
                gasenginenew=0
                coalenginenew=0
                biomassenginenew=0
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Heat Exchanger':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatexused/(value)
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheatused/(value)
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electric Motor':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotorused/(value)
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Electronic':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=electronused/(value)
            lightingdevicenew=lightingdevice
            renheaternew=renheater
        if Device=='Lighting Device':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightused/(value)
            renheaternew=renheater
        if Device=='Renewable Heater':
            oilburnernew=oilburner
            gasburnernew=gasburner
            coalburnernew=coalburner
            biomassburnernew=biomassburner
            oilenginenew=oilengine
            gasenginenew=gasengine
            coalenginenew=coalengine
            biomassenginenew=biomassengine
            heatexnew=heatex
            elecheaternew=elecheater
            elecmotornew=elecmotor
            applianceelecnew=applianceelec
            lightingdevicenew=lightingdevice
            renheaternew=renheatused/(value)        

    #calculate energy lost
    oilburnlossnew=oilburnernew-oilburnused
    gasburnlossnew=gasburnernew-gasburnused
    coalburnlossnew=coalburnernew-coalburnused
    biomassburnlossnew=biomassburnernew-biomassburnused
    dieslossnew=(oilenginenew+coalenginenew+gasenginenew+biomassenginenew)-engused
    heatexlossnew=heatexnew-heatexused
    elecheatlossnew=elecheaternew-elecheatused
    elecmotorlossnew=elecmotornew-elecmotorused
    electronlossnew=applianceelecnew-electronused
    lightlossnew=lightingdevicenew-lightused
    renheatlossnew=renheaternew-renheatused
    
    #efficiencies from original Efficiency Sankey required for subsequent calculations
    fueleff=np.zeros(6)
    for i in range(6):
        if (ind_losses[i]+ind_used[i]+indelec_used[i])!=0: #to avoid divide zero errors
            fueleff[i]=(ind_used[i]+indelec_used[i])/(ind_losses[i]+ind_used[i]+indelec_used[i])
        else:
            fueleff[i]=0
    if np.sum(indelec_used)!=0:
        alleleceff=(heatex+elecmotor+elecheater+applianceelec+lightingdevice)/(np.sum(indelec_used))
    else:
        alleleceff=0
    
    
    if alleleceff!=0:
        elossnew=(1/alleleceff-1)*(elecmotornew+elecheaternew+applianceelecnew+lightingdevicenew+heatexnew) #new electricity loss, based on same electricity efficiency as previously
    else:
        elossnew=0
        
    #calculate new primary energy values, based on new final energy demand
    ind_usednew=np.zeros(6)
    indelec_usednew=np.zeros(6)  
    ind_lossesnew=np.zeros(6)  
    ind_usednew[0]=oilenginenew+oilburnernew
    ind_usednew[1]=gasenginenew+gasburnernew
    ind_usednew[2]=nuclearheater
    ind_usednew[3]=renheaternew
    ind_usednew[4]=biomassenginenew+biomassburnernew
    ind_usednew[5]=coalenginenew+coalburnernew
    for i in range(6):
        if np.sum(indelec_used)!=0:
            indelec_usednew[i]=(indelec_used[i]/np.sum(indelec_used))*(elossnew+elecmotornew+elecheaternew+applianceelecnew+lightingdevicenew+heatexnew)
        else:
            indelec_usednew[i]=0
        if fueleff[i]!=0:
            ind_lossesnew[i]=(indelec_usednew[i]+ind_usednew[i])*(1/fueleff[i]-1) #using same fuel transformation efficiency as previously
        else:
            ind_lossesnew[i]=0
            
    #values for Sankey labels
    PrimEngnew=np.sum(indelec_usednew)+np.sum(ind_lossesnew)+np.sum(ind_usednew)

    DFUnew='DFU ({:.0f}PJ)'.format(np.sum(ind_usednew))
    TEGnew='TEG ({:.0f}PJ)'.format(np.sum(indelec_usednew))
    FuelLossnew='Fuel Loss ({:.0f}PJ)'.format(np.sum(ind_lossesnew))

    ConvDevnew=oilburnernew+gasburnernew+nuclearheater+renheaternew+biomassburnernew+coalburnernew+oilenginenew+gasenginenew+biomassenginenew+coalenginenew+elecmotornew+elecheaternew+lightingdevicenew+applianceelecnew+heatexnew
    GenerationLossnew='Generation Loss ({:.0f}PJ)'.format(elossnew)

    ConversionLossnew='Conversion Loss ({:.0f}PJ)'.format(oilburnlossnew+gasburnlossnew+coalburnlossnew+biomassburnlossnew+elecheatlossnew+heatexlossnew+dieslossnew+elecmotorlossnew+electronlossnew+lightlossnew+renheatlossnew)
    useful=oilburnused+gasburnused+coalburnused+biomassburnused+nuclearheater+renheatused+elecheatused+heatexused+engused+elecmotorused+electronused+lightused
    UsefulEnergy='Useful \n Energy \n ({:.0f}PJ)'.format(useful)
    Lossnew='Loss \n ({:.0f}PJ)'.format(np.sum(ind_lossesnew)+elossnew+oilburnlossnew+gasburnlossnew+coalburnlossnew+biomassburnlossnew+elecheatlossnew+heatexlossnew+dieslossnew+elecmotorlossnew+electronlossnew+lightlossnew+renheatlossnew)
    
    #set up links for Industry Sankey
    links_changed = [
        #direct fuel use
        {'source': 'Oil', 'target': DFUnew, 'value': ind_usednew[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': DFUnew, 'value': ind_usednew[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': DFUnew, 'value': ind_usednew[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': DFUnew, 'value': ind_usednew[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': DFUnew, 'value': ind_usednew[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': DFUnew, 'value': ind_usednew[2], 'type': 'E', 'color': 'purple'},

        #fuel for electricity generation
        {'source': 'Oil', 'target': TEGnew, 'value': indelec_usednew[0], 'type': 'A', 'color': 'darkkhaki' },
        {'source': 'Coal', 'target': TEGnew, 'value': indelec_usednew[5], 'type': 'D', 'color': 'dimgrey'},
        {'source': 'Gas', 'target': TEGnew, 'value': indelec_usednew[1], 'type': 'C', 'color': 'gold'},
        {'source': 'Biomass', 'target': TEGnew, 'value': indelec_usednew[4], 'type': 'B', 'color': 'green'},
        {'source': 'Renewables', 'target': TEGnew, 'value': indelec_usednew[3], 'type': 'F', 'color': 'dodgerblue'},
        {'source': 'Nuclear', 'target': TEGnew, 'value': indelec_usednew[2], 'type': 'E', 'color': 'purple'},

        #fuel transformation losses
        {'source': 'Oil', 'target': FuelLossnew, 'value': ind_lossesnew[0], 'type': 'Z', 'color': 'gainsboro' },
        {'source': 'Coal', 'target': FuelLossnew, 'value': ind_lossesnew[5], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Gas', 'target': FuelLossnew, 'value': ind_lossesnew[1], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Biomass', 'target': FuelLossnew, 'value': ind_lossesnew[4], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Renewables', 'target': FuelLossnew, 'value': ind_lossesnew[3], 'type': 'Z', 'color': 'gainsboro'},
        {'source': 'Nuclear', 'target': FuelLossnew, 'value': ind_lossesnew[2], 'type': 'Z', 'color': 'gainsboro'},

        #direct fuel to conversion devices for heat
        {'source': DFUnew, 'target': 'Oil Burner', 'value': oilburnernew, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUnew, 'target': 'Coal Burner', 'value': coalburnernew, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUnew, 'target': 'Gas Burner', 'value': gasburnernew, 'type': 'C', 'color': 'gold'},
        {'source': DFUnew, 'target': 'Biomass Burner', 'value': biomassburnernew, 'type': 'B', 'color': 'green'},
        {'source': DFUnew, 'target': 'Renewable Heater', 'value': renheaternew, 'type': 'F', 'color': 'dodgerblue'},
        {'source': DFUnew, 'target': 'Nuclear Heater', 'value': nuclearheater, 'type': 'E', 'color': 'purple'},

        #direct fuel to conversion devices for motion
        {'source': DFUnew, 'target': 'Engine', 'value': oilenginenew, 'type': 'A', 'color': 'darkkhaki' },
        {'source': DFUnew, 'target': 'Engine', 'value': coalenginenew, 'type': 'D', 'color': 'dimgrey'},
        {'source': DFUnew, 'target': 'Engine', 'value': gasenginenew, 'type': 'C', 'color': 'gold'},
        {'source': DFUnew, 'target': 'Engine', 'value': biomassenginenew, 'type': 'B', 'color': 'green'}, 

        #electricity to conversion devices
        {'source': TEGnew, 'target': 'Electric Motor', 'value': elecmotornew, 'type': 'H', 'color': 'silver' },
        {'source': TEGnew, 'target': 'Electric Heater', 'value': elecheaternew, 'type': 'H', 'color': 'silver'},
        {'source': TEGnew, 'target': 'Lighting Device', 'value': lightingdevicenew, 'type': 'H', 'color': 'silver'},
        {'source': TEGnew, 'target': 'Electronic', 'value': applianceelecnew, 'type': 'H', 'color': 'silver'},
        {'source': TEGnew, 'target': 'Heat Exchanger', 'value': heatexnew, 'type': 'G', 'color': 'red'},

        #electricity generation losses
        {'source': TEGnew, 'target': GenerationLossnew, 'value': elossnew, 'type': 'Z', 'color': 'gainsboro'},  

        #energy to provide motion
        {'source': 'Engine', 'target': Motioneff, 'value': engused, 'type': 'I', 'color':'lightblue'},
        {'source': 'Electric Motor', 'target': Motioneff, 'value': elecmotorused, 'type': 'I', 'color':'lightblue'},

        #energy to provide heat
        {'source': 'Oil Burner', 'target': Heateff, 'value': oilburnused, 'type': 'G', 'color':'red'},
        {'source': 'Gas Burner', 'target': Heateff, 'value': gasburnused, 'type': 'G', 'color':'red'},
        {'source': 'Coal Burner', 'target': Heateff, 'value': coalburnused, 'type': 'G', 'color':'red'},
        {'source': 'Biomass Burner', 'target': Heateff, 'value': biomassburnused, 'type':'G', 'color':'red'},
        {'source': 'Renewable Heater', 'target': Heateff, 'value': renheatused, 'type': 'G', 'color': 'red'},
        {'source': 'Nuclear Heater', 'target': Heateff, 'value': nuclearheater, 'type': 'E', 'color': 'red'},
        {'source': 'Electric Heater', 'target': Heateff, 'value': elecheatused, 'type': 'G', 'color':'red'},
        {'source': 'Heat Exchanger', 'target': Heateff, 'value': heatexused, 'type': 'G', 'color':'red'},

        #energy used for other purposes
        {'source': 'Lighting Device', 'target': Othereff, 'value': lightused, 'type': 'J', 'color':'black'},
        {'source': 'Electronic', 'target': Othereff, 'value': electronused, 'type': 'J', 'color':'black'},

        #device conversion losses
        {'source': 'Engine', 'target': ConversionLossnew, 'value': dieslossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Motor', 'target': ConversionLossnew, 'value': elecmotorlossnew, 'type': 'Z', 'color':'gainsboro'},

        {'source': 'Oil Burner', 'target': ConversionLossnew, 'value': oilburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Gas Burner', 'target': ConversionLossnew, 'value': gasburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Coal Burner', 'target': ConversionLossnew, 'value': coalburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Biomass Burner', 'target': ConversionLossnew, 'value': biomassburnlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electric Heater', 'target': ConversionLossnew, 'value': elecheatlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Heat Exchanger', 'target': ConversionLossnew, 'value': heatexlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Renewable Heater', 'target': ConversionLossnew, 'value': renheatlossnew, 'type': 'Z', 'color':'gainsboro'},

        {'source': 'Lighting Device', 'target': ConversionLossnew, 'value': lightlossnew, 'type': 'Z', 'color':'gainsboro'},
        {'source': 'Electronic', 'target': ConversionLossnew, 'value': electronlossnew, 'type': 'Z', 'color':'gainsboro'},

        #energy lost
        {'source': ConversionLossnew, 'target': Lossnew, 'value': oilburnlossnew+gasburnlossnew+coalburnlossnew+biomassburnlossnew+elecheatlossnew+heatexlossnew+dieslossnew+elecmotorlossnew+electronlossnew+lightlossnew+renheatlossnew, 'type': 'A', 'color': 'gainsboro'},#
        {'source': GenerationLossnew, 'target': Lossnew, 'value': elossnew, 'type': 'Z', 'color': 'gainsboro'},
        {'source': FuelLossnew, 'target': Lossnew, 'value': np.sum(ind_lossesnew), 'type': 'Z', 'color': 'gainsboro'},

        #energy used
        {'source': Heateff, 'target': UsefulEnergy, 'value': oilburnused+gasburnused+coalburnused+biomassburnused+elecheatused+heatexused+renheatused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Motioneff, 'target': UsefulEnergy, 'value': engused+elecmotorused, 'type': 'K', 'color': 'whitesmoke'},
        {'source': Othereff, 'target': UsefulEnergy, 'value': electronused+lightused, 'type': 'K', 'color': 'whitesmoke'}

    ]

    #groups for showing total primary energy supply and labelling conversion devices
    groups_changed = [
        {'id': 'G', 'title': 'TPE ({:.0f}PJ)'.format(PrimEngnew), 'nodes': ['Oil', 'Coal', 'Gas', 'Biomass', 'Nuclear', 'Renewables']},
        {'id': 'G', 'title': 'Conversion Devices ({:.0f}PJ)'.format(ConvDevnew), 'nodes': ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Lighting Device']},
    ]

    #set order in which nodes appear
    order_changed = [
        [['Oil', 'Biomass', 'Gas', 'Coal', 'Nuclear', 'Renewables']],
        [DFUnew, TEGnew, FuelLossnew],
        ['Oil Burner','Biomass Burner', 'Gas Burner', 'Coal Burner', 'Nuclear Heater', 'Renewable Heater', 'Engine', 'Biomass Engine', 'Gas Engine', 'Coal Engine', 'Heat Exchanger', 'Electric Heater', 'Electric Motor', 'Electronic', 'Lighting Device', GenerationLossnew],
        [[Heateff, Motioneff, Othereff, ConversionLossnew]],
        [UsefulEnergy, Lossnew]

    ]
    neweff=useful/PrimEngnew
    print('The Total', Exergy, 'Efficiency of the', Sector, ' sector in', Country,  'is {:.0f}%'.format(neweff*100))
    print('The Energy Savings are {:.1f} PJ'.format((PrimEng-PrimEngnew)))
    eff=useful/PrimEng #initial efficiency
    print('The Efficiency Improvements are {:.3f}%'.format((neweff-eff)*100))
    return sankey(links=links_changed, groups=groups_changed, linkLabelFormat='.0f', linkLabelMinWidth=10, order=order_changed, align_link_types=True).auto_save_png(Country+Sector+'_Efficiency_Sankey_'+Year+Device+'Efficiency'+Value+'.png')