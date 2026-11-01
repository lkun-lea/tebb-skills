from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
files=list((root/'skills').glob('*/SKILL.md'))
assert files,'no skills'
for path in files:
    assert not path.is_symlink()
    text=path.read_text('utf-8')
    match=re.fullmatch(r'---\r?\n(.*?)\r?\n---\r?\n(.+)',text,re.S)
    assert match and match[2].strip(),path
    meta=dict(line.split(':',1) for line in match[1].splitlines() if ':' in line)
    assert meta.get('name','').strip()==path.parent.name,path
    assert meta.get('description','').strip(),path
print(f'{len(files)} skills validated')
