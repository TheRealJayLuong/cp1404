"""Dynamically  create labels on Grid layout"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class DynamicLabels(GridLayout):
    """Main program dynamic labels creation"""
    def __init__(self, **kwargs):
        """Construct main app"""
        super(DynamicLabels, self).__init__(**kwargs)

        self.rows = 3
        self.add_widget(Label(text="First name: Phong"))
        self.add_widget(Label(text="Middle name: Quoc"))
        self.add_widget(Label(text="Last name: Luong"))


class MyApp(App):
    """Build kivy GUI and title"""
    def build(self):
        self.title = "Dynamic Label"
        return DynamicLabels()


if __name__ == '__main__':
    MyApp().run()
