from datetime import date, datetime
from fpdf import FPDF

def write_pdf(person):


    pdf = FPDF()

    pdf.add_page()
    pdf.set_font(family = 'helvetica', size = 14)

    pdf.set_xy(x = 0, y = 0)
    pdf.image(name = '1.jpg', w = 210, h = 297.6, x = 0, y = 0)

    values = ['HONESTY', 'PERSEVERANCE', 'LOYALTY', 'COMPASSION']

    pdf.set_text_color(50)
    pdf.set_xy(x = 65.5, y = 55)
    pdf.cell(txt = person['NAME'])

    pdf.set_xy(x = 143.5, y = 55)
    pdf.cell(txt = person['LEVEL'])

    pdf.set_xy(x = 142.8, y = 66.7)
    pdf.cell(txt = f'{datetime.today().strftime("%x")}')

    pdf.set_xy(x = 64.5, y = 66.7)
    pdf.cell(txt = person['TUTOR'])



    pdf.set_fill_color(200)
    y = 95.7
    for value in values:

        pdf.set_font(style='B', size=12)
        pdf.set_xy(x = 52, y = y)
        pdf.cell(txt = f'  {value}',  fill = True, w = 50, h = 14)

        pdf.set_font(style='', size=8)
        pdf.set_xy(x = 107, y = y)
        pdf.cell(txt = '',  fill = True, w = 98.5, h = 14)
        pdf.set_xy(x = 107, y = y)
        pdf.multi_cell(txt = f'  {person[value]}',  fill = False, w = 98.5, h = 14, max_line_height=4)

        y += 17

#dif in height = 17

    y = 175.7
    subcom = list(person.keys())[7:]
    subjects =  []
    for item in subcom:
        if 'COMMENT' not in item:
            subjects.append(item)
    for subject in subjects:

        if person[subject] != '':

            pdf.set_font(style='B', size = 12)
            pdf.set_xy(x = 52, y = y)
            pdf.cell(txt = f'  {subject}',  fill = True, w = 50, h = 14)
            pdf.set_xy(x = 52, y = y)
            pdf.cell(txt = person[subject],  fill = False, w = 48, h = 14, align = 'R')

            pdf.set_font(style='', size=8)
            pdf.set_xy(x = 107, y = y)
            pdf.cell(txt = "",  fill = True, w = 98.5, h = 14)
            pdf.set_xy(x = 107, y = y)
            pdf.multi_cell(txt = f'  {person[f"{subject} COMMENT"]}',  fill = False, max_line_height=4, w = 98.5, h = 14)

            y += 17

    pdf.output(f'{person["NAME"]}.pdf')
    print(f'saved {person["NAME"]}')

    return True