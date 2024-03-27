import requests as r
from fastapi import FastAPI, status, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import itertools
import starlette.responses as _responses
import uvicorn


app = FastAPI()


# Disabling The CORS To Make The API Publicly Accessible
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# The Home Endpoint
@app.get("/")
def home(request: Request):
    return _responses.RedirectResponse("/docs")


# Available Language Endpoint
@app.get("/langs")
def available_languages():
    langs = {
        "Arabic": "ar",
        "English": "eng",
        "French": "fr",
        "Russian": "ru",
        "German": "de",
        "Spanish": "es",
        "Turkish": "tr",
        "Chineese": "cn",
        "Farsi": "fa",
        "Portuese": "pt",
        "sweedish": "sw",
    }
    return langs


# The Surah's Endpoint
@app.get("/surahs")
def get_Surahs(lang: str):

    if str(lang.strip()) not in [
        "ar",
        "eng",
        "fr",
        "ru",
        "de",
        "es",
        "tr",
        "cn",
        "fa",
        "pt",
        "sw",
    ]:
        return {"Error": "Invalid Language Code"}

    else:

        res = r.get(
            f"https://mp3quran.net/api/v3/suwar?language={str(lang.strip())}"
        ).json()
        surahs = []

        for surah in res["suwar"]:
            surahs.append(
                {"id": surah["id"], "name": surah["name"], "makkiah": surah["makkia"]}
            )
        return surahs


# The Readers Endpoint
@app.get("/readers")
def readers(lang: str):

    if str(lang.strip()) not in [
        "ar",
        "eng",
        "fr",
        "ru",
        "de",
        "es",
        "tr",
        "cn",
        "fa",
        "pt",
        "sw",
    ]:
        return {"Error": "Invalid Language Code"}
    else:

        res = r.get(
            f"https://mp3quran.net/api/v3/reciters?language={str(lang.strip())}"
        ).json()
        readers = []
        for reader in res["reciters"]:
            readers.append(
                {
                    "id": reader["id"],
                    "name": reader["name"],
                    "surahs": reader["moshaf"][0]["surah_list"],
                }
            )
        return readers


# Get Available Surahs for s Specific Reader
@app.get("/reader_surahs")
def reader_surahs(lang: str, reader_id: int):

    if str(lang.strip()) not in [
        "ar",
        "eng",
        "fr",
        "ru",
        "de",
        "es",
        "tr",
        "cn",
        "fa",
        "pt",
        "sw",
    ]:
        return {"Error": "Invalid Language Code"}
    elif reader_id > 217 or reader_id < 1:
        return {"Error": "Invalid Reader ID"}
    else:
        res = r.get(
            f"https://www.mp3quran.net/api/v3/reciters?language={str(lang.strip())}&reciter={str(reader_id)}"
        ).json()
        return res["reciters"][0]["moshaf"][0]["surah_list"].split(",")


# Get Surah Link Endpoint
@app.get("/get_surah_link")
def surah_link(lang: str, reader_id: int, surah_id: int):

    if str(lang.strip()) not in [
        "ar",
        "eng",
        "fr",
        "ru",
        "de",
        "es",
        "tr",
        "cn",
        "fa",
        "pt",
        "sw",
    ]:
        return {"Error": "Invalid Language Code"}
    elif reader_id > 217 or reader_id < 0:
        return {"Error": "Invalid Reader ID"}
    elif surah_id < 1 or surah_id > 114:
        return {"Error": "Invalid Surah ID"}
    else:
        avs = r.get(
            f"https://www.mp3quran.net/api/v3/reciters?language={str(lang.strip())}&reciter={str(reader_id)}"
        ).json()
        av = avs["reciters"][0]["moshaf"][0]["surah_list"].split(",")
        if str(surah_id) in av:
            res = r.get(
                f"https://www.mp3quran.net/api/v3/reciters?language={str(lang)}&reciter={str(reader_id)}"
            ).json()
            link = res["reciters"][0]["moshaf"][0]["server"]
            i = 0
            if int(surah_id) < 10:
                i = f"00{surah_id}.mp3"
            elif int(surah_id) > 9 and int(surah_id) < 100:
                i = f"0{surah_id}.mp3"
            else:
                i = f"{surah_id}.mp3"

            return {"link": f"{link}{i}"}

        else:
            return {"Error": "This Reader Doesn't Have This Surah"}


# Server Prefrences learn more at 'https://fastapi.tiangolo.com/tutorial/'
if __name__ == "__main__":
    uvicorn.run(app, port=8212, host="127.0.0.1")
