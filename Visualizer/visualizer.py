import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Conveyor.Conveyor import Conveyor

class ConveyorVisualizer:
    def __init__(self, conveyor):
        self.conveyor = conveyor
        self.fig, self.ax = plt.subplots()
        self.carton_positions = []

    def update_positions(self, i):
        self.ax.clear()
        self.ax.set_xlim(0, self.conveyor.length)
        self.ax.set_ylim(-1, 1)

        self.carton_positions = [carton.position for carton in self.conveyor.cartons]

        for pos in self.carton_positions:
            self.ax.add_patch(plt.Rectangle((pos, -0.2), 0.5, 0.4, color='blue'))

        self.ax.text(0.5, 1.05, f"Time: {self.conveyor.env.now:.1f} seconds", ha="center", transform=self.ax.transAxes)

    def visualize(self):
        ani = animation.FuncAnimation(self.fig, self.update_positions, frames=range(100), interval=100, repeat=False)
        plt.show()
