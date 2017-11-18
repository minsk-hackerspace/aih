require './roboarm.rb'

@inpose = [0.0007, 89.998, 0.002, -89.998, 89.9987, 0.002]
@arm = Roboarm.new(initial_pose: @inpose)
@arm.open_gripper

# pos x,y,z,roll,pitch,yaw
#position1 = Position.new()
#@arm.position_no_angle = position1


def klac
  @arm.open_gripper(40)
  @arm.close_gripper(40)  
  @arm.open_gripper(40)
end


def greet
  pose0 = [-80, 90, 0, -90, 90, 0]  
  pose1 = [-80, 105, 0, -72, 90, 0]  
  @arm.pose = @inpose  
  @arm.pose = pose0  
  @arm.pose = pose1
  @arm.pose = pose0  
  @arm.pose = @inpose  
  
end

def no
  pose0 = [-80, 89.998, 0.002, -89.998, 90, 0]  
  
  pose1 = [-80, 89.998, 0.002, -89.998, 85, 0]  
  pose2 = [-80, 89.998, 0.002, -89.998, 95, 0]    

  @arm.pose = @inpose  
  @arm.pose = pose0  
  @arm.pose = pose1
  @arm.pose = pose2
  @arm.pose = pose1
  @arm.pose = pose2
  @arm.pose = @inpose  
  
end

def yes

  pose0 = [-80, 89.998, 0.002, -90, 90, 0]  
  pose1 = [-80, 89.998, 0.002, -78, 90, 0]  
  pose2 = [-80, 89.998, 0.002, -90, 90, 0]    

  @arm.pose = @inpose  
  @arm.pose = pose0  
  @arm.pose = pose1
  @arm.pose = pose2
  @arm.pose = pose1
  @arm.pose = pose2
  @arm.pose = @inpose  
  
end

def sniff

  pose0 = [0, 90, 0, -90, 90, 0]  
  pose1 = [0, 90, 30, -60, 90, 0]  
  
  @arm.pose = @inpose  
  @arm.pose = pose0  
  @arm.pose = pose1
  @arm.pose = @inpose  
  
end


klac

greet