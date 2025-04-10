def move_towards_target(sprite, target_x, target_y, speed, delta_time):
    # Calculate direction vector
    dx = target_x - sprite.center_x
    dy = target_y - sprite.center_y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    # Only move if we're not already at the target
    if distance > 1:
        # Normalize the direction vector
        dx /= distance
        dy /= distance
        
        # Apply easing for smoother movement
        # Use a smaller fraction of the distance when closer to target
        ease_factor = min(1.0, distance / 100.0)
        actual_speed = speed * ease_factor
        
        # Update position with normalized direction and speed
        sprite.center_x += dx * actual_speed * delta_time
        sprite.center_y += dy * actual_speed * delta_time
