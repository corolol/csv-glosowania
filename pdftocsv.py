import tabula
import os

# df = tabula.read_pdf("dokument1.pdf", pages='all')[0]
# tabula.convert_into("dokument1.pdf", "dokument1.csv", output_format="csv", pages='all')
# print(df)

for x in os.listdir("pdfs"):
    if (x.endswith(".pdf")):
        df = tabula.read_pdf("./pdfs/" + x, pages='all', encoding="utf-8")
        print(df)
        tabula.convert_into("./pdfs/" + x, "csv/" + x.split(".pdf")[0] + ".csv", output_format="csv", pages='all')
        # os.system("mv '" + x + "' pdfs")
        # print(x)
        # print(df)
