import PySimpleGUI as sg
from identifier import Identifier

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [ [sg.Text('Please input text!'), sg.InputText(key='input')],
           [sg.Text('Output:'), sg.Text(key='output')],
           [sg.Button('OK'), sg.Button('close')],
        ]

# ウィンドウの生成
window = sg.Window('xxxbody identifier', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'close':
        break
    elif event == 'OK':
        id = Identifier()
        values['output'] = ' '.join(id.analyze(list(values['input'].split())))

    window['output'].update(values['output'])

window.close()
