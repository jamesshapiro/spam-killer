import postgrid
import os
import base64
from dotenv import load_dotenv

load_dotenv()

# api_key = os.environ.get('POSTGRID_TEST_API_KEY')
api_key = os.environ.get('POSTGRID_LIVE_API_KEY')
postgrid.pm_key = api_key
my_first_name = os.environ.get('MY_FIRST_NAME')
my_last_name = os.environ.get('MY_LAST_NAME')
my_address = os.environ.get('MY_ADDRESS')
my_city = os.environ.get('MY_CITY')
my_state = os.environ.get('MY_STATE')
my_zip_code = os.environ.get('MY_ZIP_CODE')
my_spam_killer_email = os.environ.get('MY_SPAM_KILLER_EMAIL')

company_name = os.getenv('COMPANY_NAME')
company_address_line = os.getenv('COMPANY_ADDRESS_LINE') 

pdf_file_path = 'Cease_and_Desist_Letter.pdf'

to_contact = postgrid.Contact.create(
    company_name=company_name,
    address_line1=company_address_line,
    country_code='US'
)


from_contact = postgrid.Contact.create(
    first_name=my_first_name,
    last_name=my_last_name,
    address_line1=my_address,
    city=my_city,
    province_or_state=my_state,
    postal_or_zip=my_zip_code,
    country_code='US'
)

with open(pdf_file_path, 'rb') as pdf_file:
    # pdf_content = base64.b64encode(pdf_file.read()).decode('utf-8')
    letter = postgrid.Letter.create(
        to=to_contact.id,
        from_=from_contact.id,
        address_placement=None,
        template=None,
        pdf = pdf_file
    )


print(letter.status)
print(letter.__dict__)

# Cancel the letter
# letter = postgrid.Letter.delete(letter.id)

# Prints 'cancelled'
# print(letter.status)
