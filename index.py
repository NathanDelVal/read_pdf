import pdfplumber
import pdfminer

laparams = {
    "char_margin":2.0,
    "line_margin":0.5,
    "word_margin":0.1,
    "boxes_flow":0,
    "detect_vertical":True
} 

pdf_content = ""

with pdfplumber.open("./WB/teste.pdf",laparams=laparams) as pdf:
    # print([x for x in range(len(pdf.pages[0].extract_words())) if "labo-" in pdf.pages[0].extract_words()[x]["text"] ])
    # print([x for x in pdf.pages[0].extract_words() if "labo-" in x["text"]])
    # print(pdf.pages[0].extract_words()[240])
    # print(pdf.pages[0].height)
    # print(pdf.pages[0].within_bbox((0,0, 0.5*pdf.pages[0].width, pdf.pages[0].height)).extract_text())
    for p in pdf.pages:
        pdf_content += "\n".join([f"{x['text']} [x:{str(x['x0'])},y:{str(round(x['doctop'], 2))}]" for x in p.extract_words(keep_blank_chars=True, use_text_flow=True, x_tolerance=6)])
        pdf_content += "\n<-------------- FIM DA PÁGINA ------------->\n\n"

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(pdf_content)
        
    
# with pdfplumber.open("teste1.pdf", laparams=laparams) as pdf:
# print(pdf.pages[0].within_bbox())
# for page in pdf.pages:
#     print(page.extract_text())