from bs4 import BeautifulSoup as bs
import requests as r
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import itertools
import starlette.responses as _responses
import uvicorn

app = FastAPI()



#Disabling The CORS To Make The API Publicly Accessible
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)







base_url = "https://mp3quran.net/eng"
# The Home Endpoint
@app.get('/')
def home():
    return _responses.RedirectResponse('/docs')

# The Surah's Endpoint - Data Stores Locally Since It Would Slow The Server Down If it's Scrapped 
@app.get('/surahs')
def get_Surahs():
    surahs = {
        "AL-Fatihah": 1,
        "AL-Baqarah": 2,
        "AL-Imran": 3,
        "AL-Nissae": 4,
        "AL-Maidah": 5,
        "AL-Anaam": 6,
        "AL-Aaraf": 7,
        "AL-Anfal": 8,
        "AL-Taubah": 9,
        "Yunus": 10,
        "Hood": 11,
        "Yussuf": 12,
        "AL-Raad": 13,
        "Ibrahim": 14,
        "Al-Hidjr": 15,
        "Al-Nahl": 16,
        "Al-Israa": 17,
        "Al-Kahf": 18,
        "Maryam": 19,
        "Taha": 20,
        "Al-Anbiyaa": 21,
        "Al-Hadj": 22,
        "Al-Muminoon": 23,
        "Al-Noor": 24,
        "Al-Furqan": 25,
        "Al-Shuaaraa": 26,
        "Al-Naml": 27,
        "Al-Qasas": 28,
        "Al-Anqaboot": 29,
        "Al-Rom": 30,
        "Lukman": 31,
        "Al-Sadjdah": 32,
        "Al-Ahzab": 33,
        "Saba'": 34,
        "Fatir": 35,
        "Yassin": 36,
        "Al-Saffat": 37,
        "Sad": 38,
        "Al-Zumar": 39,
        "Ghafir": 40,
        "Fussilat": 41,
        "Al-Shura": 42,
        "Al-Zukhrof": 43,
        "Al-Dukhan": 44,
        "Al-Jathiya": 45,
        "Al-Ahqaf": 46,
        "Muhammad": 47,
        "Al-Fath": 48,
        "Al-Hujurat": 49,
        "Qaf": 50,
        "Al-Dhariyat": 51,
        "AL-Tor": 52,
        "AL-Najm": 53,
        "Al-QAmar": 54,
        "Al-Rahman": 55,
        "Al-Waqiaa": 56,
        "Al-Hadid": 57,
        "Al-Mujadilah": 58,
        "Al-Hashr": 59,
        "Al-Mumtahinah": 60,
        "Al-Saff": 61,
        "AL-Jumuaah": 62,
        "Al-Munafiqun": 63,
        "Al-Taghabun": 64,
        "Al-Talaq": 65,
        "Al-Tahrim": 66,
        "Al-Mulk": 67,
        "Al-Qalam": 68,
        "Al-Haqqah": 69,
        "Al-Maarij": 70,
        "Nooh": 71,
        "Al-Jinn": 72,
        "Al-Muzzammil": 73,
        "Al-Muddathir": 74,
        "Al-Qiyamah": 75,
        "Al-Insan": 76,
        "Al-Mursalat": 77,
        "Al-Naba'": 78,
        "Al-Naziaat": 79,
        "aabasa": 80,
        "Al-Takwir": 81,
        "Al-Infitar": 82,
        "Al-Mutaffifin": 83,
        "Al-Inshiqaq": 84,
        "Al-Buruj": 85,
        "Al-Tariq": 86,
        "Al-Aala": 87,
        "Al-Ghashiyah": 88,
        "Al-Fadjr": 89,
        "Al-Balad": 90,
        "Al-Shams": 91,
        "AL-Lail": 92,
        "Al-Duha": 93,
        "Al-Sharh": 94,
        "AL-Tin": 95,
        "Al-Alaq": 96,
        "Al-Qadr": 97,
        "Al-Bayyinah": 98,
        "Al-Zalzalah": 99,
        "Al-Aadiyat": 100,
        "AL-Qariaah": 101,
        "Al-Takathur": 102,
        "AL-Asr": 103,
        "AL-Humazah": 104,
        "Al-Fil": 105,
        "Quraish": 106,
        "Al-Maoun": 107,
        "AL-Kawthar": 108,
        "AL-Kafirun": 109,
        "Al-Nasr": 110,
        "AL-Massad": 111,
        "Al-Ikhlas": 112,
        "Al-Falaq": 113,
        "Al-Nas": 114,
    }
    return surahs


# The Readers Endpoint - Readers Fetched Using BS4 Web Scrapping From an External Website.
@app.get('/readers')
def get_readers():
    base_soup = bs(r.get(base_url).text,'lxml')
    readers_letters = base_soup.find('div',{"class":"reads-list"})
    letters = readers_letters.find_all('div', {"class": "home-read-group"})

    readers_groupped = []
    for letter in range(len(letters)):
        readers_group_item = letters[letter].find_all('a', href=True)
        readers_groupped.append(readers_group_item)


    # Collecting and Storing The Readers Names And Codes 
    readers_names = []
    readers_codes = []
    readers = {}
    try:
        for i in range(len(readers_groupped)+1):
            for x in readers_groupped[i]:
                readers[x.contents[0].strip()] = x["href"].split('/')[-1]
        

    except IndexError:
        pass

    return {"Reader : Code":readers}

# Get Surah Link Endpoint - Links Are Auto-Fetched(scrapped also :))  Based On The Users Specified Reader&Surah IDs. 
@app.get('/get-surah-link')
def get_surah_link(reader_code: str, surah_code: int):

    try:
        link = bs(r.get(
            f"{base_url}/{reader_code}/{str(surah_code)}").text, 'lxml').find("a", {"class": "download-btn"})['href']

        return {"link":link}

    except:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail={'msg':'Invalid Reader Code / Surah Code'})
# Server Prefrences learn more at 'https://fastapi.tiangolo.com/tutorial/'        
if __name__ == '__main__':
    uvicorn.run(app,port=8000,host='127.0.0.1')

