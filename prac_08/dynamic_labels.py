"""
CP1404/CP5632 Practical 8
Kivy GUI program to create dynamic labels
Zhao Changlin
Started 04/09/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Kivy App tp create dynamic labels."""
    # status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct the app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Charlie Hustle"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()
