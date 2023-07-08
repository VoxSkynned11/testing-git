from pathlib import Path
import os, sys

if len(sys.argv) < 2:
    sys.exit("Usage: start.py <dir name>")


text = """<!DOCTYPE html>
<html lang="en">
  <head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">

  </head>
  <body>


	<script src="index.js"></script>
  </body>
</html>"""

cdir = Path.cwd()


ndir = sys.argv[1]

fdir = cdir / ndir

if not fdir.exists():
   fdir.mkdir()
else:
    sys.exit(f"directory {ndir} already exists")

with open(str(fdir / f'{ndir}.html'), 'w') as html:
    html.write(text)

js = open(str(fdir / 'index.js'), 'w')
js.close()

