from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random

class FakeBookingApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text="Salon Booking (Demo)", font_size=24))

        self.add_widget(Label(text="Enter Name:"))
        self.name_input = TextInput(multiline=False)
        self.add_widget(self.name_input)

        self.add_widget(Label(text="Select Service:"))
        self.service_input = TextInput(multiline=False, hint_text="e.g., Haircut, Massage")
        self.add_widget(self.service_input)

        self.book_button = Button(text="Book Now", font_size=18, background_color=(0, 0.5, 1, 1))
        self.book_button.bind(on_press=self.fake_booking)
        self.add_widget(self.book_button)

        self.response_label = Label(text="")
        self.add_widget(self.response_label)

    def fake_booking(self, instance):
        responses = [
            "✅ Booking confirmed!",
            "⚠️ No slots available. Try another time.",
            "✅ Your appointment is set. See you soon!"
        ]
        self.response_label.text = random.choice(responses)

class SalonApp(App):
    def build(self):
        return FakeBookingApp()

if __name__ == "__main__":
    SalonApp().run()
