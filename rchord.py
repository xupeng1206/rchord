from tkinter import *
from theory import Theory


class GlobalState:
    scale_root = "C"
    scale_pattern = "Natural Maj"
    chord_root = "C"
    chord_pattern = "X"
    chord_bass = "C"


class ChordRootNoteList(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        scale_root_index = Theory.note_lst_x3.index(GlobalState.scale_root)
        nice_notes = Theory.make_scale(f"{GlobalState.scale_root}/{GlobalState.scale_pattern}")[1]

        for i in range(12):
            nice = False
            note = Theory.note_lst_x3[scale_root_index:scale_root_index+12][i]
            if note in nice_notes:
                nice = True
            note = note.split("/")[0]
            btn = Button(self, text=note)
            if nice:
                 btn.configure(bg="pink")
            btn.pack(side=TOP, fill=BOTH, expand=YES)
            setattr(self, f"note_{i}", btn)


class ChordBaseNoteList(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        scale_root_index = Theory.note_lst_x3.index(GlobalState.scale_root)
        nice_notes = Theory.make_chord(GlobalState.chord_pattern.replace("X", GlobalState.chord_root))[1]

        for i in range(12):
            nice = False
            note = Theory.note_lst_x3[scale_root_index:scale_root_index+12][i]
            if note in nice_notes:
                nice = True
            note = note.split("/")[0]
            btn = Button(self, text=note)
            if nice:
                 btn.configure(bg="pink")
            btn.pack(side=TOP, fill=BOTH, expand=YES)
            setattr(self, f"note_{i}", btn)



class Piano(Frame):

    def __init__(self, oct_num, **kwargs):
        super().__init__(**kwargs)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        for col_index in range(oct_num*14):
            self.columnconfigure(col_index, weight=1)
        for oct_index in range(oct_num):
            for note_index, note in enumerate(Theory.note_lst[:5]):
                shift = 14 * oct_index
                if note_index % 2 == 0:
                    note = f'{note}{oct_index}'
                    btn = Button(self, text="", bg="white", fg="black")
                    setattr(self, note, btn)
                    btn.grid(row=1, column=note_index+shift, columnspan=2, sticky="nesw", padx=1, pady=1)
                else:
                    note = note.split('/')[0]
                    note = f'{note}{oct_index}'
                    btn = Button(self, text="", bg="black", fg="white")
                    setattr(self, note, btn)
                    btn.grid(row=0, column=note_index+shift, columnspan=2, sticky="nesw", padx=1, pady=1)

            for note_index, note in enumerate(Theory.note_lst[5:12]):
                shift = 14 * oct_index + 6
                if note_index % 2 == 0:
                    note = f'{note}{oct_index}'
                    btn = Button(self, text="", bg="white", fg="black")
                    setattr(self, note, btn)
                    btn.grid(row=1, column=note_index+shift, columnspan=2, sticky="nesw", padx=1, pady=1)
                else:
                    note = note.split('/')[0]
                    note = f'{note}{oct_index}'
                    btn = Button(self, text="", bg="black", fg="white")
                    setattr(self, note, btn)
                    btn.grid(row=0, column=note_index + shift, columnspan=2, sticky="nesw", padx=1, pady=1)


class App:

    def __init__(self):
        self.app = Tk()
        self.app.title('rChord')
        self.app.geometry("600x450+2000+800")
        self.build()

    def build(self):
        piano = Piano(3, bg="gray")
        piano.master = self.app
        piano.pack(side=TOP, fill=BOTH, expand=True)

        chord_root_note_list = ChordRootNoteList()
        chord_root_note_list.master = self.app
        chord_root_note_list.pack(side=LEFT, fill=BOTH, expand=True)

        chord_bass_note_list = ChordBaseNoteList()
        chord_bass_note_list.master = self.app
        chord_bass_note_list.pack(side=LEFT, fill=BOTH, expand=True)

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    App().run()
