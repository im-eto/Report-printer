   # PDF Report card printer
    #### Video Demo:  <URL HERE>
    #### Description:

    The project idea came as a possibility after the shitificate pset where I was introduced to the FPDF module that allows one to create PDFs in python. This project is done with a single module called FPDF and only requires "pip install fpdf2" to run and execute

    The program is not very complex but did take some time to get eveything exact it is custom made and can be adapted to fit other people's custom needs. For now the template needs the following csv format:   https://docs.google.com/spreadsheets/d/1nTGyIkVzLsvZ4FDMelhREGg9PCDB7yzSQZcF9P0n8Lc/edit?usp=sharing

    Withou the above format the outcome won't be as desired and changes to the code should need to be made. Should a user or client need the template changed a quick change to the pdf.py file should suffice (the program currently only requires a name paramater in the csv file but more requirements can be added)

    The project is designed for a client who though writing reports into a pdf for students is a waste of time and there has to be a quicker way of doing it, so I designed a python program that does all that with a simple provision of a csv file. So the causes the program to be very symplistic in narture but is designed with the idea of automation of a standard monotonous task.

    The cells are "fixed" for the most part and would need changing in the code to change I believe this would be possible to change more dynamically but would need further investigation into GUI and determining the positions on the pdf from that. For this client it was not needed and a simple fixed position from a given template will suffice.

    The pdf printing function is done in a seperate file so that it can be imported seperatly into different projects for ease of use. The PDFs are labled by name of the person who's report it is.