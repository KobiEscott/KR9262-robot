def Forward():
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED2, 40, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED4, 40, 67)
def TurnLeft():
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED2, 55, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED4, 20, 67)
def Back():
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED1, 100, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED2, 35, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED3, 100, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED4, 35, 67)
def TurnRight():
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED2, 20, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED4, 55, 67)
def Stop():
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED2, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.set_led_duty_cycle(PCA9685.LEDNum.LED4, 0, 67)
strip = neopixel.create(DigitalPin.P5, 18, NeoPixelMode.RGB)
strip.clear()
PCA9685.init(67, 0)

def on_forever():
    Forward()
    basic.pause(500)
    Stop()
    basic.pause(500)
basic.forever(on_forever)

def on_forever2():
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
    basic.pause(500)
basic.forever(on_forever2)
