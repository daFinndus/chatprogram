from led import LED


class RGB:
    # Register small amount of colors
    colors = {
        "purple": [130, 0, 255],
        "pink": [130, 0, 130],
        "red": [255, 0, 0],
        "orange": [255, 130, 0],
        "yellow": [255, 255, 0],
        "green": [0, 255, 0],
        "turquoise": [10, 175, 160],
        "blue": [0, 0, 255],
        "white": [255, 255, 255]
    }

    # Set gpio board pins to certain channel
    channels = {
        "red_channel": 37,
        "blue_channel": 35,
        "green_channel": 33
    }

    def __init__(self):
        self.actual_color = None

        self.LED_red = LED(self.channels["red_channel"])
        self.LED_green = LED(self.channels["green_channel"])
        self.LED_blue = LED(self.channels["blue_channel"])

    # Function to set the intensity of every channel to display certain color
    def set_color(self, color_light):
        if color_light.lower() in self.colors.keys():
            self.LED_red.set_intensity(self.colors.get(color_light)[0])
            self.LED_green.set_intensity(self.colors.get(color_light)[1])
            self.LED_blue.set_intensity(self.colors.get(color_light)[2])
            self.actual_color = color_light
        else:
            print("\nColor not registered. Please use a color that is already registered. For example:\n")
            for color in self.colors:
                print(f"{color}")

    # Clean up all pins afterward to avoid a short circuit
    def turn_off_pins(self):
        self.LED_red.switch_off()
        self.LED_green.switch_off()
        self.LED_blue.switch_off()
        print("\nCleaned up all used pins.\n")
