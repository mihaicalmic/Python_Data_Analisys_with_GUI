# PySimpleGUI program: Temperature Analyser GUI by Mihai Calmic
import re
#import gui and figure classes
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from draw_figure import draw_figure
#import the 4 programs that analyse the data
import Part4_singlevariable as single
import Part4_Date as date
import Part4_Time as time
import Part4_category as category


# pathname of data file, required for analysis
data_pathname = None

# change the theme
sg.theme("SystemDefault1")
#create menu layout
menu_def =  [ 
                ["File", ["Open", "Save", "Exit"]],
                ["Help",["Versions","About"]]
            ]

# create the layout of the GUI
layout = [
           [sg.Menu(menu_def)],          #menu at the top      
           [sg.Button("Analyse"),sg.Button("Visualyse"), sg.Button("Clear")] , #fallowed by 3 buttons          
           [sg.Multiline(key="-OUT-", size=(60,12))], #fallowed by a multiline box, fallowed by 4 choice buttons on the next line
           [sg.Radio("All","-RB-",key="-RBALL-",default=True),sg.Radio("Date","-RB-",key="-RBDATE-"),sg.Radio("Time","-RB-",key="-RBTIME-"),sg.Radio("Category","-RB-",key="-RBCATEGORY-")],
           [sg.StatusBar("", size=60, key="-STAT-")]  #and a status bar at the bottom
         ]

# create the window
window = sg.Window("Temperature Analysis", layout)

# event loop
while True:
    # read the window
    event, values = window.read()
    
    # exit event will exit the loop
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    elif event == "Analyse":  #if analyse botton was pressed
        # check if the data file has been selected    
        if data_pathname:
            match = re.search(".*Edited_data.csv",data_pathname) #check filename
            if match:  #if file is edited_data.csv
                # check which radio button is selected
                if window["-RBALL-"].get() == True:  #if all button is selected
                    # analyse the data from the singlevariable file
                    air_temperature, sea_temperature = single.get_data(data_pathname)      #call out the get_data and analyse data classes
                    output = single.analyse_temperatures(air_temperature, sea_temperature)
                    # display in the Multiline element the data returned
                    window["-OUT-"].update(output)
                    
                elif window["-RBDATE-"].get() == True:  #if Date button is selected
                    # analyse the data from the date analysis file
                    dates_temperature, dates_frequencies, temp_averages = date.get_data(data_pathname) #call out the get_data and analyse data classes
                    output = date.analyse_temperatures(dates_temperature, dates_frequencies, temp_averages)
                    # display in the Multiline element the data returned
                    window["-OUT-"].update(output)
                    
                elif window["-RBTIME-"].get() == True: #if Time button is selected
                    # analyse the data from the time analysis program
                    time_temperature, time_frequencies, temp_averages1 = time.get_data(data_pathname)  #call out the get_data and analyse data classes
                    output = time.analyse_temperatures(time_temperature, time_frequencies, temp_averages1)
                    # display in the Multiline element the data returned
                    window["-OUT-"].update(output)
                    
                elif window["-RBCATEGORY-"].get() == True:  #if Category button is selected
                    # analyse the data from the category program 
                    station_data, station_frequencies, temp_average2 = category.get_data(data_pathname)  #call out the get_data and analyse data classes
                    output = category.analyse_temperatures(station_data, station_frequencies, temp_average2)
                    # display in the Multiline element the data reurned
                    window["-OUT-"].update(output)
            else: #if a different file was selected
                sg.popup("Incorect file data", "Please select the data file called Edited_data.csv")  #open a window to tell the person to select the corect file
        else:  #if no data file was selected
            sg.popup("No Data File", "Please select the data file using File-Open")  #open a window to tell the person to select the file
    
    elif event == "Visualyse":  #if visualyse botton was pressed
        # check if the data file has been selected        
        if data_pathname: 
            match = re.search(".*Edited_data.csv",data_pathname) #check filename
            if match:  #if corect file
                # check which radio button is selected
                if window["-RBALL-"].get() == True:   #if all button is selected
                    #visualise the data for the singlevariable file
                    air_temperature, sea_temperature = single.get_data(data_pathname)  #call out the get_data and visualise data classes
                    fig = single.viz_temperatures(air_temperature, sea_temperature)
                    #don't display the figure normally
                    plt.ioff()
                    #define the window layout
                    layout = [[sg.Canvas(key="-CANVAS-")]]
                    #create the window
                    window1 = sg.Window("Temperature Visualisation",layout,finalize=True)
                    #display the figure in the canvas
                    draw_figure(fig, window1["-CANVAS-"].TKCanvas)
                    #display the window
                    event, values = window1.read()
                    #close the window
                    window1.close()
                    
                elif window["-RBDATE-"].get() == True:  #if date button is selected
                    #visualise the data for the date analysis file
                    dates_temperature, dates_frequencies, temp_averages = date.get_data(data_pathname)  #call out the get_data and visualise data classes
                    fig = date.viz_temperatures(dates_temperature, dates_frequencies, temp_averages)
                    #don't display the figure normally
                    plt.ioff()
                    #define the window layout
                    layout = [[sg.Canvas(key="-CANVAS-")]]
                    #create the window
                    window2 = sg.Window("Temperature Visualisation",layout,finalize=True)
                    #display the figure in the canvas
                    draw_figure(fig, window2["-CANVAS-"].TKCanvas)
                    #display the window
                    event, values = window2.read()
                    #close the window
                    window2.close()
                
                elif window["-RBTIME-"].get() == True:  #if time button is selected
                    #visualise the data for the time analysis program
                    time_temperature, time_frequencies, temp_averages1 = time.get_data(data_pathname)  #call out the get_data and visualise data classes
                    fig = time.viz_temperatures(time_temperature, time_frequencies, temp_averages1)
                    #don't display the figure normally
                    plt.ioff()
                    #define the window layout
                    layout = [[sg.Canvas(key="-CANVAS-")]]
                    #create the window
                    window3 = sg.Window("Temperature Visualisation",layout,finalize=True)
                    #display the figure in the canvas
                    draw_figure(fig, window3["-CANVAS-"].TKCanvas)
                    #display the window
                    event, values = window3.read()
                    #close the window
                    window3.close()
                
                elif window["-RBCATEGORY-"].get() == True:  #if category button is selected
                    #visualise the data for the category program
                    station_data, station_frequencies, temp_average2 = category.get_data(data_pathname)  #call out the get_data and visualise data classes
                    fig = category.viz_temperatures(station_data, station_frequencies, temp_average2)
                    #don't display the figure normally
                    plt.ioff()
                    #define the window layout
                    layout = [[sg.Canvas(key="-CANVAS-")]]
                    #create the window
                    window4 = sg.Window("Temperature Visualisation",layout,finalize=True)
                    #display the figure in the canvas
                    draw_figure(fig, window4["-CANVAS-"].TKCanvas)
                    #display the window
                    event, values = window4.read()
                    #close the window
                    window4.close()
            else: #if a difefrent file was chosen
                sg.popup("Incorect file data", "Please select the data file called Edited_data.csv")  #open a window to tell the person to select the corect file
                
        else:    #if no data file was selected
            sg.popup("No Data File", "Please select the data file using File-Open") #open a window to tell the person to select the file
    
    
    # if botton clear is pressed, clear the multiline and the status bar, reset the pathname
    elif event == "Clear":
        window["-OUT-"].update("")
        window["-STAT-"].update("")
        data_pathname = None

    # file - open menu
    elif event == "Open":   #if open button is pressed     
        data_pathname = sg.popup_get_file("Select the file to open","Open File")  #open a file selecter
                    
        # change the status bar
        window["-STAT-"].update("Data File: " + data_pathname)  #update the stat bar with the name and location of the file
        
    # file - save menu
    elif event == "Save": #if save button is pressed       
        out_pathname = sg.popup_get_folder("Select the folder and then add the filename","Save Output") #open a save file window
        
        # open the file and write the output
        with open(out_pathname, "w") as outfile: #open the file location
            outfile.write(window["-OUT-"].get()) #write the data to the file
            
        # change the status bar
        window["-STAT-"].update("Output saved to " + out_pathname)  #update the stat bar with details and location of the saved data
    # Help - versions menu    
    elif event == "Versions":  # if versions button is pressed
        sg.popup_scrolled("Versions ",sg.get_versions()) #open window with versions data
    #Help - about menu    
    elif event == "About":  #if versions button is pressed
        sg.popup("About","File Analyser Utility GUI created using PySimpleGUI.\nThis program uses the previous made data analyser programs and displays the data you select.\nFor Scripting3.2 Part 4 Assigment\nBy: Mihai Calmic")
        #open about data window
                       
# close the window when the program exited the while True loop
window.close()
