import pdfplumber
import pdfminer
import math

laparams = {
    "char_margin":2.0,
    "line_margin":0.5,
    "word_margin":0.1,
    "boxes_flow":0,
    "detect_vertical":True
} 

detailed_content = ""
raw_content = ""

with pdfplumber.open("./WB/teste.pdf",laparams=laparams) as pdf:
    for p in pdf.pages:
        raw_content += "\n".join([x['text'] for x in p.extract_words(keep_blank_chars=True, use_text_flow=True, x_tolerance=6)])
        raw_content += "\n\n"
        detailed_content += "\n".join([f"{x['text']} [x:{str(x['x0'])},y:{str(round(x['doctop'], 2))}]" for x in p.extract_words(keep_blank_chars=True, use_text_flow=True, x_tolerance=6)])
        detailed_content += "\n<-------------- FIM DA PÁGINA ------------->\n\n"
        # dict_content = {math.floor(x["x0"]):"" for x in p.extract_words(keep_blank_chars=True, use_text_flow=True, x_tolerance=6)}
        # print(dict_content)
    # print([x for x in range(len(pdf.pages[0].extract_words())) if "labo-" in pdf.pages[0].extract_words()[x]["text"] ])
    # print([x for x in pdf.pages[0].extract_words() if "labo-" in x["text"]])
    # print(pdf.pages[0].extract_words()[240])
    # print(pdf.pages[0].height)
    # print(pdf.pages[0].within_bbox((0,0, 0.5*pdf.pages[0].width, pdf.pages[0].height)).extract_text())

with open("commented_text.txt", "w", encoding="utf-8") as f:
    f.write(detailed_content)
        
with open("raw_text.txt", "w", encoding="utf-8") as f:
    f.write(raw_content)