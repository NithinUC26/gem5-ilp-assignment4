src = open('configs/deprecated/example/se.py').read().split('\n')
out = ['import os as _os']
names = ['fetchWidth','decodeWidth','renameWidth','dispatchWidth','issueWidth','wbWidth','commitWidth']
n = 0
for line in src:
    out.append(line)
    if line.strip().endswith('.createThreads()'):
        ind = line[:len(line) - len(line.lstrip())]
        obj = line.strip()[:-len('.createThreads()')]
        out.append(f"{ind}if _os.environ.get('WIDTH'):")
        out.append(f"{ind}    for _nm in {names}:")
        out.append(f"{ind}        if hasattr({obj}, _nm):")
        out.append(f"{ind}            setattr({obj}, _nm, int(_os.environ['WIDTH']))")
        out.append(f"{ind}            print('set', _nm, _os.environ['WIDTH'])")
        n += 1
open('configs/deprecated/example/se_w.py', 'w').write('\n'.join(out))
print('patched', n, 'place(s)')
