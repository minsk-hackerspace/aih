require_relative 'barman'
b = Barman.new
@arm = b.arm

@nad_gin_2 = [-22.3942,91.8484,41.3573,8.621499999999997,-119.03059999999999,-13.3023]
@nad_gin = [-25.2486, 115.491, 59.2375, 13.857799999999997, -128.3333, 2.9333]
@gin = [-25.0618,113.0033,87.6056,-17.101,-128.8222,6.2237]

@nad_tonic_2 = [-43.6617,79.0316,47.0256,27.719099999999997,-157.6366,-13.2529]
@nad_tonic = [-55.3807,70.9202,110.9873,-1.9651999999999958,-145.9794,0.7649]
@tonic = [-55.3244,75.9396,133.9899,-29.8643,-144.887,0.8898]

@glass_path = [[142.8517, 102.8759, 107.9811, -31.1374, 53.945, -64.4341], [142.8579, 102.8327, 105.2764, -26.5567, 57.109, -128.3855]]
@stop_glass = [142.8517, 102.8759, 107.9811, -31.1374, 53.945, -64.4341]

def get_gin
  @arm.open
  @arm.pose = @nad_gin_2
  @arm.pose = @nad_gin
  @arm.pose = @gin
  @arm.close
  @arm.pose = @nad_gin
  @arm.pose = @nad_gin_2
end

def put_gin
  @arm.pose = @nad_gin_2
  @arm.pose = @nad_gin
  @arm.pose = @gin
  @arm.open
  @arm.pose = @nad_gin_2
end

def get_tonic
  @arm.open
  @arm.pose = @nad_tonic_2
  @arm.pose = @nad_tonic
  @arm.pose = @tonic
  @arm.close
  @arm.pose = @nad_tonic
  @arm.pose = @nad_tonic_2
  @arm.home
end

def put_tonic
  @arm.pose = @nad_tonic_2
  @arm.pose = @nad_tonic
  @arm.pose = @tonic
  @arm.open
  @arm.pose = @nad_tonic_2
  @arm.home
end

def pour(volume = 0)
  @glass_path.each do |pose|
    @arm.pose = pose
  end
  sleep volume
  @arm.pose = @stop_glass
  @arm.home
end

get_gin
pour
put_gin

# get_tonic
# pour 8
# put_tonic
# b.take_cola(8)

