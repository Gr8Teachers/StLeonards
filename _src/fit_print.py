import json, subprocess, os
ROOT = '/home/claude/build'
langs = 'en ar my prs fa hi id ja km ko kmr ckb mn ne ps pt pa ru zh es sw ta th ti tr uk ur vi'.split()
steps = [0.86, 0.83, 0.80, 0.77, 0.74, 0.71, 0.68, 0.65]
zoom = {l: steps[0] for l in langs}
done = set()
os.makedirs(f'{ROOT}/pdf', exist_ok=True)

def pages(l):
    f = f'{ROOT}/site/index.html' if l == 'en' else f'{ROOT}/site/{l}/index.html'
    pdf = f'{ROOT}/pdf/{l}.pdf'
    subprocess.run(['google-chrome', '--headless', '--no-sandbox', '--disable-gpu', '--virtual-time-budget=3000',
                    f'--print-to-pdf={pdf}', 'file://' + f], capture_output=True)
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    return int([x for x in out.splitlines() if x.startswith('Pages')][0].split()[-1])

for i, z in enumerate(steps):
    todo = [l for l in langs if l not in done]
    if not todo:
        break
    for l in todo:
        zoom[l] = z
    json.dump(zoom, open(f'{ROOT}/zoom.json', 'w'), indent=0)
    subprocess.run(['python3', f'{ROOT}/build.py'], capture_output=True)
    for l in todo:
        if pages(l) == 1:
            done.add(l)
    print(z, 'fit so far:', len(done), 'remaining:', [l for l in langs if l not in done])
json.dump(zoom, open(f'{ROOT}/zoom.json', 'w'), indent=0)
subprocess.run(['python3', f'{ROOT}/build.py'], capture_output=True)
print(zoom)
