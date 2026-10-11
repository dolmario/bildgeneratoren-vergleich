# Make the same compass with FLUX and Qwen

Use the same positive prompt, 1024-square output and fixed seed to try three recorded image profiles. Open the saved images side by side and follow each connected graph back to its model, text input and sampler. The profiles differ in model, quantization, guidance and step count; the examples are individual runs.

## Install the source

From the extracted kit, use the Python path of your working AMD ComfyUI environment:

```powershell
py -3.12 install_sources.py --python C:\AI\venv\Scripts\python.exe --output my-image-sources
```

The installer downloads pinned official ComfyUI and ComfyUI-GGUF source archives into a new folder and checks them. The recorded setup reuses the existing Windows AMD driver, Python and PyTorch environment. Versions are in `ENVIRONMENT.json`; source commits and checksums are in `SOURCES.json`.

## Put the model files in place

`MODELS.json` contains the seven model files, full checksums and pinned links. Model weights are separate downloads. For a single native graph, download its model group. The comparison runner uses all seven files. `download_models.py` can fetch all seven from their pinned links into one new model root.

- Klein: `diffusion_models/flux-2-klein-4b-fp8.safetensors`, `text_encoders/qwen_3_4b.safetensors`, `vae/flux2-vae.safetensors`.
- Qwen 2512: `diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors`, `text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors`, `vae/qwen_image_vae.safetensors`.
- FLUX dev: `unet/flux2-dev-Q4_K_M.gguf`, with the same FLUX VAE and the supplied compass conditioning.

The supplied FLUX conditioning comes from the actual text run in our first FLUX.2 tutorial. Its positive words are copied exactly into `PROMPT.txt`, the Klein graph and the Qwen text graph. For different FLUX words, use the separate text step in that first-image guide before choosing the new conditioning file.

## Run the three image profiles

```powershell
C:\AI\venv\Scripts\python.exe run_compare.py --comfyui .\my-image-sources\ComfyUI --python C:\AI\venv\Scripts\python.exe --models C:\Models --output my-compass-images
```

Use a new output directory. If your GGUF file is in another model root, add `--flux-models C:\OtherModels`; otherwise both roots default to `--models`. The runner checks full model and baseline-asset hashes, then runs four separate owned processes: Klein, Qwen text, Qwen image, and FLUX dev with the supplied conditioning. Each process is stopped before the next starts.

The finished images go into `results`. Requests, histories and timings remain beside them. Close your own other model work before starting. The runner checks current ports, model processes, GPU activity and available Windows RAM; it never stops an existing server.

## Follow the native graphs

- `01-KLEIN.json`: prompt, 4 steps, guidance 1, Euler, fixed seed 205932306, 1024×1024.
- `02-QWEN-TEXT.json`: encode the positive and negative text and save both conditioning files.
- `03-QWEN-IMAGE.json`: load those files, use 50 steps, CFG 4, Euler/simple, shift 3.1, the same seed and size.
- `04-FLUX-DEV.json`: supplied compass conditioning, 20 steps, guidance 4, Euler, the same seed and size.

For Qwen, close your own text process before starting the image process. Register the `embeddings` folder in your model-path configuration and copy both saved conditioning files into it. The recorded image processes use `--disable-pinned-memory --gpu-only --disable-dynamic-vram`.

The earlier FLUX compass reference is retained separately in `example/FLUX-DEV-REFERENCE.png`. The comparison runner samples a new FLUX image from that saved text; it does not treat copying the reference PNG as a new generation.

Model terms are linked from their primary sources: [Klein 4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4b-fp8), [Qwen-Image 2512](https://huggingface.co/Qwen/Qwen-Image-2512), and [FLUX.2 dev](https://huggingface.co/black-forest-labs/FLUX.2-dev). Qwen 2.1 is a different model and is outside this kit.
