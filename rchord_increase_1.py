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
        "Natural Maj": "1,2,3,4,5,6,7",
        "Harmonic Maj": "1,2,3,4,5,b6,7",
        "Melodic Maj": "1,2,3,4,5,b6,b7",
        "Natural Min": "1,2,b3,4,5,b6,b7",
        "Harmonic Min": "1,2,b3,4,5,b6,7",
        "Melodic Min": "1,2,b3,4,5,6,7",
        "Ionian": "1,2,3,4,5,6,7",
        "Dorian": "1,2,b3,4,5,6,b7",
        "Phrygian": "1,b2,b3,4,5,b6,b7",
        "Lydian": "1,2,3,#4,5,6,7",
        "Mixolydian": "1,2,3,4,5,6,b7",
        "Aeolian": "1,2,b3,4,5,b6,b7",
        "Locrian": "1,b2,b3,4,b5,b6,b7",
        "Whole Half Dim": "1,2,b3,4,b5,b6,6,7",
        "Half Whole Dim": "1,b2,b3,3,b5,5,6,b7",
        "Diatonic": "1,2,3,#4,#5,#6",
        "Blues": "1,b3,4,b5,5,b7",
        "Mix Blues": "1,b3,3,4,b5,5,b7",
        "Aux Blues": "1,2,b3,3,4,#4,5,6,b7",
        "Jazz Min": "1,2,b3,4,5,6,7",
        "Blues Maj": "1,2,b3,4,b5,b6,7",
        "Phrygian Dominant": "1,b2,3,4,5,b6,b7",
        "Lydian Dominant": "1,2,3,#4,5,6,b7",
        "Super Locrian": "1,b2,b3,3,b5,b6,b7",
        "Gypsy": "1,b3,#4,5,b6,b7",
        "Hungarian Maj": "1,#2,3,#4,5,6,b7",
        "Hungarian Min": "1,2,b3,#4,5,b6,7",
        "Bibop": "1,2,3,4,5,6,b7,7",
        "India": "1,2,3,4,5,b6,b7",
        "Jap": "1,3,4,6,7",
        "Russia": "1,b2,2,b3,4,5,b6,6,b7,7",
        "Arabian": "1,b2,3,4,5,b6,b7",
        "Oriental": "1,b2,3,4,b5,6,b7",
        "Spanish": "1,b2,b3,3,4,b5,b6,b7",
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
        return cls.parse(root, cls.scale_map[tag])

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

    @classmethod
    def scale_trans(cls, note, diff):
        note = cls.note_lst_x4[cls.note_index(cls.note_lst_x4[12:], note) + 12 + diff]
        return note.split("/")[0]

    @classmethod
    def chord_trans(cls, chord, diff, nice_notes):
        chord_pattern = chord.split('/')[0]
        chord_bass = chord.split('/')[0]
        if "/" in chord:
            chord_bass = chord.split('/')[1]
        new_bass = cls.note_lst_x4[cls.note_index(cls.note_lst_x4[12:], chord_bass) + 12 + diff]
        if "/" in new_bass:
            for n in new_bass.split("/"):
                if n in nice_notes:
                    new_bass = n
        if "/" in new_bass:
            new_bass = new_bass.split("/")[0]
        if len(chord_pattern) >= 2 and chord_pattern[1] in "b#":
            root = chord_pattern[:2]
            new_root = cls.note_lst_x4[cls.note_index(cls.note_lst_x4[12:], root) + 12 + diff]
            if "/" in new_root:
                for n in new_root.split("/"):
                    if n in nice_notes:
                        new_root = n
            if "/" in new_root:
                new_root = new_root.split("/")[0]

            chord_tag = chord_pattern[2:]
        else:
            root = chord_pattern[0]
            chord_tag = chord_pattern[1:]
            new_root = cls.note_lst_x4[cls.note_index(cls.note_lst_x4[12:], root) + 12 + diff]
            if "/" in new_root:
                for n in new_root.split("/"):
                    if n in nice_notes:
                        new_root = n
            if "/" in new_root:
                new_root = new_root.split("/")[0]
        if new_bass == new_root:
            return f"{new_root}{chord_tag}"
        else:
            return f"{new_root}{chord_tag}/{new_bass}"


class ReaperUtil:
    ChordTrackName = "__CHORD_TRACK__"
    ChordTrackMeta = "__CHORD_META__"
    ChordTrackMidi = "__CHORD_MIDI__"

    scale_cache = {}

    @classmethod
    def process(cls):
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
        if not all([chord_track, meta_track, midi_track]):
            return
        if len(set([chord_track.n_items, meta_track.n_items, midi_track.n_items])) > 1:
            return
        for idx, item in enumerate(chord_track.items):
            if item.is_selected:
                select_idx = idx
                chord = rpi.ULT_GetMediaItemNote(item.id)
                meta = rpi.ULT_GetMediaItemNote(meta_track.items[select_idx].id)
                scale_root = meta.split("/")[0]
                scale_patt = meta.split("/")[1]
                voicing = meta.split("/")[2]
                oct = meta.split("/")[3]
                new_root = Theory.scale_trans(scale_root, 1)
                scale_notes = cls.scale_cache.get(f"{new_root}/{scale_patt}", None)
                if scale_notes is None:
                    scale_notes = Theory.make_scale(f"{new_root}/{scale_patt}")[0]
                    cls.scale_cache[f"{new_root}/{scale_patt}"] = scale_notes
                new_chord = Theory.chord_trans(chord, 1, scale_notes)
                notes = meta.split("/")[-1]
                new_notes = [int(x)+1 for x in notes.split(',')]
                new_notes_str = ",".join([str(x) for x in new_notes])
                new_meta = f"{new_root}/{scale_patt}/{voicing}/{oct}/{new_notes_str}"
                rpi.ULT_SetMediaItemNote(item.id, new_chord)
                rpi.ULT_SetMediaItemNote(meta_track.items[select_idx].id, new_meta)

                midi_item = midi_track.items[select_idx]
                st = midi_item.position
                ed = midi_item.position + midi_item.length
                midi_item.delete()

                midi_item = midi_track.add_midi_item(
                    start=st,
                    end=ed,
                )

                midi_take = rpi.GetActiveTake(midi_item.id)
                for note in new_notes:
                    rpi.MIDI_InsertNote(
                        midi_take,
                        False,
                        False,
                        rpi.MIDI_GetPPQPosFromProjTime(midi_take, st),
                        rpi.MIDI_GetPPQPosFromProjTime(midi_take, ed),
                        0,
                        note,
                        96,
                        False
                    )


if __name__ == "__main__":
    ReaperUtil.process()
