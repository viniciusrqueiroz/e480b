# E-480B Palco

App web para controlar o Roland E-480B (versão brasileira do E-300) por MIDI, focado no modo Palco.

## Pastas
- `src/index.html` — código legível (é aqui que editamos).
- `src/build.py` — gera a versão embaralhada a partir do `src/index.html` (usa esbuild).
- `public/index.html` — versão embaralhada, a única publicada pelo Netlify.
- `netlify.toml` — o Netlify publica só a pasta `public/` e desliga o cache.

O repositório é privado. Só a pasta `public/` vai para o site.
