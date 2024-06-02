
from fastapi import FastAPI, Request, APIRouter, Form
from fastapi.responses import HTMLResponse
from config.db import conn
from fastapi.templating import Jinja2Templates
from schemas.note import notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")

# @note.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs = conn.PDFS.PDFS.find({})
#     newDocs = notesEntity(docs)
#     return templates.TemplateResponse(
#         "index.html", {"request": request, "newDocs": newDocs}
#     )

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    try:
        docs = conn.PDFS.PDFS.find({})
        newDocs = notesEntity(docs)
        if not newDocs:
            print("No documents found.")  # Debug: print if no documents are found
        return templates.TemplateResponse(
            "index.html", {"request": request, "newDocs": newDocs}
        )
    except Exception as e:
        print(f"An error occurred: {e}")  # Debug: print the error message
        return templates.TemplateResponse(
            "index.html", {"request": request, "newDocs": []}
        )
@note.post("/", response_class=HTMLResponse)
async def create_item(request: Request, title: str = Form(...), desc: str = Form(...), important: bool = Form(False)):
    new_note = {
        "title": title,
        "desc": desc,
        "important": important
    }
    conn.PDFS.PDFS.insert_one(new_note)
    docs = conn.PDFS.PDFS.find({})
    newDocs = notesEntity(docs)
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs}
    )

