from time import sleep
from RPi import GPIO

pins = []


# This is nearly the same LED class from task one
class LED:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)  # Address pins with their numbers
        GPIO.setwarnings(False)  # Mute all these stupid warnings, don't need them anyway
        GPIO.setup(pin, GPIO.OUT)  # Set pins as output

        self.pwm_object = GPIO.PWM(pin, 100)  # Initialize object with 100hz
        self.pwm_object.start(0)  # Start the pwm_object

        self.__intensity = 0  # Private object to calibrate LEDs
        self.pin = pin  # Private object

        pins.append(pin)  # Adding used pin to our pins object, useful for our cleanup

        print(f"LED-Device setup for pin {pin} is complete.")
        print(f"The LED is starting with an intensity of {self.__intensity}.\n")

    # Set the intensity to a certain value and translate it into percent
    def set_intensity(self, value):
        if value in range(0, 256):
            self.__intensity = value
            self.pwm_object.ChangeDutyCycle(
                100 - (self.__intensity / 255 * 100))  # Set duty cycle as difference to a hundred percent
        else:
            self.__intensity = 0
            print("\nWarning: The intensity value is not between 0 and 255.")
            print("Please enter a number between 0 and 255.\n")

    # Function to make the LED blink with a certain delay between the blinks <- this function is new
    def start_blink_light(self):
        while True:
            self.set_intensity(255)
            sleep(0.5)
            self.set_intensity(0)
            sleep(1)

    # Function to stop the blinking
    def stop_blink_light(self):
        self.switch_off()
        self.clean_up_pin(self.pin)

    # Function to turn off the pwm_object
    def switch_off(self):
        self.pwm_object.stop()
        GPIO.output(self.pin, False)

    # Change certain pin to input
    @staticmethod
    def clean_up_pin(pin):
        GPIO.cleanup(pin)
        print(f"\nCleaned pin {pin}.")

    # Change all outputs to inputs
    @staticmethod
    def clean_up_gpio():
        GPIO.cleanup()
        print(f"\nChanged all pins to IN.")
