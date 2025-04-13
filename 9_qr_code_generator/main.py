import qrcode



def qr_code(deta):
    img = qrcode.make(deta)
    img.save("qr_code.png")



qr_code("03272760036")