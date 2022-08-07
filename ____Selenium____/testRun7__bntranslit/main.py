from bntranslit import BNTransliteration

import pandas as pd
import re
# torch==1.12.1

xls = pd.ExcelFile(r"final_revision.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Banglish'].astype('string')



model_path = "bntranslit_model.pth"
bntrans = BNTransliteration(model_path)

# * ================= doc =================
# a = "amar  toh thake na bhi….as you wish ami clipboard use kori oita onk comfortable. apni use korle korte paren na korle nai…"
# for i in range(len(word)):
# output = bntrans.predict(word, topk=10)
# print(output)
# # output: ['আমি', 'আমী', 'অ্যামি', 'আমিই', 'এমি', 'আমির', 'আমিদ', 'আমই', 'আমে', 'আমিতে']
# * =======================================

out_csv = []
output_file = "output.xlsx"

# for i in range(len(unmodified)):
for i in range(len(var1)):
# for i in range(10):
    try:
        out_text = ""
        semi_mod = var1[i].replace('/', ' ')
        modified = re.split('\s+|\…|\.+|\?+|\,+|\&+|\-+|\:+|\(+|\)+|\।+|\“+|\”+|\’+|\;+|\++', semi_mod.lower())
        modified = list(filter(lambda x : x != '', modified))
        # print(modified)
        for i in range(len(modified)):
            output = bntrans.predict(modified[i], topk=1)
            # print(output)
            out_text = f"{out_text} {output[0]} " 
            # out_text = out_text + " " + output[0] + " "
    except:
        print(modified, " ",i)
        print("="*50)
        out_text = ""
    
    # print(out_text)
    out_text = out_text.strip()
    out_csv.append(out_text)


# df3 = pd.DataFrame(out_csv, index=None)

# with pd.ExcelWriter(output_file, mode='w') as writer:
#     df3.to_excel(writer, sheet_name='Sheet1', header=None)

for i in range(len(out_csv)):
    with open('output.csv', "ab") as file:
        foo = f"\"{out_csv[i]}\",\n"
        file.write(foo.encode('utf-8'))





# * file 
# for i in range(len(out_csv)):
#     with open('out.txt', 'a', encoding='utf-8') as file:
#         file.writelines(out_csv[i] + "\n")