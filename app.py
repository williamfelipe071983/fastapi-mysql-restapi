from fastapi import FastAPI
from routes.user import user

app = FastAPI(
        title= "My first API"
        
            
)

    


app.include_router(user)

