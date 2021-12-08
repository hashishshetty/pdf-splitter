import PySimpleGUI as pysg
from PyPDF2 import PdfFileReader
from pdf_split import PdfSplitter

layout = [
    [pysg.Text('Choose a file'), pysg.Input(key = 'pdf', enable_events = True), pysg.FileBrowse(key = 'pdf', enable_events = True)],
    [
        pysg.Text('Start page'), pysg.Input(key = 'start', enable_events = True, disabled = True),
        pysg.Text('End page'), pysg.Input(key = 'end', enable_events = True, disabled = True)
    ],
    [
        pysg.Button('Split PDF', key = 'split', enable_events = True, disabled = True), 
        pysg.Button('Cancel')
    ]
]

window = pysg.Window('PDF Splitter', layout)

while True:
    event, values = window.read()
    if event in (pysg.WIN_CLOSED, 'Cancel'):
        break

    if event == 'pdf':
        if values['pdf'][-3:] != 'pdf':
            pysg.PopupError('Only a .pdf file is accepted. Please reupload a valid file.')
            window['pdf'].update('')
            window['end'].update(disabled = True)
        else:
            window['pdf'].update(disabled = True)
            file_path = values['pdf']
            pdf = PdfFileReader(open(file_path, 'rb'))
            number_of_pages = pdf.getNumPages()
            window['start'].update(disabled = False)

    if event == 'start' and values['start']:
        if len(values['start']) > 0 and values['start'][-1] not in ('0123456789'):
            window['start'].update(values['start'][:-1])
        else:
            page_start = int(values['start'])
            if page_start == 0 or page_start > number_of_pages:
                pysg.PopupError('The PDF has', number_of_pages, 'pages. Please provide a valid start page number.')
                window['start'].update('')
                window['end'].update(disabled = True)
            else:
                window['end'].update(disabled = False)
    
    if event == 'end' and values['end']:
        if len(values['end']) > 0 and values['end'][-1] not in ('0123456789'):
            window['end'].update(values['end'][:-1])
        else:
            page_end = int(values['end'])
            if page_end < page_start or page_end > number_of_pages:
                pysg.PopupError('The PDF has', number_of_pages, 'pages. Please provide a valid end page number larger than the start page number.')
                window['end'].update('')
            else:
                window['split'].update(disabled = False)

    if event == 'split':
        splitter = PdfSplitter()
        splitter.split(file_path, page_start, page_end)

window.close()