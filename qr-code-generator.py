# Importing library
import qrcode
 
# Data to be encoded
data = 'https://www.americancodelab.com/info-form/'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('my-qrcode.png')