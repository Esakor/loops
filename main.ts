input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 3; index++) {
        for (let index = 0; index < 4; index++) {
            sprite.move(1)
            basic.pause(100)
        }
        sprite.turn(Direction.Right, 165)
        basic.pause(500)
    }
})
let sprite: game.LedSprite = null
sprite = game.createSprite(5, 0)
basic.forever(function () {
	
})
