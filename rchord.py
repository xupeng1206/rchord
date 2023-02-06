from tkinter import *
from theory import Theory


class ChordRootNoteList(Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(10):
            btn = Button(self, text=f"Button {i}")
            btn.pack(fill=BOTH, expand=YES)


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

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    App().run()
