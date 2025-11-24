extends Node

# Create and export the mob_scene to add later using the scope
@export var mob_scene: PackedScene

# Create a score variable for score tracking
var score


# Called when the player dies, performs clean-up actions
func game_over() -> void:
    # Stop the timers
    $ScoreTimer.stop()
    $MobTimer.stop()

    # Show the game over screen
    $HUD.show_game_over()


# This will be called when the player presses the start button
func new_game():
    # Give the score a default value
    score = 0
    
    # Assign the player character the start position value
    $Player.start($StartPosition.position)

    # Start the timer we use trigger the game start after a 2.0s delay
    $StartTimer.start()
    
    # Set the score to 0
    $HUD.update_score(score)
    
    # Show a temporary message of "Get Ready"
    $HUD.show_message("Get Ready")

    # Clear any mobs that might still be on screen
    get_tree().call_group("mobs", "queue_free")

    # Start the game music
    $Music.play()


# Called by the MobTimer timeout signal
func _on_mob_timer_timeout() -> void:
    # Create a new instance of the Mob scene.
    var mob = mob_scene.instantiate()

    # Choose a random location on Path2D.
    var mob_spawn_location = $MobPath/MobSpawnLocation
    mob_spawn_location.progress_ratio = randf()

    # Set the mob's direction perpendicular to the path direction.
    var direction = mob_spawn_location.rotation + PI / 2

    # Set the mob's position to a random location.
    mob.position = mob_spawn_location.position

    # Add some randomness to the direction.
    direction += randf_range(-PI / 4, PI / 4)
    mob.rotation = direction

    # Choose the velocity for the mob.
    var velocity = Vector2(randf_range(150.0, 250.0), 0.0)
    mob.linear_velocity = velocity.rotated(direction)

    # Get the AnimatedSprite from the mob node
    var mob_sprite = mob.get_node("AnimatedSprite")

    # Change the vertical flip of the sprite if the mob moves left
    # Note: You can flip horizontally by using `flip_h`
    if cos(direction) < 0:
        mob_sprite.flip_v = true
    else:
        mob_sprite.flip_v = false

    # Spawn the mob by adding it to the Main scene.
    add_child(mob)


# Called by the ScoreTimer timeout signal
func _on_score_timer_timeout() -> void:
    # Increment the score by 1
    score += 1

    # Update the score with the incremented value
    $HUD.update_score(score)


# Called by the StartTimer timeout signal
func _on_start_timer_timeout() -> void:
    # Start the MobTimer
    $MobTimer.start()

    # Start the ScoreTimer
    $ScoreTimer.start()
