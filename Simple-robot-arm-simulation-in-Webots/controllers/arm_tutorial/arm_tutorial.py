from controller import Robot

robot=Robot()
timestep=64

m=robot.getMotor("motor")
m.setPosition(float('inf'))
m.setVelocity(0.0)

pSensor=robot.getPositionSensor("ps")
pSensor.enable(timestep)

speed=1
k=0  #to get position sensor reading
while (robot.step(timestep) !=-1):
    m.setVelocity(speed)
    k=pSensor.getValue()
    print(k)
    if (k>1.57):
        if (speed==1):
            speed=-1
    if (k<0):
        if (speed==-1):
            speed=1
    
    pass