#Program of time temperature analyser using a dictionary that provides classes to be accesed by the GUI


#import of regular expressions and matplotlib
import re

def get_data(filename):  #get data class
    #create temp by date and frequency by time dicationary
    time_temperature = {}
    time_frequencies = {}
    temp_averages = {} #create dictionary of mean temperature by hour
    #create regular expression to use later
    regex = ("\d{4}-\d{2}-\d{2}T(\d{2}:\d{2}:\d{2})Z,(\d+(?:\.\d+)?),")
    
    with open(filename, encoding="utf-8") as data_file:      #open file as data_file
        for line in data_file:                                        #for each line
            match = re.search(regex,line)                             #search using regular expression
            if match:                                                 #if match is found
                time1 = (match.group(1))                              #set capture group 1 as time
                air_temperature = float(match.group(2))               #set capture group 2 as temp
                if time1 in time_frequencies:                         #if time value is found in frequency dictionary
                    time_frequencies[time1] += 1                      # add 1 to frequency
                    time_temperature[time1] += air_temperature        # add temp to the temp dictionary
                else:                                           #if time value not foun in the frequency dictionary
                    time_frequencies[time1] = 1                 #add time with frequency equals 1
                    time_temperature[time1] = air_temperature   #add time with its current temp value
    
    for time1 in time_temperature:                                               #for each hour in the dictionary
        #devive the total temperature by the frequency of an hour to find mean temp for each hour
        temp_averages[time1] = time_temperature[time1]/time_frequencies[time1] 
    
    return time_temperature, time_frequencies, temp_averages  #return all 3 dictionaries
 
def analyse_temperatures(time_temperature, time_frequencies, temp_averages): #analyse data class
    results_string = ""                #create empty string
    #results_string += str(time_frequencies) + "\n"
    #add number of hours to the string
    results_string += str(len(time_frequencies)) + " is the number of individual time variables that were found in the file" + "\n"
    #add hour with the maximum frequency to string
    results_string += str(max(time_frequencies,key=time_frequencies.get)) + " is the hour with the highest frequency of data." + "\n"
    #add hour with the minimum frequency
    results_string += str(min(time_frequencies,key=time_frequencies.get)) + " is the hour with the lowest frequency of data." + "\n"
    #print()
    #results_string += str(temp_averages) + "\n"
    #print()
    results_string += str(max(temp_averages,key=temp_averages.get)) + " is the hour with the highest average temperature." + "\n" #add max temp hour
    results_string += str(min(temp_averages,key=temp_averages.get)) + " is the hour with the lowest average temperature." + "\n"  #add min temp hour
    return results_string   #return data string

def viz_temperatures(time_temperature, time_frequencies, temp_averages):  #visualise data class
    import matplotlib.pyplot as plt
    # Create the figure and axes
    fig,  ax  =  plt.subplots(1,2,figsize=(10,5),sharey=True)
    
    # set a title
    fig.suptitle("Temperature by hour")
    
    ###### plot 0: bar chart of data frequency by hour
    
    # set a label for the x-axis 
    ax[0].set_xlabel("Temperature Frequency")
    
    # set a label hour for the y-axis 
    ax[0].set_ylabel("Hour")
    y_pos  =  range(len(time_frequencies))
    ax[0].set_yticks(y_pos)
    ax[0].set_yticklabels(time_frequencies.keys())
    
    # draw the visualisation bar chart
    ax[0].barh(y_pos,  time_frequencies.values())
    i  =  0  #  counter  for  y-axis  position
    for  value  in  time_frequencies.values():
        ax[0].text(value+1,  i,  str(round(float(value),2)))
        i += 1
    
    
    ###### plot 1: bar chart of air temperature by hour
    
    # set a label for the x-axis 
    ax[1].set_xlabel("Temperature Average")
    
    # set a label hour for the y-axis 
    y_pos2  =  range(len(temp_averages))
    ax[1].set_yticks(y_pos2)
    ax[1].set_yticklabels(temp_averages.keys())
    
    # draw the visualisation bar chart
    ax[1].barh(y_pos,  temp_averages.values())
    i  =  0  #  counter  for  y-axis  position
    for  value  in  temp_averages.values():
        ax[1].text(value+1,  i,  str(round(float(value),2))) 
        i += 1
    return fig  #return graph to be used by GUI
    
        
if __name__ == "__main__":  #test out program
    time_temperature, time_frequencies, temp_averages = get_data("Edited_data.csv")
    print(analyse_temperatures(time_temperature, time_frequencies, temp_averages))
    viz_temperatures(time_temperature, time_frequencies, temp_averages)

