---
title: KineForge
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 4.44.1
app_file: ../demo/gradio_app.py
pinned: false
license: apache-2.0
short_description: Public demo — embodied RL with frozen priors (mock inference)
---

# KineForge (public demo)

**KineForge** trains embodied policies with **~157K trainable parameters** and **~2.6M frozen semantic priors** on **MuJoCo MJX** — without human demonstrations.

This Space runs the **sanitized Gradio mock** from the [portfolio repo](https://github.com/illiaovcharenko1/kineforge-portfolio-). Weights and prior databases are **not** published.

## Highlights (Nebius H200, March 2026)

| Variant | Steps | env-steps/s | task reward |
|---------|-------|-------------|-------------|
| baseline | 100K | ~159 | ~0.70 |
| rich128_grounded | 100K | ~108 | ~0.70 |

## Links

- GitHub: https://github.com/illiaovcharenko1/kineforge-portfolio-
- Paper: see `paper/main.tex` in repo (Overleaf / arXiv pack)

## Citation (draft)

```bibtex
@techreport{kineforge2026,
  title={KineForge: Sample-Efficient Embodied Control with Frozen Semantic Priors},
  author={Ovcharenko, Illia},
  year={2026},
  note={Technical report v1.0}
}
```

## Limitations

- Simulation-only evidence in public materials
- Proprietary prior corpus withheld
- Demo does not load private checkpoints
