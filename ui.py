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

from theory import Theory


class GlobalState:
    scale_root = "C"
    scale_pattern = "Natural Maj"
    chord_root = "C"
    chord_pattern = "X"
    chord_bass = "C"


class GlobalSetting:
    background_color = get_color_from_hex("#838B8B")
    nice_btn_color = get_color_from_hex("#CD5B45")
    btn_color = get_color_from_hex("#8B8386")
    selected_color = get_color_from_hex("#4876FF")


class UiContainer(GridLayout):
    Builder.load_file("ui.kv")

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


class UiChordRootNoteList(GridLayout):
    Builder.load_file("ui.kv")

    default_colors = DictProperty({})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)
        self.cols = 1
        scale_note = GlobalState.scale_root
        scale_pattern = GlobalState.scale_pattern
        note_start = Theory.note_lst_x3.index(scale_note)
        loop_notes = Theory.note_lst_x3[note_start:note_start+12]
        nice_notes = Theory.make_scale(f"{scale_note}/{scale_pattern}")[1]
        for note in loop_notes:
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
        GlobalState.chord_root = instance.text


class UiChordBassNoteList(GridLayout):
    Builder.load_file("ui.kv")

    default_colors = DictProperty({})

    def __init__(self, nice_notes, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)
        self.cols = 1
        for note in Theory.note_lst:
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
        GlobalState.chord_bass = instance.text


class UiChordList(GridLayout):
    Builder.load_file("ui.kv")

    def __init__(self, cols, nice_notes, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)
        self.cols = cols
        # todo for chords
        for note in Theory.note_lst:
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
        GlobalState.chord_bass = GlobalState.chord_root
        GlobalState.chord_pattern = instance.text.replace(GlobalState.chord_root, "X")


class UiChordSelectorPage(FloatLayout):
    Builder.load_file("ui.kv")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(GlobalSetting.background_color)

        # Init Button
        init_btn = Button(text="init", background_normal="")
        init_btn.bind(on_release=self.act_init_release)
        init_btn.background_color = GlobalSetting.btn_color
        init_btn.size_hint = [0.05, 0.05]
        init_btn.pos_hint = {"x": 0, "y": 0.95}
        self.add_widget(init_btn)

        # Select Scale Root
        note_drop = DropDown()
        for note in Theory.note_lst:
            note_name = ""
            if "/" not in note:
                note_name = note
            else:
                for s_note in note.split("/"):
                    if "b" in s_note:
                        note_name = s_note
            if note_name:
                btn = Button(text=note_name, size_hint_y=None, height=30)
                btn.bind(on_release=lambda btn: note_drop.select(btn.text))
                note_drop.add_widget(btn)
        note_drop_main_btn = Button(text=GlobalState.scale_root, size_hint=(None, None))
        note_drop_main_btn.bind(on_release=note_drop.open)
        note_drop.bind(on_select=self.act_note_drop_on_select)
        note_drop_main_btn.size_hint = [0.05, 0.05]
        note_drop_main_btn.pos_hint = {"x": 0.1, "y": 0.95}
        self.ids.note_drop = note_drop
        self.ids.note_drop_main_btn = note_drop_main_btn
        self.add_widget(note_drop_main_btn)

        # Select Scale Pattern
        scale_drop = DropDown()
        for scale_name in Theory.scale_map.keys():
            btn = Button(text=scale_name, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: scale_drop.select(btn.text))
            scale_drop.add_widget(btn)
        scale_drop_main_btn = Button(text=GlobalState.scale_pattern, size_hint=(None, None))
        scale_drop_main_btn.bind(on_release=scale_drop.open)
        scale_drop.bind(on_select=lambda instance, x: setattr(scale_drop_main_btn, "text", x))
        scale_drop_main_btn.size_hint = [0.2, 0.05]
        scale_drop_main_btn.pos_hint = {"x": 0.15, "y": 0.95}
        self.ids.scale_drop = scale_drop
        self.ids.scale_drop_main_btn = scale_drop_main_btn
        self.add_widget(scale_drop_main_btn)

        # Chord root list
        self.ui_refresh_chord_root_list()

    def ui_refresh_chord_root_list(self):
        chord_root_list = UiChordRootNoteList()
        chord_root_list.size_hint = [0.05, 0.7]
        chord_root_list.pos_hint = {"x": 0, "y": 0.25}
        self.ids.chord_root_list = chord_root_list
        self.add_widget(chord_root_list)

    def act_init_release(self, instance):
        print("init")

    def act_note_drop_on_select(self, instance, val):
        self.ids.note_drop_main_btn.text = val
        GlobalState.scale_root = val

    def act_scale_drop_on_select(self, instance, val):
        self.ids.scale_drop_main_btn.text = val
        GlobalState.scale_pattern = val


class RChordApp(App):
    def build(self):
        return UiChordSelectorPage()


if __name__ == "__main__":
    RChordApp().run()
