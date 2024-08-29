from fastapi import FastAPI

app = FastAPI(title="Workout API")


@app.get("/")
async def root():
    return {"message": "Hello World"}
