import platform
from tkinter import *
from tkinter import ttk

if platform.system() == "Darwin":
    from tkmacosx import *

from theory import Theory


class GlobalState:
    scale_root = "C"
    scale_pattern = "Natural Maj"
    chord_root = "C"
    chord_pattern = "X"
    chord_bass = "C"


class GlobalSetting:
    lan = "zh"
    # background_color = "gray"
    # nice_btn_color = "pink"
    # btn_color = "white"
    # selected_color = "blue"


class ChordRootNoteList(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "和弦根音" if GlobalSetting.lan == "zh" else "Chord Root"
        Button(self, text=col_name, bg="gray").pack(side=TOP, fill=BOTH, expand=YES)

        for i in range(12):
            btn = Button(self)
            btn.pack(side=TOP, fill=BOTH, expand=YES)
            btn.bind("<Button-1>", self.left_click)
            setattr(self, f"root_note_{i}", btn)
        self.refresh()

    def refresh(self):
        scale_root_index = Theory.note_lst_x3.index(GlobalState.scale_root)
        nice_notes = Theory.make_scale(f"{GlobalState.scale_root}/{GlobalState.scale_pattern}")[1]
        note_list = Theory.note_lst_x3[scale_root_index:scale_root_index + 12]
        for i in range(12):
            btn = getattr(self, f"root_note_{i}")
            btn.configure(bg="white", fg="black")
            note = note_list[i]
            if note in nice_notes:
                btn.configure(bg="pink", fg="black")
            note = note.split("/")[0]
            if note == GlobalState.chord_root:
                btn.configure(bg="blue", fg="white")
            btn.configure(text=note)

    def left_click(self, event):
        note = event.widget.cnf.get("text")
        GlobalState.chord_root = note
        GlobalState.chord_bass = note
        app.state_info.refresh()
        self.refresh()


class ChordBaseNoteList(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "和弦贝斯" if GlobalSetting.lan == "zh" else "Chord Bass"
        Button(self, text=col_name, bg="gray").pack(side=TOP, fill=BOTH, expand=YES)

        for i in range(12):
            btn = Button(self)
            btn.pack(side=TOP, fill=BOTH, expand=YES)
            setattr(self, f"bass_note_{i}", btn)

        self.refresh()

    def refresh(self):
        scale_root_index = Theory.note_lst_x3.index(GlobalState.scale_root)
        nice_notes = Theory.make_chord(GlobalState.chord_pattern.replace("X", GlobalState.chord_root))[1]
        note_list = Theory.note_lst_x3[scale_root_index:scale_root_index + 12]
        for i in range(12):
            btn = getattr(self, f"bass_note_{i}")
            note = note_list[i]
            btn.configure(bg="white", fg="black")
            if note in nice_notes:
                btn.configure(bg="pink", fg="black")
            note = note.split("/")[0]
            if note == GlobalState.chord_bass:
                btn.configure(bg="blue", fg="white")
            btn.configure(text=note)


class ChordList(Frame):
    def __init__(self, cols, **kwargs):
        super().__init__(**kwargs)
        for i in range(len(Theory.chord_map)):
            btn = Button(self)
            btn.grid(column=i % cols, row=int(i / cols))
            setattr(self, f"chord_{i}", btn)

        self.refresh()

    def refresh(self):
        for i in range(len(Theory.chord_map)):
            btn = getattr(self, f"chord_{i}")
            btn.configure(text=list(Theory.chord_map.keys())[i].replace("X", GlobalState.chord_root))


class Piano(Frame):

    def __init__(self, oct_num, **kwargs):
        super().__init__(**kwargs)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        for col_index in range(oct_num * 14):
            self.columnconfigure(col_index, weight=1)
        for oct_index in range(oct_num):
            for note_index, note in enumerate(Theory.note_lst[:5]):
                shift = 14 * oct_index
                if note_index % 2 == 0:
                    note = f'{note}{oct_index}'
                    btn = Button(self, text="", bg="white", fg="black")
                    setattr(self, note, btn)
                    btn.grid(row=1, column=note_index + shift, columnspan=2, sticky="nesw", padx=1, pady=1)
                else:
                    note = note.split('/')[0]
                    note = f'{note}{oct_index}'
                    btn = Button(self, text="", bg="black", fg="white")
                    setattr(self, note, btn)
                    btn.grid(row=0, column=note_index + shift, columnspan=2, sticky="nesw", padx=1, pady=1)

            for note_index, note in enumerate(Theory.note_lst[5:12]):
                shift = 14 * oct_index + 6
                if note_index % 2 == 0:
                    note = f'{note}{oct_index}'
                    btn = Button(self, text="", bg="white", fg="black")
                    setattr(self, note, btn)
                    btn.grid(row=1, column=note_index + shift, columnspan=2, sticky="nesw", padx=1, pady=1)
                else:
                    note = note.split('/')[0]
                    note = f'{note}{oct_index}'
                    btn = Button(self, text="", bg="black", fg="white")
                    setattr(self, note, btn)
                    btn.grid(row=0, column=note_index + shift, columnspan=2, sticky="nesw", padx=1, pady=1)


class SelectMainScaleUi(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label_context = "主音" if GlobalSetting.lan == "zh" else "Main Note"
        Label(self, text=label_context).pack(side=LEFT)
        self.drop_down_note = ttk.Combobox(self)
        note_list = tuple([x[0] for x in Theory.note_lst])
        self.drop_down_note["value"] = note_list
        self.drop_down_note.bind("<<ComboboxSelected>>", self.select_note)
        self.drop_down_note.pack(side=LEFT, fill=BOTH, expand=YES)

        label_context = "音阶" if GlobalSetting.lan == "zh" else "Main Scale"
        Label(self, text=label_context).pack(side=LEFT)

        self.drop_down_scale = ttk.Combobox(self)
        scale_list = tuple([x["zh"] for x in Theory.scale_map.values()]) if GlobalSetting.lan == "zh" \
            else tuple([x["en"] for x in Theory.scale_map.values()])
        self.drop_down_scale["value"] = scale_list
        self.drop_down_scale.bind("<<ComboboxSelected>>", self.select_scale)
        self.drop_down_scale.pack(side=LEFT, fill=BOTH, expand=YES)

        self.refresh()

    def refresh(self):
        self.drop_down_note.current(Theory.note_lst.index(GlobalState.scale_root))
        self.drop_down_scale.current(list(Theory.scale_map.keys()).index(GlobalState.scale_pattern))

    def select_note(self, event):
        GlobalState.scale_root = self.drop_down_note.get()
        app.chord_root_note_list.refresh()
        app.chord_bass_note_list.refresh()

    def select_scale(self, event):
        GlobalState.scale_pattern = Theory.find_scale_tag_by_scale_name(self.drop_down_scale.get(), GlobalSetting.lan)
        app.chord_root_note_list.refresh()
        app.chord_bass_note_list.refresh()


class StateInfoUi(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.scale_pattern_label = Label(self)
        self.scale_pattern_label.pack(side=LEFT, fill=BOTH, expand=YES)

        self.scale_note_label = Label(self)
        self.scale_note_label.pack(side=LEFT, fill=BOTH, expand=YES)

        self.scale_chord_label = Label(self)
        self.scale_chord_label.pack(side=LEFT, fill=BOTH, expand=YES)

        self.scale_voicing_label = Label(self)
        self.scale_voicing_label.pack(side=LEFT, fill=BOTH, expand=YES)

        self.refresh()

    def refresh(self):
        label_context = "模式: " if GlobalSetting.lan == "zh" else "Pattern: "
        self.scale_pattern_label.configure(text=label_context + Theory.scale_map[GlobalState.scale_pattern]["pattern"])

        label_context = "音名: " if GlobalSetting.lan == "zh" else "Notes: "
        notes = ",".join(Theory.make_scale(f"{GlobalState.scale_root}/{GlobalState.scale_pattern}")[0])
        self.scale_note_label.configure(text=label_context + notes)

        label_context = "和弦: " if GlobalSetting.lan == "zh" else "Chord: "
        chord = GlobalState.chord_pattern.replace("X", GlobalState.chord_root)
        if GlobalState.chord_bass != GlobalState.chord_root:
            chord = chord + "/" + GlobalState.chord_bass
        self.scale_chord_label.configure(text=label_context + chord)

        label_context = "排列: " if GlobalSetting.lan == "zh" else "Voicing: "
        chord = GlobalState.chord_pattern.replace("X", GlobalState.chord_root)
        voicing = ','.join(Theory.make_chord(chord)[0])
        if GlobalState.chord_bass != GlobalState.chord_root:
            voicing = GlobalState.chord_bass + "," + voicing
        self.scale_voicing_label.configure(text=label_context + voicing)


class App:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.app = Tk()
        self.app.title('rChord')
        self.app.geometry("600x450+800+400")
        self.build()

    def build(self):
        self.select_main_scale = SelectMainScaleUi()
        self.select_main_scale.master = self.app
        self.select_main_scale.pack(side=TOP, fill=BOTH, expand=False)

        self.state_info = StateInfoUi()
        self.state_info.master = self.app
        self.state_info.pack(side=TOP, fill=BOTH, expand=False)

        self.piano_aux_scale = Piano(3, bg="gray")
        self.piano_aux_scale.master = self.app
        self.piano_aux_scale.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.piano_chord = Piano(3, bg="white")
        self.piano_chord.master = self.app
        self.piano_chord.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.chord_root_note_list = ChordRootNoteList()
        self.chord_root_note_list.master = self.app
        self.chord_root_note_list.pack(side=LEFT, fill=BOTH, expand=True)

        self.chord_list = ChordList(5)
        self.chord_list.master = self.app
        self.chord_list.pack(side=LEFT, fill=BOTH, expand=True)

        self.chord_bass_note_list = ChordBaseNoteList()
        self.chord_bass_note_list.master = self.app
        self.chord_bass_note_list.pack(side=LEFT, fill=BOTH, expand=True)

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
