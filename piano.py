from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from theory import TheoryUtil


class UiPianoX3Widget(FloatLayout):
    Builder.load_file("piano_x3.kv")


class UiPianoX1Widget(FloatLayout):
    Builder.load_file("piano_x1.kv")

    def change(self):
        # for test
        self.ids.note_c1.background_color = get_color_from_hex("#7EC0EE")
        self.ids.note_ds1.background_color = get_color_from_hex("#7EC0EE")
        self.ids.note_g1.background_color = get_color_from_hex("#7EC0EE")
        self.ids.note_b1.background_color = get_color_from_hex("#7EC0EE")


class UiNoteList(GridLayout):
    Builder.load_file("notes.kv")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for note in TheoryUtil.note_lst:
            self.add_widget(Button(text=note))


class RChordApp(App):
    def build(self):
        return UiNoteList()


if __name__ == "__main__":
    RChordApp().run()
