class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print("This {} is driving".format(self.model))
    
    def stop(self):
        print("This {} is stopped".format(self.model))