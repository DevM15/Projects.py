import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make("www.youtube.com/watch?v=IUQVO97zcE0")
myqr.save("")

b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))