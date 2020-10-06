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
    . . . . . . f f . . . . . . . .
    . . . . . f f f f . . . . . . .
    . . . f f f f f f f f . . . . .
    . . . f f f f f 6 8 f . . . . .
    . . . f f f f f 6 8 f . . . . .
    . . . f f f f f f f f . . . . .
    . . . f f f f f f f f . . . . .
    . . . f f f f f f f f . . . . .
    . . . f f f f f f f f . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
`
let jumper_facing_left = img`
    . . . . f f . . . . . . . . . .
    . . . f f f f . . . . . . . . .
    . f f f f f f f f . . . . . . .
    . f 8 6 f f f f f . . . . . . .
    . f 8 6 f f f f f . . . . . . .
    . f f f f f f f f . . . . . . .
    . f f f f f f f f . . . . . . .
    . f f f f f f f f . . . . . . .
    . f f f f f f f f . . . . . . .
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
`)
//  player death
scene.onHitTile(SpriteKind.Player, 2, function on_hit_tile(sprite: Sprite) {
    // jumper.say("tsss")
    sprite.setPosition(50, 50)
    scene.cameraShake()
    info.changeLifeBy(-1)
})
scene.onHitTile(SpriteKind.Player, 15, function on_hit_tile2(sprite: Sprite) {
    game.over(true)
})
scene.onHitTile(SpriteKind.Player, 5, function on_hit_tile3(sprite: Sprite) {
    info.changeScoreBy(1)
})
