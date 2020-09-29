/** 
Title: a big Drag castle
Creators: Noah Martinez, Raymond Waffle
Description:hi 

 */
//  Setup game
info.setScore(0)
info.setLife(1)
//  Player
let my_sprite = sprites.create(img`
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
`)
//  player movement
controller.player1.moveSprite(null)
