#Program of two variables analyser using lists that provides classes to be accesed by the GUI

#import of regular expressions and statistics modules
import re
import statistics as st
import scipy.stats

def get_data(filename):     #get data class
    #create list for air and sea temperature values
    air_temperature = []
    sea_temperature = []
    #regular expression defined to be used later
    regex = ("Z,(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)")
    #open file as data_file
    with open(filename, encoding="utf-8") as data_file:
        for line in data_file:                                      #for each line
            match = re.search(regex,line)                           #search for the rehular expression
            if match:                                               #if found
                air_temperature.append(float(match.group(1)))       #add match 1 to the air temperature list
                sea_temperature.append(float(match.group(2)))       #add match 2 to the sea temperature list
    #return the 2 lists            
    return air_temperature, sea_temperature
    
def analyse_temperatures(air_temperature, sea_temperature):  #analuse data class
    results_string = "" #string to be returned, add any text to return at the end of the function
    results_string += "Number of values " + str(len(air_temperature)) + "\n"               #add number of values in the air temperature to string
    results_string += "Total " + str(sum(air_temperature)) + "\n"                            #add the total of the values in air temp list
    results_string += "Average: " + str(sum(air_temperature)/len(air_temperature)) + "\n"  #device total by number fo values to display
    results_string += "Maximum " + str(max(air_temperature)) + "\n"                         #add max temperaure
    results_string += "Minimum " + str(min(air_temperature)) + "\n"                         #add min temperaure
    results_string += "Range " + str(max(air_temperature)-min(air_temperature)) + "\n"      #max take away min to get range

    quartiles = st.quantiles(air_temperature) #find quantiles
    lower_q = quartiles[0] 
    results_string += "Lower Quartile " + str(lower_q) + "\n"   #add lower quartile
    upper_q = quartiles[2] 
    results_string += "Upper Quartile " + str(upper_q) + "\n"   #add upper quartile
    iq_range = upper_q - lower_q
    results_string += "Interquartile Range " + str(iq_range) + "\n"  #add quartile range
    standard_deviation = st.stdev(air_temperature)   #find deviation
    results_string += "Standard Deviation " + str(standard_deviation) + "\n"   #add deviation to the string
    correlations = scipy.stats.pearsonr(air_temperature,sea_temperature)  #find corelation using pearsonr
    results_string += "Correlation: " + str(round(correlations[0],2))     #add corelation to the string
    return results_string  #return all of the data from above

def viz_temperatures(air_temperature, sea_temperature):  #visualise data class
    
    #import matplotlib libraries
    import matplotlib.pyplot as plt
    from  matplotlib.ticker  import  MultipleLocator
    #create fig
    fig,ax = plt.subplots(2,2,figsize=(10,10))

    ###### plot 0,0: histogram of air temperatures
    ###### plot 1,0: histogram of sea temperatures

    # set the title
    ax[0,0].set_title("Air Temperature Histogram") 
    ax[1,0].set_title("Sea Temperature Histogram") 
    # set the label for the x axis
    ax[1,0].set_xlabel("Temperature ranges") 
    # set the label for the y axis
    ax[0,0].set_ylabel("Frequency of data") 
    ax[1,0].set_ylabel("Frequency of data") 
    # set the bins
    intervals = range(0,26,5)
     # set the x tick marks at the bins
    ax[0,0].set_xticks(intervals)
    # draw the histogram
    ax[0,0].hist(air_temperature,bins=intervals,ec="black",color="green")
    ax[1,0].hist(sea_temperature,bins=intervals,ec="black",color="blue") 
     

    ###### plot 0,1: box plot of the air and sea temperature

    # set the title
    ax[0,1].set_title("Temperature Boxplot") 
    # set the label for the y axis
    ax[0,1].set_ylabel("Temperature")
    ax[0,1].yaxis.set_minor_locator(MultipleLocator(5))
    # draw the box plot
    ax[0,1].boxplot([air_temperature,  sea_temperature],  showmeans=True, meanline=True,labels=["AIR","SEA"])

    ###### plot 1,1: scatter plot of the sea temperature vs air temperature

    # Set the title
    ax[1,1].set_title("Temperature Scatter Box") 
    # set the label for the x axis
    ax[1,1].set_xlabel("Sea Temperature") 
    # set the label for the y axis
    ax[1,1].set_ylabel("Air Temperature") 
    # display the scatter plot
    ax[1,1].scatter(sea_temperature,air_temperature,marker=".")
    
    return fig    #return graph

if __name__ == "__main__":   ##test out class
    air_temperature, sea_temperature = get_data("dited_data.csv")
    print(analyse_temperatures(air_temperature, sea_temperature)) 
   

