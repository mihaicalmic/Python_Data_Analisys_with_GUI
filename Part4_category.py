#Program of category temperature analyser using a dictionary that provides classes to be accesed by the GUI


#import of regular expressions module and matplotlib
import re
import  matplotlib.pyplot  as  plt

def get_data(filename):  #get data class
    #create temp by station and frequency by station dicationary
    station_data = {}
    station_frequencies = {}
    temp_average = {}   #create dictionary for average temp
    #create regular expression to use later
    regex = ("(.*\d),.*Z,(\d+(?:\.\d+)?),")
    
    with open(filename, encoding="utf-8") as data_file:  #Open file as data_file
        for line in data_file:                                    #for each line in the file
            match = re.search(regex,line)                         #search using above defined regular expression
            if match:                                             #if match found
                station1 = (match.group(1))                       #set capture group 1 as station
                air_temperature = float(match.group(2))           #set capture group 2 as temp
                if station1 in station_frequencies:               #if station is found in the frequency dictionary
                    station_frequencies[station1] += 1            #add 1 to frequency 
                    station_data[station1] += air_temperature     #add it temp value to temp sictionary
                else:                                        #if station is not found
                    station_frequencies[station1] = 1        #add it with the frequency of 1
                    station_data[station1] = air_temperature #add it the the temp dictionary along with its temp
    
    for category in station_data:        #for each staation in the temp dictionary
        #devide the temp by freqeuncy to find mean for that station
        temp_average[category] = station_data[category]/station_frequencies[category]
        
    return station_data, station_frequencies, temp_average  #return dictionaries to be used


def analyse_temperatures(station_data, station_frequencies, temp_average):  #analyse data class
    results_string = ""    #create empty data string
    # The variable being used as the “category” – what does it represent? 
    results_string += "The category is different weather stations." + "\n"  #add to string
    # The number of distinct values for this category 
    results_string += str(len(station_frequencies)) + " different stations collect data." + "\n"
    # The frequencies of each value in the category
    #print()
    #print(station_frequencies)
    # The category with the highest frequency
    results_string += str(max(station_frequencies,key=station_frequencies.get)) + " is the station with the highest frequency of data." + "\n"
    # The category with the lowest frequency
    results_string += str(min(station_frequencies,key=station_frequencies.get)) + " is the station with the lowest frequency of data." + "\n"
    #print()
    #print(temp_average) #print the temp average by station dictionary
    
    # print category with the highest average
    results_string += str(max(temp_average,key=temp_average.get)) + " is the station with the highest temperature mean." + "\n"
    # print category with the lowest average
    results_string += str(min(temp_average,key=temp_average.get)) + " is the station with the lowest temperature mean." + "\n"
    return results_string   #return the string that has all of the data

def viz_temperatures(station_data, station_frequencies, temp_average):  #visualise data class
    #Create the figure and axes
    fig,  ax  =  plt.subplots(1,3,figsize=(15,5))
    
    
    ###### plot 0: pie chart of data frequency by station
    
    # Set the title for frequency by stations
    ax[0].set_title("Frequency of data by station")
    # Set colours for pie charts
    colours  =  ["red",  "green",  "yellow",  "brown",  "blue",  "purple", "orange"]
    # Draw the pie chart of frequencies
    ax[0].pie(station_frequencies.values(),labels=station_frequencies.keys(),colors=colours,shadow=True,autopct="%.0f%%")
    
    ###### plot 1: pie chart of temperature mean by station
    
    # Set the title for temperature by stations
    ax[1].set_title("Temperature Average by station")
    # Draw the pie chart of frequencies
    ax[1].pie(temp_average.values(),labels=temp_average.keys(),colors=colours,shadow=True,autopct="%.1f%%")
    
    
    ###### plot 2: Box plot of temperature mean by station
    
    #name of graph
    ax[2].set_title("Temperature by station box plot")
    #name of y-axis and y-axis
    ax[2].set_ylabel("Temperature")
    # draw the box plot
    ax[2].boxplot(temp_average.values(),showmeans=True,meanline=True)
    
    return fig   #return graphs to be used
    
if __name__ == "__main__":   #test out program class
    station_data, station_frequencies, temp_average = get_data("Edited_data.csv")
    print(analyse_temperatures(station_data, station_frequencies, temp_average))
    viz_temperatures(station_data, station_frequencies, temp_average)
