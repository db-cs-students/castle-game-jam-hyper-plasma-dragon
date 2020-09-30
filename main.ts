/** 
Title: a big Drag castle
Creators: Noah Martinez, Raymond Waffle
Description:hi 

 */
//  Setup game
info.setScore(0)
info.setLife(1)
//  Player
let jump = sprites.create(img`
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
jump.ay = 100
//  controls
controller.player1.moveSprite(jump, 50, 0)
let can_double_jump = true
function jump(): Sprite {
    
    if (can_double_jump) {
        jump.vy = -100
        can_double_jump = jump.isHittingTile(CollisionDirection.Bottom)
    }
    
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed() {
    
})
