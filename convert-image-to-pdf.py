from PIL import Image
from datetime import datetime

import sys

def main():
	nameOfFileFromArgument = sys.argv[1]
	image = Image.open(nameOfFileFromArgument)
	imgPdf = image.convert('RGB')
	currentDate = str(datetime.now())
	dateTimeWithoutSpaces = currentDate.replace(" ", "")
	imgPdf.save('image'+dateTimeWithoutSpaces+'.pdf')
  

if __name__ == '__main__':
	main()