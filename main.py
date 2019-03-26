from fpdf import FPDF
import arrow

class PDF(FPDF):
    def header(self):
        self.image('head.png', 0, 0, 210)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.ln(28)


    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Arial', '', 12)
epw = pdf.w - 2*pdf.l_margin
col_width = epw/4
th = pdf.font_size
pdf.ln(4*th)
pdf.set_font('Arial','B',15.0) 
pdf.cell(epw, 0.0, 'Informações da Versão', align='L')
pdf.set_font('Arial','',10.0) 
pdf.ln(4)

Client = ''
System = ''
Version= ''
DateNow = str(arrow.now().format('DD/MM/YYYY'))


data = [['Cliente :',Client],
['Sistema :',System],
['Versão :',Version],[
'Emitido em :',DateNow]
]

for row in data:
    for datum in row:
        pdf.cell(col_width, 2*th, str(datum), border=0)
    pdf.ln(2*th)
pdf.output('tuto2.pdf', 'F')
