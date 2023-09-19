"""
CP1404/CP5632 Practical 8
Kivy GUI program to convert miles to kilometers
Zhao Changlin
Started 04/09/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

# from kivy.properties import StringProperty

MILE_TO_KILOMETER_RATIO = 1.609344


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy App for converting miles to kilometers."""

    # output = StringProperty()

    def build(self):
        """Build the Kivy app from convert_miles_km.kv."""
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Convert miles to km."""
        mile = self.validate_input()
        kilometer = mile * MILE_TO_KILOMETER_RATIO
        self.root.ids.output_label.text = str(kilometer)

    def handle_increment(self, increment):
        """Increment the value."""
        mile = self.validate_input() + increment
        self.root.ids.input_mile.text = str(mile)
        self.handle_convert()

    def validate_input(self):
        """Validate the input mile."""
        try:
            mile = float(self.root.ids.input_mile.text)
            return mile
        except ValueError:
            return 0


ConvertMilesToKmApp().run()
