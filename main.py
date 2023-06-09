basic.showIcon(IconNames.Yes)
basic.pause(2000)
for (let index = 0; index < 15; index++) {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showIcon(IconNames.SmallSquare)
    basic.showIcon(IconNames.Square)
}
basic.forever(function () {
    basic.showIcon(IconNames.Skull)
    basic.showLeds(`
        # . # . #
        # . # . #
        # . # . #
        . . . . .
        # . # . #
        `)
})
