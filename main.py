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
    ........8888............
    ........8832............
    ........8888............
    ........8888............
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
    ........................
""")
jumper_facing_left = img("""
    ........................
    ........................
    ........................
    .......8888.............
    .......2388.............
    .......8888.............
    .......8888.............
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
    ..........aaaaaaaaaaaa.....22aaaaaaaaaaaaaaaaaaaaaaaaaaaaa.a
    ..........aaaaaaa......a.aa22aaaaaaaaaaa.2.2aaaaaaaaaaf....a
    .............aa...aaaaaaaaaaaaaaa.aaa...2...2aaaaaaaaaaaaa..
    ................aaaaaaaaaa...................2aaaaaaaaaaa..a
    .............a..aaaaaa.....aaaaaaaaaaaa.......aaaaaaaaaaa2..
    .............aa........aaaaaaaaaaaaaaaa.a2.2.2aaaaaa..aaa..a
    ..........aa...a.....aaaaaaaaaaaa.aaaaaaaaaaaaaaaaa.........
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
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
"""),True)

coin1 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""), SpriteKind.food)
tiles.place_on_tile(coin1, tiles.get_tile_location(3, 4))

coin2 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""), SpriteKind.food)
tiles.place_on_tile(coin2, tiles.get_tile_location(12, 2))

coin3 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""), SpriteKind.food)
tiles.place_on_tile(coin3, tiles.get_tile_location(24, 1))

coin4 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""), SpriteKind.food)
tiles.place_on_tile(coin4, tiles.get_tile_location(17,6))

coin5 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""), SpriteKind.food)
tiles.place_on_tile(coin5, tiles.get_tile_location(33,2))

coin6 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""), SpriteKind.food)
tiles.place_on_tile(coin6, tiles.get_tile_location(33,6))

coin7 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""), SpriteKind.food)
tiles.place_on_tile(coin7, tiles.get_tile_location(39,5))

coin8 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""), SpriteKind.food)
tiles.place_on_tile(coin8, tiles.get_tile_location(46,9))

coin9 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
"""), SpriteKind.food)
tiles.place_on_tile(coin9, tiles.get_tile_location(53,7))

coin10 = sprites.create(img("""
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
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
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    33333333333333333333333333333333333333333333333333333333333333333333333333333333333333ee333333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333eeee33333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333eeee33333333333333333333333333333333333333333333333333333333333333333333333
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333eeeee3333333333333333333333333333333333333333333333333333333333333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333333333333333eeeeee3333333333333333333333333333333333333333333333333333333333333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333333333333333eeeeee3333333333333333333333333333333333333333333333333333333333333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333333333333333eeeeee3333333333333333333333333333333333333333333333333333333333333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333333333333333eeeeee3333333333333333333333333333333333333333333333333333333333333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333333333333333eeeeee3333333333333333333333333333333333333333333333333333333333333333333333
    33333333333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeee3333333333333333333333333333333333333333333333333333333333333333333333
    33333333333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeee3333333333333333333333333333333333333333333333333333333333eeeeeeeeee33
    ee333333333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeeee33333333333333333333333333333333333333333333333333333333eeeeeeeeeeeee
    eeeee333333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeeee3333333333333333333333333333333333333333333333333333333eeeeeeeeeeeeee
    eeeeee33333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeeee3333333333333333333333333333333333333333333333333333333eeeeeeeeeeeeee
    eeeeeee3333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeeee3333333333333333333333333333333333333333333333333333333eeeeeeeeeeeeee
    eeeeeee3333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeeee333333333333333333333333333333333333333333333333eeeeeeeeeeeeeeeeeeeee
    eeeeeee3333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeeee33333333333333333333333333333333333333333333333eeeeeeeeeeeeeeeeeeeeee
    eeeeeee3333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeeeee333333333333333333333333333333333333333333333eeeeeeeeeeeeeeeeeeeeeee
    eeeeeee3333333333333333333333333333333333333333333333333333333333333333333333333333eeeeeeeee333333333333333333333333333333333333333333333eeeeeeeeeeeeeeeeeeeeeee
    eeeeeee333333333333333333333333333333333eee3333333333333333333333333333333333333333eeeeeeeee333333333333333333333333333333333333333333333ee1111111111111eeeeeeee
    eeeeeee333333333333333333333333333333eeeeeee333333333333333333333333333333333333333eeeeeeeeee333333333333333333333333333333333333333311111111111111111111eeeeeee
    eeeeeee3333333333333333333333333333eeeeeeeee333333333333333333333333333333333333333eeeeeeeeee3333333333333333333333333333333333333111111111111111111111111eeeeee
    eeeeeee33333333333333333333333333eeeeeeeeeeee33333333333333333333333333333333333333eeeeeeeeeee333333333333311111111111111111111111111111111111111111111111eeeeee
    eeeeeee3333333333333333333333333eeeeeeeeeeeee3333333333333333333333333333333333333eeeeeeeeeeee311111111111111111111111111111111111111111111111111111111111eeeeee
    eeeeeee333333333333333333333333eeeeeeeeeeeeee333333333333333333333333333333333333eeeeeeeeeeeee311111111111111111111111111111111111111111111111111111111111eeeeee
    eeeeeee333333333331333333333333eeeeeeeeeeeeee333333333333333333333333333333333333eeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111eeeeee
    eeeeeee333331111111133333333333eeeeeeeeeeeeee333333333333333333333333ee333333333eeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111eeeeee
    eeeeeee331111111111133333333333eeeeeeeeeeeeeee3333333333333333333333eeeeeee3333eeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111eeeeee
    eeeeeee11111111111113333333333eeeeeeeeeeeeeeee333333333333333333333eeeeeeeeee33eeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111eeeeee
    eeeeeee11111111111113333333333eeeeeeeeeeeeeeee333333333333333333333eeeeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111eeeeee
    eeeeeee11111111111111333333333eeeeeeeeeeeeeeee333333333333333333333eeeeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111eeeeee
    eeeee1111111111111111333333333eeeeeeeeeeeeeeee33333333333333333333eeeeeeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111eeeeee
    eeee11111111111111111333333eeeeeeeeeeeeeeeeeee33333333333333333333eeeeeeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111eeeeee
    eeee11111111111111111eeeeeeeeeeeeeeeeeeeeeeeee33eee333333333333333eeeeeeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111eeeeee
    eee111111111111111111eeeeeeeeeeeeeeeeeeeeeeeee33eeee33333333333333eeeeeeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111eeeeee
    eee111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee3333333333333eeeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111111eeeee
    ee1111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee333333333333eeeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111111eeeee
    ee1111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee33333333333eeeeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111111eeeee
    e11111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee33333333333eeeeeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111eeeee
    e11111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee33333333333eeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111111111eeee
    e11111111111111111111eeeeeeeeeeee11111eeeeeeeeeeeeeeee33333333333eeeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111111eeee
    1111111111111111111111eeeeeeeeeee1111111eeeeeeeeeeeeee33333333333eeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111eeeeeeeeee11111111eeeeeeeeeeeeee3333333333eeeeeeeeeeeeeeee11111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111eeeeeee11111111111eeeeeeeeeeeeeeeeeeeeee3eeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111eeee111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee11111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee11111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeeeeee111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    111111111111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeeeeeee1111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111111111111eeeeeeeeeeeeeeeeee11111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111eeeeee111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
"""))
# player death
def on_hit_tile(sprite):
    #jumper.say("tsss")
    info.change_life_by(-1)
scene.on_hit_tile(SpriteKind.player, 2, on_hit_tile)

def on_hit_tile2(sprite):
    game.over(True)
scene.on_hit_tile(SpriteKind.player, 15, on_hit_tile2)

def on_hit_tile3(sprite):
    info.change_score_by(1)
scene.on_hit_tile(SpriteKind.player, 5, on_hit_tile3)
