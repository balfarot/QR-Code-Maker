#first project: QR Code Maker 1
#install a library called qrcode

import qrcode

#data that we want inside the qrcode
data = 'https://www.google.com/search?q=juice&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiR4YSm8sv1AhVED0QIHY8kAm0Q_AUoAnoECAIQBA&biw=914&bih=847&dpr=2'
#the code below encodes our message to qrcode
img = qrcode.make(data)
#save the ing file we created above in our computer
img.save('myqrcode.jpg')
