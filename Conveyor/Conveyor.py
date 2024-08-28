# conveyor.py

from .Carton import Carton

class Conveyor:
    def __init__(self, length):
        self.length = length
        self.cartons = []

    def add_carton(self, carton):
        """Add a carton to the conveyor."""
        if carton.position == 0:
            self.cartons.append(carton)
        else:
            print("Carton must start at position 0 to be added to the conveyor.")

    def move_cartons(self, distance):
        """Move all cartons on the conveyor."""
        for carton in self.cartons:
            carton.move(distance)
            # Check if the carton has reached the end of the conveyor
            if carton.position >= self.length:
                self.cartons.remove(carton)
                print(f"Carton {carton.carton_id} has reached the end of the conveyor.")

    def __str__(self):
        return f"Conveyor with {len(self.cartons)} cartons"
