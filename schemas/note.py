# def noteEntity(item)->dict:
#     return{
#         "id":str(item("_id")),
#         "title":str(item("title")),
#         "desc":item["desc"]
#     }

# def notesEntity(items)->list:
#     return [noteEntity(item) for item in items]




def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item.get("title", "No title found"),
        "desc": item.get("desc", "No description found")
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]

