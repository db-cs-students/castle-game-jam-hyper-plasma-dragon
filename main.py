"""
Title: a big Drag castle
Creators: Noah Martinez, Raymond Waffle
Description:hi 
"""
# Setup game
info.set_score(0)
info.set_life(5)

# Player
jumper_facing_right = img("""
    ........................
    ........................
    ........88888...........
    ........88128...........
    ........88328...........
    ........88888...........
    ........88888...........
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
""")
jumper_facing_left = img("""
    ........................
    ........................
    ........................
    ......88888.............
    ......82188.............
    ......82388.............
    ......88888.............
    ......88888.............
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
""")
jumper = sprites.create(jumper_facing_right,SpriteKind.player)

jumper.ay = 100
scene.camera_follow_sprite(jumper)
# controls
controller.player1.move_sprite(jumper, 60,0)
can_double_jump = True
def jump():
    global can_double_jump
    if can_double_jump:
        jumper.vy = -60
        can_double_jump = jumper.is_hitting_tile(CollisionDirection.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, jump)

# tilemap
scene.set_tile_map(img("""
    aaaaaaaaaaaaaaaaaaaaaa.....22aaaaaaaaaaaaaaaaaaaaaaaaaaaaa.a
    aaaaaaaaaaaaaaaaa......a.aa22aaaaaaaaaaaa2a2aaaaaaaaaaf....a
    aaaaaaaaaaaa.aa...aaaaaaaaaaaaaaa.aaa...2...2aaaaaaaaaaaaa..
    aa..............aaaaaaaaaa...................2aaaaaaaaaaa..a
    aa...........a..aaaaaa.....aaaaaaaaaaaa.......aaaaaaaaaaa2..
    aa...........aa........aaaaaaaaaaaaaaaa.a2a2a2aaaaaa..aaa..a
    aa........aa...a.....aaaaaaaaaaaa.aaaaaaaaaaaaaaaaa.........
    aaaaaa22aaaa.a..a.aaaaaa....aaa.....aaa...aaaaaaa...a.aa...a
    aaaaaaaaaaaaaaa...................................aaaaaaa222
    aaaaaaaaaaaaaaaaaaaaaa222aaaaaaaaaaaaa222aaaaa.aaaaaaaaaaaaa
"""))
scene.set_tile(10, img("""
    a a f a a a f a a a f a a f a a
    a a f a a a f a a a f a a f a a
    f f f f f f f f f f f f f f f f
    a f a a a f a a a f a a f a a a
    a f a a a f a a a f a a f a a a
    f f f f f f f f f f f f f f f f
    a a a f a a a f a a a f a a f a
    a a a f a a a f a a a f a a f a
    f f f f f f f f f f f f f f f f
    a f a a a f a a f a a a f a a a
    a f a a a f a a f a a a f a a a
    f f f f f f f f f f f f f f f f
    a a f a a a f a a a f a a a f a
    a a f a a a f a a a f a a a f a
    f f f f f f f f f f f f f f f f
    a f a a a f a a a f a a a f a a
"""),True)
scene.set_tile(2, img("""
    5 4 4 5 5 4 4 4 4 2 2 2 4 4 4 4
    4 4 4 4 4 5 5 4 2 2 2 2 4 4 4 5
    4 2 2 2 4 4 5 4 2 2 4 4 5 5 5 5
    2 2 4 2 4 4 5 4 2 2 4 5 5 5 5 4
    2 2 2 2 4 4 5 4 2 2 4 4 5 5 4 4
    4 2 2 2 4 5 5 4 4 4 4 4 4 4 4 2
    2 2 2 4 4 5 5 5 4 4 2 2 2 2 2 2
    4 2 2 4 5 5 5 5 4 2 2 4 2 2 2 4
    5 4 4 4 4 4 4 5 5 4 2 2 2 4 4 4
    4 4 4 2 2 2 4 4 5 5 4 4 4 4 5 5
    4 2 2 2 2 2 2 2 4 5 5 5 5 5 5 5
    5 4 4 2 4 2 2 4 4 5 5 5 4 4 4 5
    5 5 4 2 2 2 4 4 4 5 5 4 2 2 2 4
    4 5 4 4 4 4 5 5 5 5 4 2 4 2 2 4
    4 5 5 5 5 5 5 4 4 4 2 4 2 4 2 4
    4 5 5 5 4 4 4 4 2 2 2 2 4 2 4 4
"""),True)
scene.set_tile(15, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . 5 2 . . . . .
    . . . . . . . . . 5 2 2 . . . .
    . . . . . . . . . 5 2 2 2 . . .
    . . . . . . . . . 5 2 2 2 2 . .
    . . . . . . . . . 5 . . . . . .
    . . . . . . . . . 5 . . . . . .
    . . . . . . . . . 5 . . . . . .
    . . . . . . . . . 5 . . . . . .
    . . . . . . . . . 5 . . . . . .
    . . . . . . . . . 5 . . . . . .
    . . . . . . 5 5 5 5 5 5 5 . . .
    . . . . . 5 5 5 5 5 5 5 5 5 . .
    . . . . 5 5 5 5 5 5 5 5 5 5 5 .
    . . . 5 5 5 5 5 5 5 5 5 5 5 5 5
    . . 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""),True)

coin1 = sprites.create(img("""
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin1, tiles.get_tile_location(3, 4))

coin2 = sprites.create(img("""
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin2, tiles.get_tile_location(12, 2))

coin3 = sprites.create(img("""
   . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin3, tiles.get_tile_location(24, 1))

coin4 = sprites.create(img("""
   . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin4, tiles.get_tile_location(17,6))

coin5 = sprites.create(img("""
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin5, tiles.get_tile_location(33,2))

coin6 = sprites.create(img("""
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin6, tiles.get_tile_location(33,6))

coin7 = sprites.create(img("""
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin7, tiles.get_tile_location(39,5))

coin8 = sprites.create(img("""
   . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin8, tiles.get_tile_location(46,9))

coin9 = sprites.create(img("""
   . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin9, tiles.get_tile_location(53,7))

coin10 = sprites.create(img("""
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
"""), SpriteKind.food)
tiles.place_on_tile(coin10, tiles.get_tile_location(58,0))





def on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.rings)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap)

def on_update():
    global can_double_jump
    if jumper.is_hitting_tile(CollisionDirection.BOTTOM):
        can_double_jump = True

    #jumper.say(str(controller.dx()))
    if controller.dx() > 0:
        jumper.set_image(jumper_facing_right)
    elif controller.dx() <0: 
        jumper.set_image(jumper_facing_left)
game.on_update(on_update)

# Generate Coins
#background_image
scene.set_background_image(img("""
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666677666666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666777766666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666777766666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666777776666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666667777776666666666666666666666666666666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666667777776666666666666666666666677766666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666667777776666666666666666666666677766666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666667777776666666666666666666666777766666666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666667777776666666666666666666666777777776666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666677777776666666666666666666666777777777666666666666666666666666666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666677777776666666666666666666677777777777666666666666666666666666666777777777766
    7766666666666666666677777666666666666666666666666666666666666666666666666666666666677777777666666666666666666677777777777666666666666666666666666667777777777777
    7777766666666666666677777776666666666666666666666666666666666666666666666666666666677777777666666666666666666777777777777776666666666666666666666677777777777777
    7777776666666666666677777776666666666666666666666666666666666666666666666666666666677777777666666666666666666777777777777776666666666666666666666677777777777777
    7777777666666666666667777777666666666666666666666666666666666666666666666666666666677777777666666666666666666777777777777777666666666666666666666677777777777777
    7777777666666666666677777777666666666666666666666666666666666666666666666666666666677777777666666666666666666777777777777777766666666666666777777777777777777777
    7777777666666666666777777777666666666666666666666666666666666666666666666666666666677777777666666666666666666777777777777777776666666666667777777777777777777777
    7777777666666666666777777776666666666666666666666666666666666666666666666666666666677777777766666666666666667777777777777777776666666666677777777777777777777777
    7777777666666666777777777776666666666666666666666666666666666666666666666666666666677777777766666666666666667777777777777777776666666666677777777777777777777777
    77777776666666667777777777766666666666667776666666666666666666666666666666666666666777777777666666666666667777777777777777777766666666667777eeeeeeeeeeee77777777
    77777776666666667777777777766666666667777777666666666666666666666666666666666666666777777777766666666666667777777777777777777766677777777777eeeeeeeeeeeee7777777
    77777776666666667777777777766666666777777777666666666666666666666666666666666666666777777777766666666666667777777777777777777777777777777777eeeeeeeeeeeeee777777
    77777776666666677777777777766666677777777777766666666666666666666666666666666666666777777777776666666667777777eeeeeeeee77777777777777777777eeeeeeeeeeeeeee777777
    777777766666677777777777777666667777777777777666666666666666666666666666666666666677777777777767777777777777eeeeeeeeeeeeee77777777777777777eeeeeeeeeeeeeee777777
    777777766677777777777777777666677777777777777666666666666666666666666666666666666777777777777777777777777777eeeeeeeeeeeeeeee77777777777777eeeeeeeeeeeeeeee777777
    777777777777777777777777776666677777777777777666666666666666666666666666666666666777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeee7777eeeeeeeeeeeeeeeeee777777
    7777777777777777eeee7777766666677777777777777666666666666666666666666776666666667777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777
    7777777777777eeeeeee7777766666677777777777777766666666666666666666667777777666677777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777
    7777777777eeeeeeeeee77776666667777777777777777666666666666666666666777777777766777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777
    7777777eeeeeeeeeeeee77777776667777777777777777666666666666666666666777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777
    7777777eeeeeeeeeeeee77777777667777777777777777666666666666666666666777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777
    77777eeeeeeeeeeeeeee7777777766777777777777777766666666666666666666777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777
    7777eeeeeeeeeeeeeeeee777777777777777777777777766666666666666666666777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777
    7777eeeeeeeeeeeeeeeee777777777777777777777777766777666666666666666777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777
    777eeeeeeeeeeeeeeeeee777777777777777777777777766777766666666666666777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777
    777eeeeeeeeeeeeeeeeee77777777777777777777777777777777666666666666677777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777
    77eeeeeeeeeeeeeeeeeee77777777777777777777777777777777766666666666677777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777
    77eeeeeeeeeeeeeeeeeee77777777777777777777777777777777766666666666777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777
    7eeeeeeeeeeeeeeeeeeee7777777777777777777777777777777776666666666677777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777
    7eeeeeeeeeeeeeeeeeeee777777777777777777777777777777777666666666667777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777
    7eeeeeeeeeeeeeeeeeeee777777777777eeeee777777777777777766666666666777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777
    eeeeeeeeeeeeeeeeeeeeee77777777777eeeeeee777777777777776666666666677777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeee7777777777eeeeeeee7777777777777766666666667777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeee7777777eeeeeeeeeee7777777777777777777777677777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeee7777eeeeeeeeeeee777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
"""))
# player death
def on_hit_tile(sprite):
    #jumper.say("tsss")
    sprite.set_position(50, 50)
    scene.camera_shake()
    info.change_life_by(-1)
scene.on_hit_tile(SpriteKind.player, 2, on_hit_tile)

def on_hit_tile2(sprite):
    game.over(True)
scene.on_hit_tile(SpriteKind.player, 15, on_hit_tile2)

def on_hit_tile3(sprite):
    info.change_score_by(1)
scene.on_hit_tile(SpriteKind.player, 5, on_hit_tile3)
