"""Gera a versão embaralhada (minificada) do app a partir do arquivo legível.
uso: python3 build.py entrada.html saida.html"""
import re, subprocess, sys
ESB='/opt/npm-tools/node_modules/.bin/esbuild'
src=open(sys.argv[1], encoding='utf-8').read()
def esb(code, loader, extra=()):
    r=subprocess.run([ESB, f'--loader={loader}', '--minify', '--charset=utf8', *extra], input=code.encode(), capture_output=True)
    if r.returncode: sys.exit(r.stderr.decode())
    return r.stdout.decode().strip()
js=re.search(r'<script>(.*?)</script>', src, re.S).group(1)
css=re.search(r'<style>(.*?)</style>', src, re.S).group(1)
# IIFE: os nomes de todas as funções e variáveis viram letras
mjs=esb(js,'js',['--format=iife','--target=es2019','--legal-comments=none'])
mcss=esb(css,'css')
html=src.replace(js,'\x00JS\x00').replace(css,'\x00CSS\x00')
html=re.sub(r'<!--.*?-->','',html,flags=re.S)              # comentários
html=re.sub(r'\n\s+','\n',html)                              # recuos
html=re.sub(r'>\s*\n\s*<','><',html)                         # quebras entre tags
out=html.replace('\x00CSS\x00',mcss).replace('\x00JS\x00',mjs)
open(sys.argv[2],'w',encoding='utf-8').write(out)
print(f'{len(src)} -> {len(out)} bytes')
