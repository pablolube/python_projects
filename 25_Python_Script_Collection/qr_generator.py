import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # CORRECT en mayúsculas
    box_size=7,
    border=2  # no boder, es border
)

qr.add_data('https://www.linkedin.com/in/pabloluberriaga/')
qr.make(fit=True)  # era mate, tiene que ser make

img = qr.make_image(fill_color='black', back_color='white')
img.save('syscurssQR.png')
