from asyncio import constants
import encodings
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
import pandas as pd


xls = pd.ExcelFile(r"New Sentences.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Banglish'].astype('string')


out_csv = []
output_file = "output_xl_new_sentences.xlsx"

for i in range(len(var1)):
    # out_csv = []
    # print(var1[1])

    try:
        # print(transliterate(data, sanscript.HK, sanscript.BENGALI))
        a =transliterate(var1[i], sanscript.HK, sanscript.BENGALI)
        out_csv.append(a)

        # with open(output_csv_file, "ab") as file:
        #     foo = f"\"{out_csv[0]}\",\n"
        #     file.write(foo.encode('utf-8'))

    except:

        print(f"{i} ==> expection", "="*20)
        continue



df3 = pd.DataFrame(out_csv,index=None)

with pd.ExcelWriter(output_file, mode='w') as writer:
    df3.to_excel(writer, sheet_name='Sheet1', header=None)

        



