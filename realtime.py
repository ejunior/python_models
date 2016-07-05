import pylab
from pylab import *
import numpy as np

xAchse = pylab.arange(0, 100, 1)
yAchse = pylab.array([0] * 100)

fig = pylab.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Waveform Plot")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.axis([0, 100, -1.5, 1.5])
line1 = ax.plot(xAchse, yAchse, '-')

manager = pylab.get_current_fig_manager()

values = [0 for x in range(100)]

Ta = 0.01
fa = 1.0 / Ta
fcos = 3.5
Konstant = cos(2 * pi * fcos * Ta)
T0 = 1.0
T1 = Konstant


def sinwaveformGenerator(arg):
    global values, T1, Konstant, T0
    # ohmegaCos=arccos(T1)/Ta
    # print "fcos=", ohmegaCos/(2*pi), "Hz"

    tNext = ((Konstant * T1) * 2) - T0
    if len(values) % 100 > 70:
        r = np.random.rand()
        values.append(r * 2 - 1)
    else:
        values.append(tNext)
    T0 = T1
    T1 = tNext


def realtimePloter(arg):
    global values
    currentXAxis = pylab.arange(len(values) - 100, len(values), 1)
    line1[0].set_data(currentXAxis, pylab.array(values[-100:]))
    ax.axis([currentXAxis.min(), currentXAxis.max(), -1.5, 1.5])
    manager.canvas.draw()
    # manager.show()

timer = fig.canvas.new_timer(interval=20)
timer.add_callback(realtimePloter, ())
timer2 = fig.canvas.new_timer(interval=20)
timer2.add_callback(sinwaveformGenerator, ())
timer.start()
timer2.start()

pylab.show()