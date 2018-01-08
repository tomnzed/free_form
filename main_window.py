from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from single_render import SingleRender

dimensions = [1 ,1]

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("free forms")
        self.renders = []

        self.layout_main = QHBoxLayout()

        self.v_layouts = []

        for j in range(0,dimensions[0]):
            self.v_layouts.append(QVBoxLayout())

            for i in range(0, dimensions[1]):
                new_render = SingleRender(Title="Render {},{}".format(j,i))
                self.renders.append(new_render)
                self.v_layouts[j].addWidget(new_render)

            self.layout_main.addLayout(self.v_layouts[j])

        main_widget = QWidget()

        main_widget.setLayout(self.layout_main)

        self.setCentralWidget(main_widget)

        self.setGeometry(100, 100, 1000, 600)
