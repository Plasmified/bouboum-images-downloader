import requests
import os

base_url = "http://transformice.com/images/x_bouboum/x_skin/x_skin_"
output_folder = "skins/x_skin_"
extensions = [".png", "x_illu_300.png", "x_magasin.jpg", "x_magasin_gauche.jpg"]

for j in range(26):
    if j != 1 :
        folder = output_folder + str(j)
        if not os.path.exists(folder):
            os.makedirs(folder)

        for i in range(12):
            url = f"{base_url}{j}/x_{i}{extensions[0]}"
            output_file = os.path.join(folder, f"x_{i}{extensions[0]}")
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                with open(output_file, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f"Downloaded: {url}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {url}: {e}")

        if j != 22:
            for ext in extensions[1:]:
                url = f"{base_url}{j}/{ext}"
                output_file = os.path.join(folder, ext)
                try:
                    response = requests.get(url, stream=True)
                    response.raise_for_status()
                    with open(output_file, "wb") as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)
                    print(f"Downloaded: {url}")
                except requests.exceptions.RequestException as e:
                    print(f"Failed to download {url}: {e}")

print("Download complete!")
