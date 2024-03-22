from fpdf import FPDF
from datetime import datetime
from django.conf import settings
import os

def generateBonafideCertificate(student):
    name = student.user.username
    rollno = student.rollNumber
    batch = student.batch
    department = student.dep.department

    if student.gender == 'M':
        salutation = "Mr"
    else:
        salutation = "Ms"

    pdf = FPDF(format=(300, 200))
    pdf.set_font('Arial', 'B', 12)
    pdf.add_page()

    # border of certificate
    pdf.rect(x=5, y=5, w=290, h=190)

    # header image
    pdf.image('APP/img1.png', h=25, w=270, x=10, y=10)
    pdf.cell(h=30, w=270, txt='', ln=5)

    # title
    pdf.cell(txt='', w=73, h=25, ln=0)
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(txt="BONAFIDE CERTIFICATE", w=130, h=15, align='C', ln=1, border=1)

    pdf.set_font('Arial', '', 30)
    pdf.cell(txt='', w=10, h=20, align='C', ln=1)
    pdf.cell(txt='', w=50, h=20, align='C', ln=0)
    pdf.cell(txt=f"This is to certify that {salutation}. ", w=115, h=20, ln=0)

    # bold text
    pdf.set_font('Arial', 'B', 30)

    pdf.cell(txt=f"{name}", w=50, h=20, ln=1)

    # light text
    pdf.set_font('Arial', '', 30)

    pdf.cell(txt='', w=20, h=20, align='C', ln=0)
    pdf.cell(txt=f"Roll No. ", w=40, h=20, ln=0)
    # bold text
    pdf.set_font('Arial', 'B', 30)

    pdf.cell(txt=f"{rollno}  ", w=55, h=20, ln=0)

    # light text
    pdf.set_font('Arial', '', 30)

    pdf.cell(txt="was a student of the", w=100, h=20, ln=0)

    # bold text
    pdf.set_font('Arial', 'B', 30)

    pdf.cell(txt=f"{department}", w=30, h=20, ln=1)

    # light text
    pdf.set_font('Arial', '', 30)

    pdf.cell(txt='', w=40, h=20, align='C', ln=0)

    pdf.cell(txt=f"Class of this college during", w=130, h=20, ln=0)

    # bold text
    pdf.set_font('Arial', 'B', 30)

    pdf.cell(txt=f"{batch} .", w=40, h=20, ln=1)

    pdf.cell(w=10, h=15, txt='', ln=1)

    # light text
    pdf.set_font('Arial', '', 30)

    pdf.cell(txt=f'Date : {datetime.now().strftime("%Y-%m-%d")}', w=100, h=15, ln=0)
    pdf.cell(txt='', w=50, h=20, align='C', ln=0)
    pdf.image('APP/sign.png', w=100, h=20)

    # Generate unique filename based on current date and time
    current_time = datetime.now()
    filename = f'{student.rollNumber}{current_time.strftime("%Y-%m-%d_%H-%M-%S")}_certificate.pdf'
    
    # Path to the certificates folder within MEDIA_ROOT
    certificates_path = os.path.join(settings.MEDIA_ROOT, 'certificates')
    
    # Ensure the certificates folder exists, if not, create it
    if not os.path.exists(certificates_path):
        os.makedirs(certificates_path)
    
    # Save the file in the certificates folder
    certificate_file_path = os.path.join(certificates_path, filename)
    pdf.output(certificate_file_path)
    
    # Return the URL of the saved certificate file
    certificate_url = os.path.join('certificates', filename)
    return certificate_url
