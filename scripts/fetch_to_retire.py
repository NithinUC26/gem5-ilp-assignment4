import sys
path = sys.argv[1] if len(sys.argv) > 1 else 'm5out/a4_trace/trace.out'
cycle = 500  # ticks per cycle (2 GHz)
fetch = None; lat = []
for line in open(path):
    if 'O3PipeView:fetch:' in line:
        fetch = int(line.strip().split('O3PipeView:fetch:')[1].split(':')[0])
    elif 'O3PipeView:retire:' in line and fetch is not None:
        r = int(line.strip().split('O3PipeView:retire:')[1].split(':')[0])
        if r > 0: lat.append((r - fetch) / cycle)
        fetch = None
print('instructions:', len(lat), ' average fetch-to-retire cycles: %.1f' % (sum(lat) / len(lat)))
