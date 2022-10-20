import json

file_parse = "./Vocabulary_Dictionary_Adjective.json"
file_write = "utf_parsed_Adjective.json"

with open(file_parse, 'r', encoding='utf-8') as file:
    sampleData = json.load(file)
    with open(file_write, 'w', encoding='utf-8') as write_file:
        json.dump(sampleData, write_file, ensure_ascii=False)

# print(sampleData)