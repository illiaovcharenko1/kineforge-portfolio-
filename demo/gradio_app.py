#!/usr/bin/env python3
"""Kineforge public Gradio demo — mock inference only (no weights)."""

from __future__ import annotations

import random

import gradio as gr


def _mock_logits(seed: int, n: int) -> list[float]:
    rng = random.Random(seed)
    return [rng.uniform(-1, 1) for _ in range(n)]


def run_inference(
    proprio_dim: int,
    seed: int,
    emotion_0: float,
    emotion_1: float,
    checkpoint_path: str,
) -> str:
    _ = checkpoint_path
    lines = [
        "Mode: public mock (no weights, no prior DB)",
        "Architecture: multi-stream policy (fast / valence / slow)",
        "",
        f"proprio_dim: {int(proprio_dim)} | seed: {int(seed)}",
        f"affect: [{emotion_0:.3f}, {emotion_1:.3f}]",
        "",
        f"locomotion (16): argmax ~ {_mock_logits(seed, 16).index(max(_mock_logits(seed, 16)))}",
        f"breath (2): argmax ~ {_mock_logits(seed + 1, 2).index(max(_mock_logits(seed + 1, 2)))}",
        f"head (2): argmax ~ {_mock_logits(seed + 2, 2).index(max(_mock_logits(seed + 2, 2)))}",
        f"macro (4): argmax ~ {_mock_logits(seed + 3, 4).index(max(_mock_logits(seed + 3, 4)))}",
        "",
        "PDF: illiaovcharenko1.github.io/kineforge-portfolio-/kineforge_tech_report_v1.0.pdf",
        "Code: github.com/illiaovcharenko1/kineforge-portfolio-",
    ]
    return "\n".join(lines)


def build_ui() -> gr.Blocks:
    with gr.Blocks(title="Kineforge Policy Demo") as demo:
        gr.Markdown(
            """
# Kineforge — Multi-Stream Embodied Policy (Public Demo)

**~157K trainable** parameters + **frozen semantic priors** on **MuJoCo MJX**.
This demo is a **sanitized mock** — no proprietary weights or prior databases.
            """
        )
        with gr.Row():
            proprio_dim = gr.Slider(8, 128, value=32, step=1, label="Proprioception dim (mock)")
            seed = gr.Number(value=42, label="Random seed", precision=0)
        with gr.Row():
            emotion_0 = gr.Slider(-1, 1, value=0.2, label="Affect dim 0")
            emotion_1 = gr.Slider(-1, 1, value=-0.1, label="Affect dim 1")
        checkpoint_path = gr.Textbox(
            label="Checkpoint path (ignored in public mock)",
            placeholder="Private checkpoints not published",
        )
        out = gr.Textbox(label="Output", lines=12)
        btn = gr.Button("Run inference", variant="primary")
        btn.click(
            run_inference,
            inputs=[proprio_dim, seed, emotion_0, emotion_1, checkpoint_path],
            outputs=out,
        )
    return demo


if __name__ == "__main__":
    build_ui().launch()
