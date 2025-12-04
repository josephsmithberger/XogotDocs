extends RigidBody2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
    # Get all the mob animation names as an array.
    var mob_types = $AnimatedSprite2D.sprite_frames.get_animation_names()
    # Pick a random animation name out of the array.
    # This is based on a random int picked out of the size of the array.
    $AnimatedSprite2D.play(mob_types[randi() % mob_types.size()])


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
    pass


# Called when the signal that a mob has exited the screen occurs.
func _on_visible_on_screen_notifier_2d_screen_exited() -> void:
    # Remove mobs from the game tree when they exit the screen.
    queue_free()
