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
    . . . . . . 1 1 . . . . . . . .
    . . . . . 1 1 1 1 . . . . . . .
    . . . 1 1 1 1 1 1 1 1 . . . . .
    . . . 1 1 1 1 1 6 8 1 . . . . .
    . . . 1 1 1 1 1 6 8 1 . . . . .
    . . . 1 1 1 2 1 1 1 1 . . . . .
    . . . 1 1 1 2 2 1 1 1 . . . . .
    . . . 1 1 1 1 2 2 2 1 . . . . .
    . . . 1 1 1 1 1 1 2 2 . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
""")
jumper_facing_left = img("""
    . . . . 1 1 . . . . . . . . . .
    . . . 1 1 1 1 . . . . . . . . .
    . 1 1 1 1 1 1 1 1 . . . . . . .
    . 1 8 6 1 1 1 1 1 . . . . . . .
    . 1 8 6 1 1 1 1 1 . . . . . . .
    . 1 1 1 1 2 1 1 1 . . . . . . .
    . 1 1 1 2 2 1 1 1 . . . . . . .
    . 1 2 2 2 1 1 1 1 . . . . . . .
    . 2 2 1 1 1 1 1 1 . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
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

# level one
level = 1
def on_update2():
    if level == 1:
        scene.set_tile_map(img("""
        aaaaaaaaaaaaaaaaaaaaaa.....22aaaaaaaaaaaaaaaaaaaaaaaaaaaaa.a
        aaaaaaaaaaaaaaaaa......a.aa22aaaaaaaaaaaa2a2aaaaaaaaaaf....a
        aaaaaaaaaaaa.aa...aaaaaaaaaaaaaaa.aaa...2...2aaaaaaaaaaaaa..
        aa..............aaaaaaaaaa...................2aaaaaaaaaaa..a
        aa...........a..aaaaaa.....aaaaaaaaaaaa.......aaaaaaaaaaa2..
        aa...........aa........aaaaaaaaaaaaaaaa.a2a2a2aaaaaa..aaa..a
        aa........aa...a.....aaaaaaaaaaaa.aaaaaaaaaaaaaaaaa.........
        aaaaaa22aaaa.a..a.aaaa......aaa.....aa....aaaaaaa...a.aa...a
        aaaaaaaaaaaaaaa...................................aaaaaaa222
        aaaaaaaaaaaaaaaaaaaaaa222aaaaaaaaaaaaa222aaaaa.aaaaaaaaaaaaa
        """))
    elif level == 2 :
        scene.set_background_image(img("""
            fffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffff
            fffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffff
            fffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffff
            fffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffff
            fffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffff
            fffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffff
            fffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffff
            fffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffff
            fffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffff
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            ffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffff
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff222222fffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            fffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffff22222ffffffffffffff
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            ffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffff222222222222222222222222222222222222222ffffffffffffffffffffff22222ffffffffffffffffffffffffff22222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            fffffffffffffffffffff22222ffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffffffffffff22222ffffffffffffffffffffffffffff22222ffffffffff
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            fffffff22222ffffffffffffffffffffffffffffff22222fffffffffffffffffffffffff22222ffffffffffffffffffffffff22222fffffffffffffffffff22222ffffffffffffffffffffffffffffff
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            ff22222fffffffffffffffffff22222ffffffffffffffffffffffffff22222ffffffffffffffffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffff22222fffffffffffffffff
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            fffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffff22222fffffffffffffffffff22222fffffff
            fffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffff22222fffffffffffffffffff22222fffffff
            fffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffff22222fffffffffffffffffff22222fffffff
            fffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffff22222fffffffffffffffffff22222fffffff
            fffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffff22222fffffffffffffffffff22222fffffff
            fffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffff22222fffffffffffffffffff22222fffffff
            fffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffff22222fffffffffffffffffff22222fffffff
            fffffffffffff22222fffffffffffffffffffff22222fffffffffffffffffffffffffff22222fffffffffffffffffffffffffffff22222ffffffffffffff22222fffffffffffffffffff22222fffffff
        """))
        scene.set_tile_map(img("""
            444444444444444444444444444444444444444444444444444444444444
            444444444444444444444444.44444444444444444444444444444444444
            ..........44..............4...............................44
            .........4444...........444..........4...3................44
            .......444...44......4444..........4.4..44................44
            .....444............44...........4.4.4....................44
            ..................444..........8...4.4....................44
            ...4..4........4444..............4.4.4....................44
            .....44444888844.............4.4.4.4.4....................44
            ..........44444..............4............................44
            444444444........4444444444444444444444444444444444444444444
            444444444444488444444444444444444444444444444444444444444444
        """)) 
game.on_update(on_update2)

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
scene.set_tile(4, img("""
    4 4 f 4 4 4 f 4 4 4 f 4 4 f 4 4
    4 4 f 4 4 4 f 4 4 4 f 4 4 f 4 4
    f f f f f f f f f f f f f f f f
    4 f 4 4 4 f 4 4 4 f 4 4 f 4 4 4
    4 f 4 4 4 f 4 4 4 f 4 4 f 4 4 4
    f f f f f f f f f f f f f f f f
    4 4 4 f 4 4 4 f 4 4 4 f 4 4 f 4
    4 4 4 f 4 4 4 f 4 4 4 f 4 4 f 4
    f f f f f f f f f f f f f f f f
    4 f 4 4 4 f 4 4 f 4 4 4 f 4 4 4
    4 f 4 4 4 f 4 4 f 4 4 4 f 4 4 4
    f f f f f f f f f f f f f f f f
    4 4 f 4 4 4 f 4 4 4 f 4 4 4 f 4
    4 4 f 4 4 4 f 4 4 4 f 4 4 4 f 4
    f f f f f f f f f f f f f f f f
    4 f 4 4 4 f 4 4 4 f 4 4 4 f 4 4
"""),True)
scene.set_tile(8, img("""
    9 6 6 9 9 6 6 6 6 8 8 8 6 6 6 6
    6 6 6 6 6 9 9 6 8 8 8 8 6 6 6 9
    6 8 8 8 6 6 9 6 8 8 6 6 9 9 9 9
    8 8 6 8 6 6 9 6 8 8 6 9 9 9 9 6
    8 8 8 8 6 6 9 6 8 8 6 6 9 9 6 6
    6 8 8 8 6 9 9 6 6 6 6 6 6 6 6 8
    8 8 8 6 6 9 9 9 6 6 8 8 8 8 8 8
    6 8 8 6 9 9 9 9 6 8 8 6 8 8 8 6
    9 6 6 6 6 6 6 9 9 6 8 8 8 6 6 6
    6 6 6 8 8 8 6 6 9 9 6 6 6 6 9 9
    6 8 8 8 8 8 8 8 6 9 9 9 9 9 9 9
    9 6 6 8 6 8 8 6 6 9 9 9 6 6 6 9
    9 9 6 8 8 8 6 6 6 9 9 6 8 8 8 6
    6 9 6 6 6 6 9 9 9 9 6 8 6 8 8 6
    6 9 9 9 9 9 9 6 6 6 8 6 8 6 8 6
    6 9 9 9 6 6 6 6 8 8 8 8 6 8 6 6
"""),True)
scene.set_tile(3, img("""
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666fff66666666666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666f88ff666666666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666f8888ff6666666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666f888888ff66666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666f88888888ff666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666666776666666666666666666666666666666666666666f88888888ff666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666667777666666666666666666666666666666666666666f888888ff66666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666667777666666666666666666666666666666666666666f8888ff6666666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666667777766666666666666666666666666666666666666f88ff666666666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666677777766666666666666666666666666666666666666fff66666666666666666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666677777766666666666666666666666777666666666666f666666666666ff66666666666666666
    666666666666666666666666666666666666666666666666666666666666666666666666666666666666777777666666666666666666666667726ff266666666f66666666666fff66666666666666666
    66666666666666666666666666666666666666666666666666666666666666666666666666666666666677777766666666666666666666667772fff266666666f6666666666fffff6666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666667777776666666666666666666666777f222f66666666f6666666666f2fff6666666666666666
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666677777776666666666666666666666777ff222f6666666f666666666fff22ff666666666666666
    666666666666666666666666666666666666666666666666666666666666666666666666666666666667777777666666666666666666667777fff2f22f666666f66666666ffffff2ff26777777777766
    77666666666666666666777776666666666666666666666666666666666666666666666666666666666777777776666666666666666666777ffff2fff2666666f66666666ffffff22227777777777777
    77777666666666666666777777766666666666666666666666666666666666666666666666666666666777777776666666666666666667777fff2ffff22fff22fffffffffffff2222ff7777777777777
    7777776666666666666677777776666666666666666666666666666666666666666666666666666666677777777666666666666666666777f2f2ffffff2ff22f22ffffffff222fff2ff7777777777777
    7777777666666666666667777777666666666666666666666666666666666666666666666666666666677777777666666666666666666777ff22fffffff222fff2222ffff22fffff2ff7777777777777
    7777777666666666666677777777666666666666666666666666666666666666666666666666666666677777777666666666666666666777fff2222ff222ffffffff222f22ffffff2ff7777777777777
    7777777666666666666777777777666666666666666666666666666666666666666666666666666666677777777666666666666666666777ffffff2222ffffffffffff222fffffff2ff7777777777777
    7777777666666666666777777776666666666666666666666666666666666666666666666666666666677777777766666666666666667777ffffff2222fffffffffff22f2222ffff2ff7777777777777
    7777777666666666777777777776666666666666666666666666666666666666666666666666666666677777777766666666666666667777fffff22ff222ffffffff22fffff22ffff2f7777777777777
    7777777666666666777777777776666666666666777666666666666666666666666666666666666666677777777766666666666666777777ff2222fffff222fffff22fffffff222fff2e2eee77777777
    7777777666666666777777777776666666666777777766666666666666666666666666666666666666677777777776666666666666777777f22ffffffffff2222222fffffffffff2ff22eeeee7777777
    7777777666666666777777777776666666677777777766666666666666666666666666666666666666677777777776666666666666777777fffffffffffffff22ffffffff777eeeeeeeeeeeeee777777
    77777776666666677777777777766666677777777777766666666666666666666666666666666666666777777777776666666667777777eefeeeeefffffffffff7777777777eeeeeeeeeeeeeee777777
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
scene.on_hit_tile(SpriteKind.player, 8, on_hit_tile)

def on_hit_tile2(sprite):
    global level
    level = 2
scene.on_hit_tile(SpriteKind.player, 15, on_hit_tile2)

def on_hit_tile3(sprite):
    info.change_score_by(1)
scene.on_hit_tile(SpriteKind.player, 5, on_hit_tile3)

def on_win(jumper):
    (True)
scene.on_hit_tile(SpriteKind.player,3, on_hit_tile)

