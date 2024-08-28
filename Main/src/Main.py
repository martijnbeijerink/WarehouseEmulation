import simpy
import time

class ConveyorBelt:
    def __init__(self, env, speed, length):
        self.env = env
        self.speed = speed  # meters per second
        self.length = length  # length of the conveyor in meters
        self.carton_position = 0  # Start at the beginning of the conveyor

    def move_carton(self, carton):
        while self.carton_position < self.length:
            yield self.env.timeout(1)
            self.carton_position += self.speed
            print(f'[{self.env.now}] Carton {carton.id} position: {self.carton_position:.2f} meters')
            time.sleep(0.1)  # Simulate a delay to see the printout in real-time

        print(f'Carton {carton.id} has reached the end of the conveyor at {self.carton_position:.2f} meters.')

class Carton:
    def __init__(self, carton_id):
        self.id = carton_id

def carton_generator(env, conveyor):
    carton_id = 1
    while True:
        carton = Carton(carton_id)
        env.process(conveyor.move_carton(carton))
        carton_id += 1
        yield env.timeout(10)  # New carton every 10 seconds

# Set up the simulation environment
env = simpy.Environment()

# Create a conveyor belt with speed 0.5 meters/second and length 10 meters
conveyor = ConveyorBelt(env, speed=0.5, length=10)

# Start generating cartons
env.process(carton_generator(env, conveyor))

# Run the simulation for a specified amount of time
env.run(until=60)
