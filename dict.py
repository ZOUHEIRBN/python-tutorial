notes = {
    "Math": 19,
    "PC": 16,
    "Fr": 17
}

print(notes)
notes.pop("Fr")
print(notes)
notes['SVT'] = 10
print(notes)

#In specific
for k in ['Math', 'SVT', 'PC']:
    print(k, ':', notes[k])