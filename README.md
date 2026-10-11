# Make the same compass with FLUX and Qwen

Install pinned ComfyUI sources, put the seven model files in place, and generate three 1024-square compass images. Follow the actual connected graphs and compare the resulting PNGs. The prompt and seed stay the same; the recorded model, quantization, step count and guidance profiles differ.

- [Working comparison download](downloads/IMAGE-MODELS-KIT.zip)
- [Installation and four connected graphs](PRACTICE-IMAGE-MODELS/README.md)
- [Execution records](PRACTICE-IMAGE-MODELS/VALIDATION.json)

The runner uses separate Klein, Qwen text, Qwen image and FLUX image processes. The supplied FLUX text conditioning and earlier compass reference come from our first FLUX.2 tutorial; the runner samples a new FLUX image. Source installation reuses a working Windows AMD Python/PyTorch environment. Model weights are separate pinned downloads.

## Other comparison exercises

The earlier count, text, layout and transparency exercises remain available:

- [Deutsch](DE/START.md) · [English](EN/START.md)
- [DE exercise download](downloads/BILDVERGLEICH-DE.zip) · [EN exercise download](downloads/BILDVERGLEICH-EN.zip)

These are separate exercises. Their blank comparison record does not report new generator runs.
