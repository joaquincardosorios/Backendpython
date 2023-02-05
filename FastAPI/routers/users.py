from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user",
                   tags=['users'])

## Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id= 1, name="Joaquin", surname="Rios", url="www.juako.com", age=33 ),
         User(id= 2, name="Kathleen", surname="Sta Teresa", url="www.kiam.com", age=32 ),
         User(id= 3, name="Bernardo", surname="Vasquez", url="www.berna.com", age=31 )]

@router.get("/sjson/")
async def usersjson():
    return [{"id": 1, "name" : "Joaquin", "surname" : "Rios", "url" : "www.juako.com" , "age" :33},
            {"id": 2, "name" : "Kathleen", "surname" : "Sta Teresa", "url" : "www.kiam.com", "age" :32},
            {"id": 3, "name" : "Bernardo", "surname" : "Vasquez", "url" : "www.berna.com", "age" :31}]

#Obtener todos los usuarios
@router.get("s/")
async def users():
    return users_list


@router.get("/{id}")                              # GET/Path
async def usersById(id: int):
    return searchUserById(id)

@router.get("/")                                 # GET/Query
async def user(id: int, name: str):
    return searchUserById(id)
    
@router.post("/", response_model=User,status_code=201)                # POST
async def user(user: User):
    if type(searchUserById(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    
    users_list.append(user)
    return(user)

@router.put("/", status_code=204)                                   # PUT
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        raise HTTPException(status_code=400, detail="No se ha actualizado el usuario")
    else:
        return user

@router.delete("/{id}", status_code=204)          # DELETE
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"error": "No se ha encontrado el usuario"}

def searchUserById(id: int):    
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}