import tabula
import os

# df = tabula.read_pdf("dokument1.pdf", pages='all')[0]
# tabula.convert_into("dokument1.pdf", "dokument1.csv", output_format="csv", pages='all')
# print(df)

for x in os.listdir("."): 
    if (x.endswith(".pdf")):
        os.system("mv '" + x + "' pdfs")
        # print(x)
        # print(df)