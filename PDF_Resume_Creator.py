from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
import json

#read the json file
def read_data():
    jsonfile = open('C:/Users/lenovo/PLD Assignments/Assignment9/my_json.json', 'r')
    jsondata = jsonfile.read()

    obj = json.loads(jsondata)
    return obj

def create_pdf(path, obj):
    my_canvas = canvas.Canvas(path, pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFillColor(colors.HexColor("#d3d3d3"))  #gray bg
    my_canvas.rect(0, 669, 1000, 500, stroke=0, fill=1)     #gray box above

    my_canvas.setFillColor(colors.HexColor("#cd853f"))
    my_canvas.rect(145, 677, 378, 56, stroke=0, fill=1) # brown border of white box
    my_canvas.setFont('Arial(Body)', 18)                #setting of font
    my_canvas.setFillColor(colors.HexColor("#fefefa"))  #white color
    my_canvas.rect(145, 680, 375, 50, stroke=0, fill=1)   #white rectangle
    my_canvas.setFillColor(colors.HexColor("#555555"))      #gray color for full name
    my_canvas.drawString(185, 707, str(obj["full_name"]))   #fullname
    my_canvas.setFont('Arial(Body)', 9)
    my_canvas.drawString(258, 690, str(obj["course"]))      #course below full name
    my_canvas.setStrokeColor(colors.HexColor("#cd853f"))    #brown color stroke
    my_canvas.setFillColor(colors.HexColor("#cd853f"))      #brown color fill
    my_canvas.rect(63, 648, 104, 104, stroke=1, fill=1)     #brown rectangle border for applicant picture
    my_canvas.drawImage(str(obj["image"]), 65, 650, width=100, height=100)  #image

    address = obj["address"]
    my_canvas.setFont('Arial(Body) - Bold', 10)
    my_canvas.setFillColor(colors.HexColor("#3d4035"))      #dark grey COLOR
    my_canvas.rect(215, 577, 0.2, 70, stroke=0, fill=1)     #line between add and contact
    my_canvas.rect(397, 577, 0.2, 70, stroke=0, fill=1)     #line between bday and contact
    my_canvas.rect(209, 537, 194, 32, stroke=0, fill=1)     #1st rect center

    my_canvas.drawString(110, 626, "Address") 
    my_canvas.drawString(260, 630, "Contact")
    my_canvas.drawString(260, 599, "E-mail")
    my_canvas.drawString(430, 617, "Date of Birth")

    my_canvas.setFont('Arial(Body)', 10)
    my_canvas.drawString(97, 613, str(address[0]["street"]))
    my_canvas.drawString(87, 600, str(address[0]["barangay"]))
    my_canvas.drawString(87.5, 587, str(address[0]["city & country"]))

    my_canvas.drawString(260, 617, "Phone: " + str(obj["contact"]))
    my_canvas.drawString(260, 586, str(obj["email"]))
    my_canvas.drawString(430, 604, str(obj["birthdate"]))

    my_canvas.save()


pdfmetrics.registerFont(TTFont('Arial(Body)', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial(Body) - Bold', 'Arialbd.ttf'))
obj = read_data()

if __name__ == '__main__':
    create_pdf('ARDIENTE_ELIJAHMAE.pdf', obj)