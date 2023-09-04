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

    def handle_convert(self, mile):
        """Convert miles to km."""
        try:
            kilometer = float(mile) * MILE_TO_KILOMETER_RATIO
            self.root.ids.output_label.text = str(kilometer)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, mile, increment):
        """Increment the value."""
        try:
            mile = float(mile) + increment
            self.root.ids.input_mile.text = str(mile)
        except ValueError:
            self.root.ids.input_mile.text = str(increment)


ConvertMilesToKmApp().run()
