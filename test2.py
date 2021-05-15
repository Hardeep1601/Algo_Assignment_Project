import imgkit
import pdfkit

# imgkit.from_url('http://google.com', 'out1.jpg')
pdfkit.from_file('map.html', 'out1.pdf')
# imgkit.from_string('Hello!', 'out3.jpg')