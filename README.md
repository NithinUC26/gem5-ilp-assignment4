# Assignment 4 (MSCS531): Exploring ILP with gem5

gem5 v25.1.0.1, X86, syscall-emulation mode.

- `benchmarks/`: C sources (int, fp, mem, branch, int1). Built with `gcc -O2 -fno-tree-vectorize -static` in a linux/amd64 Docker container.
- `configs/`: copies of gem5's `se.py` patched to set LocalBP size, O3 pipeline widths, and Minor issue limits from environment variables.
- `scripts/`: run scripts, config patch scripts, the stats table script, and `fetch_to_retire.py` (average fetch-to-retire latency from an O3PipeView trace).
- `results/`: `stats.txt` and `config.ini` for each run, plus the O3PipeView trace and its rendered timeline.
- `figures/`: cropped screenshots used in the report.

Run scripts from the gem5 root, after building `build/X86/gem5.opt`.
