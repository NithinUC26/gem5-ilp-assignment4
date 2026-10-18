import re, sys, glob, os
def get(txt, pat):
    m = re.search(r'^' + pat + r'\s+([0-9.eE+-]+)', txt, re.M)
    return float(m.group(1)) if m else None
print(f"{'run':34s}{'simSec(ms)':>11s}{'cycles':>12s}{'insts':>11s}{'IPC':>8s}{'CPI':>8s}")
for d in sorted(glob.glob(sys.argv[1] if len(sys.argv)>1 else 'm5out/a4_*')):
    f = os.path.join(d, 'stats.txt')
    if not os.path.exists(f): continue
    t = open(f).read()
    sec = get(t, r'simSeconds'); cyc = get(t, r'system\.cpu\.numCycles')
    if sec is None or cyc is None: continue
    ipc = get(t, r'system\.cpu\.ipc'); cpi = get(t, r'system\.cpu\.cpi')
    ins = get(t, r'system\.cpu\.committedInsts') or (cyc / cpi if cyc and cpi else 0)
    print(f"{os.path.basename(d):34s}{sec*1000:11.3f}{cyc:12.0f}{ins:11.0f}{ipc:8.3f}{cpi:8.3f}")
