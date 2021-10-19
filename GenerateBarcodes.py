import pandas as pd
from barcode import Code128
from barcode.writer import ImageWriter
dataFrame = pd.read_excel('TheCodes.xlsx')
results = list(dataFrame['codes'])
for item in results:
    codes = Code128(item, writer=ImageWriter())
    image = Code128.save(codes,f'barcode{item}.png')
