#!/usr/bin/env python3
"""artifact.html（Claudeのアーティファクト用）から、GitHub Pages用の index.html を作る。"""
import pathlib
here = pathlib.Path(__file__).parent
src = (here / "artifact.html").read_text(encoding="utf-8")
head, body = src.split("</style>", 1)
# アーティファクトの枠が入れてくれるリセットを自前で足す（[hidden] が無いとモーダルが出っぱなしになる）
head = head.replace("<style>", "<style>\nhtml{-webkit-text-size-adjust:100%}body{margin:0}img{max-width:100%}[hidden]{display:none!important}\n", 1)
out = ('<!DOCTYPE html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       '<meta name="robots" content="noindex,nofollow">\n' + head + "</style>\n</head>\n<body>" + body + "\n</body>\n</html>\n")
(here / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out))
