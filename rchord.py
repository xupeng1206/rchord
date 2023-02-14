from tkinter import *
from tkinter import ttk

import reapy as rpy
from reapy import reascript_api as rpi


def r_set_text(self, text):
    self.r_text = text


def r_get_text(self):
    return getattr(self, "r_text")


setattr(Button, "r_set_text", r_set_text)
setattr(Button, "r_get_text", r_get_text)


class Theory:
    note_letters = "CDEFGAB" * 4
    note_lst = ["C", "Db/C#", "D", "Eb/D#", "E", "F", "Gb/F#", "G", "Ab/G#", "A", "Bb/A#", "B"]
    note_lst_x4 = note_lst * 4

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
        "Natural Maj": {"pattern": "1,2,3,4,5,6,7", "zh": "", "en": "Natural Maj"},
        "Harmonic Maj": {"pattern": "1,2,3,4,5,b6,7", "zh": "", "en": "Harmonic Maj"},
        "Melodic Maj": {"pattern": "1,2,3,4,5,b6,b7", "zh": "", "en": "Melodic Maj"},
        "Natural Min": {"pattern": "1,2,b3,4,5,b6,b7", "zh": "", "en": "Natural Min"},
        "Harmonic Min": {"pattern": "1,2,b3,4,5,b6,7", "zh": "", "en": "Harmonic Min"},
        "Melodic Min": {"pattern": "1,2,b3,4,5,6,7", "zh": "", "en": "Melodic Min"},
        "Ionian": {"pattern": "1,2,3,4,5,6,7", "zh": "", "en": "Ionian"},
        "Dorian": {"pattern": "1,2,b3,4,5,6,b7", "zh": "", "en": "Dorian"},
        "Phrygian": {"pattern": "1,b2,b3,4,5,b6,b7", "zh": "", "en": "Phrygian"},
        "Lydian": {"pattern": "1,2,3,#4,5,6,7", "zh": "", "en": "Lydian"},
        "Mixolydian": {"pattern": "1,2,3,4,5,6,b7", "zh": "", "en": "Mixolydian"},
        "Aeolian": {"pattern": "1,2,b3,4,5,b6,b7", "zh": "", "en": "Aeolian"},
        "Locrian": {"pattern": "1,b2,b3,4,b5,b6,b7", "zh": "", "en": "Locrian"},
        "Whole Half Dim": {"pattern": "1,2,b3,4,b5,b6,6,7", "zh": "", "en": "Whole Half Dim"},
        "Half Whole Dim": {"pattern": "1,b2,b3,3,b5,5,6,b7", "zh": "", "en": "Half Whole Dim"},
        "Diatonic": {"pattern": "1,2,3,#4,#5,#6", "zh": "", "en": "Diatonic"},
        "Blues": {"pattern": "1,b3,4,b5,5,b7", "zh": "", "en": "Blues"},
        "Mix Blues": {"pattern": "1,b3,3,4,b5,5,b7", "zh": "", "en": "Mix Blues"},
        "Aux Blues": {"pattern": "1,2,b3,3,4,#4,5,6,b7", "zh": "", "en": "Aux Blues"},
        "Jazz Min": {"pattern": "1,2,b3,4,5,6,7", "zh": "", "en": "Jazz Min"},
        "Blues Maj": {"pattern": "1,2,b3,4,b5,b6,7", "zh": "", "en": "Blues Maj"},
        "Phrygian Dominant": {"pattern": "1,b2,3,4,5,b6,b7", "zh": "", "en": "Phrygian Dominant"},
        "Lydian Dominant": {"pattern": "1,2,3,#4,5,6,b7", "zh": "", "en": "Lydian Dominant"},
        "Super Locrian": {"pattern": "1,b2,b3,3,b5,b6,b7", "zh": "", "en": "Super Locrian"},
        "Gypsy": {"pattern": "1,b3,#4,5,b6,b7", "zh": "", "en": "Gypsy"},
        "Hungarian Maj": {"pattern": "1,#2,3,#4,5,6,b7", "zh": "", "en": "Hungarian Maj"},
        "Hungarian Min": {"pattern": "1,2,b3,#4,5,b6,7", "zh": "", "en": "Hungarian Min"},
        "Bibop": {"pattern": "1,2,3,4,5,6,b7,7", "zh": "", "en": "Bibop"},
        "India": {"pattern": "1,2,3,4,5,b6,b7", "zh": "", "en": "India"},
        "Jap": {"pattern": "1,3,4,6,7", "zh": "", "en": "Jap"},
        "Russia": {"pattern": "1,b2,2,b3,4,5,b6,6,b7,7", "zh": "", "en": "Russia"},
        "Arabian": {"pattern": "1,b2,3,4,5,b6,b7", "zh": "", "en": "Arabian"},
        "Oriental": {"pattern": "1,b2,3,4,b5,6,b7", "zh": "", "en": "Oriental"},
        "Spanish": {"pattern": "1,b2,b3,3,4,b5,b6,b7", "zh": "", "en": "Spanish"},
    }

    @classmethod
    def notes_to_notes_pitched(cls, notes):
        pre_num = 0
        note_indexes = []
        for note in notes:
            tmp_index = cls.note_index(cls.note_lst_x4[pre_num:], note)
            note_indexes.append(pre_num + tmp_index)
            pre_num = pre_num + tmp_index + 1
        notes_pitched = []
        for idx in note_indexes:
            pitch = int(idx / 12)
            note = cls.note_lst_x4[idx]
            note_pitched = "/".join([x + str(pitch) for x in note.split("/")])
            notes_pitched.append(note_pitched)
        return notes_pitched, note_indexes

    @classmethod
    def find_scale_tag_by_scale_name(cls, name, lan="en"):
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
        try:
            chord = cls.make_chord(chord_name)
        except Exception:
            return False
        try:
            scale = cls.make_scale(scale_name)
        except Exception:
            return False
        return all([bool(x in scale[1]) for x in chord[1]])

    @classmethod
    def find_scales_by_chord(cls, chord_name):
        try:
            chord = cls.make_chord(chord_name)
        except Exception:
            return []
        scales = []
        for notes in cls.note_lst:
            for note in notes.split("/"):
                for tag, val in cls.scale_map.items():
                    try:
                        tmp_scale = cls.make_scale(f"{note}/{tag}")
                    except Exception:
                        continue
                    if all([bool(x in tmp_scale[1]) for x in chord[1]]):
                        scales.append(f"{note}/{tag}")
        return scales

    @classmethod
    def find_similar_chord(cls, chord_name):
        try:
            chord = cls.make_chord(chord_name)
        except Exception:
            return []
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
                    try:
                        tmp_chord = cls.make_chord(tmp_chord_name)
                    except Exception:
                        continue
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
        root_start = cls.note_index(cls.note_lst_x4, root)
        root_letter = root.strip("#b")
        root_letter_start = cls.note_letters.index(root_letter)
        ret_multi_notes = []
        ret_single_notes = []
        for s_note in pattern.split(","):
            note = cls.note_lst_x4[root_start + cls.note_index(cls.simple_note_lst, s_note)]
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
    _scale_notes = "C,D,E,F,G,A,B"
    _chord_root = "C"
    _chord_pattern = "X"
    _chord_bass = "C"
    _chord_default_voicing = "C,E,G"
    _chord_voicing = "C,E,G"
    _analyse_chord = ""
    _oct = 0

    _playing_note = []

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def oct(self):
        return self._oct

    @oct.setter
    def oct(self, value):
        self._oct = value

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
            self._scale_change()
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
            self._scale_change()
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
        refresh = False
        if value != self._chord_pattern:
            refresh = True
        self._chord_voicing = value
        if refresh:
            app.chord_selector.main_piano.play([self._chord_bass] + self._chord_voicing.split(','))

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

    @property
    def playing_note(self):
        return self._playing_note

    @playing_note.setter
    def playing_note(self, value):
        self._playing_note = value

    @property
    def scale_notes(self):
        return self._scale_notes

    @property
    def analyse_chord(self):
        return self._analyse_chord

    @analyse_chord.setter
    def analyse_chord(self, value):
        refresh = False
        if value != self._analyse_chord:
            refresh = True
        self._analyse_chord = value
        if refresh:
            app.chord_analyser.refresh()

    def _chord_change(self):
        chord = self._chord_pattern.replace("X", self._chord_root)
        notes = Theory.make_chord(chord)[0]
        self._chord_voicing = ",".join(notes)
        self._chord_default_voicing = ",".join(notes)

    def _scale_change(self):
        notes = Theory.make_scale(f"{self._scale_root}/{self._scale_pattern}")[0]
        self._scale_notes = ",".join(notes)

    def play_aux_piano(self, notes):
        app.chord_analyser.aux_piano.play(notes)


GlobalState = GlobalStateClz()


class ChordRootNoteList(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "Chord Root"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        for i in range(12):
            btn = Button(self)
            btn.pack(side=TOP, fill=BOTH, expand=YES)
            btn.bind("<Button-1>", self.left_click)
            setattr(self, f"root_note_{i}", btn)

    def refresh(self):
        scale_root_index = Theory.note_index(Theory.note_lst_x4, GlobalState.scale_root)
        nice_notes = Theory.make_scale(f"{GlobalState.scale_root}/{GlobalState.scale_pattern}")[1]
        note_list = Theory.note_lst_x4[scale_root_index:scale_root_index + 12]
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
        ReaperUtil.stop_play()
        ReaperUtil.play([GlobalState.chord_root])


class ChordBaseNoteList(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "Chord Bass"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        for i in range(12):
            btn = Button(self)
            btn.pack(side=TOP, fill=BOTH, expand=YES)
            btn.bind("<Button-1>", self.left_click)
            setattr(self, f"bass_note_{i}", btn)

    def refresh(self):
        scale_root_index = Theory.note_index(Theory.note_lst_x4, GlobalState.scale_root)
        nice_notes = Theory.make_chord(GlobalState.chord_pattern.replace("X", GlobalState.chord_root))[1]
        note_list = Theory.note_lst_x4[scale_root_index:scale_root_index + 12]
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
        ReaperUtil.stop_play()
        ReaperUtil.play([GlobalState.chord_bass] + GlobalState.chord_voicing.split(','))


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
        ReaperUtil.stop_play()
        ReaperUtil.play([GlobalState.chord_bass] + GlobalState.chord_voicing.split(','))


class ChordSelectorMiddle(Frame):

    def __init__(self, cols, **kwargs):
        super().__init__(**kwargs)

        col_name = "Chord"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        self.voicing = ChordDetailVoicing(master=self)
        self.voicing.pack(side=TOP, fill=X, expand=False)

        self.chord_grid = ChordGrid(cols, master=self)
        self.chord_grid.master = self
        self.chord_grid.pack(side=TOP, fill=BOTH, expand=True)

    def refresh(self):
        self.voicing.refresh()
        self.chord_grid.refresh()


class ChordDetailVoicing(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "Chord Voicing:"
        Label(self, text=col_name, bg="gray").pack(side=LEFT, fill=X)

        self.bass = Label(self, bg="gray")
        self.bass.pack(side=LEFT, fill=X, padx=5)

        self.voicing_entry = Entry(self)
        self.voicing_entry.pack(side=LEFT, fill=X, expand=True)

        context = "Listen"
        self.listen_btn = Button(self, text=context)
        self.listen_btn.bind("<Button-1>", self.listen_btn_left_click)
        self.listen_btn.pack(side=LEFT, fill=X, expand=False)

        context = "Stop"
        self.listen_btn = Button(self, text=context)
        self.listen_btn.bind("<Button-1>", self.stop_btn_left_click)
        self.listen_btn.pack(side=LEFT, fill=X, expand=False)

        context = "Insert"
        self.insert_btn = Button(self, text=context)
        self.insert_btn.bind("<Button-1>", self.insert_btn_left_click)
        self.insert_btn.pack(side=LEFT, fill=X, expand=False)

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
        ReaperUtil.stop_play()
        ReaperUtil.play([GlobalState.chord_bass] + GlobalState.chord_voicing.split(','))

    def stop_btn_left_click(self, event):
        # todo play sound
        ReaperUtil.stop_play_all()

    def insert_btn_left_click(self, event):
        # todo insert item to daw
        chord = GlobalState.chord_pattern.replace("X", GlobalState.chord_root)
        if GlobalState.chord_root != GlobalState.chord_bass:
            chord = chord + "/" + GlobalState.chord_bass

        note_indexes = Theory.notes_to_notes_pitched([GlobalState.chord_bass] + GlobalState.chord_voicing.split(','))[1]
        notes = [x + 36 + GlobalState.oct * 12 for x in note_indexes]
        ReaperUtil.insert_chord_item(chord, f"{GlobalState.scale_root}/{GlobalState.scale_pattern}/{GlobalState.chord_voicing}", notes)
        # todo play sound
        ReaperUtil.stop_play()
        ReaperUtil._play(notes)


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
        note_pitched = Theory.notes_to_notes_pitched(notes)
        for note in note_pitched[0]:
            btn = getattr(self, note.split("/")[0])
            btn.configure(bg="blue", fg="white")


class SelectMainScaleUi(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label_context = "Main Note"
        Label(self, text=label_context).pack(side=LEFT)
        self.drop_down_note = ttk.Combobox(self)
        note_list = tuple([x.split('/')[0] for x in Theory.note_lst])
        self.drop_down_note["value"] = note_list
        self.drop_down_note.bind("<<ComboboxSelected>>", self.select_note)
        self.drop_down_note.pack(side=LEFT, fill=BOTH, expand=YES)

        label_context = "Main Scale"
        Label(self, text=label_context).pack(side=LEFT)

        self.drop_down_scale = ttk.Combobox(self)
        scale_list = tuple(Theory.scale_map.keys())
        self.drop_down_scale["value"] = scale_list
        self.drop_down_scale.bind("<<ComboboxSelected>>", self.select_scale)
        self.drop_down_scale.pack(side=LEFT, fill=BOTH, expand=YES)

        label_context = "Oct"
        Label(self, text=label_context).pack(side=LEFT)

        self.drop_down_oct = ttk.Combobox(self)
        oct_list = tuple([-1, 0, 1])
        self.drop_down_oct["value"] = oct_list
        self.drop_down_oct.bind("<<ComboboxSelected>>", self.select_oct)
        self.drop_down_oct.pack(side=LEFT, fill=BOTH, expand=YES)

    def refresh(self):
        self.drop_down_note.current(Theory.note_index(Theory.note_lst, GlobalState.scale_root))
        self.drop_down_scale.current(list(Theory.scale_map.keys()).index(GlobalState.scale_pattern))
        self.drop_down_oct.current([-1, 0, 1].index(GlobalState.oct))

    def select_note(self, event):
        GlobalState.scale_root = self.drop_down_note.get()

    def select_scale(self, event):
        GlobalState.scale_pattern = self.drop_down_scale.get()

    def select_oct(self, event):
        GlobalState.oct = int(self.drop_down_oct.get())


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

    def refresh(self):
        label_context = "Pattern: "
        self.scale_pattern_label.configure(text=label_context + Theory.scale_map[GlobalState.scale_pattern]["pattern"])

        label_context = "Notes: "
        notes = GlobalState.scale_notes
        self.scale_note_label.configure(text=label_context + notes)

        label_context = "Chord: "
        chord = GlobalState.chord_pattern.replace("X", GlobalState.chord_root)
        if GlobalState.chord_bass != GlobalState.chord_root:
            chord = chord + "/" + GlobalState.chord_bass
        self.scale_chord_label.configure(text=label_context + chord)

        label_context = "Chord Notes: "
        voicing = GlobalState.chord_voicing
        if GlobalState.chord_bass != voicing[0]:
            voicing = GlobalState.chord_bass + "," + voicing
        self.scale_voicing_label.configure(text=label_context + voicing)


class Top(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selector = SelectMainScaleUi(master=self)
        self.selector.pack(side=TOP, fill=X, expand=False)

        self.state_info = StateInfoUi(master=self)
        self.state_info.pack(side=TOP, fill=X, expand=False)

    def refresh(self):
        self.selector.refresh()
        self.state_info.refresh()


class ChordSelector(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.top = Top(master=self)
        self.top.pack(side=TOP, fill=BOTH, expand=False)

        self.main_piano = Piano(4, bg="white", master=self)
        self.main_piano.pack(side=BOTTOM, fill=BOTH, expand=False)

        self.main_piano.play([GlobalState.chord_bass] + GlobalState.chord_voicing.split(","))

        col_name = "Chord Display"
        Label(self, text=col_name, bg="gray").pack(side=BOTTOM, fill=BOTH, expand=False)

        self.chord_root_note_list = ChordRootNoteList(master=self)
        self.chord_root_note_list.pack(side=LEFT, fill=BOTH, expand=False)

        self.chord_map = ChordSelectorMiddle(5, master=self)
        self.chord_map.pack(side=LEFT, fill=BOTH, expand=True)

        self.chord_bass_note_list = ChordBaseNoteList(master=self)
        self.chord_bass_note_list.pack(side=LEFT, fill=BOTH, expand=False)

    def refresh(self):
        self.top.refresh()
        self.chord_root_note_list.refresh()
        self.chord_bass_note_list.refresh()
        self.chord_map.refresh()
        self.main_piano.play([GlobalState.chord_bass] + GlobalState.chord_voicing.split(","))


class ChordDetailAuxScales(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "Aux Scales"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        self.aux_scale_list = Listbox(self)
        self.aux_scale_list.bind("<<ListboxSelect>>", self.aux_scale_list_select)
        self.aux_scale_list.pack(side=TOP, fill=BOTH, expand=True)

    def refresh(self):
        if self.aux_scale_list.size() > 0:
            self.aux_scale_list.delete(0, self.aux_scale_list.size())
        chord = GlobalState.analyse_chord
        scales = Theory.find_scales_by_chord(chord)
        for idx, scale in enumerate(scales):
            note, tag = scale.split("/")
            # self.aux_scale_list.insert(idx, f"{note} | {Theory.scale_map[tag][GlobalSetting.lan]}")
            self.aux_scale_list.insert(idx, f"{note} | {tag}")

    def aux_scale_list_select(self, event):
        aux_scale = None
        try:
            index = self.aux_scale_list.curselection()
            aux_scale = self.aux_scale_list.get(index)
        except Exception:
            pass
        if aux_scale is None:
            return
        note, scale = aux_scale.split("|")
        note = note.strip()
        # scale = Theory.find_scale_tag_by_scale_name(scale.strip(), GlobalSetting.lan)
        scale = scale.strip()
        notes = Theory.make_scale(f"{note}/{scale}")[0]
        GlobalState.play_aux_piano(notes)
        # todo play sound (not support)


class ChordDetailAuxChords(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        col_name = "Aux Chords"
        Label(self, text=col_name, bg="gray").pack(side=TOP, fill=X)

        self.aux_chord_list = Listbox(self)
        self.aux_chord_list.bind("<<ListboxSelect>>", self.aux_chord_list_select)
        self.aux_chord_list.pack(side=TOP, fill=BOTH, expand=True)

    def refresh(self):
        if self.aux_chord_list.size() > 0:
            self.aux_chord_list.delete(0, self.aux_chord_list.size())
        target_chord = GlobalState.analyse_chord
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
        notes = Theory.make_chord(aux_chord)[0]
        GlobalState.play_aux_piano(notes)
        ReaperUtil.stop_play()
        ReaperUtil.play(notes)


class ChordAnalyserTop(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.chord = Entry(self)
        self.chord.pack(side=LEFT, fill=BOTH, expand=True)

        self.analyser = Button(self, text="Analyser")
        self.analyser.bind('<Button-1>', self.analyser_click)
        self.analyser.pack(side=LEFT, fill=BOTH, expand=True)

        self.analyser = Button(self, text="Stop")
        self.analyser.bind('<Button-1>', self.stop_click)
        self.analyser.pack(side=LEFT, fill=BOTH, expand=True)

    def analyser_click(self, event):
        GlobalState.analyse_chord = self.chord.get()

    def stop_click(self, event):
        # todo play sound
        ReaperUtil.stop_play_all()


class ChordAnalyser(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.top = ChordAnalyserTop(master=self)
        self.top.pack(side=TOP, fill=BOTH, expand=False)

        self.aux_piano = Piano(2, bg="white", master=self)
        self.aux_piano.pack(side=BOTTOM, fill=BOTH, expand=False)

        col_name = "Aux Display"
        Label(self, text=col_name, bg="gray").pack(side=BOTTOM, fill=BOTH, expand=False)

        self.aux_scale_list = ChordDetailAuxScales(master=self)
        self.aux_scale_list.pack(side=LEFT, fill=BOTH, expand=True)

        self.aux_chord_list = ChordDetailAuxChords(master=self)
        self.aux_chord_list.pack(side=LEFT, fill=BOTH, expand=True)

    def refresh(self):
        self.aux_scale_list.refresh()
        self.aux_chord_list.refresh()


class App:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        ReaperUtil.parse_item()
        self.app = Tk()
        self.app.title('rChord')
        self.app.geometry("900x800+800+400")
        self.app.bind("<KeyPress-Escape>", self.esc)
        self.app.attributes('-topmost', 1)

        self.tabs = ttk.Notebook(self.app)
        self.tabs.pack(fill=BOTH, expand=True)

        self.chord_selector = ChordSelector(master=self.app)
        self.chord_analyser = ChordAnalyser(master=self.app)

        self.tabs.add(self.chord_selector, text="ChordSelector")
        self.tabs.select(self.tabs.tabs()[0])
        self.tabs.add(self.chord_analyser, text="ChordAnalyser")
        self.tabs.tabs()

        self.refresh()

    def run(self):
        self.app.mainloop()

    def refresh(self):
        self.chord_selector.refresh()

    def esc(self, event):
        self.app.destroy()


class ReaperUtil:
    ChordTrackName = "__CHORD_TRACK__"
    ChordTrackMeta = "__CHORD_META__"
    ChordTrackMidi = "__CHORD_MIDI__"

    @classmethod
    def parse_item(cls):
        ReaperUtil.stop_play_all()
        chord, meta = ReaperUtil.select_chord_item()
        if None in [chord, meta]:
            return
        if "/" in chord:
            GlobalState._chord_bass = chord.split('/')[1]
            chord = chord.split('/')[0]
            GlobalState._scale_root = meta.split("/")[0]
            GlobalState._scale_pattern = meta.split("/")[1]
            GlobalState._chord_voicing = meta.split("/")[2]
            chord_notes = Theory.make_chord(chord)[0]
            GlobalState._chord_root = chord_notes[0]
            GlobalState._chord_default_voicing = chord_notes
            GlobalState._chord_pattern = chord.replace(GlobalState._chord_root, "X")
            GlobalState._scale_notes = ",".join(
                Theory.make_scale(f"{GlobalState.scale_root}/{GlobalState.scale_pattern}")[0])
        else:
            GlobalState._scale_root = meta.split("/")[0]
            GlobalState._scale_pattern = meta.split("/")[1]
            GlobalState._chord_voicing = meta.split("/")[2]
            chord_notes = Theory.make_chord(chord)[0]
            GlobalState._chord_root = chord_notes[0]
            GlobalState._chord_bass = chord_notes[0]
            GlobalState._chord_default_voicing = chord_notes
            GlobalState._chord_pattern = chord.replace(GlobalState._chord_root, "X")
            GlobalState._scale_notes = ",".join(
                Theory.make_scale(f"{GlobalState.scale_root}/{GlobalState.scale_pattern}")[0])

    @classmethod
    def insert_chord_item(cls, chord, meta, notes):
        p = rpy.Project()
        chord_track = None
        meta_track = None
        midi_track = None
        for t in p.tracks:
            if t.name == cls.ChordTrackName:
                chord_track = t
            if t.name == cls.ChordTrackMeta:
                meta_track = t
            if t.name == cls.ChordTrackMidi:
                midi_track = t
            if all([chord_track, meta_track, midi_track]):
                break
        if not midi_track:
            chord_track = p.add_track(0, cls.ChordTrackMidi)
        if not meta_track:
            meta_track = p.add_track(0, cls.ChordTrackMeta)
        if not chord_track:
            chord_track = p.add_track(0, cls.ChordTrackName)
        end_pos = p.cursor_position + p.beats_to_time(4)
        chord_item = chord_track.add_item(
            start=p.cursor_position,
            end=end_pos,
        )
        meta_item = meta_track.add_item(
            start=p.cursor_position,
            end=end_pos,
        )

        rpi.ULT_SetMediaItemNote(chord_item.id, chord)
        rpi.ULT_SetMediaItemNote(meta_item.id, meta)

        midi_item = midi_track.add_midi_item(
            start=p.cursor_position,
            end=end_pos,
            quantize=True
        )
        midi_take = midi_item.add_take()
        for note in notes:
            midi_take.add_note(
                start=p.cursor_position,
                end=end_pos,
                pitch=note,
                velocity=96
            )

        p.cursor_position = end_pos

    @classmethod
    def select_chord_item(cls):
        p = rpy.Project()
        chord_track = None
        meta_track = None
        for t in p.tracks:
            if t.name == cls.ChordTrackName:
                chord_track = t
            if t.name == cls.ChordTrackMeta:
                meta_track = t
            if all([chord_track, meta_track]):
                break
        if not all([chord_track, meta_track]):
            return None, None
        if chord_track.n_items != meta_track.n_items:
            return None, None
        chord = None
        select_idx = -1
        for idx, item in enumerate(chord_track.items):
            if item.is_selected:
                select_idx = idx
                chord = rpi.ULT_GetMediaItemNote(item.id)
                break
        if select_idx == -1:
            return chord, None
        meta = rpi.ULT_GetMediaItemNote(meta_track.items[select_idx].id)
        return chord, meta

    @classmethod
    def play(cls, notes):
        note_indexes = Theory.notes_to_notes_pitched(notes)[1]
        notes = [x + 36 + GlobalState.oct * 12 for x in note_indexes]
        cls._play(notes)

    @classmethod
    def _play(cls, notes):
        keyboard_mode = 0  # virtualKeyboardMode
        channel = 0
        note_on = 0x90 + channel
        velocity = 96
        for note in notes:
            rpi.StuffMIDIMessage(keyboard_mode, note_on, note, velocity)
        GlobalState.playing_note = GlobalState.playing_note + notes

    @classmethod
    def stop_play(cls):
        keyboard_mode = 0  # virtualKeyboardMode
        channel = 0
        note_off = 0x80 + channel
        velocity = 0
        for note in GlobalState.playing_note:
            rpi.StuffMIDIMessage(keyboard_mode, note_off, note, velocity)
        GlobalState.playing_note = []

    @classmethod
    def stop_play_all(cls):
        keyboard_mode = 0  # virtualKeyboardMode
        channel = 0
        note_off = 0x80 + channel
        velocity = 0
        for note in range(0, 128):
            rpi.StuffMIDIMessage(keyboard_mode, note_off, note, velocity)
        GlobalState.playing_note = []


if __name__ == "__main__":
    app = App()
    app.run()
