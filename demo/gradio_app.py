#!/usr/bin/env python3
"""
Public-safe Gradio demo for KineForge multi-stream policy.
Does NOT load proprietary prior databases. Optional local checkpoint via KINEFORGE_CHECKPOINT env.
"""

from __future__ import annotations

import os
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import gradio as gr

MOCK_MODE = True
NETWORK = None

try:
    from kineforge_runtime.triune_neural_network import TriuneNeuralNetwork

    MOCK_MODE = False
except Exception:
    TriuneNeuralNetwork = None  # type: ignore


def _mock_logits(seed: int, n: int) -> list[float]:
    rng = random.Random(seed)
    return [rng.uniform(-1, 1) for _ in range(n)]


def run_inference(
    proprio_dim: int,
    seed: int,
    emotion_0: float,
    emotion_1: float,
    route_0: float,
    checkpoint_path: str,
) -> str:
    rng = random.Random(seed)
    features = [rng.uniform(-0.5, 0.5) for _ in range(max(8, proprio_dim))]
    root_embeddings = [rng.uniform(-0.1, 0.1) for _ in range(41)]
    pentagram_vector = [rng.uniform(-0.2, 0.2) for _ in range(22)]
    emotion_vector = [emotion_0, emotion_1] + [0.0] * 5

    ckpt = checkpoint_path.strip() or os.environ.get("KINEFORGE_CHECKPOINT", "")
    if not MOCK_MODE and ckpt and Path(ckpt).is_file():
        net = TriuneNeuralNetwork.from_checkpoint(ckpt, rng)
        logits = net.forward(features, root_embeddings, pentagram_vector, emotion_vector)
        actions, probs = net.sample(logits)
        lines = ["Mode: checkpoint inference", f"Checkpoint: {ckpt}", ""]
        for branch in ("locomotion", "breath", "head", "macro"):
            a = actions.get(branch, 0)
            p = probs.get(branch, [0.0])[a] if branch in probs else 0.0
            lines.append(f"{branch}: action={a} prob={p:.4f}")
        return "\n".join(lines)

    # Mock / public-safe path
    lines = [
        "Mode: public mock (no weights, no prior DB)",
        "Architecture: multi-stream policy (fast / valence / slow)",
        "",
        f"locomotion (16): argmax ~ {_mock_logits(seed, 16).index(max(_mock_logits(seed, 16)))}",
        f"breath (2): argmax ~ {_mock_logits(seed + 1, 2).index(max(_mock_logits(seed + 1, 2)))}",
        f"head (2): argmax ~ {_mock_logits(seed + 2, 2).index(max(_mock_logits(seed + 2, 2)))}",
        f"macro (4): argmax ~ {_mock_logits(seed + 3, 4).index(max(_mock_logits(seed + 3, 4)))}",
        "",
        "Set KINEFORGE_CHECKPOINT=/path/to/step_*.json for local private demo.",
    ]
    return "\n".join(lines)


def build_ui() -> gr.Blocks:
    with gr.Blocks(title="KineForge Policy Demo") as demo:
        gr.Markdown(
            """
# KineForge — Multi-Stream Embodied Policy (Public Demo)

Sample-efficient control with **frozen semantic priors** + **differentiable physics**.
This demo does **not** expose proprietary embeddings or full checkpoints.
            """
        )
        with gr.Row():
            proprio_dim = gr.Slider(8, 128, value=32, step=1, label="Proprioception dim (mock)")
            seed = gr.Number(value=42, label="Random seed", precision=0)
        with gr.Row():
            emotion_0 = gr.Slider(-1, 1, value=0.2, label="Affect dim 0")
            emotion_1 = gr.Slider(-1, 1, value=-0.1, label="Affect dim 1")
            route_0 = gr.Slider(-1, 1, value=0.0, label="Route dim 0 (display only in mock)")
        checkpoint_path = gr.Textbox(
            label="Checkpoint path (optional, local only)",
            placeholder="KINEFORGE_CHECKPOINT or path to step_*.json",
        )
        out = gr.Textbox(label="Output", lines=12)
        btn = gr.Button("Run inference", variant="primary")
        btn.click(
            run_inference,
            inputs=[proprio_dim, seed, emotion_0, emotion_1, route_0, checkpoint_path],
            outputs=out,
        )
    return demo


if __name__ == "__main__":
    demo = build_ui()
    demo.launch(server_name="127.0.0.1", server_port=int(os.environ.get("GRADIO_PORT", "7860")))
