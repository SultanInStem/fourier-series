from config import SCREEN_SIZE 
CENTER_X = SCREEN_SIZE[0] // 2
CENTER_Y = SCREEN_SIZE[1] // 2


def to_screen_coords(math_x, math_y): 
    screen_x = CENTER_X + math_x 
    screen_y = CENTER_Y - math_y
    return (screen_x, screen_y) 

def to_math_coords(screen_x, screen_y): 
    math_x = screen_x - CENTER_X 
    math_y = screen_y - CENTER_Y
    return (math_x, math_y)


import math

def resample_points(raw_points, n_target):
    if len(raw_points) < 2: return raw_points
    
    # 1. Calculate distances and total length
    total_length = 0
    segment_lengths = []
    for i in range(len(raw_points) - 1):
        d = math.dist(raw_points[i], raw_points[i+1])
        segment_lengths.append(d)
        total_length += d
        
    step_size = total_length / (n_target - 1)
    resampled = [raw_points[0]]
    
    # 2. Walk along segments to place new points
    current_segment_idx = 0
    accumulated_dist = 0
    
    for i in range(1, n_target - 1):
        target_dist = i * step_size
        
        while accumulated_dist + segment_lengths[current_segment_idx] < target_dist:
            accumulated_dist += segment_lengths[current_segment_idx]
            current_segment_idx += 1
            
        # Interpolate within the current segment
        part_dist = target_dist - accumulated_dist
        ratio = part_dist / segment_lengths[current_segment_idx]
        
        p1 = raw_points[current_segment_idx]
        p2 = raw_points[current_segment_idx + 1]
        
        new_x = p1[0] + (p2[0] - p1[0]) * ratio
        new_y = p1[1] + (p2[1] - p1[1]) * ratio
        resampled.append((new_x, new_y))
        
    resampled.append(raw_points[-1])
    return resampled



def compute_fourier_coefficients(points, n):
    N = len(points)
    coefficients = []




    return coefficients