import pandas as pd
from barcode import Code128
from barcode.writer import ImageWriter
dataFrame = pd.read_excel('TheCodes.xlsx')
results = list(dataFrame['codes'])
resultsStr = []
for result in results:
    resultsStr.append(str(result))
writer = ImageWriter()
for itemx in resultsStr:
    codes = Code128(itemx, writer)
    image = Code128.save(codes,f'barcode{itemx}.png')
