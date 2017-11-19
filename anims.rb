require './roboarm.rb'

@inpose = [0.0007, 89.998, 0.002, -89.998, 89.9987, 0.002]
@gpose = [-22.9161,85.2533,86.3724,-100.7,102.2827,4.9829]
@arm = Roboarm.new(initial_pose: @inpose)

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

def cls
  @arm.close_gripper(40)  
end  

def opn
  @arm.open_gripper(40)  
end  

def f
  puts '>>> !'
  pt = @arm.position
  puts pt
  pose = @arm.pose
  puts pose
  @arm.freeze
end

def r
  @arm.relax
  puts '>>> relaxed'
end

def loork
  @arm.pose = [-0.0034,90.0,0.0027,-89.9973,90.0,0.0013]
  @arm.pose = [-0.162,76.7231,-0.0322,-35.396,107.8363,-0.0061]
  @arm.pose = [-11.6777,66.4618,6.5238,-21.532600000000002,105.2895,-0.0096]
  @arm.pose = [-11.6523,66.43299999999999,6.5409,-21.494799999999998,105.2915,-0.0157]
  @arm.pose = [-18.3506,58.8147,6.5279,-13.487200000000001,104.7821,-0.0137]
  @arm.pose = [-23.9261,51.0377,4.9692,-10.161699999999996,97.6341,-0.0171]
  @arm.pose = [-5.3606,48.7958,5.0564,-10.720699999999994,108.4261,4.9074]
  @arm.pose = [-11.4477,66.0959,8.7128,-20.126999999999995,108.1013,4.9122]
  @arm.pose = [-11.4189,80.1357,8.7046,-30.6787,100.702,4.9191]  
  @arm.pose = [-20.5938,84.879,8.7142,-28.191699999999997,104.30760000000001,5.0008]
  @arm.pose = [-20.4819,70.7719,54.4887,-62.9009,104.0961,4.9912]
  @arm.pose = [-27.5077,58.5489,83.7364,-86.2805,97.4143,4.9919]
  puts 'Done'  

end

def get(x,y)
  @arm.pose = @gpose
  @arm.open_gripper()
  _x = (5-x.to_f-10)/100.0
  _y = y.to_f/100.0
  #@arm.pose = [-28.8548,129.0872,42.7272,-82.726,95.2349,4.9809]
  @arm.pose = [-28.8548, 122.0872, 42.7272, -70.726, 95.2349, 4.9809]
  @arm.position_no_angle = Position.new(_x, _y, 0.033, 0.05, -3.09, 0)  
  @arm.close_gripper(50)
  @arm.pose = @gpose
  puts 'Done'
end

def get_20_0
  get(20,0)
end

def get1
  @arm.pose = @gpose
  @arm.pose = [-28.8548,129.0872,42.7272,-82.726,95.2349,4.9809]
  @arm.position_no_angle = Position.new(-0.20, 0, 0.03, 0.05, -3.09, 0)  
  @arm.close_gripper(50)
  @arm.pose = @gpose
end

def drop
  @arm.pose = @gpose
  @arm.pose = [-115.8075,103.4623,53.6812,-88.7469,117.507,-0.0926]
  @arm.pose = [-115.7766,113.773,72.8098,-84.7239,117.4871,-0.1091]
  @arm.open_gripper()
  @arm.pose = @inpose
  puts 'Done'
end


#loork

#get1

#drop
