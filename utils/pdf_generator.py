from fpdf import FPDF

def generar_pdf(data, nombre_archivo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Reporte de Ventas", ln=True, align='C')
    for row in data:
        pdf.cell(200, 10, txt=str(row), ln=True)
    pdf.output(nombre_archivo)
