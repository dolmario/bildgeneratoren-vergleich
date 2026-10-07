"""Read local image properties only; never generates or edits an image."""
from pathlib import Path
import argparse,json,hashlib
from PIL import Image
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--image',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
s=Path(a.image).resolve();o=Path(a.output).resolve()
if o.exists():raise SystemExit('Existing report preserved; choose a new file')
with Image.open(s) as im:
 im.load();bands=im.getbands();alpha=im.getchannel('A') if 'A' in bands else None
 if alpha is None and 'transparency' in im.info:alpha=im.convert('RGBA').getchannel('A')
 alpha_extrema=list(alpha.getextrema()) if alpha else None
 nonopaque=sum(alpha.histogram()[:255]) if alpha else 0
 d={'input_name':s.name,'sha256':hashlib.sha256(s.read_bytes()).hexdigest(),'bytes':s.stat().st_size,'format':im.format,'mode':im.mode,'size':list(im.size),'has_alpha_data':alpha is not None,'alpha_extrema':alpha_extrema,'nonopaque_pixel_count':nonopaque,'has_actual_nonopaque_pixels':nonopaque>0,'prompt_compliance':'not automatically checked','visual_review':'required separately','inference_started':False,'input_edited':False}
o.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(d,ensure_ascii=False))
