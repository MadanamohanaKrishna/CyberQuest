from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "project": "CyberQuest",
        "version": "1.0",
        "status": "Sprint 0 Complete"
    }