from PyQt5.QtWidgets import *
import os
import random


from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

from PyQt5 import QtCore, QtWidgets


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.gca(projection='3d')

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    plot_length = 10
    num_lines = 1
    lines = [[range(10), range(10)] for i in range(0, 1)]
    colours = ['r', 'b', 'y', 'c', 'g', 'm', 'k', '#ee00ff', '#00feee', '#ffee00']
    colours_dim = ['#ffaaaa', 'b', 'y', 'c', 'g', 'm', 'k', '#ee00ff', '#00feee', '#ffee00']

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(10000)

    def update_and_plot(self):

        for i in range(0, self.num_lines):
            self.lines[i][0] = [random.randint(0, 10) for i in range(self.plot_length)]
            self.lines[i][1] = [random.randint(0, 10) for i in range(self.plot_length)]

        zeros = [0 for i in range(0,10)]
        maxes = [10 for i in range(0, 10)]

        for i in range(0, self.num_lines):
            self.axes.plot(range(self.plot_length), self.lines[i][0], zeros,                color=self.colours_dim[i])
            self.axes.plot(zeros,                   self.lines[i][0], zs=self.lines[i][1],  color=self.colours_dim[i])
            self.axes.plot(range(self.plot_length), maxes,            zs=self.lines[i][1],  color=self.colours_dim[i])

            self.axes.plot(range(self.plot_length), self.lines[i][0], zs=self.lines[i][1], color=self.colours[i])


    def compute_initial_figure(self):
        self.update_and_plot()

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        self.axes.cla()
        self.update_and_plot()
        self.draw()

class SingleRender(QGroupBox):
    def __init__(self, *args, **kwargs):
        self.title_name = kwargs.pop("Title")
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()

        self.title_label = QLabel(self.title_name)

        layout.addWidget(self.title_label)

        #l = QtWidgets.QVBoxLayout(self.main_widget)
        dc = MyDynamicMplCanvas( width=5, height=4, dpi=100)
        layout.addWidget(dc)


        self.setLayout(layout)