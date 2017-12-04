#Biker - Eulers Method
#Physics 322 Computational Practical
#Group members: Xola, Simon, Mziyanda

import numpy as np 
import matplotlib.pyplot as plt

while (True):
	try:
		option = input("Please select which program to run: \n1.Biker \n2.Motorbike \nYour selection: ")
	except:
		option = 0

	#Option 1 is selected
	#Biker program
	if(option == 1):
		#Initial constraints as per the problem
		vi = 2.0 #Initial velocity
		P = 350 #Initial power
		m = 70 #Initial mass
		k = 1 #Air resistance
		u = 0.01 #Coefficient of friction
		g = -9.8 #Force of gravity
		h = 0.1 #step size
		velocity = [] #velocity data array
		time = np.arange(0,10.1,0.1) #time data array

		#This function uses Eulers Method to return values from the given equation
		def f(t,vi):
			return ((P/m*vi) - (k*vi**2)/m -u*g)

		#This function populates the time and velocity arrays with the returned function data
		def calcVel():
			global vi
			del velocity[:]
			for t in time:
				vf = vi + h*f(t,vi)
				vi = vf
				velocity.append(vf)

		#The first run using only the given constraints
		calcVel()
		plt.plot(time, velocity, 'r', label='Normal')

		#Exploring the model
		#Increasing the air resistance and recalculating the velocity
		k = 3*k
		vi = 2.0
		calcVel()
		plt.plot(time, velocity, 'k', label='6*k')

		#Exploring the model
		#Increasing the coefficient of friction and recalculating the velocity
		k = 1
		u = 150*u
		vi = 2.0
		calcVel()

		#Setting up the plotting frame
		plt.plot(time, velocity, 'g', label= '150*u')
		plt.legend(loc = 4, ncol = 1,title = 'Plots')	
		plt.xlabel("Time")
		plt.ylabel("Velocity")
		plt.title("Velocity vs. Time graph")
		plt.show()
		break;

	#Option 2 is selected
	#Motorbike program
	#Assume 20km/l and that 1lt = 1kg
	elif(option == 2):
		#Initial constraints as per the problem
		vi = 2.0 #Initial velocity
		P = 350 #Initial power
		m = 70 #Initial mass
		k = 1 #Air resistance
		u = 0.01 #Coefficient of friction
		g = -9.8 #Force of gravity
		h = 0.01 #step size
		velocity = [] #velocity data array
		time = np.arange(0,100.1,0.01) #time data array
		vf = 0

		#This function uses Eulers Method to return values from the given equation
		def f(t,vi):
			return ((P/m*vi) - (k*vi**2)/m -u*g)

		#This function populates the time and velocity arrays with the returned function data
		def calcVel():
			global vi, vf, m
			del velocity[:]
			for t in time:
				x = vf*t;
				if((x/1000)%20 < 0.00002 and t != 0):
					m -= 1
				vf = vi + h*f(t,vi)
				vi = vf
				velocity.append(vf)
			fuel = int((x/1000)/20)
			print "Fuel used:", fuel, "lt. Distance travelled:", (vf*100)/1000, "km"

		#The first run using only the given constraints
		print "\nNormal run"
		calcVel()
		plt.plot(time, velocity, 'r', label='Normal')

		#Exploring the model
		#Increasing the air resistance and recalculating the velocity
		print "Increased air resistance"
		vi = 2.0
		m = 70
		k = 3*k
		calcVel()
		plt.plot(time, velocity, 'k', label='6*k')

		#Exploring the model
		#Increasing the coefficient of friction and recalculating the velocity
		print "Increased friction"
		vi = 2.0
		m = 70
		k = 1
		u = 150*u
		calcVel()

		#Setting up the plotting frame
		plt.plot(time, velocity, 'g', label= '150*u')
		plt.legend(loc = 4, ncol = 1,title = 'Plots')	
		plt.xlabel("Time")
		plt.ylabel("Velocity")
		plt.title("Velocity vs. Time graph")
		plt.show()
		break;

	#Invalid option is selected
	else:
		print "\nInvalid option selected! Please try again\n"

