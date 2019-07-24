class Car:
    def __init__(self, regno, no_gears):
        self.regno = regno
        self.no_gears = no_gears
    def start(self):
        print(f"car with regno: {self.regno} started....")
    def stop(self):
          print(f"car with regno: {self.regno} stopped....")
    def change_gear(self):
          print(f"car with regno: {self.regno} changed gear....")