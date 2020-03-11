g=9.81
def projectile_motion (t,v0):
    return v0*t-0.5*g*t**2

def change_in_time (n,v0):
    tlist=[]
    ylist=[]
    t=0
    dt=(2*v0/(g*n))
    while t <=2*v0/g:
        y=projectile_motion(t,v0)
        tlist.append(t)
        ylist.append(y)
        t=t+dt
   # tlist.append(2*v0/g)
   # ylist.append(projectile_motion(2*v0/g,v0))
    return [tlist, ylist]

v0=100 #Lets assume v0 is in m/s
n=11
#What we should have here is a list within a list
listty=change_in_time(n,v0)
print(listty[0]) #Listty left side
print(listty[1]) #Listty right side

