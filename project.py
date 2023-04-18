#from pdf import write_pdf
from datetime import date, datetime
from fpdf import FPDF
import csv
import sys

def main():

    try:
        fileName = str(input('file to read from: '))

    except ValueError:
        raise ValueError


    dictInfo = data_import(fileName)

    if not validate(dictInfo):
        sys.exit('Invalid data provided')

    for person in dictInfo:
        if not person["TUTOR"]:
            continue
        if person["NAME"] != 'Van Staden Jeanelle':
            continue
        if not write_pdf(person):
            print('something went wrong')
            sys.exit()


def data_import(fileName):

    if not fileName.endswith('.csv'):
        print('Invalid file type')
        sys.exit()

    DictInfo = []

    try:
        with open(fileName, 'r') as data:
            reader = csv.DictReader(data)
            for row in reader:
                DictInfo.append(row)
    except ValueError:
        raise ValueError
    except FileNotFoundError:
        raise FileNotFoundError

    return DictInfo


def validate(dictInfo):

    keys = list(dictInfo[0].keys())
    if 'NAME' not in keys:
        return False

    return True


def write_pdf(person):


    pdf = FPDF()

    pdf.add_page()
    pdf.set_font(family = 'Arial', size = 14)

    pdf.set_xy(x = 0, y = 0)
    pdf.image(name = '1.jpg', w = 210, h = 297.6, x = 0, y = 0)

    values = ['HONESTY', 'PERSEVERANCE', 'LOYALTY', 'COMPASSION']

    pdf.set_text_color(50)
    pdf.set_xy(x = 65.5, y = 57.5)
    pdf.cell(txt = person['NAME'], w=0)

    pdf.set_xy(x = 143.5, y = 57.5)
    pdf.cell(txt = person['LEVEL'],w=0)

    pdf.set_xy(x = 142.8, y = 69.2)
    pdf.cell(txt = f'{datetime.today().strftime("%x")}',w=0)

    pdf.set_xy(x = 64.5, y = 69.2)
    pdf.cell(txt = person['TUTOR'],w=0)



    pdf.set_fill_color(200)
    y = 95.7
    for value in values:

        pdf.set_font(family='Arial',style='B', size=12)
        pdf.set_xy(x = 52, y = y)
        pdf.cell(txt = f'  {value}',  fill = True, w = 50, h = 14)

        pdf.set_font(family='Arial', style='', size=8)
        pdf.set_xy(x = 107, y = y)
        pdf.cell(txt = '',  fill = True, w = 98.5, h = 14)
        pdf.set_xy(x = 108, y = y+0.5)
        pdf.multi_cell(txt = f'{person[value]}',  fill = False, w = 97.5, h = 3)

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
            #subject
            pdf.set_font(family='Arial',style='B', size = 12)
            pdf.set_xy(x = 52, y = y)
            pdf.cell(txt = f'  {subject}',  fill = True, w = 50, h = 14)
            pdf.set_xy(x = 52, y = y)
            pdf.cell(txt = person[subject],  fill = False, w = 48, h = 14, align = 'R')
            #comment
            pdf.set_font(family='Arial', style='', size=8)
            pdf.set_xy(x = 107, y = y)
            pdf.cell(txt = "",  fill = True, w = 98.5, h = 14)
            pdf.set_xy(x = 108, y = y+0.5)
            pdf.multi_cell(txt = f'{person[f"{subject} COMMENT"]}',  fill = False, w = 97.5, h = 3)

            y += 17

    pdf.output(f'{person["NAME"]}.pdf')
    print(f'saved {person["NAME"]}')

    return True



if __name__ == '__main__':
    main()