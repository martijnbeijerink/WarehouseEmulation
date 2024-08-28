# simulation.py

from .Conveyor import Conveyor
from .Carton import Carton

def run_simulation():
    # Create a conveyor of length 10 units
    conveyor = Conveyor(length=10)

    # Create some cartons
    carton1 = Carton(carton_id=1, weight=5, destination="Zone A")
    carton2 = Carton(carton_id=2, weight=3, destination="Zone B")

    # Add cartons to the conveyor
    conveyor.add_carton(carton1)
    conveyor.add_carton(carton2)

    # Simulate the conveyor moving
    for step in range(5):
        print(f"Step {step + 1}")
        conveyor.move_cartons(distance=2)  # Move cartons by 2 units per step
        for carton in conveyor.cartons:
            print(carton)
        print()

if __name__ == "__main__":
    run_simulation()
