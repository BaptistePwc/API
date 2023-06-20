import csv
import random
from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List, Optional

app = FastAPI()
security = HTTPBasic()

# Lecture des questions depuis le fichier CSV
def read_questions():
    questions = []
    with open('questions.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions

questions_db = read_questions()

@app.get("/")
def check_api():
    return {"message": "Bienvenue sur votre API de question"}

@app.post("/questions")
def create_question(question: dict, credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "4dm1N":
        raise HTTPException(status_code=401, detail="identifiant ou mot de passe incorrect")

    return {"message": "Question créée"}

@app.get("/questions")
def get_questions(
    use: Optional[str] = None,
    subjects: Optional[List[str]] = None,
    count: Optional[int] = 10,
    credentials: HTTPBasicCredentials = Depends(security)
):
    if credentials.username not in ["alice", "bob", "clementine"] or credentials.password != "wonderland":
        raise HTTPException(status_code=401, detail="identifiant ou mot de passe incorrect")

    filtered_questions = questions_db

    if use:
        filtered_questions = [q for q in filtered_questions if q["use"] == use]

    if subjects:
        filtered_questions = [q for q in filtered_questions if q["subject"] in subjects]

    random.shuffle(filtered_questions)

    return filtered_questions[:count]
