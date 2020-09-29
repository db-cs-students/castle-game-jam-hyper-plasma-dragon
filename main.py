"""
Title: a big Drag castle
Creators: Noah Martinez, Raymond Waffle
Description:hi 
"""
# Setup game
info.set_score(0)
info.set_life(1)

# Player
my_sprite = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 2 2 2 2 . . . . . . .
    . . . . . 2 2 2 2 . . . . . . .
    . . . . . 2 2 2 2 . . . . . . .
    . . . . . 2 2 2 2 . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))

# player movement
controller.player1.move_sprite(None)