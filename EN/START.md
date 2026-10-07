# Compare image generators yourself

Use an already working image generator and existing Python3/Pillow for the optional file checker. This kit installs or downloads nothing. It teaches a small documented comparison, not a universal winner.

1. Extract completely, read AUFGABEN.json, QUELLEN.md and checker code. Four own prompts test object count, exact German text, spatial layout and actual alpha transparency.
2. Choose one task. Copy its prompt unchanged into your existing tool and keep the explicit criteria beside it. Beauty, face consistency and literal prompt compliance are separate ratings.
3. Record exact model/revision/quantisation and a model-compatible workflow. Existing FLUX installation/workflow guide: https://github.com/dolmario/flux-comfyui-lokal . Do not interchange incompatible loaders or encoders. This kit is not a new universal installation for five model families.
4. Record size, steps, CFG, sampler and scheduler. Equal seeds across different models do not give identical noise or images. Distilled and base models need different settings; equal steps are not automatically a fair comparison.
5. Try four documented repeats per candidate, for example seeds11,22,33,44 where supported. Keep failed and unattractive results. Mark missing seed controls or RGBA support explicitly.
6. Save original files and record full elapsed time including loading, then a separate warm run. Old own8-second and11-minute observations are archived examples, not a speed promise for your computer.
7. Inspect every count, literal character and placement. The new exact text includes both ö and ß; an old prompt claimed an umlaut test despite containing neither. Separate visual preference from factual compliance.
8. Run the file checker against the actual saved image:
```powershell
python ./BILD-DATEI-PRUEFEN.py --image ./my-image.png --output ./my-image-check.json
```
It reads dimensions, hash and alpha only. It neither edits images nor evaluates faces or lettering. Existing reports are preserved. A fully opaque alpha channel is not transparency; nonopaque pixels alone do not prove a clean cutout. A painted checkerboard has no actual transparency.
9. Fill DEIN-VERGLEICH.csv with model settings, exact files, criteria, preference, timings and errors. API success is not visual success. Our author-generated checker fixtures are not model benchmark outputs.
10. Separate local computation from cloud services. Check remote encoders/nodes and model-specific licences. Local generation is not automatically unfiltered, watermark-free or commercially unrestricted. Private references need separate care.
11. Choose for your actual task and documented constraints. Four tasks and four repeats do not establish a universal ranking. Own historical images remain archived observations; no fresh six-model run is claimed here.
