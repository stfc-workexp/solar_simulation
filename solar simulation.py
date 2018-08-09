import math
from turtle import *
screen = Screen()
screen.bgcolor('#000000')
G = 6.67408e-11 # gravitational constant (m^3 kg^-1 s^-2)
AU = 149.6e9    # Astronomical unit (m)
#scale = 500 / AU
'''these are all the attributes that each planetary body will have:
-A name
-a mass (kg)
-a velocity in both x and y (m/s)
-a position in terms of (x , y)
'''
class body(Turtle):
    name = ''
    mass = 0    #these are the variables that every object in this class will have assigned to them
    velox = 0
    veloy = 0
    posix = 0
    posiy = 0
    colour = ''
    #attraction force is the Newton equation. Applies to both the object performing function and the object it is performing with.
    def attractionforce(self,other):
        if self == other:
            raise ValueError('Attraction of objects to itself requested')
        else:
            sx = self.posix
            sy = self.posiy
            ox = other.posix
            oy = other.posiy
            dx = ox - sx     # these are the sides of the 'triangle' joining the two bodies      
            dy = oy - sy
            dis = math.sqrt((dx ** 2) + (dy ** 2))  #pythagoras theorem to determine the direct distance between the bodies
            if dis == 0:
                raise ValueError('The bodies have collided')
            F = (G * self.mass * other.mass) / dis ** 2 #calculating the force of attraction (F)
            AngleF = math.atan2(dy, dx) #using inverse tangent to calculate the angle between the bodies
            fx = F * math.cos(AngleF)
            fy = F * math.sin(AngleF)
            return(fx,fy)

        #Print method here        
def update_info(step,bodies):
            print('Step: %d \n' % step)
            for body in bodies:         
                string = 'Body: {:<8s}     Position: ({:^9.2f},{:^9.2f}) AU from Sun      Velocity: ({:>9.3f},{:>9.3f}) m/s'.format(  # used to format into a table structure
                    body.name,body.posix / AU ,body.posiy / AU ,body.velox,body.veloy)    # 'posi's are converted back into AU
                print(string)                       
            print() #empty brackets are effectively '\n'
                   
def loop(bodies):
   
    for body in bodies:
        body.hideturtle()
        body.penup()
    step = 1
    time = 24 * 60 * 60 # a day = a second in this program
    scale = float(input('What scale would you like to use? ')) # taking user input for the scale
    scale /= AU
    while True:     # pythons version of a 'forever loop'
        
        update_info(step,bodies)

        step +=1 # step counter ( adds one every time its looped )

        ForceValues = {}

        for body in bodies:
            tfx = 0.0
            tfy = 0.0

            for other in bodies:

                if other is body:
                    continue

                fx, fy = body.attractionforce(other) # this will apply 'attractionforce' to every body, and do the calculation for it with every other body
                
                tfx += fx # this adds all the calculations done with the 'other's together
                tfy += fy
            ForceValues[body] = (tfx, tfy)# total force is saved in a dict.
        for body in bodies:
            tfx, tfy = ForceValues[body] 
            body.velox += (tfx / body.mass) * time
            body.veloy += (tfy / body.mass) * time
            body.posix += body.velox * time     #this is updating the values by performing an action and then instantly replacing itself with the new value
            body.posiy += body.veloy * time
            
            body.goto(body.posix * scale,body.posiy * scale)
            body.dot(3) 
          
#this is the main part of the program. involves assigning data to the attibutes of the class for each body
def main():     #allows new bodies to be added with out the need to add new code.
    earth = body()
    earth.name = 'Earth'
    earth.mass = 5.9742e24
    earth.velox = 0
    earth.veloy = 29783
    earth.posix = -1 * AU
    earth.posiy = 0
    earth.pencolor('#49FF33')

    sun = body()        # tells program that the object is within the 'body' class
    sun.name = 'Sun'
    sun.mass = 1.98892e30
    sun.velox = 0
    sun.veloy = 0   #the sun s h o u l d n ' t move (but it does slightly)
    sun.posix = 0
    sun.posiy = 0
    sun.pencolor('#FFDD00')
    sun.dot(20)
    
    venus = body()
    venus.name = 'Venus'
    venus.mass = 4.867e24
    venus.velox = 0
    venus.veloy = -35000
    venus.posix = -0.723 * AU
    venus.posiy = 0
    venus.pencolor('#FF9400')

    mercury = body()
    mercury.name = 'Mercury'
    mercury.mass = 3.3e23
    mercury.velox = 0
    mercury.veloy = 47400
    mercury.posix = -0.387 * AU
    mercury.posiy = 0
    mercury.pencolor('#C672FF')

    mars = body()
    mars.name = 'Mars'
    mars.mass = 6.42e23
    mars.velox = 0
    mars.veloy = 24100
    mars.posix = -1.524 * AU
    mars.posiy = 0
    mars.pencolor('#7A0202')

    jupiter = body()
    jupiter.name = 'Jupiter'
    jupiter.mass = 1.9e27
    jupiter.velox = 0
    jupiter.veloy = 13100
    jupiter.posix = -5.203 * AU
    jupiter.posiy = 0
    jupiter.pencolor('#DDAA42')

    saturn = body()
    saturn.name = 'Saturn'
    saturn.mass = 5.69e26
    saturn.velox = 0
    saturn.veloy = 9600
    saturn.posix = -9.582 * AU
    saturn.posiy = 0
    saturn.pencolor('#DDD452')

    moon = body()
    moon.name = 'Moon'
    moon.mass = 7.35e22
    moon.velox = 0
    moon.veloy = 28783
    moon.posix = -1.00256955 * AU
    moon.posiy = 0
    moon.pencolor('#BABABA')


##    x = body()
##    x.name = 'X'
##    x.mass = 5.69e31
##    x.velox = 0
##    x.veloy = 0
##    x.posix = -2.5 * AU
##    x.posiy = 0
##    x.pencolor('#FFFFFF')
##
##    '''y = body()
##    y.name = 'y'
##    y.mass = 5.69e16
##    y.velox = 0
##    y.veloy = 1000
##    y.posix = -0.1 * AU
##    y.posiy = 0
##    y.pencolor('#FFFFFF')
##
##    u = body()
##    u.name = 'u'
##    u.mass = 5.69e5
##    u.velox = 100000
##    u.veloy = 0
##    u.posix = -5 * AU
##    u.posiy = 0                       # must add the theoretical bodies into list below
##    u.pencolor('#FFFFFF')
##
##    i = body()
##    i.name = 'i'
##    i.mass = 5.69e29
##    i.velox = 0
##    i.veloy = 40000
##    i.posix = -3 * AU
##    i.posiy = 0
##    i.pencolor('#FFFFFF')'''
##

    bodies = [sun, mercury, venus, earth, moon, mars, jupiter, saturn] # a list of all the bodies and their respective properties

    
    
    loop(bodies)
    
if __name__ == '__main__': # there is a hidden variable set to __main__ at the start of the program.
    main()



