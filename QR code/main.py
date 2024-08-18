import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

// Qr code generator
myqr = qrcode.make("www.youtube.com/watch?v=IUQVO97zcE0")
myqr.save("")

// Qr code reader
b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))
