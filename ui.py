from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.graphics import Color
from kivy.properties import DictProperty
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown

from theory import TheoryUtil


class GlobalSelectedStatus:
    scale_root = "C"
    scale_pattern = "natural_maj"
    chord_root = "C"
    chord_pattern = "X"
    chord_bass = "C"


class GlobalSetting:
    background_color = get_color_from_hex("#838B8B")
    nice_btn_color = get_color_from_hex("#CD5B45")
    btn_color = get_color_from_hex("#CDC1C5")
    selected_color = get_color_from_hex("#4876FF")


class UiContainer(GridLayout):
    Builder.load_file("container.kv")

    def __init__(self, left_padding=10, up_padding=10, right_padding=10, down_padding=10, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)
        self.cols = 1
        self.rows = 1
        self.padding = [left_padding, up_padding, right_padding, down_padding]


class UiPianoX3(FloatLayout):
    Builder.load_file("piano_x3.kv")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)


class UiPianoX1(FloatLayout):
    Builder.load_file("piano_x1.kv")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)

    def change(self):
        # for test
        self.ids.note_c1.background_color = get_color_from_hex("#7EC0EE")
        self.ids.note_ds1.background_color = get_color_from_hex("#7EC0EE")
        self.ids.note_g1.background_color = get_color_from_hex("#7EC0EE")
        self.ids.note_b1.background_color = get_color_from_hex("#7EC0EE")


class UiScaleNoteList(GridLayout):
    Builder.load_file("ui.kv")

    default_colors = DictProperty({})

    def __init__(self, nice_notes, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)
        self.cols = 1
        for note in TheoryUtil.note_lst:
            nice_btn = False
            if note in nice_notes:
                nice_btn = True
            map = {}
            if "/" not in note:
                map["id"] = note.lower()
                map["show"] = note
            else:
                for s_note in note.split("/"):
                    if "#" in s_note:
                        map["id"] = s_note.replace("#", "s").lower()
                    if "b" in s_note:
                        map["show"] = s_note
            btn = Button(text=map["show"], background_normal="", on_press=self.press)
            btn.background_color = GlobalSetting.btn_color
            if nice_btn:
                btn.background_color = GlobalSetting.nice_btn_color
            self.ids[f"note_{map['id']}"] = btn
            self.default_colors[f"note_{map['id']}"] = btn.background_color

            btn_container = UiContainer(10, 10, 10, 10)
            btn_container.add_widget(btn)
            self.add_widget(btn_container)

    def press(self, instance):
        for btn_id, btn in self.ids.items():
            btn.background_color = self.default_colors[btn_id]
        instance.background_color = GlobalSetting.selected_color
        GlobalSelectedStatus.chord_root = instance.text


class UiBassNoteList(GridLayout):
    Builder.load_file("ui.kv")

    default_colors = DictProperty({})

    def __init__(self, nice_notes, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)
        self.cols = 1
        for note in TheoryUtil.note_lst:
            nice_btn = False
            if note in nice_notes:
                nice_btn = True
            map = {}
            if "/" not in note:
                map["id"] = note.lower()
                map["show"] = note
            else:
                for s_note in note.split("/"):
                    if "#" in s_note:
                        map["id"] = s_note.replace("#", "s").lower()
                    if "b" in s_note:
                        map["show"] = s_note
            btn = Button(text=map["show"], background_normal="", on_press=self.press)
            btn.background_color = GlobalSetting.btn_color
            if nice_btn:
                btn.background_color = GlobalSetting.nice_btn_color
            self.ids[f"note_{map['id']}"] = btn
            self.default_colors[f"note_{map['id']}"] = btn.background_color

            btn_container = UiContainer(10, 10, 10, 10)
            btn_container.add_widget(btn)
            self.add_widget(btn_container)

    def press(self, instance):
        for btn_id, btn in self.ids.items():
            btn.background_color = self.default_colors[btn_id]
        instance.background_color = GlobalSetting.selected_color
        GlobalSelectedStatus.chord_bass = instance.text


class UiChordList(GridLayout):
    Builder.load_file("ui.kv")

    def __init__(self, cols, nice_notes, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)
        self.cols = cols
        # todo for chords
        for note in TheoryUtil.note_lst:
            nice_btn = False
            if note in nice_notes:
                nice_btn = True
            map = {}
            if "/" not in note:
                map["id"] = note.lower()
                map["show"] = note
            else:
                for s_note in note.split("/"):
                    if "#" in s_note:
                        map["id"] = s_note.replace("#", "s").lower()
                    if "b" in s_note:
                        map["show"] = s_note
            btn = Button(text=map["show"], background_normal="", on_press=self.press)
            btn.background_color = GlobalSetting.btn_color
            if nice_btn:
                btn.background_color = GlobalSetting.nice_btn_color
            self.ids[f"chord_{map['id']}"] = btn
            self.default_colors[f"chord_{map['id']}"] = btn.background_color

            btn_container = UiContainer(10, 10, 10, 10)
            btn_container.add_widget(btn)
            self.add_widget(btn_container)

    def press(self, instance):
        for btn_id, btn in self.ids.items():
            btn.background_color = self.default_colors[btn_id]
        instance.background_color = GlobalSetting.selected_color
        GlobalSelectedStatus.chord_bass = GlobalSelectedStatus.chord_root
        GlobalSelectedStatus.chord_pattern = instance.text.replace(GlobalSelectedStatus.chord_root, "X")


class UiScaleSelector(GridLayout):
    Builder.load_file("scale_selector.kv")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)
        self.cols = 4
        label_note = Label(text="root")
        # label_note.size_hint = [0.15, 1]
        # label_note.pos_hint = {"x":0, "y": 0}
        self.add_widget(label_note)
        # todo drop
        note_drop = DropDown()
        for note in TheoryUtil.note_lst:
            note_name = ""
            if "/" not in note:
                note_name = note
            else:
                for s_note in note.split("/"):
                    if "b"in s_note:
                        note_name = s_note
            if note_name:
                btn = Button(text=note_name, size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: note_drop.select(btn.text))
                note_drop.add_widget(btn)
        note_drop_main_btn = Button(text="C", size_hint=(None, None))
        note_drop_main_btn.bind(on_release=note_drop.open)
        note_drop.bind(on_select=lambda instance, x: setattr(note_drop_main_btn, "text", x))
        note_drop_main_btn.size_hint = [0.2, 0.2]
        note_drop_main_btn.pos_hint = {"x": 0.15, "y": 0}
        self.add_widget(note_drop_main_btn)


class RChordApp(App):
    def build(self):
        return UiScaleSelector()


if __name__ == "__main__":
    RChordApp().run()
