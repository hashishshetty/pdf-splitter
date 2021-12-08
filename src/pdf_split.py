from os import remove
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

class PdfSplitter:
    def split(self, file_path: str, page_start: int, page_end: int):
        pdf = PdfFileReader(open(file_path, 'rb'))

        pdfs = []
        for i in range(page_start, page_end + 1):
            output = PdfFileWriter()
            output.addPage(pdf.getPage(i - 1))
            output_filename = '{}_page_{}.pdf'.format(file_path, i)
            pdfs.append(output_filename)
            with open(output_filename, 'wb') as stream:
                output.write(stream)

        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)
        merged_filename = '{}_page_{}-{}.pdf'.format(file_path[:-4], page_start, page_end)
        merger.write(merged_filename)
        merger.close()

        for pdf in pdfs:
            remove(pdf)