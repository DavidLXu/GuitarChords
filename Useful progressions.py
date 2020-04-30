from pychord import Chord,ChordProgression


def progression(scale = "Cmaj",prog = "15634125"):
    chord = [0,1,2,3,4,5,6,7]
    chord[1] = Chord.from_note_index(note=1, quality="", scale=scale) 
    chord[2] = Chord.from_note_index(note=2, quality="m", scale=scale)
    chord[3] = Chord.from_note_index(note=3, quality="m", scale=scale)
    chord[4] = Chord.from_note_index(note=4, quality="", scale=scale)
    chord[5] = Chord.from_note_index(note=5, quality="", scale=scale)
    chord[6] = Chord.from_note_index(note=6, quality="m", scale=scale)
    chord[7] = Chord.from_note_index(note=7, quality="m7", scale=scale)
    p = ChordProgression([])
    for key in prog:
        p.append(chord[int(key)])
    print(p)

# 纸短情长
# progression("Dmaj",prog = "156341625")

progression("Gmaj")

# progression("Fmaj")
# progression("Gmaj")
# progression("Amaj")
