---
title: Kineforge Demo
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 4.44.1
python_version: 3.12.8
app_file: app.py
pinned: false
license: apache-2.0
short_description: Public mock — embodied RL with frozen priors (no weights)
---

# Kineforge (public demo)

**Kineforge** trains embodied policies with **~157K trainable parameters** and **~2.6M frozen semantic priors** on **MuJoCo MJX** — without human demonstrations.

This Space runs the **sanitized Gradio mock** from the [portfolio repo](https://github.com/illiaovcharenko1/kineforge-portfolio-). Weights and prior databases are **not** published.

## Highlights (Nebius H200, March 2026)

| Variant | Steps | env-steps/s | task reward |
|---------|-------|-------------|-------------|
| baseline | 100K | ~159 | ~0.70 |
| rich128_grounded | 100K | ~108 | ~0.70 |

## Links

- PDF: https://illiaovcharenko1.github.io/kineforge-portfolio-/kineforge_tech_report_v1.0.pdf
- GitHub: https://github.com/illiaovcharenko1/kineforge-portfolio-
- Site: https://illiaovcharenko1.github.io/kineforge-portfolio-/

## Citation (draft)

```bibtex
@techreport{kineforge2026,
  title={Kineforge: Sample-Efficient Embodied Control with Frozen Semantic Priors and Differentiable Physics},
  author={Ovcharenko, Illia},
  year={2026},
  note={Technical report v1.0, Brightforge Software Inc.}
}
```

## Limitations

- Simulation-only evidence in public materials
- Proprietary prior corpus withheld
- Demo does not load private checkpoints
