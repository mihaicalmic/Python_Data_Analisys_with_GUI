#This is a helper program to draw a canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_figure(figure, canvas):   #class draw_figure
    """
    Draw a Matplotlib figure in a PySimpleGUI Canvas  #function discription
    """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)  #creates a canvas using the input given
    figure_canvas_agg.draw()                               #draw the canvas
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)  #some extra personalisation





