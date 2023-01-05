import qrcode

#制作的二维码内容
img=qrcode.make("zevin")
img.save('qrcode.png')