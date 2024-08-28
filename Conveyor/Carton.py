# carton.py

class Carton:
    def __init__(self, carton_id, weight, destination):
        self.carton_id = carton_id
        self.weight = weight
        self.destination = destination
        self.position = 0  # Start position on the conveyor

    def move(self, distance):
        """Move the carton along the conveyor."""
        self.position += distance

    def __str__(self):
        return f"Carton {self.carton_id} at position {self.position}"
