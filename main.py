
def get_coordinates(obj)
    images = get_undistorted_images
    borders = find_objects(obj, images)
    target_border = find_closest_object(borders)
    return get_world_coordinates(target_border)


object_to_take = ARGV[0]
place_to_drop = ARGV[1]

arm.init_pose()
arm.look_around(object_to_take)
coorditates = get_coordinates(object_to_take)

while current_distance < ready_to_take_distance
    arm.get_closer(coorditates, min(delta, ready_to_take_distance))
    coorditates = filter_coordinates(get_coordinates(object_to_take))
    current_distance = get_distance(coordinates, arm.get_position())

arm.take(object_to_take)

arm.init_pose()
arm.look_around(place_to_drop)
coorditates = get_coordinates(place_to_drop)

while current_distance < ready_to_drop_distance
    arm.get_closer(coorditates, delta)
    coorditates = get_coordinates(object_to_take)
    current_distance = get_distance(coordinates, arm.get_position())

arm.drop(object_to_take)
arm.init_pose()