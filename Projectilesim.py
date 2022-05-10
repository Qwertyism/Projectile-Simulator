import matplotlib.pyplot as plt
import numpy as np
import math

delx = int(input("Enter The X-Coordinate: "))
dely = int(input("Enter The Y-Coordinate: "))

def sqrt(x):
    return np.sqrt(x)

def draw_graph(x, y, xmin, xmax, sol):
    plt.plot(x,y,markersize=.8)
    plt.xlabel('x-pos')
    plt.ylabel('y-pos')
    plt.title('Lightning Ball Trajectory')
    plt.xlim([xmin,1.5*xmax])

def traj_graph(v0, sol):
    g = 9.8
    x = np.arange(0.0,delx,.01)
    theta1 = np.arctan((delx + sqrt(delx**2 - 2*(g*delx**2 / v0**2)*(g*delx**2/(2.0*v0**2) + dely)))/(g*delx**2/v0**2))
    theta2 = np.arctan((delx - sqrt(delx**2 - 2*(g*delx**2 / v0**2)*(g*delx**2/(2.0*v0**2) + dely)))/(g*delx**2/v0**2))
    theta = 0
    
    if sol == 1:
        theta = theta1
    elif sol == 2:
        theta = theta2
    
    y = math.tan(theta)*x - 0.5*g*x**2/(v0**2*math.cos(theta)**2)
    
    return draw_graph(x, y, min(x), max(x), 1)

sol_list = [1,2]
vel = 12
for s in sol_list:
    traj_graph(vel, s)


plt.legend(['solution 1','solution 2'])
plt.savefig('./Projectile_sim.pdf')

vel1 = int(input("Enter A Velocity: "))
vel2 = int(input("Enter A Velocity: "))
vel3 = int(input("Enter A Velocity: "))

vels = [vel1, vel2, vel3]
plt.figure()
for v in vels:
    traj_graph(v, 1)
   
    
plt.legend(['init velocity = '+str(vels[0])+' m/s','init velocity = '+str(vels[1])+' m/s','init velocity = '+str(vels[2])+' m/s'])
plt.savefig('./Projectile_sim.pdf')


