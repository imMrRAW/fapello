import os
import requests
import threading
import time
from tqdm import tqdm

def create_directory(base_path, name):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    path = os.path.join(base_path, name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def get_image_url(base_url, image_number):
    return f"{base_url}_{str(image_number).zfill(4)}.jpg"

def get_video_url(base_url, video_number):
    return f"{base_url}_{str(video_number).zfill(4)}.mp4"

def download_media(file_url, folder_path, is_video=False):
    filename = file_url.split('/')[-1]
    filepath = os.path.join(folder_path, filename)
    
    if is_video:
        print(f"Laddar ned: {filename}")
    
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        with open(filepath, 'wb') as f, tqdm(
            total=total_size, unit='B', unit_scale=True, unit_divisor=1024, disable=not is_video
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                pbar.update(len(chunk))
        print(f"Fil nedladdad: {filename}")
        return True
    elif is_video and response.status_code == 404:
        print(f"404 Not Found: {filename}")
        return False
    return False

def download_all_media(urls, folder_path):
    video_download_count = 0  # Räknare för antal nedladdade videor
    failed_video_count = 0  # Räknare för antal misslyckade videor
    
    for url in urls:
        is_video = url.endswith(".mp4")
        if is_video:
            success = download_media(url, folder_path, is_video=is_video)
            if success:
                video_download_count += 1
            else:
                failed_video_count += 1
                if failed_video_count >= 50:
                    print("50 misslyckade nedladdningar har nåtts. Går vidare till nästa URL.")
                    return video_download_count
        else:
            download_media(url, folder_path, is_video=is_video)
    
    return video_download_count

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "urls.txt")
    
    # Läs länkarna från textfilen
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    downloads_path = os.path.join(current_dir, "Downloads")
    
    for url in urls:
        if not url.startswith("https://fapello.com/"):
            print(f"Fel: '{url}' är inte en giltig URL till en undersida på fapello.com.")
            continue
        
        username = url.split('/')[-2]
        folder_path = create_directory(downloads_path, username)
        base_url = f"https://fapello.com/content/{username[0]}/{username[1]}/{username}/1000/{username}"
        
        # Ladda ner bilder och videor parallellt
        image_urls = [get_image_url(base_url, i) for i in range(1, 1000)]
        video_urls = [get_video_url(base_url, i) for i in range(1, 1000)]
        
        image_thread = threading.Thread(target=download_all_media, args=(image_urls, folder_path))
        video_thread = threading.Thread(target=download_all_media, args=(video_urls, folder_path))
        
        image_thread.start()
        
        # Starta video-nedladdning efter att ha väntat i 2 sekunder
        # för att se till att texten "Laddar ned" har skrivits ut
        # innan progressbaren för videon visas.
        time.sleep(2)
        video_thread.start()
        
        # Avsluta med att vänta på att alla trådar ska slutföras
        image_thread.join()
        video_thread.join()

if __name__ == "__main__":
    main()
