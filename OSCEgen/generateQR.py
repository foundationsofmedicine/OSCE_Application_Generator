import pyqrcode
import png

def generate_link_code(base_url, osce_id):
    qr = pyqrcode.create(base_url + "/" + osce_id + "/prompt")
    qr.png('./public/' + osce_id + "/prompt_qr.png", scale = 10)
    qr2 = pyqrcode.create(base_url + "/" + osce_id + "/actor_prompt")
    qr2.png('./public/' + osce_id + "/actor_prompt_qr.png", scale = 10)
    print("QR code generated for: " + osce_id)
    return