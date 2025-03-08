import qrcode

from Cash_machine.settings import BASE_URL


def generate_qr(filename):
    img = qrcode.make(f'{BASE_URL}{filename}')
    img.save("media/QR-code/qr_code.png")
