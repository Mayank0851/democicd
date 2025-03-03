from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"HELLOOO": "INDIAAAA"}

@app.get("/print/{this}")
def print_this(this):
    print(this)
    return {"this": this}