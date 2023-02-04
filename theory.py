class TheoryUtil:
    note_letters = "CDEFGAB" * 3
    note_lst = ["C", "Db/C#", "D", "Eb/D#", "E", "F", "Gb/F#", "G", "Ab/G#", "A", "Bb/A#", "B"]
    note_lst_x3 = note_lst * 3

    simple_note_lst = ["1", "b2/#1", "2", "b3/#2", "3", "4", "b5/#4", "5", "b6/#5", "6", "b7/#6", "7"] + \
                      ["-", "b9", "9", "#9", "-", "11", "#11", "-", "b13", "13", "-", "-"]

    chord_map = {
        "X": "1,b3,5",
        "Xm": "1,b3,5",
        "Xaug": "1,3,#5",
        "Xdim": "1,b3,b5",
        "Xsus4": "1,4,5",
        "Xsus2": "1,2,5",
        "X6": "1,3,5,6",
        "XM7": "1,3,5,7",
        "XmM7": "1,b3,5,7",
        "X7": "1,3,5,b7",
        "Xm7": "1,b3,5,b7",
        "Xm7b5": "1,b3,b5,b7",
        "Xdim7": "1,b3,b5,6",
        "Xadd9": "1,3,5,9",
        "XM9": "1,3,5,7,9",
        "XmM9": "1,b3,5,7,9",
        "X9": "1,3,5,b7,9",
        "Xm9": "1,b3,5,b7,9",
        "X11": "1,3,5,b7,9,11",
        "Xm11": "1,b3,5,b7,9,11",
        "X13": "1,3,5,b7,9,11,13",
    }

    scale_map = {
        "maj_nature": {"pattern": "1,2,3,4,5,6,7", "cn": "自然大调", "en": ""},
        "maj_harmonic": {"pattern": "1,2,3,4,5,b6,7", "cn": "和声大调", "en": ""},
        "maj_melodic": {"pattern": "1,2,3,4,5,b6,b7", "cn": "旋律大调", "en": ""},
        "min_nature": {"pattern": "1,2,b3,4,5,b6,b7", "cn": "自然小调", "en": ""},
        "min_harmonic": {"pattern": "1,2,b3,4,5,b6,7", "cn": "和声小调", "en": ""},
        "min_melodic": {"pattern": "1,2,b3,4,5,6,7", "cn": "旋律小调", "en": ""},
        "ionian": {"pattern": "1,2,3,4,5,6,7", "cn": "伊奥尼亚", "en": ""},
        "dorian": {"pattern": "1,2,b3,4,5,6,b7", "cn": "多利亚", "en": ""},
        "phrygian": {"pattern": "1,b2,b3,4,5,b6,b7", "cn": "弗里几亚", "en": ""},
        "lydian": {"pattern": "1,2,3,#4,5,6,7", "cn": "利底亚", "en": ""},
        "mixolydian": {"pattern": "1,2,3,4,5,6,b7", "cn": "混合利底亚", "en": ""},
        "aeolian": {"pattern": "1,2,b3,4,5,b6,b7", "cn": "爱奥尼亚", "en": ""},
        "locrian": {"pattern": "1,b2,b3,4,b5,b6,b7", "cn": "洛克里亚", "en": ""},
        "full_half_dim": {"pattern": "1,2,b3,4,b5,b6,6,7", "cn": "全半减音阶", "en": ""},
        "half_full_dim": {"pattern": "1,b2,b3,3,b5,5,6,b7", "cn": "半全减音阶", "en": ""},
        "full": {"pattern": "1,2,3,#4,#5,#6", "cn": "全音阶", "en": ""},
        "blus": {"pattern": "1,b3,4,b5,5,b7", "cn": "布鲁斯", "en": ""},
        "mix_blus": {"pattern": "1,b3,3,4,b5,5,b7", "cn": "混合布鲁斯", "en": ""},
        "aux_blus": {"pattern": "1,2,b3,3,4,#4,5,6,b7", "cn": "辅助布鲁斯", "en": ""},
        "jazz_min": {"pattern": "1,2,b3,4,5,6,7", "cn": "爵士小音阶", "en": ""},
        "blue_maj": {"pattern": "1,2,b3,4,b5,b6,7", "cn": "蓝调大音阶", "en": ""},
        "phrygian_dominant": {"pattern": "1,b2,3,4,5,b6,b7", "cn": "大弗里几亚", "en": ""},
        "lydian_dominant": {"pattern": "1,2,3,#4,5,6,b7", "cn": "大利底亚", "en": ""},
        "super_locrian": {"pattern": "1,b2,b3,3,b5,b6,b7", "cn": "超级洛克里亚", "en": ""},
        "gypsy": {"pattern": "1,b3,#4,5,b6,b7", "cn": "吉普赛音阶", "en": ""},
        "hungarian_maj": {"pattern": "1,#2,3,#4,5,6,b7", "cn": "匈牙利大音阶", "en": ""},
        "hungarian_min": {"pattern": "1,2,b3,#4,5,b6,7", "cn": "匈牙利小音阶", "en": ""},
        "bibop": {"pattern": "1,2,3,4,5,6,b7,7", "cn": "比波普属音阶", "en": ""},
        "india": {"pattern": "1,2,3,4,5,b6,b7", "cn": "印度音阶", "en": ""},
        "jap": {"pattern": "1,3,4,6,7", "cn": "日本音阶", "en": ""},
        "russia": {"pattern": "1,b2,2,b3,4,5,b6,6,b7,7", "cn": "俄罗斯音阶", "en": ""},
        "arabian": {"pattern": "1,b2,3,4,5,b6,b7", "cn": "阿拉伯音阶", "en": ""},
        "oriental": {"pattern": "1,b2,3,4,b5,6,b7", "cn": "东方音阶", "en": ""},
        "spanish": {"pattern": "1,b2,b3,3,4,b5,b6,b7", "cn": "西班牙音阶", "en": ""},
    }

    @classmethod
    def make_chord(cls, chord_name):
        if len(chord_name) >= 2 and chord_name[1] in "b#":
            root = chord_name[:2]
            chord_tag = "X" + chord_name[2:]
            return cls.parse(root, cls.chord_map[chord_tag])
        else:
            root = chord_name[0]
            chord_tag = "X" + chord_name[1:]
            return cls.parse(root, cls.chord_map[chord_tag])

    @classmethod
    def make_scale(cls, scale_name):
        # scale_tag example: D#/blus
        root, tag = scale_name.split("/")
        return cls.parse(root, cls.scale_map[tag]["pattern"])

    @classmethod
    def chord_in_scale(cls, chord, scale):
        return all([bool(x in scale[1]) for x in chord[1]])

    @classmethod
    def find_scales_by_chord(cls, chord):
        scales = []
        for notes in cls.note_lst:
            for note in notes.split("/"):
                for attr in dir(cls):
                    if not attr.startswith("s_"):
                        continue
                    tmp_scale = getattr(cls, attr)(note)
                    if cls.chord_in_scale(chord, tmp_scale):
                        scales.append({
                            "root": note,
                            "scale": attr,
                            "notes": tmp_scale,
                        })
        return scales

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


if __name__ == "__main__":
    from pprint import pprint
    pprint(TheoryUtil.make_chord("Dbm7b5"))
    pprint(TheoryUtil.make_scale("D#/blus"))
