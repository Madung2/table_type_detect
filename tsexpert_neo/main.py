# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import Dict
from docx import Document
from io import BytesIO
from services.table_detection import DocxTableTypeDetector
app = FastAPI()

# TABLE_TYPE = {
#     1: '1차원 가로', # 1D Horizontal
#     2: '1차원 세로', # 1D Vertical
#     3: '1차원 가로 복수', # 1D Horizontal plural keys
#     4: '2차원 RDB' #2D
# }
def detect_table_type(doc,table_idx):
    table = doc.tables[table_idx]
    detector = DocxTableTypeDetector(table)
    table_data = detector.table_extract
    type_num =detector.type_num
    type_name = detector.type_name_kor
    con1 = detector.first_col_is_all_keys
    con2 = detector.first_row_is_all_keys
    con3 = detector.key_cell_is_scatterd
    con4 = detector.exp_condition1
    return {'type_num':type_num, 'type_name': type_name, 'con1':con1, 'con2':con2,'con3':con3, 'con4':con4, 'tabel_data':table_data}



@app.post("/table_type/{table_idx}")
async def get_table_type(table_idx: int, file:UploadFile = File(...)):
    contents = await file.read()
    doc = Document(BytesIO(contents))
    detected = detect_table_type(doc, table_idx)
    return {"table_idx": table_idx, "detected": detected}

