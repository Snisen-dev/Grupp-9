from fastapi import FastAPI
import asyncio
import time

app = FastAPI

class Rum:
    RumID = int
    Bokat = bool
    '''Mer logik för vad rummen behöver för information'''


@app.get("/")
async def nonsens():
    '''Root'''
    return{'Message':'Tjena'}


@app.post("/Boka")
async def boka_rum():
    '''Logik för att boka ett rum'''

@app.get("/VetEj")
async def kolla_bokningar():
    '''Logik för att kolla vad som är bokat'''