require_relative 'barman'

b = Barman.new
@arm = b.arm

@rom_2 = [-48.3569,99.374,18.7001,33.866,-38.93889999999999,12.2586]
@rom_1 = [-48.381,103.3346,71.9803,1.1281000000000034,-32.6348,3.0061]
@rom_0 = [-49.5744,108.7193,82.8156,-8.235,-29.599900000000005,-3.3556]
@glass_path = [[142.8517, 102.8759, 107.9811, -31.1374, 53.945, -64.4341], [142.8579, 102.8327, 105.2764, -26.5567, 57.109, -128.3855], [142.8517, 102.8759, 107.9811, -31.1374, 53.945, -64.4341]]


def get_rum
  @arm.open
  @arm.pose = @rom_2
  @arm.pose = @rom_1
  @arm.pose = @rom_0
  @arm.close
  @arm.pose = @rom_2
  @arm.home
end

def put_rum
  @arm.pose = @rom_2
  @arm.pose = @rom_1
  @arm.pose = @rom_0
  @arm.open
  @arm.pose = @rom_2
  @arm.home
end

def pour
  @glass_path.each do |pose|
    @arm.pose = pose
  end
  @arm.home
end
get_rum
pour
put_rum

# b.take_cola(10)