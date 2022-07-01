import qrcode as qr
img = qr.make("https://www.youtube.com/channel/UCvEPMLShPKN4QZqc7Nw_Q_g")
img.save("generatedQRcode.png")