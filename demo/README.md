# KineForge Public Demo

Safe for portfolio: **no weights**, **no prior database**.

```bash
cd "/Volumes/Samsung T7/urban-octo-broccoli-main"
pip install -r demo/requirements.txt
export PYTHONPATH=src
python demo/gradio_app.py
# open http://127.0.0.1:7860
```

Optional private mode (local only):

```bash
export KINEFORGE_CHECKPOINT=remote_training_data/checkpoints/step_10000.json
python demo/gradio_app.py
```

Do not commit checkpoint files or `roots_db.json` to public GitHub.
