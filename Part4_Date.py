#Program of date temperature analyser using a dictionary that provides classes to be accesed by the GUI

#import of regular expressions and datetime module
import re
import datetime

def get_data(filename):  ##get data class
    #create temp by date, frequency by data dicationary and temp_averages dictionary
    dates_temperature = {}
    dates_frequencies = {}
    temp_averages = {}
    #create regular expression to use later
    regex = ("(\d{4}-\d{2}-\d{2})T.*Z,(\d+(?:\.\d+)?),")
    
    with open(filename, encoding="utf-8") as data_file:     #open file as data_file
        for line in data_file:                                       #for each line
            match = re.search(regex,line)                            #search using regular expression
            if match:                                                #if match is found
                date1 = datetime.date.fromisoformat(match.group(1))  #change format using datetime module of date 
                air_temperature = float(match.group(2))              #match group 2 is set as ait temp
                if date1 in dates_frequencies:                       #if date is in the dictionary
                    dates_frequencies[date1] += 1                    #add 1 to frequency
                    dates_temperature[date1] += air_temperature      #add the temp to the temp dictionary
                else:                                            #if date is found first time
                    dates_frequencies[date1] = 1                 #add it with the frequency of 1
                    dates_temperature[date1] = air_temperature   #add to temp dictionary using the value it has
    
    for date1 in dates_frequencies:   #for all dates
        temp_averages[date1] = dates_temperature[date1]/dates_frequencies[date1]    #add data to temp_average dictionary            
    return dates_temperature, dates_frequencies, temp_averages  #reutn all three dictionaries to be used
            
def analyse_temperatures(dates_temperature, dates_frequencies, temp_averages):  #analuse data class
    results_string = ""             #create empty string
    results_string +="Number of distinct dates in the file is " + str(len(dates_frequencies)) + "\n"  #add distinct dates to string
    results_string += str(min(dates_temperature)) + " is the earliest date found in the file" + "\n"    #add min temp
    results_string += str(max(dates_temperature)) + " is the most recent date found in the file" + "\n" #add max temp
    #print(dates_frequencies)       #print list of frequencies by date
    #add max frequency date
    results_string += "The maximum number of values recorded happened on " + str(max(dates_frequencies,key=dates_frequencies.get)) + "\n"
    #add min frequency date
    results_string += "The minimum number of values recorded happened on " + str(min(dates_frequencies,key=dates_frequencies.get)) + "\n"
        
    #print(temp_averages)      #print list of temp average by date
    results_string += "Lowest temp adverage was recorded on " + str(min(temp_averages,key=temp_averages.get)) + "\n"  #add highest average in a day
    results_string += "Highest temp adverage was recorded on " + str(max(temp_averages,key=temp_averages.get)) + "\n" #add lowest average in a day
    return results_string  #return the string with all of the data

def viz_temperatures(dates_temperature, dates_frequencies, temp_averages): #visualise data class
            
    #import matplotlib libraries
    import matplotlib.pyplot  as  plt
    import matplotlib.dates as  mdates
    
    # Create the figure and axes
    fig,  ax  =  plt.subplots(2,1, sharex=True, figsize=(7,7))
    
    # set a title
    fig.suptitle("Date Plots")
    # set the date label for the x-axis
    ax[1].xaxis.set_major_locator(mdates.MonthLocator())
    date_format  =  mdates.DateFormatter("%b")
    ax[1].xaxis.set_major_formatter(date_format)
    #ax[1].set_xlabel("year")
    # set a label for the y-axis
    ax[0].set_ylabel("Air Temperature")
    ax[1].set_ylabel("Temperature Frequency")
    # draw the visualisation for the 2 date plots
    ax[0].plot_date(temp_averages.keys(),  temp_averages.values(), color="red",  marker='',  linestyle="-")
    ax[1].plot_date(dates_frequencies.keys(),  dates_frequencies.values(), color="green",  marker='',  linestyle="-")

    return fig #return the graphs created
    
if __name__ == "__main__":  ##test functions code
    dates_temperature, dates_frequencies, temp_averages = get_data("Edited_data.csv")
    print(analyse_temperatures(dates_temperature, dates_frequencies, temp_averages))
    viz_temperatures(dates_temperature, dates_frequencies, temp_averages)



        
    