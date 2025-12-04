extends Area2D

@export var speed = 400 # How fast the player will move (pixels/sec).
var screen_size # Size of the game window.

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
    # Get screen size to use for stoping the player from exiting the screen.
    screen_size = get_viewport_rect().size
    # Hide the player when the game starts.
    hide()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
    var velocity = Vector2.ZERO # The player's movement vector.
    
    # Check for button pressed signals and then set the velocity Vector2 accordingly.
    if Input.is_action_pressed("move_right"):
        velocity.x += 1
    if Input.is_action_pressed("move_left"):
        velocity.x -= 1
    if Input.is_action_pressed("move_down"):
        velocity.y += 1
    if Input.is_action_pressed("move_up"):
        velocity.y -= 1
    
    # If the player is moving, play the animation, else stop it.
    if velocity.length() > 0:
        # Normalize the velocity Vector2 (converting it to maintain direction and will equal "1").
        # Multiply it against the speed variable we set and exported before.
        velocity = velocity.normalized() * speed
        $AnimatedSprite2D.play()
    else:
        $AnimatedSprite2D.stop()
    
    # Set player position to velocity Vector2 * frame rate delta.
    # Note: This helps make movement framerate agnostic.
    position += velocity * delta
    # Clamp the position so the player stays in the screen.
    position = position.clamp(Vector2.ZERO, screen_size)
    
    # Change the animation based on direction.
    if velocity.x != 0:
        $AnimatedSprite2D.animation = "walk"
    elif velocity.y != 0:
        $AnimatedSprite2D.animation = "up"
    
    # Rotate the player to look where its moving.
    if velocity.length() > 0:
        # Rotate the player to look at its motion vector.
        look_at(position + velocity)
        # Apply a 90-degree (PI/2) correction for proper visual alignment.
        # Note: Without this the player would be rotated 90-degrees off axis.
        rotation += PI / 2
