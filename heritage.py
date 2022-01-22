class Vehicule:
  def __init__(self, started = False, speed = 0):
    self.started = started
    self.speed = speed
  
  def start(self):
    self.started = True
    print("Car started, let's ride !")
  
  def stop(self):
    self.speed = 0
    print('Halting')
  
  def increase_speed(self, delta):
    if self.started:
      self.speed = self.speed + delta
      print('Vrooooom !')
    else:
      print("You need to start the car firt")

# Car hérite de Vehicule
class Car(Vehicule):
  trunk_open = False
  
  def open_trunk(self):
    self.trunk_open = True
    print('Open car trunk !')
  
  def close_trunk(self):
    self.trunk_open = False
    print('Close car trunk !')
# Motorcycle hérite de Vehicule
class Motorcycle(Vehicule):
  def __init__(self, center_stand_out = False):
    self.center_stand_out = center_stand_out
    super().__init__()
  
  def start(self):
    self.started = True
    print('Motorcycle started, let\'s ride !')

# Création objet Car
car = Car()
car.increase_speed(10)
car.start()
car.increase_speed(10)
car.open_trunk()
car.stop()
car.close_trunk()
motorcycle = Motorcycle()
motorcycle.start()