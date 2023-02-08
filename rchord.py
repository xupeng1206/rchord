import platform
from tkinter import *
from tkinter import ttk

if platform.system() == "Darwin":
    from tkmacosx import *


def r_set_text(self, text):
    self.r_text = text


def r_get_text(self):
    return getattr(self, "r_text")


setattr(Button, "r_set_text", r_set_text)
setattr(Button, "r_get_text", r_get_text)


class Theory:
    note_letters = "CDEFGAB" * 3
    note_lst = ["C", "Db/C#", "D", "Eb/D#", "E", "F", "Gb/F#", "G", "Ab/G#", "A", "Bb/A#", "B"]
    note_lst_x3 = note_lst * 3

    simple_note_lst = ["1", "b2/#1", "2", "b3/#2", "3", "4", "b5/#4", "5", "b6/#5", "6", "b7/#6", "7"] + \
                      ["-", "b9", "9", "#9", "-", "11", "#11", "-", "b13", "13", "-", "-"]

    chord_map = {
        "X": "1,3,5",
        "Xm": "1,b3,5",
        "Xaug": "1,3,#5",
        "Xdim": "1,b3,b5",
        "Xsus4": "1,4,5",
        "Xsus2": "1,2,5",
        "X6": "1,3,5,6",
        "Xm6": "1,b3,5,6",
        "XM7": "1,3,5,7",
        "XmM7": "1,b3,5,7",
        "X7": "1,3,5,b7",
        "X7sus4": "1,4,5,b7",
        "X7b9": "1,3,5,b7,b9",
        "X7#9": "1,3,5,b7,#9",
        "X7#11": "1,3,5,b7,#11",
        "X7b13": "1,3,5,b7,b13",
        "X7b9#9": "1,3,5,b7,b9,#9",
        "X7b9#11": "1,3,5,b7,b9,#11",
        "X7b9b13": "1,3,5,b7,b9,b13",
        "X7#9#11": "1,3,5,b7,#9,#11",
        "X7#9b13": "1,3,5,b7,#9,b13",
        "X7#11b13": "1,3,5,b7,#11,b13",
        "X7b9#9#11": "1,3,5,b7,b9,#9,#11",
        "X7b9#9b13": "1,3,5,b7,b9,#9,b13",
        "X7b9#11b13": "1,3,5,b7,b9,#11,b13",
        "X7#9#11b13": "1,3,5,b7,#9,#11,b13",
        "X7b9#9#11b13": "1,3,5,b7,b9,#9,#11,b13",
        "Xm7": "1,b3,5,b7",
        "Xm7b5": "1,b3,b5,b7",
        "Xdim7": "1,b3,b5,6",
        "Xaug7": "1,3,#5,7",
        "X69": "1,3,5,6,9",
        "Xm69": "1,b3,5,6,9",
        "Xadd9": "1,3,5,9",
        "XM9": "1,3,5,7,9",
        "XmM9": "1,b3,5,7,9",
        "X9": "1,3,5,b7,9",
        "X9sus4": "1,4,5,b7,9",
        "Xm9": "1,b3,5,b7,9",
        "Xm9b5": "1,b3,b5,b7,9",
        "Xaug9": "1,3,#5,b7,9",
        "XaugM9": "1,3,#5,7,9",
        "Xdim9": "1,b3,b5,6,9",
        "X11": "1,3,5,b7,9,11",
        "Xm11": "1,b3,5,b7,9,11",
        "X13": "1,3,5,b7,9,11,13",
    }

    scale_map = {
        "Natural Maj": {"pattern": "1,2,3,4,5,6,7", "zh": "自然大调", "en": "Natural Maj"},
        "Harmonic Maj": {"pattern": "1,2,3,4,5,b6,7", "zh": "和声大调", "en": "Harmonic Maj"},
        "Melodic Maj": {"pattern": "1,2,3,4,5,b6,b7", "zh": "旋律大调", "en": "Melodic Maj"},
        "Natural Min": {"pattern": "1,2,b3,4,5,b6,b7", "zh": "自然小调", "en": "Natural Min"},
        "Harmonic Min": {"pattern": "1,2,b3,4,5,b6,7", "zh": "和声小调", "en": "Harmonic Min"},
        "Melodic Min": {"pattern": "1,2,b3,4,5,6,7", "zh": "旋律小调", "en": "Melodic Min"},
        "Ionian": {"pattern": "1,2,3,4,5,6,7", "zh": "伊奥尼亚", "en": "Ionian"},
        "Dorian": {"pattern": "1,2,b3,4,5,6,b7", "zh": "多利亚", "en": "Dorian"},
        "Phrygian": {"pattern": "1,b2,b3,4,5,b6,b7", "zh": "弗里几亚", "en": "Phrygian"},
        "Lydian": {"pattern": "1,2,3,#4,5,6,7", "zh": "利底亚", "en": "Lydian"},
        "Mixolydian": {"pattern": "1,2,3,4,5,6,b7", "zh": "混合利底亚", "en": "Mixolydian"},
        "Aeolian": {"pattern": "1,2,b3,4,5,b6,b7", "zh": "爱奥尼亚", "en": "Aeolian"},
        "Locrian": {"pattern": "1,b2,b3,4,b5,b6,b7", "zh": "洛克里亚", "en": "Locrian"},
        "Whole Half Dim": {"pattern": "1,2,b3,4,b5,b6,6,7", "zh": "全半减音阶", "en": "Whole Half Dim"},
        "Half Whole Dim": {"pattern": "1,b2,b3,3,b5,5,6,b7", "zh": "半全减音阶", "en": "Half Whole Dim"},
        "Diatonic": {"pattern": "1,2,3,#4,#5,#6", "zh": "全音阶", "en": "Diatonic"},
        "Blues": {"pattern": "1,b3,4,b5,5,b7", "zh": "布鲁斯", "en": "Blues"},
        "Mix Blues": {"pattern": "1,b3,3,4,b5,5,b7", "zh": "混合布鲁斯", "en": "Mix Blues"},
        "Aux Blues": {"pattern": "1,2,b3,3,4,#4,5,6,b7", "zh": "辅助布鲁斯", "en": "Aux Blues"},
        "Jazz Min": {"pattern": "1,2,b3,4,5,6,7", "zh": "爵士小音阶", "en": "Jazz Min"},
        "Blues Maj": {"pattern": "1,2,b3,4,b5,b6,7", "zh": "蓝调大音阶", "en": "Blues Maj"},
        "Phrygian Dominant": {"pattern": "1,b2,3,4,5,b6,b7", "zh": "大弗里几亚", "en": "Phrygian Dominant"},
        "Lydian Dominant": {"pattern": "1,2,3,#4,5,6,b7", "zh": "大利底亚", "en": "Lydian Dominant"},
        "Super Locrian": {"pattern": "1,b2,b3,3,b5,b6,b7", "zh": "超级洛克里亚", "en": "Super Locrian"},
        "Gypsy": {"pattern": "1,b3,#4,5,b6,b7", "zh": "吉普赛音阶", "en": "Gypsy"},
        "Hungarian Maj": {"pattern": "1,#2,3,#4,5,6,b7", "zh": "匈牙利大音阶", "en": "Hungarian Maj"},
        "Hungarian Min": {"pattern": "1,2,b3,#4,5,b6,7", "zh": "匈牙利小音阶", "en": "Hungarian Min"},
        "Bibop": {"pattern": "1,2,3,4,5,6,b7,7", "zh": "比波普属音阶", "en": "Bibop"},
        "India": {"pattern": "1,2,3,4,5,b6,b7", "zh": "印度音阶", "en": "India"},
        "Jap": {"pattern": "1,3,4,6,7", "zh": "日本音阶", "en": "Jap"},
        "Russia": {"pattern": "1,b2,2,b3,4,5,b6,6,b7,7", "zh": "俄罗斯音阶", "en": "Russia"},
        "Arabian": {"pattern": "1,b2,3,4,5,b6,b7", "zh": "阿拉伯音阶", "en": "Arabian"},
        "Oriental": {"pattern": "1,b2,3,4,b5,6,b7", "zh": "东方音阶", "en": "Oriental"},
        "Spanish": {"pattern": "1,b2,b3,3,4,b5,b6,b7", "zh": "西班牙音阶", "en": "Spanish"},
    }

    @classmethod
    def find_scale_tag_by_scale_name(cls, name, lan):
        for k, v in cls.scale_map.items():
            if v[lan] == name:
                return k

    @classmethod
    def make_chord(cls, chord_name):
        if len(chord_name) >= 2 and chord_name[1] in "b#":
            root = chord_name[:2]
            chord_tag = "X" + chord_name[2:]
            if chord_tag not in cls.chord_map:
                raise Exception("chord not support.")
            return cls.parse(root, cls.chord_map[chord_tag])
        else:
            root = chord_name[0]
            chord_tag = "X" + chord_name[1:]
            if chord_tag not in cls.chord_map:
                raise Exception("chord not support.")
            return cls.parse(root, cls.chord_map[chord_tag])

    @classmethod
    def make_scale(cls, scale_name):
        # scale_tag example: D#/blues
        root, tag = scale_name.split("/")
        if tag not in cls.scale_map:
            raise Exception("scale not support.")
        return cls.parse(root, cls.scale_map[tag]["pattern"])

    @classmethod
    def chord_in_scale(cls, chord_name, scale_name):
        chord = cls.make_chord(chord_name)
        scale = cls.make_scale(scale_name)
        return all([bool(x in scale[1]) for x in chord[1]])

    @classmethod
    def find_scales_by_chord(cls, chord_name):
        chord = cls.make_chord(chord_name)
        scales = []
        for notes in cls.note_lst:
            for note in notes.split("/"):
                for tag, val in cls.scale_map.items():
                    tmp_scale = cls.make_scale(f"{note}/{tag}")
                    if all([bool(x in tmp_scale[1]) for x in chord[1]]):
                        scales.append(f"{note}/{tag}")
        return scales

    @classmethod
    def find_similar_chord(cls, chord_name):
        chord = cls.make_chord(chord_name)
        if len(chord[1]) > 4:
            return []
        ret = []
        similar_chords = {}
        for notes in cls.note_lst:
            for note in notes.split("/"):
                for chord_tag, chord_pattern in cls.chord_map.items():
                    if len(chord_pattern.split(",")) > 4:
                        continue
                    tmp_chord_name = chord_tag.replace("X", note)
                    if tmp_chord_name == chord_name:
                        continue
                    tmp_chord = cls.make_chord(tmp_chord_name)
                    same_notes = set(chord[1]) & set(tmp_chord[1])
                    if len(same_notes) < 2:
                        continue
                    if len(same_notes) not in similar_chords:
                        similar_chords[len(same_notes)] = []
                    similar_chords[len(same_notes)].append(tmp_chord_name)
        similar_chords = sorted(similar_chords.items(), key=lambda x: x[0])[::-1]
        for chords in similar_chords:
            ret = ret + chords[1]
        return ret

    @classmethod
    def note_index(cls, lst, target):
        for idx, ele in enumerate(lst):
            if target in ele.split("/"):
                return idx

    @classmethod
    def parse(cls, root, pattern):
        root_start = cls.note_index(cls.note_lst_x3, root)
        root_letter = root.strip("#b")
        root_letter_start = cls.note_letters.index(root_letter)
        ret_multi_notes = []
        ret_single_notes = []
        for s_note in pattern.split(","):
            note = cls.note_lst_x3[root_start + cls.note_index(cls.simple_note_lst, s_note)]
            ret_multi_notes.append(note)
            name = cls.note_letters[root_letter_start + int(s_note.strip("#b")) - 1]
            ret_note = note
            for n in note.split('/'):
                if n.strip("#b") == name:
                    ret_note = n
                    break
            ret_single_notes.append(ret_note)
        return ret_single_notes, ret_multi_notes


class GlobalStateClz:
    _scale_root = "C"
    _scale_pattern = "Natural Maj"
    _chord_root = "C"
    _chord_pattern = "X"
    _chord_bass = "C"
    _chord_default_voicing = "C,E,G"
    _chord_voicing = "C,E,G"

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def scale_root(self):
        return self._scale_root

    @scale_root.setter
    def scale_root(self, value):
        refresh = False
        if value != self._scale_root:
            refresh = True
        self._scale_root = value
        if refresh:
            app.refresh()

    @property
    def scale_pattern(self):
        return self._scale_pattern

    @scale_pattern.setter
    def scale_pattern(self, value):
        refresh = False
        if value != self._scale_pattern:
            refresh = True
        self._scale_pattern = value
        if refresh:
            app.refresh()

    @property
    def chord_root(self):
        return self._chord_root

    @chord_root.setter
    def chord_root(self, value):
        refresh = False
        if value != self._chord_root:
            refresh = True
        self._chord_root = value
        if refresh:
            self._chord_change()
            app.refresh()

    @property
    def chord_pattern(self):
        return self._chord_pattern

    @chord_pattern.setter
    def chord_pattern(self, value):
        refresh = False
        if value != self._chord_pattern:
            refresh = True
        self._chord_pattern = value
        if refresh:
            self._chord_change()
            app.refresh()

    @property
    def chord_voicing(self):
        return self._chord_voicing

    @chord_voicing.setter
    def chord_voicing(self, value):
        self._chord_voicing = value

    @property
    def chord_default_voicing(self):
        return self._chord_default_voicing

    # @chord_default_voicing.setter
    # def chord_default_voicing(self, value):
    #     self._chord_default_voicing = value

    @property
    def chord_bass(self):
        return self._chord_bass

    @chord_bass.setter
    def chord_bass(self, value):
        refresh = False
        if value != self._chord_bass:
            refresh = True
        self._chord_bass = value
        if refresh:
            app.refresh()

    def _chord_change(self):
        chord = self._chord_pattern.replace("X", self._chord_root)
        notes = Theory.make_chord(chord)[0]
        self._chord_voicing = ",".join(notes)
        self._chord_default_voicing = ",".join(notes)

    def play_main_piano(self):
        notes = [self._chord_bass] + self._chord_voicing.split("/")
        app.main_piano.play(notes)

    def play_aux_piano(self, notes):
        app.aux_piano.play(notes)


GlobalState = GlobalStateClz()


class GlobalSetting:
    lan = "zh"


class ChordRootNoteList(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "和弦根音" if GlobalSetting.lan == "zh" else "Chord Root"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        for i in range(12):
            btn = Button(self)
            btn.pack(side=TOP, fill=BOTH, expand=YES)
            btn.bind("<Button-1>", self.left_click)
            setattr(self, f"root_note_{i}", btn)
        self.refresh()

    def refresh(self):
        scale_root_index = Theory.note_index(Theory.note_lst_x3, GlobalState.scale_root)
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
            btn.r_set_text(note)

    def left_click(self, event):
        note = event.widget.r_get_text()
        GlobalState.chord_root = note
        GlobalState.chord_bass = note
        # todo play sound


class ChordBaseNoteList(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "和弦贝斯" if GlobalSetting.lan == "zh" else "Chord Bass"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        for i in range(12):
            btn = Button(self)
            btn.pack(side=TOP, fill=BOTH, expand=YES)
            btn.bind("<Button-1>", self.left_click)
            setattr(self, f"bass_note_{i}", btn)

        self.refresh()

    def refresh(self):
        scale_root_index = Theory.note_index(Theory.note_lst_x3, GlobalState.scale_root)
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
            btn.r_set_text(note)

    def left_click(self, event):
        note = event.widget.r_get_text()
        GlobalState.chord_bass = note
        # todo play sound


class ChordGrid(Frame):
    def __init__(self, cols, **kwargs):
        super().__init__(**kwargs)

        chord_num = len(Theory.chord_map)
        for col_index in range(cols):
            self.columnconfigure(col_index, weight=1)
        for row_index in range(int(chord_num / cols) + 1):
            self.rowconfigure(row_index, weight=1)

        for i in range(chord_num):
            btn = Button(self)
            btn.bind("<Button-1>", self.left_click)
            btn.grid(column=i % cols, row=int(i / cols), sticky="nesw")
            setattr(self, f"chord_{i}", btn)

        self.refresh()

    def refresh(self):
        nice_chords = []
        special_chords = []
        for tag in Theory.chord_map.keys():
            chord = tag.replace("X", GlobalState.chord_root)
            if Theory.chord_in_scale(chord, f"{GlobalState.scale_root}/{GlobalState.scale_pattern}"):
                nice_chords.append(chord)
            else:
                special_chords.append(chord)
        chords = nice_chords + special_chords
        for i in range(len(Theory.chord_map)):
            btn = getattr(self, f"chord_{i}")
            context = chords[i]
            if context in nice_chords:
                btn.configure(bg="pink", fg="black")
            if context in special_chords:
                btn.configure(bg="white", fg="black")
            if context == GlobalState.chord_pattern.replace("X", GlobalState.chord_root):
                btn.configure(bg="blue", fg="white")
            btn.configure(text=context)
            btn.r_set_text(context)

    def left_click(self, event):
        text = event.widget.r_get_text()
        GlobalState.chord_pattern = text.replace(GlobalState.chord_root, "X")
        # todo play sound


class ChordList(Frame):

    def __init__(self, cols, **kwargs):
        super().__init__(**kwargs)

        col_name = "和弦" if GlobalSetting.lan == "zh" else "Chord"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        self.chord_grid = ChordGrid(cols, master=self)
        self.chord_grid.master = self
        self.chord_grid.pack(side=TOP, fill=BOTH, expand=True)
        self.refresh()

    def refresh(self):
        self.chord_grid.refresh()


class ChordDetailVoicing(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "和弦排列:" if GlobalSetting.lan == "zh" else "Chord Voicing:"
        Label(self, text=col_name, bg="gray").pack(side=LEFT, fill=X)

        self.bass = Label(self, bg="gray")
        self.bass.pack(side=LEFT, fill=X, padx=5)

        self.voicing_entry = Entry(self)
        self.voicing_entry.pack(side=LEFT, fill=X, expand=True)

        context = "试听" if GlobalSetting.lan == "zh" else "Listen"
        self.listen_btn = Button(self, text=context)
        self.listen_btn.bind("<Button-1>", self.listen_btn_left_click)
        self.listen_btn.pack(side=LEFT, fill=X, expand=False)

    def refresh(self):
        self.bass.configure(text=GlobalState.chord_bass)
        self.voicing_entry.delete(0, len(self.voicing_entry.get()))
        self.voicing_entry.insert(0, GlobalState.chord_voicing)

    def listen_btn_left_click(self, event):
        voicing = self.voicing_entry.get()
        if set(voicing.split(',')) - set(GlobalState.chord_default_voicing.split(",")):
            # voicing error
            self.voicing_entry.delete(0, len(self.voicing_entry.get()))
            self.voicing_entry.insert(0, GlobalState.chord_voicing)
        else:
            GlobalState.chord_voicing = voicing
        # todo play sound


class ChordDetailAuxScales(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "辅助音阶" if GlobalSetting.lan == "zh" else "Aux Scales"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        self.aux_scale_list = Listbox(self)
        self.aux_scale_list.bind("<<ListboxSelect>>", self.aux_scale_list_select)
        self.aux_scale_list.pack(side=TOP, fill=BOTH, expand=True)

    def refresh(self):
        if self.aux_scale_list.size() > 0:
            self.aux_scale_list.delete(0, self.aux_scale_list.size())
        chord = GlobalState.chord_pattern.replace("X", GlobalState.chord_root)
        scales = Theory.find_scales_by_chord(chord)
        for idx, scale in enumerate(scales):
            note, tag = scale.split("/")
            self.aux_scale_list.insert(idx, f"{note} | {Theory.scale_map[tag][GlobalSetting.lan]}")

    def aux_scale_list_select(self, event):
        aux_scale = None
        try:
            index = self.aux_scale_list.curselection()
            aux_scale = self.aux_scale_list.get(index)
        except Exception:
            pass
        if aux_scale is None:
            return
        print(aux_scale)
        # todo play sound


class ChordDetailAuxChords(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "辅助和弦" if GlobalSetting.lan == "zh" else "Aux Chords"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        self.aux_chord_list = Listbox(self)
        self.aux_chord_list.bind("<<ListboxSelect>>", self.aux_chord_list_select)
        self.aux_chord_list.pack(side=TOP, fill=BOTH, expand=True)

    def refresh(self):
        if self.aux_chord_list.size() > 0:
            self.aux_chord_list.delete(0, self.aux_chord_list.size())
        target_chord = GlobalState.chord_pattern.replace("X", GlobalState.chord_root)
        chords = Theory.find_similar_chord(target_chord)
        for idx, chord in enumerate(chords):
            self.aux_chord_list.insert(idx, chord)

    def aux_chord_list_select(self, event):
        aux_chord = None
        try:
            index = self.aux_chord_list.curselection()
            aux_chord = self.aux_chord_list.get(index)
        except Exception:
            pass
        if aux_chord is None:
            return
        # todo play sound
        print(aux_chord)


class ChordDetailBottom(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.aux_scale_list = ChordDetailAuxScales(master=self)
        self.aux_scale_list.pack(side=LEFT, fill=BOTH, expand=True)

        self.aux_chord_list = ChordDetailAuxChords(master=self)
        self.aux_chord_list.pack(side=LEFT, fill=BOTH, expand=True)

    def refresh(self):
        self.aux_scale_list.refresh()
        self.aux_chord_list.refresh()


class ChordDetailAll(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "和弦详情" if GlobalSetting.lan == "zh" else "Chord Detail"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        self.voicing = ChordDetailVoicing(master=self)
        self.voicing.pack(side=TOP, fill=X)

        context = "插入" if GlobalSetting.lan == "zh" else "Insert"
        self.insert_btn = Button(self, text=context)
        self.insert_btn.bind("<Button-1>", self.insert_btn_left_click)
        self.insert_btn.pack(side=TOP, fill=X, expand=False)

        self.listbox = ChordDetailBottom(master=self)
        self.listbox.pack(side=TOP, fill=BOTH, expand=True)

        self.refresh()

    def refresh(self):
        self.voicing.refresh()
        self.listbox.refresh()

    def insert_btn_left_click(self, event):
        # todo insert item to daw
        pass


class Piano(Frame):

    def __init__(self, oct_num, **kwargs):
        super().__init__(**kwargs)
        self.oct_num = oct_num
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

    def play(self, notes):
        for oct_index in range(self.oct_num):
            for note_index, note in enumerate(Theory.note_lst[:5]):
                if note_index % 2 == 0:
                    note = f'{note}{oct_index}'
                    btn = getattr(self, note)
                    btn.configure(bg="white", fg="black")
                else:
                    note = note.split('/')[0]
                    note = f'{note}{oct_index}'
                    btn = getattr(self, note)
                    btn.configure(bg="black", fg="white")

            for note_index, note in enumerate(Theory.note_lst[5:12]):
                shift = 14 * oct_index + 6
                if note_index % 2 == 0:
                    note = f'{note}{oct_index}'
                    btn = getattr(self, note)
                    btn.configure(bg="white", fg="black")
                else:
                    note = note.split('/')[0]
                    note = f'{note}{oct_index}'
                    btn = getattr(self, note)
                    btn.configure(bg="black", fg="white")

        # make note to note with oct_index


class SelectMainScaleUi(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label_context = "主音" if GlobalSetting.lan == "zh" else "Main Note"
        Label(self, text=label_context).pack(side=LEFT)
        self.drop_down_note = ttk.Combobox(self)
        note_list = tuple([x.split('/')[0] for x in Theory.note_lst])
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
        self.drop_down_note.current(Theory.note_index(Theory.note_lst, GlobalState.scale_root))
        self.drop_down_scale.current(list(Theory.scale_map.keys()).index(GlobalState.scale_pattern))

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

        label_context = "和弦音: " if GlobalSetting.lan == "zh" else "Chord Notes: "
        chord = GlobalState.chord_pattern.replace("X", GlobalState.chord_root)
        voicing = ','.join(Theory.make_chord(chord)[0])
        if GlobalState.chord_bass != GlobalState.chord_root:
            voicing = GlobalState.chord_bass + "," + voicing
        self.scale_voicing_label.configure(text=label_context + voicing)

    def select_note(self, event):
        GlobalState.scale_root = self.drop_down_note.get()

    def select_scale(self, event):
        GlobalState.scale_pattern = Theory.find_scale_tag_by_scale_name(self.drop_down_scale.get(), GlobalSetting.lan)


class App:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.app = Tk()
        self.app.title('rChord')
        self.app.geometry("800x600+800+400")
        self.build()

    def build(self):
        self.select_main_scale = SelectMainScaleUi(master=self.app)
        self.select_main_scale.pack(side=TOP, fill=BOTH, expand=False)

        self.aux_piano = Piano(3, bg="white", master=self.app)
        self.aux_piano.pack(side=BOTTOM, fill=BOTH, expand=False)

        col_name = "辅助图示" if GlobalSetting.lan == "zh" else "Aux Display"
        Label(self.app, text=col_name, bg="gray").pack(side=BOTTOM, fill=BOTH, expand=False)

        self.main_piano = Piano(3, bg="white", master=self.app)
        self.main_piano.pack(side=BOTTOM, fill=BOTH, expand=False)

        col_name = "和弦图示" if GlobalSetting.lan == "zh" else "Chord Display"
        Label(self.app, text=col_name, bg="gray").pack(side=BOTTOM, fill=BOTH, expand=False)

        self.chord_root_note_list = ChordRootNoteList(master=self.app)
        self.chord_root_note_list.pack(side=LEFT, fill=BOTH, expand=False)

        self.chord_list = ChordList(5, master=self.app)
        self.chord_list.pack(side=LEFT, fill=BOTH, expand=True)

        self.chord_bass_note_list = ChordBaseNoteList(master=self.app)
        self.chord_bass_note_list.pack(side=LEFT, fill=BOTH, expand=False)

        self.chord_detail = ChordDetailAll(master=self.app)
        self.chord_detail.pack(side=LEFT, fill=BOTH, expand=False)

    def refresh(self):
        self.select_main_scale.refresh()
        self.chord_root_note_list.refresh()
        self.chord_bass_note_list.refresh()
        self.chord_list.refresh()
        self.chord_detail.refresh()

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
