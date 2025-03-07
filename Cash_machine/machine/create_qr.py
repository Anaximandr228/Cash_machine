import qrcode


def generate_qr(filename):
        img = qrcode.make(f'http://192.168.0.103:8000/{filename}')
        img.save("media/QR-code/qr_code.png")