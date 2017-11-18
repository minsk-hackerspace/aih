require 'roboarm.rb'

@inpose = [0.0007, 89.998, 0.002, -89.998, 89.9987, 0.002]
@arm = Roboarm.new(initial_pose: @inpose)


def init
  pose = [0.0007, 89.998, 0.002, -89.998, 89.9987, 0.002]
  puts arm.position
  arm.open_gripper
end