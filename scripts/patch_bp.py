src = open('configs/deprecated/example/se.py').read().split('\n')
out = ['import os as _os']
n = 0
for line in src:
    out.append(line)
    if line.strip().endswith('.createThreads()'):
        ind = line[:len(line) - len(line.lstrip())]
        obj = line.strip()[:-len('.createThreads()')]
        out.append(f"{ind}if _os.environ.get('LOCAL_SIZE'):")
        out.append(f"{ind}    {obj}.branchPred.conditionalBranchPred = LocalBP(localPredictorSize=int(_os.environ['LOCAL_SIZE']))")
        n += 1
open('configs/deprecated/example/se_bp.py', 'w').write('\n'.join(out))
print('patched', n, 'place(s)')
