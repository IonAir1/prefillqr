import config
import bitlyshortener
import qrcode
from PIL import Image
import pandas as pd


shortener = bitlyshortener.Shortener(tokens=config.bitly_token)


def generate_prefill(name, email): #generates a prefill link with the input
    url = config.forms_link.replace('=name', '=' + name)
    url = url.replace('=email', '=' + email)
    return(url)


def shorten(urls):
    urls= shortener.shorten_urls(urls)
    return urls


def generate_qr(url, name):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black").convert('RGB')
    img.save(config.destination + "/" + name + ".png")

    
def read_file():
    items = {}
    n = 0
    empty = False
    df = pd.read_excel(config.excel_file, header=None)
    
    while not empty:
        data = []
        data.append(df.iloc[n][0])
        data.append(df.iloc[n][1])
        data.append(df.iloc[n][2])
        items.update({data[0]: data})
        n += 1
        try:
            pd.isnull(df.iloc[n][0])
        except:
            empty = True
    return items


def run():
    data = read_file()
    urls = []

    for i in range(len(data.keys())):
        item = list(data)[i]
        last_name = data[item][0]
        first_name = data[item][1]
        email = data[item][2]
        url = generate_prefill(first_name + " " + last_name, email)
        data[item].append(url)
        urls.append(url)

    urls = shorten(urls)

    for i in range(len(data.keys())):
        item = list(data)[i]
        data[item].append(urls[i])
        generate_qr(urls[i], data[item][0])
    print(data)