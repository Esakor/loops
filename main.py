def on_button_pressed_a():
    for index in range(3):
        for index2 in range(4):
            sprite.move(1)
            basic.pause(100)
        sprite.turn(Direction.RIGHT, 165)
        basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

sprite: game.LedSprite = None
sprite = game.create_sprite(5, 0)

def on_forever():
    pass
basic.forever(on_forever)
