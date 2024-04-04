from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.transaction import router as trans_router
from router.product import router as product_router

app = FastAPI()

# Allow all origins for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#Root greeting
@app.get("/")
async def root():
    return {"message": "Hello API"}
 
app.include_router(trans_router, prefix="/trans", tags=["trans"])
app.include_router(product_router, prefix="/product", tags=["product"])