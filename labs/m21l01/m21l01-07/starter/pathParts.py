from pathlib import Path

folder = Path('data')
folder.mkdir(exist_ok=True)
note = folder / 'note.txt'
print(note)
print(note.exists())

note.write_text('hello from pathlib\n', encoding='utf-8')
print(note.exists())
print(note.read_text(encoding='utf-8'), end='')
print(note.name, note.suffix, note.parent)

(folder / 'second.txt').write_text('two\n', encoding='utf-8')
for item in sorted(folder.iterdir()):
    print(item)
