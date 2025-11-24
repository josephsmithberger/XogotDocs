extends RigidBody2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
    # Get all the mob animation names as an array.
    var mob_types = $AnimatedSprite2D.sprite_frames.get_animation_names()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
    pass
