/** 
Title: a big Drag castle
Creators: Noah Martinez, Raymond Waffle
Description:hi 

 */
//  Setup game
info.setScore(0)
info.setLife(3)
//  Player
let jumper_facing_right = img`
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 8 8 8 8 8 . . . . . .
    . . . . . 8 8 1 2 8 . . . . . .
    . . . . . 8 8 3 2 8 . . . . . .
    . . . . . 8 8 8 8 8 . . . . . .
    . . . . . 8 8 8 8 8 . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
`
let jumper_facing_left = img`
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 8 8 8 8 8 . . . . . .
    . . . . . 8 2 1 8 8 . . . . . .
    . . . . . 8 2 3 8 8 . . . . . .
    . . . . . 8 8 8 8 8 . . . . . .
    . . . . . 8 8 8 8 8 . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
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
//  tilemap
scene.setTileMap(img`
    ..........444444444444.....224444444444444444444444444444444
    ..........4444444......44442244444444444.2.24444444444.....4
    .............44...4444444444444444444...2...24444444444444..
    ................4444444444...................244444444444..4
    .............4..444444.....444444444444.......444444444442..
    .............44........4444444444444444442.2.2444444..444..4
    ..........44...4.....444444444444444444444444444444.........
    444444224444.4..4.444444....444.....444...4444444...4444...4
    444444444444444...................................4444444222
    444444444444444444444422244444444444442224444444444444444444
`)
scene.setTile(4, img`
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
`, true)
scene.setTile(2, img`
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
`, true)
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
`)
//  player death
scene.onHitTile(SpriteKind.Player, 2, function on_hit_tile(sprite: Sprite) {
    // jumper.say("tsss")
    info.changeLifeBy(-1)
})
