require_relative 'roboarm'

class Barman
  attr_accessor :arm
  def initialize
    @arm = Roboarm.new(speed: 100)
    @glass_path = [[142.8517, 102.8759, 107.9811, -31.1374, 53.945, -64.4341], [142.8579, 102.8327, 105.2764, -26.5567, 57.109, -128.3855]]
  end

  def pose=(pose)
    @arm.pose = pose
  end

  def up(d = 0.1)
    position = JSON.parse(@arm.position.to_json)
    position['point']['z'] += d
    p = Position.new(position['point']['x'], position['point']['x'], position['point']['x'], position['rotation']['roll'], position['rotation']['pitch'], position['rotation']['yaw'])
    @arm.position = p
  end

  def up_n(d = 0.1)
    position = JSON.parse(@arm.position.to_json)
    position['point']['z'] += d
    p = Position.new(position['point']['x'], position['point']['x'], position['point']['x'], position['rotation']['roll'], position['rotation']['pitch'], position['rotation']['yaw'])
    @arm.position_no_angle = p
  end

  def take_juice(volume = 0)
    take_path = [[29.1803,140.8303,26.3699,13.900400000000005,-152.9763,1.4522]]
    lift_path = [[30.1574,141.6597,3.4593,25.811000000000007,-152.3178,-10.8599], [26.7125,132.0728,-1.3396,24.867500000000007,-140.9113,-15.9782]]
    glass_path = @glass_path
    pour(glass_path, lift_path, take_path, volume)
  end

  def take_whisky(volume = 0)
    take_path = [[78.4808,84.2061,57.7681,17.0693,-132.9071,-10.9753], [57.0396,142.0779,51.6638,-14.083799999999997,-224.60449999999997,-1.1707]]
    lift_path = [[58.9704,128.8723,46.6259,-2.7226,-221.35320000000002,-5.7266], [78.4808,84.2061,57.7681,17.0693,-132.9071,-10.9753]]
    glass_path = @glass_path
    pour(glass_path, lift_path, take_path, volume)
  end

  def take_vodka(volume = 0)
    take_path = [[-19.191,98.9524,76.1366,6.690600000000003,-72.2776,2.351],[-18.4742,100.8586,102.5017,-22.137500000000003,-73.59119999999999,1.1357]]
    lift_path = [[-19.2762,86.2654,50.8268,32.9898,-65.9708,-6.659]]
    glass_path = @glass_path
    pour(glass_path, lift_path, take_path, volume)
  end

  def take_cola(volume = 0)
    take_path = [[-30.3305, 104.2293, 100.1108, -17.076899999999995, -168.01999999999998, 4.8532]]
    lift_path = [[-30.3078, 94.2723, 86.474, -5.941599999999994, -167.8429, -2.8104], [-24.8929,87.0976,40.0849,-4.919200000000004,-168.59210000000002,-52.5029]]
    glass_path = @glass_path
    pour(glass_path, lift_path, take_path, volume)
  end

  def take_rum(volume = 0)
    take_path =[[-53.3166,113.955,52.2564,16.300200000000004,-19.632499999999993,-3.5005], ]
  end

  def pour(glass_path, lift_path, take_path, volume)
    @arm.open(40)
    @arm.home

    take_path.each do |take_pose|
      @arm.pose = take_pose
    end
    @arm.close


    lift_path.each do |lift_pose|
      @arm.pose = lift_pose
    end
    @arm.home

    glass_path.each do |glass_pose|
      @arm.pose = glass_pose
    end

    sleep volume # pouring itself

    glass_path.reverse[1..-1].each do |glass_pose|
      @arm.pose = glass_pose
    end
    @arm.home

    lift_path.reverse.each do |lift_pose|
      @arm.pose = lift_pose
    end

    take_path.reverse.each do |take_pose|
      @arm.pose = take_pose
      @arm.open(40)
    end
    @arm.home
  end
end

# b = Barman.new
# a = b.arm
# b.take_juice