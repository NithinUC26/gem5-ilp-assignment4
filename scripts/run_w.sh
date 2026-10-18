#!/bin/bash
for w in 1 2 4 8; do
  for b in int fp mem branch; do
    echo "=== $b, width $w ==="
    WIDTH=$w ./build/X86/gem5.opt --outdir=m5out/a4_w${w}_${b} \
      configs/deprecated/example/se_w.py --cpu-type=X86O3CPU \
      --caches --l2cache -c a4/${b}_bench 2>&1 | grep -E "checksum|Exiting|fatal|panic|Error|^set "
  done
done
