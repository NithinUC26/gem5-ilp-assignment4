#!/bin/bash
for s in 2 64 2048; do
  for b in branch int; do
    echo "=== $b, LocalBP size $s ==="
    LOCAL_SIZE=$s ./build/X86/gem5.opt --outdir=m5out/a4_bp_${b}_local${s} \
      configs/deprecated/example/se_bp.py --cpu-type=X86O3CPU \
      --caches --l2cache -c a4/${b}_bench 2>&1 | grep -E "checksum|Exiting|fatal|panic|Error"
  done
done
