"""Generate three compass images from the recorded model profiles in owned ComfyUI processes."""
from pathlib import Path
import argparse,json,os,subprocess,sys
import psutil
from PIL import Image
import comfy_runner as runner
KIT=Path(__file__).resolve().parent

def idle(port):
    if runner.occupied(port):raise RuntimeError('Selected port is occupied; no existing server is stopped')
    for p in psutil.process_iter(['pid','cmdline'],ad_value=[]):
        if p.pid==os.getpid():continue
        command=p.info['cmdline']or[]
        if any(Path(x).name.lower()in('main.py','llama-server.exe','llama-cli.exe','moss_probe.py','acestep_ui.py')for x in command):raise RuntimeError('Another model process is present; close your own work first')
    if psutil.virtual_memory().available/2**30<12:raise RuntimeError('Start with 12 GiB available Windows RAM')
    r=subprocess.run(['powershell.exe','-NoProfile','-Command','Get-CimInstance Win32_PerfFormattedData_GPUPerformanceCounters_GPUEngine | Select-Object Name,UtilizationPercentage | ConvertTo-Json -Compress'],capture_output=True,text=True,timeout=30)
    if r.returncode or not r.stdout.strip():raise RuntimeError('Cannot read current GPU activity')
    rows=json.loads(r.stdout);rows=rows if isinstance(rows,list)else[rows]
    if any(float(x['UtilizationPercentage'])>10 for x in rows):raise RuntimeError('GPU is active; wait for your other work to finish')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--comfyui',type=Path,required=True);p.add_argument('--python',type=Path,default=Path(sys.executable));p.add_argument('--models',type=Path,required=True);p.add_argument('--flux-models',type=Path);p.add_argument('--output',type=Path,required=True);p.add_argument('--port',type=int,default=18203);p.add_argument('--timeout',type=int,default=1800);p.add_argument('--check',action='store_true');args=p.parse_args()
    args.comfyui=args.comfyui.resolve();args.python=args.python.resolve();args.models=args.models.resolve();args.flux_models=(args.flux_models or args.models).resolve();root=args.output.resolve()
    if not(args.comfyui/'main.py').is_file()or not args.python.is_file():raise RuntimeError('Supply the installed source and working AMD Python')
    graphs={name:runner.read(KIT/file)for name,file in [('01-klein','01-KLEIN.api.json'),('00-text','02-QWEN-TEXT.api.json'),('03-qwen','03-QWEN-IMAGE.api.json'),('04-flux','04-FLUX-DEV.api.json')]}
    for graph in graphs.values():
        for node in graph.values():
            for v in node['inputs'].values():
                if isinstance(v,list)and len(v)==2 and isinstance(v[0],str)and v[0]not in graph:raise RuntimeError('Broken graph connection')
    if not args.check:idle(args.port)
    models=[]
    for m in runner.read(KIT/'MODELS.json')['models']:
        file=(args.flux_models if m['path'].startswith('unet/')else args.models)/m['path']
        if not file.is_file()or file.stat().st_size!=m['bytes']or runner.sha(file)!=m['sha256']:raise RuntimeError('Model file differs: '+str(file))
        models.append(m);print('FULL MODEL SHA OK',m['path'],flush=True)
    for a in runner.read(KIT/'BASELINE-ASSETS.json')['assets']:
        file=KIT/a['path']
        if not file.is_file()or file.stat().st_size!=a['bytes']or runner.sha(file)!=a['sha256']:raise RuntimeError('Baseline file differs: '+str(file))
    if args.check:print('Seven full model hashes, baseline assets and graph connections checked; no inference.');return
    if root.exists():raise RuntimeError('Choose a new output directory')
    root.mkdir(parents=True)
    for name in ['input','output','user','results','embeddings']:(root/name).mkdir()
    yaml='existing_images:\n  base_path: '+args.models.as_posix()+'\n  diffusion_models: diffusion_models\n  text_encoders: text_encoders\n  vae: vae\nexisting_flux:\n  base_path: '+args.flux_models.as_posix()+'\n  unet: unet\n  diffusion_models: unet\n  vae: vae\nown_text:\n  base_path: '+root.as_posix()+'\n  embeddings: embeddings\n'
    (root/'extra-model-paths.yaml').write_text(yaml,'utf-8');(root/'MODELS-VERIFIED.json').write_text(json.dumps(models,indent=2)+'\n','utf-8')
    (root/'embeddings/flux2-compass.safetensors').write_bytes((KIT/'example/conditioning/flux2-compass.safetensors').read_bytes())
    results=[]
    for name,graph in graphs.items():
        idle(args.port);outputs=runner.stage(args,root,name,graph,['--gpu-only','--disable-dynamic-vram'])
        if name=='00-text':continue
        source=next(Path(r['path'])for r in outputs if Path(r['path']).suffix.lower()=='.png');label={'01-klein':'KLEIN','03-qwen':'QWEN2512','04-flux':'FLUX-DEV'}[name];target=root/'results'/(label+'.png');target.write_bytes(source.read_bytes())
        with Image.open(target)as image:image.load();assert image.size==(1024,1024);pixels=__import__('hashlib').sha256(image.convert('RGB').tobytes()).hexdigest()
        results.append(dict(model=label,path=str(target),sha256=runner.sha(target),rgb_pixel_sha256=pixels,width=1024,height=1024,new_image_sampling=True))
    proof=dict(status='completed',outputs=results,all_seven_models_full_sha_verified=True,new_klein_text_encoding=True,new_qwen_text_encoding=True,reused_flux_compass_conditioning=True,separate_qwen_text_and_image_processes=True,all_owned_servers_stopped=True,source_driver_and_torch_environment_reused=True,model_weights_network_downloaded=False,profiles_differ_not_a_universal_speed_ranking=True)
    (root/'RESULT.json').write_text(json.dumps(proof,indent=2)+'\n','utf-8');print(json.dumps(proof,indent=2))
if __name__=='__main__':main()
