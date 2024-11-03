import FreeSimpleGUI as pSG
import time
import zipfile
import os

now = time.strftime('%Y%m%d')

label1 = pSG.Text('Select files to compress:')
input1 = pSG.Input()
chooseBtn1 = pSG.FilesBrowse('Choose')

label2 = pSG.Text('Select destination folder:')
input2 = pSG.Input()
chooseBtn2 = pSG.FolderBrowse('Choose')

compressBtn = pSG.Button('Compress!')

window = (pSG.Window('File Zipper',
                     layout=[[label1, input1, chooseBtn1],
                             [label2, input2, chooseBtn2],
                             [pSG.VPush()],
                             [pSG.Push(), compressBtn, pSG.Push()],
                             [pSG.VPush()]
                             ]
                     )
          )
while True:
    event, values = window.read()
    if event == pSG.WIN_CLOSED:
        break
    if event == 'Compress!':
        files = values[0].split(';')
        dest_folder = values[1]
        if files and dest_folder:
            zip_filename = os.path.join(dest_folder, f'Compressed-{now}.zip')
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for file in files:
                    zipf.write(file, os.path.basename(file))
            pSG.popup('Files compressed successfully!', title='Success')

window.close()

