# pyodide repl code: load ifc spaces info from file picker
import js
import asyncio
from js import document as doc


web_ifc = js.window.WebIFC
ifc_api = web_ifc.IfcAPI.new()
ifc_api.SetWasmPath("http://127.0.0.1:8888/static/wasm/ifcjs/", True)

await ifc_api.Init()

if not getattr(js.window, "ifc_text", None):
    print("please select an ifc file above, first")
else:
    uint8array = js.TextEncoder.new().encode(js.window.ifc_text)
    model_id = ifc_api.OpenModel(uint8array)
    all_lines = ifc_api.GetAllLines(model_id)
    for i in range(all_lines.size()):
        item_id = all_lines.get(i)
        elem = ifc_api.GetLine(model_id, item_id)
        ifc_class = elem.__proto__.constructor.name
        if ifc_class == "IfcSpace":
            ifc_guid = elem.GlobalId.value
            elem_name = elem.Name.value
            li = doc.createElement("li")
            li.textContent = f"{ifc_guid =}: {ifc_class =} {elem_name =}"
            doc.getElementById("element_list").appendChild(li)
            print(li.textContent)
