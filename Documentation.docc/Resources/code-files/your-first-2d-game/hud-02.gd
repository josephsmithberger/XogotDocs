extends CanvasLayer

# Notifies `Main` node that the button has been pressed
signal start_game


# Updates, shows the message text and starts the timer
func show_message(text):
    $Message.text = text
    $Message.show()
    $MessageTimer.start()
