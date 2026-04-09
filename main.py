from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random

class WingoPredictor(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # টাইটেল
        self.label = Label(text="WIN GO PREDICTOR", font_size='25sp', color=(1, 1, 0, 1))
        
        # ইনপুট বক্স (পিরিয়ড নম্বর দেওয়ার জন্য)
        self.period_input = TextInput(hint_text="Enter last 3 digits of period", multiline=False, input_filter='int', font_size='20sp')
        
        # প্রেডিকশন বাটন
        self.btn = Button(text="GET PREDICTION", background_color=(0, 0.7, 1, 1), font_size='20sp')
        self.btn.bind(on_press=self.predict)
        
        # রেজাল্ট দেখানোর জায়গা
        self.result_label = Label(text="Result: --", font_size='30sp', bold=True)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.period_input)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.result_label)
        
        return self.layout

    def predict(self, instance):
        if self.period_input.text:
            val = int(self.period_input.text)
            # একটি গাণিতিক লজিক (যাতে এটি র্যান্ডম মনে না হয়)
            if (val + 7) % 2 == 0:
                self.result_label.text = "Result: BIG"
                self.result_label.color = (0, 1, 0, 1) # Green
            else:
                self.result_label.text = "Result: SMALL"
                self.result_label.color = (1, 0, 0, 1) # Red
        else:
            self.result_label.text = "Enter Period!"

if __name__ == "__main__":
    WingoPredictor().run()
