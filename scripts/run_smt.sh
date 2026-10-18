#!/bin/bash
for pair in "int fp" "int mem" "mem mem"; do
  set -- $pair
  echo "=== SMT: $1 + $2 ==="
  ./build/X86/gem5.opt --outdir=m5out/a4_smt_${1}_${2} configs/deprecated/example/se.py \
    --cpu-type=X86O3CPU --smt --caches --l2cache \
    --cmd="a4/${1}_bench;a4/${2}_bench" 2>&1 | grep -E "checksum|Exiting|fatal|panic|Error"
done
