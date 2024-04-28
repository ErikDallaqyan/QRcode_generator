import qrcode # type: ignore
import qrcode.constants # type: ignore
https = input("Enter the https file:")

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size = int(input("Enter the box size:")),
                   border = int(input("Enter the border size")))

qr.add_data(str(https))
qr.make(fit=True)

img = qr.make_image(fill_colour="black", back_colour="white")
img.save("qrcode.png")