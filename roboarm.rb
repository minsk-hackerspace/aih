require 'typhoeus'
require 'json'

class Roboarm
  SERVER = '192.168.128.163:8080'
  attr_accessor :speed, :time

  def initialize(speed: 50, time: 0)
    @speed = speed
    @time = time
    # @pose = [0.0007, 89.9 98, 0.002, -89.998, 89.9987, 0.002]
    @pose = [0.0878,92.2302,25.7025,53.86179999999999,-57.86150000000001,-42.7793]
    @home = [0.0878,92.2302,25.7025,53.86179999999999,-57.86150000000001,-42.7793]
    freeze
    self.pose = @pose
    position
    self.position = @position
    open
  end

  def home
    self.pose = @home
  end

  def position=(position)
    res = Typhoeus.post(SERVER + '/setPosition', headers: {position: position, speed: @speed, time: @time})
    puts res.code
    puts res.body
    @position.parse(res.body)
    @position
  end

  def position_no_angle=(position)
    res = Typhoeus.post(SERVER + '/setPositionWithoutAngle', headers: {position: position, speed: @speed, time: @time})
    puts res.code unless res.code == 200
    puts res.body
    @position.parse(res.body)
    @position
  end

  def position
    @position ||= Position.new(0, 0, 0, 0, 0, 0)
    res = Typhoeus.get(SERVER + '/getPosition')
    puts res.body
    @position.parse(res.body)
    @position
  end

  def pose=(pose)
    res = Typhoeus.post(SERVER + '/setPose', headers: {angles: pose.to_s, speed: @speed, time: @time}, verbose: true)
    puts res.code unless res.code == 200
    puts res.body
    res.body
  end

  def pose
    res = Typhoeus.get(SERVER + '/getPose')
    puts res.code unless res.code == 200
    puts res.body
    res.body
  end

  def open(power = 5)
    res = Typhoeus.post(SERVER + '/openGripper', headers: {power: power})
    puts res.body
  end

  def close(power = 40)
    res = Typhoeus.post(SERVER + '/closeGripper', headers: {power: power})
    puts res.body
  end

  def freeze
    res = Typhoeus.post(SERVER + '/freeze')
    puts res.body
  end
  alias_method :f, :freeze

  def relax
    res = Typhoeus.post(SERVER + '/relax')
    puts res.body
  end
  alias_method :r, :relax
end

class Position
  attr_accessor :x, :y, :z, :r, :p, :yaw

  def initialize(x, y, z, r, p, yaw)
    set(x, y, z, r, p, yaw)
  end

  def to_json
    {
        point: {x: @x, y: @y, z: @z},
        rotation: {pitch: @p, roll: @r, yaw: @yaw}
    }.to_json
  end

  def inspect
    to_json
  end

  def to_s
    {
        point: {x: @x.round(2), y: @y.round(2), z: @z.round(2)},
        rotation: {pitch: @p.round(2), roll: @r.round(2), yaw: @yaw.round(2)}
    }.to_json
  end

  def parse(str)
    json = Hash[JSON.parse(str, symbolize_names: true)]
    @x = json[:point][:x]
    @y = json[:point][:y]
    @z = json[:point][:z]
    @p = json[:rotation][:pitch]
    @r = json[:rotation][:roll]
    @yaw = json[:rotation][:yaw]
  end

  def set(x, y, z, r, p, yaw)
    @x = x
    @y = y
    @z = z
    @r = r
    @p = p
    @yaw = yaw
  end
end

# arm = Roboarm.new
# puts arm.position
#
# arm.position_no_angle = Position.new(-0.20062832771524025,-0.004640170661140133,0.007, 3.1309878826141357,0.16760402917861938,2.1582844257354736)
# # pose_observe = [-155,180,-85,-130,-75,10]
# # pose_observe = [-155,185,-85,-145,-75,10]
# # arm.pose = pose_observe
# # pose_observe2 = [-110,160,-75,-170,-57,65]
# # arm.pose = pose_observe2
#
#
# pose3 = [-16, 57, 90, -88, 102, -3]
# arm.pose =pose3
# arm.photos(n: 3)
#
# pose4 = [-34.4998, 74.2862, 84.2891, -87.8275, 89.4796, -3.1551]
# arm.pose = pose4
# arm.photos(n: 4)
#
# pose5 = [-33.5714, 29.8444, 125.0786, -107.3913, 89.8627, -3.153]
# arm.pose = pose5
# arm.photos(n: 5)
#
# pose6 = [-33.533, 26.705800000000004, 61.2549, -40.0109, 88.05, -3.1434]
# arm.pose = pose6
# arm.photos(n: 6)
#
# pose7 = [-49.814, 13.466499999999996, 78.693, -52.7578, 84.8475, -3.1475]
# arm.pose = pose7
# arm.photos(n: 7)
#
# pose8 = [-49.8717, 56.8701, 23.7757, -23.214200000000005, 82.0981, -3.1304]
# arm.pose = pose8
# arm.photos(n: 8)
#
# pose9 = [-44.8036, 91.7839, -2.9388, -17.607, 86.2146, -3.1379]
# arm.pose = pose9
# arm.photos(n: 9)
#
# pos_int = Position.new(-0, 0.15, 0.5, 3.14, -1.57, 1.57)
# arm.position_no_angle = pos_int
#
# pos_to_take = Position.new(-0.3, 0.3, 0.25, 3.14, -1.57, 1.57)
# arm.position_no_angle = pos_to_take
# arm.close_gripper
# puts arm.position
#
# pos_to_drop = Position.new(0.6, 0.3, 0.25, 3.14, -1.57, 1.57)
# arm.position_no_angle = pos_to_drop
# arm.open_gripper
# puts arm.position
#
#
# arm.position_no_angle = Position.new(0.0272, -0.3185, 0.88848, 3.14, -1.57, 1.57)
# puts arm.position
# arm.open_gripper
#
# # pos_end = Position.new(0.00, -0.0, 0.2, Math::PI, 0, 0)
# # arm.position = pos_end
#
# arm.pose = pose
# p t - Time.now