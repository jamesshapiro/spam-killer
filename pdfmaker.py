from fpdf import FPDF
import os
from dotenv import load_dotenv

load_dotenv()

my_name = os.environ.get('MY_NAME')
my_address = os.environ.get('MY_ADDRESS')
my_city = os.environ.get('MY_CITY')
my_state = os.environ.get('MY_STATE')
my_zip_code = os.environ.get('MY_ZIP_CODE')
my_spam_killer_email = os.environ.get('MY_SPAM_KILLER_EMAIL')

company_name = os.getenv('COMPANY_NAME')
company_address_line = os.getenv('COMPANY_ADDRESS_LINE')
company_address_street = os.getenv('COMPANY_ADDRESS_STREET')
company_address_city_state_zip = os.getenv('COMPANY_ADDRESS_CITY_STATE_ZIP')

pdf = FPDF(format='letter')
pdf.add_page()

pdf.set_font("Arial", size=12)

def add_line(text, space=10):
    pdf.cell(0, space, text, ln=True)

pdf.set_xy(10, 20)
pdf.set_text_color(255, 255, 255)
sender_info = [my_name, my_address, f"{my_city}, {my_state} {my_zip_code}",
               f"{my_spam_killer_email}"]
for line in sender_info:
    add_line(line, space=5)

# pdf.set_text_color(0, 0, 0)

recipient_info = [
    company_name, 
    company_address_street, 
    company_address_city_state_zip
]

for line in recipient_info:
    pdf.cell(0, 5, line, ln=True, align='C')
    # add_line(line, space=5)

pdf.set_text_color(0, 0, 0)
pdf.ln(16)
add_line("Date: November 10, 2023")
pdf.set_font("Arial", 'B', size=12)
add_line("Subject: Cease and Desist Notice for Unsolicited Mail")

pdf.set_font("Arial", size=12)
letter_body = [
    f"Dear {company_name},",
    "",
    "I am writing to formally request the immediate cessation of all unsolicited mail sent to my",
    f"address from {company_name}. Despite not consenting to such mailings, I have",
    "continually received them, which I consider to be an infringement on my personal",
    "privacy.",
    "",
    "Under Florida Statutes, individuals have the right to request the cessation of unsolicited",
    "mailings and expect compliance from businesses. In light of this, I demand that",
    f"{company_name}:",
    "",
    "1. Immediately stop sending all unsolicited mail to my address.",
    f"2. Provide a written assurance via email (to {my_spam_killer_email})",
    "within 15 days of receipt of this letter that you have ceased sending unsolicited ",
    "mail to my address.",
    "",
    "Failure to comply with these demands will leave me with no choice but to consider further legal",
    "action, including but not limited to filing a claim in small claims court in Florida. This",
    "action may seek compensation for any continued infringement on my privacy and any costs",
    "associated with pursuing this matter legally.",
    "",
    "I hope that this matter can be resolved amicably and without the need for further legal action.",
    "Please take this letter as a serious and urgent request.",
    "",
    "Sincerely,",
    "",
    f"{my_name}"
]

for line in letter_body:
    add_line(line, space=5)

# Save the pdf with name
pdf.output("Cease_and_Desist_Letter.pdf")
