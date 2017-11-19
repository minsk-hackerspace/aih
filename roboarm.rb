require 'typhoeus'
require 'json'

class Roboarm
  SERVER = '100.95.255.181:8080'
  attr_accessor :speed, :time, :server

  def initialize(initial_pose: nil, speed: 100, time: 0, server: SERVER)
    @server = server
    @speed = speed
    @time = time
    @pose = initial_pose
    self.pose = @pose
    @position = Position.new(0, 0, 0, 0, 0, 0)
    position
  end

  def freeze
    res = Typhoeus.post(@server + '/freeze')
    puts res.code unless res.code == 200
    res.body
  end

  def relax
    res = Typhoeus.post(@server + '/relax')
    puts res.code unless res.code == 200
    res.body
  end

  def position=(position)
    res = Typhoeus.post(@server + '/setPosition', headers: {position: position, speed: @speed, time: @time})
    puts res.code
    puts res.body
    @position.parse(res.body)
    @position
  end

  def position_no_angle=(position)
    res = Typhoeus.post(@server + '/setPositionWithoutAngle', headers: {position: position, speed: @speed, time: @time})
    puts res.code unless res.code == 200
    @position.parse(res.body)
    @position
  end

  def position
    res = Typhoeus.get(@server + '/getPosition')
    @position.parse(res.body)
    @position
  end

  def pose=(pose)
    res = Typhoeus.post(@server + '/setPose', headers: {angles: pose.to_s, speed: @speed, time: @time})
    puts res.code unless res.code == 200
    res.body
  end

  def pose
    res = Typhoeus.get(@server + '/getPose')
    puts res.code unless res.code == 200
    res.body
  end

  def open_gripper(power = 5)
    Typhoeus.post(@server + '/openGripper', headers: {power: power})
  end

  def close_gripper(power = 40)
    Typhoeus.post(@server + '/closeGripper', headers: {power: power})
  end

  def photo(filename= 'photo'+ Time.now.to_s + '.jpg')
    downloaded_file = File.open filename, 'wb'
    request = Typhoeus::Request.new(@server + '/getPhoto')
    request.on_headers do |response|
      if response.code != 200
        raise 'Download failed'
      end
    end
    request.on_body do |chunk|
      downloaded_file.write(chunk)
    end
    request.on_complete do |_|
      downloaded_file.close
    end
    request.run
    filename
  end
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
