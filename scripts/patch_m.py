src = open('configs/deprecated/example/se.py').read().split('\n')
out = ['import os as _os']
names = ['decodeInputWidth','executeInputWidth','executeIssueLimit','executeCommitLimit']
n = 0
for line in src:
    out.append(line)
    if line.strip().endswith('.createThreads()'):
        ind = line[:len(line) - len(line.lstrip())]
        obj = line.strip()[:-len('.createThreads()')]
        out.append(f"{ind}if _os.environ.get('MINOR_W'):")
        out.append(f"{ind}    for _nm in {names}:")
        out.append(f"{ind}        if hasattr({obj}, _nm):")
        out.append(f"{ind}            setattr({obj}, _nm, int(_os.environ['MINOR_W']))")
        out.append(f"{ind}            print('set', _nm, _os.environ['MINOR_W'])")
        n += 1
open('configs/deprecated/example/se_m.py', 'w').write('\n'.join(out))
print('patched', n, 'place(s)')
