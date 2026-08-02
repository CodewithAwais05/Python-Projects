import qrcode  # import the qrcode library

data = "https://www.google.com"  # string to be encoded in the QR code

qr = qrcode.QRCode(  # create a QR code object
    version = 1,  # version of the QR code (1-40)
    error_correction = qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size = 10,  # size of each box in pixels
    border = 4,  # border size in boxes
)

qr.add_data(data)  # add data to the QR code
qr.make(fit = True)  # generate the QR code
img = qr.make_image(fill_color = "black", back_color = "white")  # create an image from the QR code
img.save("google_qr.png")  # save the image as a PNG file

print("QR code created and saved as 'google_qr.png'")