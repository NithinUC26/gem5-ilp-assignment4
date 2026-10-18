#!/bin/bash
# Baseline: 4 benchmarks x 2 CPU models (in-order Minor vs out-of-order O3)
for b in int fp mem branch; do
  for c in X86MinorCPU X86O3CPU; do
    out=m5out/a4_${b}_${c}
    echo "=== $b on $c ==="
    ./build/X86/gem5.opt --outdir=$out configs/deprecated/example/se.py \
      --cpu-type=$c --caches --l2cache -c a4/${b}_bench 2>&1 | grep -E "checksum|Exiting"
  done
done
