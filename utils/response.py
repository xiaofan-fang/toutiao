from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def success_response(message:str = "success",data = None):
    content = {
        "code": 200,
        "message":message,
        "data":data
    }
    #JSONResponse可以将字典类型的数据转化成json输出给前端，这里加上jsonable_encoder可以递归content
    #将里面的FastAPI,Pydantic,ORM对象转化成字典类型，使得JSONResponse正常响应
    return JSONResponse(content=jsonable_encoder(content))

