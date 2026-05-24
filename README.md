# kineforge-portfolio (public portfolio)

**Live site:** https://illiaovcharenko1.github.io/kineforge-portfolio-/  
**Repo:** https://github.com/illiaovcharenko1/kineforge-portfolio-  
**HF Space:** https://huggingface.co/spaces/Brightforge-Software-Inc/kineforge-demo

Safe public subset — **no weights, no roots_db, no topology JSON**.

## Contents

- `demo/` — Gradio public inference mock
- `paper/` — Tech report PDF (generate locally)
- `figures/` — SVG plots from Nebius experiments
- `LICENSE` — Apache-2.0 (suggested)

## Setup

```bash
pip install -r demo/requirements.txt
export PYTHONPATH=src   # only if using private submodule
python demo/gradio_app.py
```

## Build paper PDF

```bash
cd research_paper_resources/paper
# install MacTeX or use Overleaf with main.tex + appendix.tex + references.bib
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
cp main.pdf ../../public_kineforge/docs/kineforge_tech_report_v1.0.pdf
```

## What stays private

- proprietary prior databases, topology graphs, private runtime package
- Full private runtime package (not shipped)
- S3 credentials (use regional endpoint `storage.us-central1.nebius.cloud`)
