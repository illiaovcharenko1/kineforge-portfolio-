# Kineforge public demo

Gradio mock for the multi-stream policy (no weights, no prior DB in public repo).

```bash
pip install -r requirements.txt
python gradio_app.py
```

Optional local checkpoint (private repo only):

```bash
export KINEFORGE_CHECKPOINT=/path/to/step_10000.json
python gradio_app.py
```

Do not commit checkpoint files or proprietary databases to public GitHub.
