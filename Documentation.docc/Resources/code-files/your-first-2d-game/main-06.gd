extends Node

# Create and export the mob_scene to add later using the scope
@export var mob_scene: PackedScene

# Create a score variable for score tracking
var score


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
    pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
    pass


# Called when the player dies, performs clean-up actions
func game_over() -> void:
    # Stop the timers
    $ScoreTimer.stop()
    $MobTimer.stop()


# This will be called when the player presses the start button
func new_game():
    # Give the score a default value
    score = 0
    
    # Assign the player character the start position value
    $Player.start($StartPosition.position)
    
    # Start the timer we use trigger the game start after a 2.0s delay
    $StartTimer.start()


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
    

# Called by the ScoreTimer timeout signal
func _on_score_timer_timeout() -> void:
    # Increment the score by 1
    score += 1


# Called by the StartTimer timeout signal
func _on_start_timer_timeout() -> void:
    # Start the MobTimer
    $MobTimer.start()
    
    # Start the ScoreTimer
    $ScoreTimer.start()
