require_relative 'barman'

b = Barman.new
@arm = b.arm

@nad_viski_2 = [89.6292,65.6653,66.1067,16.5557,-180.495,-11.8672]
@nad_viski = [89.6044,71.08160000000001,122.2558,-17.632400000000004,-181.95069999999998,-3.6776]
@viski = [91.9912,86.7975,145.4301,-54.0562,-182.66410000000002,-0.0748]

@glass_path = [[142.8517, 102.8759, 107.9811, -31.1374, 53.945, -64.4341], [142.8579, 102.8327, 105.2764, -26.5567, 57.109, -128.3855], [142.8517, 102.8759, 107.9811, -31.1374, 53.945, -64.4341]]


def get_viski
  @arm.open
  @arm.pose = @nad_viski_2
  @arm.pose = @nad_viski
  @arm.pose = @viski
  @arm.close

  @arm.pose = @nad_viski
  @arm.pose = @nad_viski_2
end

def put_viski
  @arm.pose = @nad_viski_2
  @arm.pose = @nad_viski
  @arm.pose = @viski
  @arm.open
 # @arm.pose = @nad_viski
  @arm.pose = @nad_viski_2
  @arm.home
end

def pour
  @glass_path.each do |pose|
    @arm.pose = pose
  end
  @arm.home
end

get_viski
pour
put_viski



# b.take_cola(10)
