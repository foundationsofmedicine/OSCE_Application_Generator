from OSCEgen import fileIO
from OSCEgen import generateQR as gqr
from OSCEgen import generatepages as gp


# VARIABLES GO HERE
baseURL = "http://foundationsofmedicine.github.io/clinicalmedicine/OSCE"

# Generates the public folder structure
fileIO.generatePublicFolderStructure()
fileIO.generateOSCEFolders()

# Generates QR codes for the prompt pages
OSCE_list = fileIO.retrieveOSCElist()
for item in OSCE_list:
    print(item)
    # generate QR codes
    gqr.generate_link_code(baseURL, item)
    # generate the pages
    gp.generate_examiner_pages(item)
    gp.generate_prompt_pages(item)
    gp.generate_actor_prompt_pages(item)


gp.generate_landing()
# gp.generate_randomiser()