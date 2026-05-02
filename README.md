# portfolio-site

> Professional portfolio showcasing biopharma computational research: antibody developability, protein engineering, glycoproteomics optimization, and CMC decision support projects.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## Overview

Static portfolio site built with vanilla HTML/CSS/JS. Loads project data from `projects.json` and renders interactive project cards with descriptions, key results, and links to GitHub repositories and live demos.

## Key content

| Section | Details |
|---------|---------|
| Research projects | 8 biopharma ML/computational projects with screenshots and briefs |
| Professional experience | Industry roles and research background |
| Publications | 8 publications including Nature Biotechnology |
| Education | PhD Chemistry |
| Skills | ML, mass spectrometry, protein engineering, regulatory science |

## Projects featured

- **ab-benchmark** — Antibody developability baseline benchmark (1,243 antibodies, 72 Spearman correlations)
- **constrained-cdr-gen** — Property-guided Gibbs sampling for CDR-H3 design (85% pass rate)
- **bo-protein-dms** — Discrete Bayesian optimization on GB1 DMS landscape
- **struct-devpred** — Descriptor ablation for developability prediction (180 experiments)
- **ProtePilot** — Developability decision orchestrator (10 molecule formats)
- **biologics-decision-engine** — Rule-based CMC decision support (600+ tests)
- **oglycan-optimizer** — EThcD parameter optimization for O-glycoproteomics
- **decision-engine-suite** — COU-first biomarker decision engine

## Preview locally

```bash
python3 -m http.server 8000
```

Then open http://127.0.0.1:8000. The page fetches `projects.json`, so preview over HTTP rather than `file://`.

## Deploy to GitHub Pages

1. Push this directory to the target Pages repository
2. In GitHub, open **Settings > Pages**
3. Select the branch and folder containing `index.html`
4. Save and wait for the Pages deployment

## License

MIT. See [LICENSE](LICENSE).
