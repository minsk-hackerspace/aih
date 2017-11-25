require_relative 'roboarm'

class Barman
  attr_accessor :arm
  def initialize
    @arm = Roboarm.new(speed: 100)
    @glass_path = [[142.8517, 102.8759, 107.9811, -31.1374, 53.945, -64.4341], [142.8579, 102.8327, 105.2764, -26.5567, 57.109, -128.3855]]
  end

  def take_juice(volume = 0)
    take_path = [[2.9992, 106.6593, 68.4722, 5.821299999999994, -94.0086, -0.0082], [2.9958, 103.2041, 89.6614, -13.132099999999994, -94.6115, 0.0205]]
    lift_path = [[3.0068, 102.339, 72.816, 4.600499999999997, -94.6046, 0.0226]]
    glass_path = @glass_path
    pour(glass_path, lift_path, take_path, volume)
  end

  def take_vodka(volume = 0)
    take_path = [[-19.191,98.9524,76.1366,6.690600000000003,-72.2776,2.351],[-18.4742,100.8586,102.5017,-22.137500000000003,-73.59119999999999,1.1357]]
    lift_path = [[-19.2762,86.2654,50.8268,32.9898,-65.9708,-6.659]]
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
# b.take_juice