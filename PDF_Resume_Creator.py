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
    my_canvas.rect(63, 110, 490, 179, stroke=0, fill=1)   #gray box below
    my_canvas.setFillColor(colors.HexColor("#cd853f"))      #setting the color brown
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
    my_canvas.rect(63, 555, 490, 1, stroke=1, fill=1)     #first brown horizontal line at the PROFILE SUMMARY
    my_canvas.rect(63, 454, 490, 1, stroke=1, fill=1)       #2nd brown horizontal line at EDUCATION
    my_canvas.rect(63, 85, 490, 1, stroke=1, fill=1)        #3rd brown horizontal line at REFERENCES
    my_canvas.rect(63, 50, 490, 1, stroke=1, fill=1)        #4th horizontal line below REFERENCES
    my_canvas.rect(304, 133, 0.5, 115, stroke=1, fill=1)      #brown vertical line between info and skills
    my_canvas.drawImage(str(obj["image"]), 65, 650, width=100, height=100)  #image

    address = obj["address"]
    my_canvas.setFont('Arial(Body) - Bold', 10)
    my_canvas.setFillColor(colors.HexColor("#3d4035"))      #dark grey COLOR
    my_canvas.rect(215, 577, 0.2, 70, stroke=0, fill=1)     #line between add and contact
    my_canvas.rect(397, 577, 0.2, 70, stroke=0, fill=1)     #line between bday and contact
    my_canvas.rect(209, 537, 194, 32, stroke=0, fill=1)     #1st rect center for PRFILE SUMMARY
    my_canvas.rect(243, 438, 128, 32, stroke=0, fill=1)     #2nd rect center for EDUCATION
    my_canvas.rect(240, 70, 133, 32, stroke=0, fill=1)      #3rd rect center for REFERENCES
    my_canvas.rect(88, 268, 189, 32, stroke=0, fill=1)      #4th rect left for BASIC INFORMATION
    my_canvas.rect(328, 268, 189, 32, stroke=0, fill=1)      #4th rec right for TECHNICAL SKILLS
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
    my_canvas.setFont('Arial(Body) - Bold', 11.5)
    my_canvas.drawString(85, 413, "•    " + str(obj["education"][0]["strand"]))    #educ strand first bullet
    my_canvas.drawString(85, 347, "•    " + str(obj["education"][1]["strand"]))     #educ strand 2nd bullet
    my_canvas.setFont('Arial(Body)', 13)
    my_canvas.drawString(67, 519, str(obj["description"][0]["line1"])) #prof summary
    my_canvas.drawString(67, 501, str(obj["description"][0]["line2"]))  #prof summary
    my_canvas.drawString(67, 483, str(obj["description"][0]["line3"]))  #prof summary

    my_canvas.drawString(67, 63, "Available upon request.")    #References message

    my_canvas.setFont('Arial(Body)', 11.5)
    my_canvas.drawString(85, 395, "     " + str(obj["education"][0]["year"]))   #educ year first bullet
    my_canvas.drawString(85, 377, "     " + str(obj["education"][0]["address"]))    #educ address first bullet
    my_canvas.drawString(85, 329, "     " + str(obj["education"][1]["year"]))    #educ year first bullet
    my_canvas.drawString(85, 311, "     " + str(obj["education"][1]["address"]))    #educ address second bullet

    my_canvas.drawString(82, 238, "Birthplace:            " + str(obj["b_info"][0]["Birthplace"]))  #basic info
    my_canvas.drawString(82, 220, "Civil Status:          " + str(obj["b_info"][0]["Civil Status"])) #basic info
    my_canvas.drawString(82, 202, "Citizenship:          " + str(obj["b_info"][0]["Citizenship"]))    #basic info
    my_canvas.drawString(82, 184, "Father's Name:    " + str(obj["b_info"][0]["Father_Name"]))         #basic info
    my_canvas.drawString(82, 166, "Occupation:         " + str(obj["b_info"][0]["Occupation"]))         #basic info
    my_canvas.drawString(82, 148, "Mother's Name:    " + str(obj["b_info"][0]["Mother_Name"]))          #basic info
    my_canvas.drawString(82, 130, "Occupation:          " + str(obj["b_info"][0]["Occupation2"]))   #basic info

    my_canvas.drawString(318, 233, "• " + str(obj["skills"][0]["skill1"]))  #skill
    my_canvas.drawString(318, 212, "• " + str(obj["skills"][0]["skill2"]))  #skill
    my_canvas.drawString(318, 191, "• " + str(obj["skills"][0]["skill3"]))  #skill
    my_canvas.drawString(318, 170, "• " + str(obj["skills"][0]["skill4"]))  #skill
    my_canvas.drawString(318, 149, "• " + str(obj["skills"][0]["skill5"]))  #skill

    my_canvas.setFont('Arial(Body)', 16)
    my_canvas.setFillColor(colors.HexColor("#fefefa"))     #white COLOR for PROFILE SUMMARY, EDUCATION, BASIC INFORMATION, TECHNICAL SKILLS, AND REFERENCES
    my_canvas.drawString(234, 547, "PROFILE SUMMARY")
    my_canvas.drawString(260, 447, "EDUCATION")
    my_canvas.drawString(100, 278, "BASIC INFORMATION")
    my_canvas.drawString(348, 278, "TECHNICAL SKILLS")
    my_canvas.drawString(252, 80, "REFERENCES")
    my_canvas.save()


pdfmetrics.registerFont(TTFont('Arial(Body)', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial(Body) - Bold', 'Arialbd.ttf'))
obj = read_data()

if __name__ == '__main__':
    create_pdf('ARDIENTE_ELIJAHMAE.pdf', obj)   #setting of file name and prompting the execution of the function for the pdf which is create_pdf()