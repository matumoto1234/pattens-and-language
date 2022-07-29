import PySimpleGUI as sg
from identifier import Identifier

sg.theme('LightBrown 1')   # デザインテーマの設定

FONT10 = ('Arial', 10)
FONT16 = ('Arial', 16)

# ウィンドウに配置するコンポーネント
layout = [
    [sg.Text('Please input text!', font=FONT16),
     sg.InputText(key='input', font=FONT16)],
    [sg.Text('Example1: XXX did I meet last week.', font=FONT10)],
    [sg.Text('Example2: I do not know XXX in this town.', font=FONT10)],
    [sg.HorizontalSeparator()],
    [sg.Text('Output:', font=FONT16), sg.Text(
        size=(50, 4), key='output', font=FONT16)],
    [sg.Button('OK', font=FONT16), sg.Button('close', font=FONT16)],
]

# ウィンドウの生成
window = sg.Window('xxxbody identifier', layout)

# イベントループ
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'close':
        break

    if event == 'OK':
        id = Identifier()
        values['output'] = ' '.join(id.analyze(list(values['input'].split())))

    window['output'].update(values['output'])

window.close()
