class ChordUtil:
    note_names = "CDEFGAB" * 3
    note_lst = ["C", "Db/C#", "D", "Eb/D#", "E", "F", "Gb/F#", "G", "Ab/G#", "A", "Bb/A#", "B"] * 3
    simple_note_lst = ["1", "b2/#1", "2", "b3/#2", "3", "4", "b5/#4", "5", "b6/#5", "6", "b7/#6", "7"] + \
                      ["-", "b9", "9", "#9", "-", "11", "#11", "-", "b13", "13", "-", "-"]

    @classmethod
    def note_index(cls, lst, target):
        for idx, ele in enumerate(lst):
            if target in ele.split("/"):
                return idx

    @classmethod
    def parse(cls, root, pattern):
        root_start = cls.note_index(cls.note_lst, root)
        root_name = root.strip("#b")
        root_name_start = cls.note_names.index(root_name)
        ret_notes = []
        for s_note in pattern.split(","):
            note = cls.note_lst[root_start+cls.note_index(cls.simple_note_lst, s_note)]
            name = cls.note_names[root_name_start + int(s_note.strip("#b"))-1]
            ret_note = note
            for n in note.split('/'):
                if n.strip("#b") == name:
                    ret_note = n
                    break
            ret_notes.append(ret_note)
        return ret_notes

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
    def x_7(cls, root):
        return cls.parse(root, "1,3,5,b7")

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


if __name__ == "__main__":
    print(ChordUtil.x("C"))
    print(ChordUtil.x_min("C"))
    print(ChordUtil.x_sus2("C"))
    print(ChordUtil.x_sus4("C"))
    print(ChordUtil.x_dim("C"))
    print(ChordUtil.x_aug("C"))
    print(ChordUtil.x_7("C"))
