# bo-protein-dms

**Problem** Protein BO plans that operate on raw pooled PLM embeddings can fail silently and are hard to defend methodologically. The field needs a discrete, sequence-aware retrospective benchmark that shows whether structured BO strategies actually beat random search on a plate-sized campaign.

**Approach**
- Anchor scope to Decision Log 006: retrospective DMS benchmarking, not wet-lab, multi-objective, or raw-ESM BO.
- Represent sequences with one-hot features and Hamming-aware geometry rather than pooled embedding vectors.
- Compare `random`, `top_predicted_ridge`, `gp_hamming`, and `turbo_lite` under one campaign simulator.
- Aggregate best-fitness-found by query round across repeated seeds with bootstrap confidence intervals.

**Key results**
- The report benchmarked a 4-position x 20-AA landscape with 160,000 variants and `max_fitness = 5.991`. [Source: /Users/di/Projects/bo-protein-dms/reports/bo_dms_benchmark.md]
- At budget 96, `random` finished at 2.57 with 95% CI `[2.28, 2.87]`, while `top_predicted_ridge`, `gp_hamming`, and `turbo_lite` each reached 5.99 with CI `[5.99, 5.99]`, a 2.33x ratio over random. [Source: /Users/di/Projects/bo-protein-dms/reports/bo_dms_benchmark.md]
- `turbo_lite` reached about 90% of max in 31 rounds, `gp_hamming` in 32, `top_predicted_ridge` in 49, and `random` never did by budget 96. [Source: /Users/di/Projects/bo-protein-dms/reports/bo_dms_benchmark.md]
- The reported run used 20 seeds, finished in about 10 minutes on a laptop CPU, and reported $0 cloud cost. [Source: /Users/di/Projects/bo-protein-dms/reports/bo_dms_benchmark.md]
- The repo reports 52/52 passing tests at 70% coverage. [Source: /Users/di/Projects/bo-protein-dms/reports/bo_dms_benchmark.md]

**Reproduce**
```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"
python -m bo_dms.cli --dataset synthetic --seeds 20 --budget 96 --n-init 8 --strategies random top_predicted_ridge gp_hamming turbo_lite --out-dir reports
```

**Status** `in-progress`

**Links**
- GitHub: https://github.com/susiefirst-maker/bo-protein-dms
- Portfolio: TODO
