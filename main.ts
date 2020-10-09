/** 
Title: a big Drag castle
Creators: Noah Martinez, Raymond Waffle
Description:hi 

 */
//  Setup game
info.setScore(0)
info.setLife(5)
//  Player
let jumper_facing_right = img`
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
`
let jumper_facing_left = img`
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
`
let jumper = sprites.create(jumper_facing_right, SpriteKind.Player)
jumper.ay = 100
scene.cameraFollowSprite(jumper)
//  controls
controller.player1.moveSprite(jumper, 60, 0)
let can_double_jump = true
controller.A.onEvent(ControllerButtonEvent.Pressed, function jump() {
    
    if (can_double_jump) {
        jumper.vy = -60
        can_double_jump = jumper.isHittingTile(CollisionDirection.Bottom)
    }
    
})
//  level one
let level = 2
game.onUpdate(function on_update2() {
    if (level == 1) {
        scene.setTileMap(img`
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
        `)
    } else if (level == 2) {
        scene.setBackgroundImage(img`
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
        `)
        scene.setTileMap(img`
            444444444444444444444444444444444444444444444444444444444444
            444444444444444444444444.44444444444444444444444444444444444
            ..........44..............4...............................44
            .........4444...........444..........4...f................44
            .......444...44......4444..........4.4..44................44
            .....444............44...........4.4.4....................44
            ..................444..........8...4.4....................44
            ......4........4444..............4.4.4....................44
            .....44444888844.............4.4.4.4.4....................44
            ..........44444..............4............................44
            444444444........4444444444444444444444444444444444444444444
            444444444444488444444444444444444444444444444444444444444444
        `)
    }
    
})
scene.setTile(10, img`
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
`, true)
scene.setTile(2, img`
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
`, true)
scene.setTile(15, img`
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
`, true)
scene.setTile(4, img`
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
`, true)
scene.setTile(8, img`
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
`, true)
let coin1 = sprites.create(img`
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin1, tiles.getTileLocation(3, 4))
let coin2 = sprites.create(img`
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin2, tiles.getTileLocation(12, 2))
let coin3 = sprites.create(img`
   . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin3, tiles.getTileLocation(24, 1))
let coin4 = sprites.create(img`
   . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin4, tiles.getTileLocation(17, 6))
let coin5 = sprites.create(img`
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin5, tiles.getTileLocation(33, 2))
let coin6 = sprites.create(img`
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin6, tiles.getTileLocation(33, 6))
let coin7 = sprites.create(img`
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin7, tiles.getTileLocation(39, 5))
let coin8 = sprites.create(img`
   . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin8, tiles.getTileLocation(46, 9))
let coin9 = sprites.create(img`
   . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin9, tiles.getTileLocation(53, 7))
let coin10 = sprites.create(img`
    . . 5 5 5 5 . .
    . 5 5 5 5 5 5 .
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    5 5 5 5 5 5 5 5
    . 5 5 5 5 5 5 .
    . . 5 5 5 5 . .
`, SpriteKind.Food)
tiles.placeOnTile(coin10, tiles.getTileLocation(58, 0))
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.rings)
    info.changeScoreBy(1)
})
game.onUpdate(function on_update() {
    
    if (jumper.isHittingTile(CollisionDirection.Bottom)) {
        can_double_jump = true
    }
    
    // jumper.say(str(controller.dx()))
    if (controller.dx() > 0) {
        jumper.setImage(jumper_facing_right)
    } else if (controller.dx() < 0) {
        jumper.setImage(jumper_facing_left)
    }
    
})
//  Generate Coins
// background_image
scene.setBackgroundImage(img`
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
`)
//  player death
scene.onHitTile(SpriteKind.Player, 2, function on_hit_tile(sprite: Sprite) {
    // jumper.say("tsss")
    sprite.setPosition(50, 50)
    scene.cameraShake()
    info.changeLifeBy(-1)
})
scene.onHitTile(SpriteKind.Player, 15, function on_hit_tile2(sprite: Sprite) {
    
    level = 2
})
scene.onHitTile(SpriteKind.Player, 5, function on_hit_tile3(sprite: Sprite) {
    info.changeScoreBy(1)
})
