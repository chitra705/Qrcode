import pyqrcode
import png
from pyqrcode import QRCode

QR="https://shopy7petshopwithyouhc76.on.drv.tw/www.shop7pets.com/"
url=pyqrcode.create(QR)
url.png('qrcode.png', scale=7)