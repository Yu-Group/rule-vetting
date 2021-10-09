# Read in the file
with open('index.html', 'r') as f:
    data = f.read()

# Fix a url
data = data.replace('&lt;https://github.com/csinva/imodels</code>&gt;',
                    'https://github.com/csinva/imodels</code>')
data = data.replace('&lt;https://doi.org/10.5281/zenodo.4026887}&gt;',
                    'https://doi.org/10.5281/zenodo.4026887}')

data = data.replace('<h1>Index</h1>',
                    '<h1>Index 🔍</h1>')

data = data.replace('<a href="https://csinva.github.io/imodels/">Docs</a>',
                    '<a href="https://github.com/Yu-Group/medical-rules">Github</a>')

data = data.replace('.html">imodels.', '.html">')
data = data.replace('<h1 class="title">Package <code>mrules</code></h1>', '') # remove header
# data = data.replace('<th>Reference</th>', '<th white-space: nowrap>Reference</th>')

# add github corner
data = data.replace('<head>', "<head>\n<link rel='icon' href='https://csinva.io/imodels/docs/favicon.ico' type='image/x-icon'/ >\n")
data += '<a href="https://github.com/Yu-Group/medical-rules" class="github-corner" aria-label="View source on GitHub"><svg width="120" height="120" viewBox="0 0 250 250" style="fill:#70B7FD; color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="m128.3,109.0 c113.8,99.7 119.0,89.6 119.0,89.6 c122.0,82.7 120.5,78.6 120.5,78.6 c119.2,72.0 123.4,76.3 123.4,76.3 c127.3,80.9 125.5,87.3 125.5,87.3 c122.9,97.6 130.6,101.9 134.4,103.2" fill="currentcolor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style>'


data += '<link rel="stylesheet" href="github.css">'

# Write the file out again
with open('index.html', 'w') as f:
    f.write(data)

