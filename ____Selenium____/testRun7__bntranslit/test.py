from bntranslit import BNTransliteration

model_path = "bntranslit_model.pth"
bntrans = BNTransliteration(model_path)
output = bntrans.predict('xray', topk=10)
# for i in range(len(output)):
#     out = output[i].encode('utf8')
print(output)