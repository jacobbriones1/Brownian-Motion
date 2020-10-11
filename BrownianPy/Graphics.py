from Wiener import WienerProcess
from numpy import sin, pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import text
from matplotlib.widgets import Slider, Button, RadioButtons
from Maps import subscr
plt.style.use('ggplot')

W = WienerProcess(50000)

def scaleTaxis(N):
    return [i/N for i in range(N+1)]

axis_color = 'lightgoldenrodyellow'

fig = plt.figure()
ax = fig.add_subplot(111)

# Adjust the subplots region to leave some space for the sliders and buttons
fig.subplots_adjust(left=0.1, bottom=0.25)



N0 = 250

# Draw the initial plot
# The 'line' variable is used for modifying the line later
[line] = ax.plot([i/N0 for i in range(N0)], W.States[:N0], linewidth=0.45, color='black')
i0 = np.random.choice([i for i in range(N0)])
t0 = i0/N0
y = W.States[i0]
[point] = ax.plot([t0],y,marker = 'o',markeredgecolor='black',markerfacecolor='blue')

title = 'The Diffusively Rescaled Random Walk: Wₜ(N)'
ax.title.set_text(title)


    

ax.set_xlim([0, 1])
ax.set_ylim([np.min(W.States[0:N0])-1,
             np.max(W.States[0:N0])+1])

# Add two sliders for tweaking the parameters
t_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor=axis_color)
t_slider = Slider(t_slider_ax, 't', 0,1 ,valinit=t0,valstep = 1/N0)

# Draw another slider
N_slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axis_color)
N_slider = Slider(N_slider_ax, 'N', 0,W.Length ,valinit=N0, valfmt='%d',valstep=10)

val_slider_ax = fig.add_axes([0.25, 0.05, 0.65, 0.03], facecolor=axis_color)
val_slider = Slider(val_slider_ax, 'y', np.min(W.States),np.max(W.States) ,valinit=y)




# Define an action for modifying the line when any slider's value changes
def sliders_on_changed(val):
    
    i = int(N_slider.val)
    Tvals = [i/(N_slider.val) for i in range(N_slider.val)]
    states = W.States[:N_slider.val]
    line.set_data(Tvals, states)
    t_slider.valstep = 1/i
  
    Tind =min(range(len(Tvals)), key=lambda i: abs(Tvals[i]-t_slider.val)) 
    T = Tvals[Tind]
    point.set_data(Tvals[Tind],states[Tind])
    
    val_slider.set_val(states[Tind])
    
    ax.set_ylim([np.min(W.States[0:N_slider.val])-1,
             np.max(W.States[0:N_slider.val])+1])
    fig.canvas.draw_idle()
N_slider.on_changed(sliders_on_changed)
t_slider.on_changed(sliders_on_changed)


# Add a button for resetting the parameters
reset_button_ax = fig.add_axes([0.8, 0.02, 0.1, 0.01])
reset_button = Button(reset_button_ax, 'Reset', color=axis_color, hovercolor='0.975')
def reset_button_on_clicked(mouse_event):
    N_slider.reset()

reset_button.on_clicked(reset_button_on_clicked)





plt.show()
