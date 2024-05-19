import os
import requests

# List of image URLs
values_list = [
    "https://i.picasion.com/sp/92/4Iq8/1.gif",
    "https://i.picasion.com/sp/92/4Iq8/2.gif",
    "https://i.picasion.com/sp/92/4Iq8/3.gif",
    "https://i.picasion.com/sp/92/4Iq8/4.gif",
    "https://i.picasion.com/sp/92/4Iq8/5.gif",
    "https://i.picasion.com/sp/92/4Iq8/6.gif",
    "https://i.picasion.com/sp/92/4Iq8/7.gif",
    "https://i.picasion.com/sp/92/4Iq8/8.gif",
    "https://i.picasion.com/sp/92/4Iq8/9.gif",
    "https://i.picasion.com/sp/92/4Iq8/10.gif",
    "https://i.picasion.com/sp/92/4Iq8/11.gif",
    "https://i.picasion.com/sp/92/4Iq8/12.gif",
    "https://i.picasion.com/sp/92/4Iq8/13.gif",
    "https://i.picasion.com/sp/92/4Iq8/14.gif",
    "https://i.picasion.com/sp/92/4Iq8/15.gif",
    "https://i.picasion.com/sp/92/4Iq8/16.gif",
    "https://i.picasion.com/sp/92/4Iq8/17.gif",
    "https://i.picasion.com/sp/92/4Iq8/18.gif",
    "https://i.picasion.com/sp/92/4Iq8/19.gif",
    "https://i.picasion.com/sp/92/4Iq8/20.gif",
    "https://i.picasion.com/sp/92/4Iq8/21.gif",
    "https://i.picasion.com/sp/92/4Iq8/22.gif",
    "https://i.picasion.com/sp/92/4Iq8/23.gif",
    "https://i.picasion.com/sp/92/4Iq8/24.gif",
    "https://i.picasion.com/sp/92/4Iq8/25.gif",
    "https://i.picasion.com/sp/92/4Iq8/26.gif",
    "https://i.picasion.com/sp/92/4Iq8/27.gif",
    "https://i.picasion.com/sp/92/4Iq8/28.gif",
    "https://i.picasion.com/sp/92/4Iq8/29.gif",
    "https://i.picasion.com/sp/92/4Iq8/30.gif",
    "https://i.picasion.com/sp/92/4Iq8/31.gif",
    "https://i.picasion.com/sp/92/4Iq8/32.gif",
    "https://i.picasion.com/sp/92/4Iq8/33.gif",
    "https://i.picasion.com/sp/92/4Iq8/34.gif",
    "https://i.picasion.com/sp/92/4Iq8/35.gif",
    "https://i.picasion.com/sp/92/4Iq8/36.gif",
    "https://i.picasion.com/sp/92/4Iq8/37.gif",
    "https://i.picasion.com/sp/92/4Iq8/38.gif",
    "https://i.picasion.com/sp/92/4Iq8/39.gif",
    "https://i.picasion.com/sp/92/4Iq8/40.gif",
    "https://i.picasion.com/sp/92/4Iq8/41.gif",
    "https://i.picasion.com/sp/92/4Iq8/42.gif",
    "https://i.picasion.com/sp/92/4Iq8/43.gif",
    "https://i.picasion.com/sp/92/4Iq8/44.gif",
    "https://i.picasion.com/sp/92/4Iq8/45.gif",
    "https://i.picasion.com/sp/92/4Iq8/46.gif",
    "https://i.picasion.com/sp/92/4Iq8/47.gif",
    "https://i.picasion.com/sp/92/4Iq8/48.gif",
    "https://i.picasion.com/sp/92/4Iq8/49.gif",
    "https://i.picasion.com/sp/92/4Iq8/50.gif",
    "https://i.picasion.com/sp/92/4Iq8/51.gif",
    "https://i.picasion.com/sp/92/4Iq8/52.gif",
    "https://i.picasion.com/sp/92/4Iq8/53.gif",
    "https://i.picasion.com/sp/92/4Iq8/54.gif",
    "https://i.picasion.com/sp/92/4Iq8/55.gif",
    "https://i.picasion.com/sp/92/4Iq8/56.gif",
    "https://i.picasion.com/sp/92/4Iq8/57.gif",
    "https://i.picasion.com/sp/92/4Iq8/58.gif",
    "https://i.picasion.com/sp/92/4Iq8/59.gif",
    "https://i.picasion.com/sp/92/4Iq8/60.gif",
    "https://i.picasion.com/sp/92/4Iq8/61.gif",
    "https://i.picasion.com/sp/92/4Iq8/62.gif",
    "https://i.picasion.com/sp/92/4Iq8/63.gif",
    "https://i.picasion.com/sp/92/4Iq8/64.gif",
    "https://i.picasion.com/sp/92/4Iq8/65.gif",
]

folder_path = "newfolder"
os.makedirs(folder_path, exist_ok=True)


for index, url in enumerate(values_list, start=1):
    filename = os.path.join(folder_path, f"image{index}.gif")
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url}")

print("Done.")