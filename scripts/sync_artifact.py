"""Copia un atlas publicado como artifact de Claude a su carpeta del repo.

Uso: python3 scripts/sync_artifact.py <html_descargado_del_artifact> <carpeta>/index.html

Ajusta el HTML del artifact para GitHub Pages: pone <title> y lang en la cabecera,
quita la meta propia de Claude y sirve d3/topojson desde <carpeta>/vendor/.
"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf8").read()
t = re.search(r"<title>([^<]*)</title>", s).group(1)
s = s.replace("<!doctype html><html><head><meta charset=utf8>",
              f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{t}</title>', 1)
s = s.replace(f"<body>\n<title>{t}</title>", "<body>", 1)
s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "", 1)
s = s.replace("https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js", "vendor/d3.min.js")
s = s.replace("https://cdn.jsdelivr.net/npm/topojson-client@3.1.0/dist/topojson-client.min.js",
              "vendor/topojson-client.min.js")
open(dst, "w", encoding="utf8").write(s)
print(f"{dst}: {len(s)} caracteres")
