extends Node2D

signal health_depleted

var health = 10


func take_damage(amount):
    health -= amount
    if health <= 0:
        health_depleted.emit()
