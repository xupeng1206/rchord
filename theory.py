class TheoryUtil:
    note_names = "CDEFGAB" * 3
    note_lst = ["C", "Db/C#", "D", "Eb/D#", "E", "F", "Gb/F#", "G", "Ab/G#", "A", "Bb/A#", "B"]
    note_lst_x3 = note_lst * 3

    simple_note_lst = ["1", "b2/#1", "2", "b3/#2", "3", "4", "b5/#4", "5", "b6/#5", "6", "b7/#6", "7"] + \
                      ["-", "b9", "9", "#9", "-", "11", "#11", "-", "b13", "13", "-", "-"]

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
        root_name = root.strip("#b")
        root_name_start = cls.note_names.index(root_name)
        ret_multi_notes = []
        ret_single_notes = []
        for s_note in pattern.split(","):
            note = cls.note_lst_x3[root_start+cls.note_index(cls.simple_note_lst, s_note)]
            ret_multi_notes.append(note)
            name = cls.note_names[root_name_start + int(s_note.strip("#b"))-1]
            ret_note = note
            for n in note.split('/'):
                if n.strip("#b") == name:
                    ret_note = n
                    break
            ret_single_notes.append(ret_note)
        return ret_single_notes, ret_multi_notes

    @classmethod
    def x(cls, root):
        return cls.parse(root, "1,3,5")

    @classmethod
    def x_min(cls, root):
        return cls.parse(root, "1,b3,5")

    @classmethod
    def x_aug(cls, root):
        return cls.parse(root, "1,3,#5")

    @classmethod
    def x_dim(cls, root):
        return cls.parse(root, "1,b3,b5")

    @classmethod
    def x_sus4(cls, root):
        return cls.parse(root, "1,4,5")

    @classmethod
    def x_sus2(cls, root):
        return cls.parse(root, "1,2,5")

    @classmethod
    def x_6(cls, root):
        return cls.parse(root, "1,3,5,6")

    @classmethod
    def x_maj7(cls, root):
        return cls.parse(root, "1,3,5,7")

    @classmethod
    def x_min_maj7(cls, root):
        return cls.parse(root, "1,b3,5,7")

    @classmethod
    def x_7(cls, root, color=[]):
        return cls.parse(root, ",".join(["1,3,5,b7", ",".join(color)]))

    @classmethod
    def x_min_7(cls, root):
        return cls.parse(root, "1,b3,5,b7")

    @classmethod
    def x_min7b5(cls, root):
        return cls.parse(root, "1,b3,b5,b7")

    @classmethod
    def x_dim7(cls, root):
        return cls.parse(root, "1,b3,b5,6")

    @classmethod
    def x_add9(cls, root):
        return cls.parse(root, "1,3,5,9")

    @classmethod
    def x_maj9(cls, root):
        return cls.parse(root, "1,3,5,7,9")

    @classmethod
    def x_min_maj9(cls, root):
        return cls.parse(root, "1,b3,5,7,9")

    @classmethod
    def x_9(cls, root):
        return cls.parse(root, "1,3,5,b7,9")

    @classmethod
    def x_min9(cls, root):
        return cls.parse(root, "1,b3,5,b7,9")

    @classmethod
    def x_11(cls, root):
        return cls.parse(root, "1,3,5,b7,9,11")

    @classmethod
    def x_min11(cls, root):
        return cls.parse(root, "1,b3,5,b7,9,11")

    @classmethod
    def x_13(cls, root):
        return cls.parse(root, "1,3,5,b7,9,11,13")

    # 自然大调
    @classmethod
    def s_maj_nature(cls, root):
        return cls.parse(root, "1,2,3,4,5,6,7")

    # 和声大调
    @classmethod
    def s_maj_harmonic(cls, root):
        return cls.parse(root, "1,2,3,4,5,b6,7")

    # 旋律大调
    @classmethod
    def s_maj_melodic(cls, root):
        return cls.parse(root, "1,2,3,4,5,b6,b7")

    # 自然小调
    @classmethod
    def s_min_nature(cls, root):
        return cls.parse(root, "1,2,b3,4,5,b6,b7")

    # 和声小调
    @classmethod
    def s_min_harmonic(cls, root):
        return cls.parse(root, "1,2,b3,4,5,b6,7")

    # 旋律小调
    @classmethod
    def s_min_melodic(cls, root):
        return cls.parse(root, "1,2,b3,4,5,6,7")

    # 伊奥尼亚 自然大调 调1
    @classmethod
    def s_ionian(cls, root):
        return cls.parse(root, "1,2,3,4,5,6,7")

    # 多利亚 调2
    @classmethod
    def s_dorian(cls, root):
        return cls.parse(root, "1,2,b3,4,5,6,b7")

    # 弗里几亚 调3
    @classmethod
    def s_phrygian(cls, root):
        return cls.parse(root, "1,b2,b3,4,5,b6,b7")

    # 利底亚 调4
    @classmethod
    def s_lydian(cls, root):
        return cls.parse(root, "1,2,3,#4,5,6,7")

    # 混合利底亚 调5
    @classmethod
    def s_mixolydian(cls, root):
        return cls.parse(root, "1,2,3,4,5,6,b7")

    # 爱奥尼亚 自然小调 调6
    @classmethod
    def s_aeolian(cls, root):
        return cls.parse(root, "1,2,b3,4,5,b6,b7")

    # 洛克里亚 调7
    @classmethod
    def s_locrian(cls, root):
        return cls.parse(root, "1,b2,b3,4,b5,b6,b7")

    # 全半减音阶
    @classmethod
    def s_full_half_dim(cls, root):
        return cls.parse(root, "1,2,b3,4,b5,b6,6,7")

    # 半全减音阶
    @classmethod
    def s_half_full_dim(cls, root):
        return cls.parse(root, "1,b2,b3,3,b5,5,6,b7")

    # 全音阶
    @classmethod
    def s_full(cls, root):
        return cls.parse(root, "1,2,3,#4,#5,#6")

    # 布鲁斯
    @classmethod
    def s_blus(cls, root):
        return cls.parse(root, "1,b3,4,b5,5,b7")

    # 混合布鲁斯
    @classmethod
    def s_mix_blus(cls, root):
        return cls.parse(root, "1,b3,3,4,b5,5,b7")

    # 辅助布鲁斯
    @classmethod
    def s_aux_blus(cls, root):
        return cls.parse(root, "1,2,b3,3,4,#4,5,6,b7")

    # 爵士小音阶
    @classmethod
    def s_jazz_min(cls, root):
        return cls.parse(root, "1,2,b3,4,5,6,7")

    # 蓝调大音阶
    @classmethod
    def s_blue_maj(cls, root):
        return cls.parse(root, "1,2,b3,4,b5,b6,7")

    # 大弗里几亚
    @classmethod
    def s_phrygian_dominant(cls, root):
        return cls.parse(root, "1,b2,3,4,5,b6,b7")

    # 大利底亚
    @classmethod
    def s_lydian_dominant(cls, root):
        return cls.parse(root, "1,2,3,#4,5,6,b7")

    # 超级洛克里亚
    @classmethod
    def s_super_locrian(cls, root):
        return cls.parse(root, "1,b2,b3,3,b5,b6,b7")

    # 吉普赛
    @classmethod
    def s_gypsy(cls, root):
        return cls.parse(root, "1,b3,#4,5,b6,b7")

    # 匈牙利大音阶
    @classmethod
    def s_hungarian_maj(cls, root):
        return cls.parse(root, "1,#2,3,#4,5,6,b7")

    # 匈牙利小音阶
    @classmethod
    def s_hungarian_min(cls, root):
        return cls.parse(root, "1,2,b3,#4,5,b6,7")

    # 比波普属
    @classmethod
    def s_bibop(cls, root):
        return cls.parse(root, "1,2,3,4,5,6,b7,7")

    # 印度音阶
    @classmethod
    def s_india(cls, root):
        return cls.parse(root, "1,2,3,4,5,b6,b7")

    # 日本
    @classmethod
    def s_jap(cls, root):
        return cls.parse(root, "1,3,4,6,7")

    # 俄罗斯
    @classmethod
    def s_russia(cls, root):
        return cls.parse(root, "1,b2,2,b3,4,5,b6,6,b7,7")

    # 阿拉伯
    @classmethod
    def s_arabian(cls, root):
        return cls.parse(root, "1,b2,3,4,5,b6,b7")

    # 东方音阶
    @classmethod
    def s_oriental(cls, root):
        return cls.parse(root, "1,b2,3,4,b5,6,b7")

    # 西班牙
    @classmethod
    def s_spanish(cls, root):
        return cls.parse(root, "1,b2,b3,3,4,b5,b6,b7")


if __name__ == "__main__":
    from pprint import pprint
    # chords
    pprint(TheoryUtil.x("C"))
    pprint(TheoryUtil.x_min("C"))
    pprint(TheoryUtil.x_sus2("C"))
    pprint(TheoryUtil.x_sus4("C"))
    pprint(TheoryUtil.x_dim("C"))
    pprint(TheoryUtil.x_aug("C"))
    pprint(TheoryUtil.x_7("C", color=["9"]))
    pprint(TheoryUtil.x_9("C"))
    pprint(TheoryUtil.x_7("C", color=["b9"]))

    # scales
    pprint(TheoryUtil.s_maj_nature("C"))
    pprint(TheoryUtil.s_maj_harmonic("C"))
    pprint(TheoryUtil.s_maj_melodic("C"))

    pprint(TheoryUtil.s_maj_nature("D"))
    pprint(TheoryUtil.s_maj_harmonic("D"))
    pprint(TheoryUtil.s_maj_melodic("D"))

    # chord in scale
    pprint(TheoryUtil.chord_in_scale(TheoryUtil.x("D"), TheoryUtil.s_maj_nature("D")))
    pprint(TheoryUtil.chord_in_scale(TheoryUtil.x_min("D"), TheoryUtil.s_maj_nature("D")))

    # find scale by chord
    pprint(TheoryUtil.find_scales_by_chord(TheoryUtil.x_maj7("F")))
