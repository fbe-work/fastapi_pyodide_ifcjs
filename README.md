# fastapi pyodide ifcjs

## about
minimalistic example of Python ( [Pyodide](https://pyodide.org/en/stable/) ) in browser interaction<br>
with dom and ifc model via [ifcjs](https://github.com/IFCjs) Javascript library.

## steps
* install requirements into virtualenv
* start server via `uvicorn main:app --host 127.0.0.1 --port 8888`
* open in browser: `http://127.0.0.1:8888`
* load an ifc file with `Choose file` button
* paste demo code from pyodide_repl_paste.py to repl and run it
* see IfcSpace data (if available in ifc model) in console and on page
* interact with ifc content from pyodide repl...
