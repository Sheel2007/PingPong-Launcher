import math

# def detect_object_depth():
#     # Simulated function to detect object and measure depth
#     # Returns x, y, z coordinates of the object
#     return x, y, z

def convert_to_polar(x, y, z):

    fov = 9
    
    pan_angle = math.atan(x / fov) * 180 / math.pi

    distance = math.sqrt(y ** 2 + x ** 2)

    tilt_angle = math.atan(z / distance) * 100 / math.pi 

    return pan_angle, tilt_angle

# Simulated object coordinates and depth measurements
# x = 1.5  # meters
# y = 0.8  # meters
# z = 2.0  # meters

# azimuth, elevation = convert_to_polar(x, y, z)
# servo_x_angle, servo_y_angle = map_to_servo_angles(azimuth, elevation)

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return radians_to_degrees(r), radians_to_degrees(theta)

def reference_angle(angle):
    if angle < 0:
        return reference_angle(angle + 360)

    elif angle <= 180 and angle > 90:
        return 180 - angle

    elif angle < 270 and angle > 180:
        return angle - 180

    elif angle < 360 and angle > 270:
        return 360 - angle

    else:
        return angle

def radians_to_degrees(angle):
    return angle * 180 / math.pi