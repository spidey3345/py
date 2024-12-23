#Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and methods start() and stop(). The Car class should have instances of Engine and Wheel classes as attributes. Implement a method start_car() in the Car class which starts the engine and prints  "Car started".

class Engine:
    def __init__(self,type):
        self.type=type
    def start(self):
        print("Engine Started")
    def stop(self):
        print("Engine Stopped")   

class Wheel:
    def __init__(self,type):
        self.type=type
    def start(self):
        print("Wheel Started")
    def stop(self):
        print("Wheel Stopped") 

class Car:
    def __init__(self):
        
    def start_car(self):
        self.start_car

        print("Car Started")



        


        
