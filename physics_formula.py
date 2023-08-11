# Formular for mass, distance and energy


# predefined parameters for testing 
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies" + " " + str(train_force) + " " +  "newtons of force" )

# C is a constant that is usually set to the speed of light, which is roughly 3 x 10^8

c = 3*10**8

def get_energy(mass, c):
  return mass * c**2

bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies" + " " + str(bomb_energy) + " " + "Joules")

def get_work(mass, acceleration, distance):
  force = train_force*distance
  work = force*distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does" + " " + str(train_work)+ " " + "Joules of work over" + " "+ str(train_distance)+ " " + "meters")




#Formulas for celcius to fahrenheit and vice versa

def f_to_c(f_temp):
  c_temp=(f_temp-32)*5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print("there are" + " " + str(f100_in_celsius) + " " + "celsius in 100 fahrenheit")


def c_to_f(c_temp):
  f_temp=c_temp*(9/5)+32
  return f_temp

c0_in_farenheit = c_to_f(0)
print("there are" + " " + str(c0_in_farenheit) + " " + "fahrenheit in 0 celsius")