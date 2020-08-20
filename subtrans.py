import PySimpleGUI as ui
import trans
import data

ui.theme("DarkAmber")

layout =[
    [ui.Text("Subtrans")],
    [ui.Text("--------------")],
    [ui.Text("select subtitle file.")],
    [ui.Input(key="file"),ui.FileBrowse(file_types=(("subtitle", "*.srt"),))],
    [ui.Text("select Language")],
    [ui.Combo(trans.getLanList(),key="lan")],
    [ui.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar'),ui.Text(text="",key='status',size=(20,1))],
    [ui.Button('Ok'), ui.Button('Cancel')],
    [ui.Text("by sandakelum priyamantha")]
    
]

window = ui.Window("Subtrans",layout)
progress_bar = window['progressbar']
# status_box = window['status']
while True:
    event,values = window.read()
    if event == ui.WIN_CLOSED or event == "Cancel":
        break
    try:
        # a = 0/1
        window.Element('status').Update(value="Loading...")
        trans.getFile(values["file"],values['lan'],progress_bar,window.Element('status'),ui)
    except Exception as e:
        print(e)
window.close()
