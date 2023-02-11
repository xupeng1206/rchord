import reapy as rpy
from reapy import reascript_api as rpi


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
            pass

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
            pass

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
            pass

    def _chord_change(self):
        chord = self._chord_pattern.replace("X", self._chord_root)
        notes = Theory.make_chord(chord)[0]
        self._chord_voicing = ",".join(notes)
        self._chord_default_voicing = ",".join(notes)

    def _scale_change(self):
        notes = Theory.make_scale(f"{self._scale_root}/{self._scale_pattern}")[0]
        self._scale_notes = ",".join(notes)


GlobalState = GlobalStateClz()


class ReaperUtil:
    ChordTrackName = "__CHORD_TRACK__"
    ChordTrackMeta = "__CHORD_META__"

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
    def insert_chord_item(cls, chord, meta):
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
    ReaperUtil.parse_item()
    ReaperUtil.play([GlobalState.chord_bass] + GlobalState.chord_voicing.split(','))
