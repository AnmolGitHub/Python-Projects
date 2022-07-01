from turtle import fillcolor
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=4)

qr.add_data("https://www.youtube.com/channel/UCvEPMLShPKN4QZqc7Nw_Q_g")
qr.make(fit=True)
img=qr.make_image(fill_color = "blue", back_color="green")
img.save("colorQR.png")