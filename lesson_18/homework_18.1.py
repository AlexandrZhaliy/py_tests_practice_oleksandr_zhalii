import requests
BASE_URL = "https://images-api.nasa.gov"

# ============================ File-search ==============================
search_url = f"{BASE_URL}/search"

search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}
response = requests.get(search_url, params=search_params)
response.raise_for_status()
search_data = response.json()


# ============================ nasa_id retrieving ==============================
items = search_data["collection"]["items"]

nasa_ids = []

for item in items[:2]:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)

# print("NASA IDs:", nasa_ids)


# ============================ files for nasa_id's retrieving ==============================
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

jpg_urls = []


for nasa_id in nasa_ids:
    asset_url = asset_url_template.format(nasa_id=nasa_id)
    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()
    asset_data = asset_response.json()
    files = asset_data["collection"]["items"]

    # ========= jpg-searching ===========
    for file in files:
        url = file["href"]
        if url.lower().endswith(".jpg"):
            jpg_urls.append(url)
            break

# print("JPG URLs:")
# for url in jpg_urls:
#     print(url)


# ============================ Pictures download ==============================
for index, url in enumerate(jpg_urls[:2], start=1):
    image_response = requests.get(url)
    image_response.raise_for_status()
    filename = f"mars_photo{index}.jpg"
    with open(filename, "wb") as file:
        file.write(image_response.content)

    # print(f"Saved {filename}")