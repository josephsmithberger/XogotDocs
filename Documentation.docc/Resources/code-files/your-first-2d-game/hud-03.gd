extends CanvasLayer

# Notifies `Main` node that the button has been pressed
signal start_game


# Updates, shows the message text and starts the timer
func show_message(text):
    $Message.text = text
    $Message.show()
    $MessageTimer.start()


# Updates the message label to `Game Over` before resetting the label
func show_game_over():
    # Update the label to `Game Over`
    show_message("Game Over")
    
    # Wait until the MessageTimer has counted down.
    await $MessageTimer.timeout
    
    # Change the label back to the title
    $Message.text = "Save the Axolotl!"
    $Message.show()
    
    # Make a one-shot timer and wait for it to finish.
    await get_tree().create_timer(1.0).timeout
    $StartButton.show()
