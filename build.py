from pathlib import Path
import json, html
root=Path(__file__).resolve().parent
d=json.loads((root/'assets/profile.json').read_text(encoding='utf-8'))
e=lambda s:html.escape(str(s),quote=True)
def education(items):
 return ''.join(f'<article class="education-row"><img class="school-logo" src="{e(x["logo"])}" alt="{e(x["title"])} logo" width="24" height="24"><div><h3><a href="{e(x["url"])}">{e(x["title"])}</a></h3><p>{e(x["detail"])}</p></div><time>{e(x["date"])}</time></article>' for x in items)
def section(id,title,body): return f'<section id="{id}"><h2>{title}</h2>{body}</section>'
pubs=''
for p in d['publications']:
 authors=e(p['authors']).replace(e(d['name']),'<strong>'+e(d['name'])+'</strong>')
 links=''.join(f'<a class="text-link" href="{e(p[k])}">{label}</a>' for k,label in [('paper','Paper'),('code','Code')] if p[k])
 image=f'<a class="figure-link" href="{e(p.get("image_large",p["image"]))}" data-lightbox aria-haspopup="dialog" aria-label="View larger figure: {e(p["title"])}"><img class="publication-image" src="{e(p["image"])}" alt="Overview of {e(p["title"])}" loading="lazy"></a>' if p.get('image') else ''
 media_class=' with-image' if image else ''
 venue=e(p['venue'])
 pubs+=f'<article class="publication{media_class}">{image}<div><h3>{e(p["title"])}</h3><p class="authors">{authors}</p><p class="pub-summary">{e(p["text"])}</p><div class="pub-bottom"><span class="pub-venue">{venue}</span><div class="paper-links">{links}</div></div></div></article>'
news=''.join(f'<div class="news-row"><time>{e(n["date"])}</time><p>{e(n["text"])}</p></div>' for n in d['news'])
nav=[('about','About'),('news','News'),('education','Education'),('publications','Publications'),('awards','Awards')]
services=''
if d['services']:
 nav.append(('services','Services'));services=section('services','Academic Services','<ul>'+''.join('<li>'+e(s)+'</li>' for s in d['services'])+'</ul>')
navigation=''.join(f'<a href="#{id}">{label}</a>' for id,label in nav)
body=section('about','About Me', '<p class="intro">'+e(d['about'])+'</p>')
body+=section('news','News',news)+section('education','Education',education(d['education']))
body+=section('publications','Publications','<p class="small">* Equal contribution · † Corresponding author</p>'+pubs)
body+=section('awards','Awards & Honors','<ul class="awards">'+''.join('<li>'+e(a)+'</li>' for a in d['awards'])+'</ul>')+services
head=f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(d["name"])} | Academic Homepage</title><meta name="description" content="Xinzhen Yu, Biomedical Engineering at Shenzhen University. Computational pathology, multiple instance learning and medical AI."><link rel="canonical" href="https://easonyxz.github.io/"><link rel="icon" href="assets/favicon.png?v=8" type="image/png"><link rel="shortcut icon" href="favicon.ico?v=8"><link rel="stylesheet" href="assets/style.css?v=9">'
profile=f'<aside class="profile"><img class="profile-avatar" src="assets/avatar.jpg" alt="Xinzhen Yu" width="160" height="160"><h1>{e(d["name"])}</h1><p class="chinese">{e(d["name_cn"])}</p><p class="position">M.Sc. Student<br>Biomedical Engineering</p><p>Shenzhen University<br>Shenzhen, China</p><div class="social"><a href="mailto:{e(d["email"])}">Email</a><a href="{e(d["scholar"])}">Google Scholar</a><a href="{e(d["github"])}">GitHub</a></div></aside>'
page=f'<!doctype html><html lang="en"><head>{head}</head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="#about">Xinzhen Yu<span> / Homepage</span></a><nav aria-label="Main navigation">{navigation}</nav></header><div class="layout">{profile}<main id="main">{body}<footer>© 2026 {e(d["name"])} · <a href="mailto:{e(d["email"])}">Get in touch</a></footer></main></div><dialog class="lightbox" aria-label="Enlarged publication figure"><button type="button" class="lightbox-close" aria-label="Close enlarged figure">×</button><img class="lightbox-image" alt=""><p class="lightbox-caption"></p></dialog><script src="assets/main.js?v=9"></script></body></html>'
(root/'index.html').write_text(page,encoding='utf-8')
print('Built index.html from assets/profile.json')
