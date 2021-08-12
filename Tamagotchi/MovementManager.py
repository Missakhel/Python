class MovementManager:
    def Move(self, sprite, pressedKey, constraint):
        if (pressedKey == "up" and sprite.top >= constraint):
            sprite.y -= 1
        elif (pressedKey == "down" and sprite.bottom <= constraint):
            sprite.y += 1
        elif (pressedKey == "left" and sprite.left >= constraint):
            sprite.x -= 1
        elif (pressedKey == "right" and sprite.right <= constraint):
            sprite.x += 1
