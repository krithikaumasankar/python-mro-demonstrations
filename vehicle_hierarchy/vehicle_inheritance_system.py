class Vehicle:
    def start_engine(self):
        print("Vehicle engine started")
    def stop_engine(self):
        print("Vehicle engine stopped")
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")
class Bicycle(Vehicle):
    def start_engine(self):
        print("Bicycle does not have an engine")
    def stop_engine(self):
        print("Bicycle stopped")
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")
    def stop_engine(self):
        print("Motorcycle engine stopped")
c = Car()
b = Bicycle()
m = Motorcycle()
c.start_engine()
c.stop_engine()
print()
b.start_engine()
b.stop_engine()
print()
m.start_engine()
m.stop_engine()
print("\nMRO Tracing")
print(Car.mro())
print(Bicycle.mro())
print(Motorcycle.mro())

for i in Car.mro():
    print(i.__name__)
print()
for i in Bicycle.mro():
    print(i.__name__)
print()
for cls in Motorcycle.mro():
    print(cls.__name__)
