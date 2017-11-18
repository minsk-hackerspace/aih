import robot

arm = robot.Robot('http://100.95.255.181:8080')

print arm.getPositionMatrix()
