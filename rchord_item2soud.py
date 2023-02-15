import reapy as rpy
from reapy import reascript_api as rpi


class ReaperUtil:
    ChordTrackName = "__CHORD_TRACK__"
    ChordTrackMeta = "__CHORD_META__"

    @classmethod
    def parse_item_simple(cls):
        ReaperUtil.stop_play_all()
        chord, meta = ReaperUtil.select_chord_item()
        if None in [chord, meta]:
            return
        meta_s = meta.split('/')
        if len(meta_s) != 4:
            return
        notes = [int(x) for x in meta_s[3].split(",")]
        return notes

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
        keyboard_mode = 0  # virtualKeyboardMode
        channel = 0
        note_on = 0x90 + channel
        velocity = 96
        for note in notes:
            rpi.StuffMIDIMessage(keyboard_mode, note_on, note, velocity)

    @classmethod
    def stop_play_all(cls):
        keyboard_mode = 0  # virtualKeyboardMode
        channel = 0
        note_off = 0x80 + channel
        velocity = 0
        for note in range(0, 128):
            rpi.StuffMIDIMessage(keyboard_mode, note_off, note, velocity)


if __name__ == "__main__":
    ReaperUtil.play(ReaperUtil.parse_item_simple())
