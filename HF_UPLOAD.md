# Hugging Face Space upload

## Error: `hf` CLI — `TypeError: type 'Choice' is not subscriptable`

Broken `typer` / `click` pair on Python 3.12. Fix:

```bash
pip install -U "click==8.1.7" "typer>=0.12.3"
```

Or skip `hf` CLI and use the script below.

## Upload (recommended)

```bash
export HF_TOKEN=hf_xxxxxxxx   # Write token from https://huggingface.co/settings/tokens
python3 "/Volumes/Samsung T7/urban-octo-broccoli-main/scripts/upload_hf_kineforge_space.py"
```

## Files uploaded

From `public_kineforge/space_upload/`:

- `README.md` — must include `python_version: 3.12.8`
- `requirements.txt` — gradio + optional `pyaudioop` for 3.13
- `app.py`

Then open Space → **Restart this Space**.
