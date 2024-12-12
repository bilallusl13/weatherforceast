from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import requests
url=#enter url
api_key=#enteryourapikey
#icon_url=f'https://openweathermap.org/img/wn/{}@2x.png'
def weather_get(city):
    params={'q':city,'appid':api_key,'lang':'en'}
    data=requests.get(url,params=params).json()
    print(data)
    if data:
        sehir=data.get('name')
        icon=data.get('weather')[0].get('icon')
        acıklama=data.get('weather')[0].get('description')
        ulke=data.get('sys').get('country')
        sicaklik=round(data.get('main').get('temp')-273.15)
        return(sehir,icon,acıklama,ulke,sicaklik)

def havadurumu(city):
    sonuc = weather_get(city)
    if not sonuc:
        print("Hava durumu bilgisi alınamadı.")
        return
    print(sonuc)  # Kontrol etmek için sonucu yazdırın
    icon_url = f'https://openweathermap.org/img/wn/{sonuc[1]}@2x.png'
    try:
        icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url, stream=True).raw))
        label_icon.config(image=icon)
        label_icon.image = icon
        label_city.config(text=f'{sonuc[0]},{sonuc[3]}')
        label_temp.config(text=f'{sonuc[4]}  °C, {sonuc[2]}')
    except Exception as e:
        print(f"Simge yüklenirken hata oluştu: {e}")
sehirler_listesi=[]
window=Tk()
window.geometry("500x500")
window.config(bg='#6fa8dc')
combo_str=StringVar(value="select a city")
lst_sehirler={
    "Adana": "Adana",
    "Adıyaman": "Adıyaman",
    "Afyonkarahisar": "Afyonkarahisar",
    "Ağrı": "Ağrı",
    "Amasya": "Amasya",
    "Ankara": "Ankara",
    "Antalya": "Antalya",
    "Artvin": "Artvin",
    "Aydın": "Aydın",
    "Balıkesir": "Balıkesir",
    "Bilecik": "Bilecik",
    "Bingöl": "Bingöl",
    "Bitlis": "Bitlis",
    "Bolu": "Bolu",
    "Burdur": "Burdur",
    "Bursa": "Bursa",
    "Çanakkale": "Çanakkale",
    "Çankırı": "Çankırı",
    "Çorum": "Çorum",
    "Denizli": "Denizli",
    "Diyarbakır": "Diyarbakır",
    "Edirne": "Edirne",
    "Elazığ": "Elazığ",
    "Erzincan": "Erzincan",
    "Erzurum": "Erzurum",
    "Eskişehir": "Eskişehir",
    "Gaziantep": "Gaziantep",
    "Giresun": "Giresun",
    "Gümüşhane": "Gümüşhane",
    "Hakkari": "Hakkari",
    "Hatay": "Hatay",
    "Iğdır": "Iğdır",
    "Isparta": "Isparta",
    "İstanbul": "İstanbul",
    "İzmir": "İzmir",
    "Kahramanmaraş": "Kahramanmaraş",
    "Karabük": "Karabük",
    "Karaman": "Karaman",
    "Kars": "Kars",
    "Kastamonu": "Kastamonu",
    "Kayseri": "Kayseri",
    "Kırıkkale": "Kırıkkale",
    "Kırklareli": "Kırklareli",
    "Kırşehir": "Kırşehir",
    "Kilis": "Kilis",
    "Kocaeli": "Kocaeli",
    "Konya": "Konya",
    "Kütahya": "Kütahya",
    "Malatya": "Malatya",
    "Manisa": "Manisa",
    "Mardin": "Mardin",
    "Mersin": "Mersin",
    "Muğla": "Muğla",
    "Muş": "Muş",
    "Nevşehir": "Nevşehir",
    "Niğde": "Niğde",
    "Ordu": "Ordu",
    "Osmaniye": "Osmaniye",
    "Rize": "Rize",
    "Sakarya": "Sakarya",
    "Samsun": "Samsun",
    "Şanlıurfa": "Şanlıurfa",
    "Siirt": "Siirt",
    "Sinop": "Sinop",
    "Şırnak": "Şırnak",
    "Sivas": "Sivas",
    "Tekirdağ": "Tekirdağ",
    "Tokat": "Tokat",
    "Trabzon": "Trabzon",
    "Tunceli": "Tunceli",
    "Uşak": "Uşak",
    "Van": "Van",
    "Yalova": "Yalova",
    "Yozgat": "Yozgat",
    "Zonguldak": "Zonguldak"
}
for sehirler in lst_sehirler:
    sehirler_listesi.append([sehirler])
label_icon=ttk.Label(window,background='#6fa8dc',justify=CENTER)
label_icon.pack()
combo_sehirler=ttk.Combobox(window,values=sehirler_listesi,textvariable=combo_str,font=('calibri','24','bold'),justify=CENTER)
combo_sehirler.pack()
combo_sehirler.bind("<<ComboboxSelected>>", lambda event: havadurumu(combo_str.get()))
label_city=ttk.Label(window,background='#6fa8dc',font=('calibri','24','bold'),justify=CENTER)
label_city.pack()
label_temp=ttk.Label(window,background='#6fa8dc',font=('calibri','24','bold'),justify=CENTER)
label_temp.pack()

window.mainloop()