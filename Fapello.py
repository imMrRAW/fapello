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
        print(f"Downloading: {filename}")
    else:
        print(f"Fetching image: {filename}")
    
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        with open(filepath, 'wb') as f, tqdm(
            total=total_size, unit='B', unit_scale=True, unit_divisor=1024, disable=not is_video
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                pbar.update(len(chunk))
        if is_video:
            print(f"File downloaded: {filename}")
        else:
            print(f"Image fetched: {filename}")
        return True
    elif is_video and response.status_code == 404:
        print(f"404 Not Found: {filename}")
        return False
    return False

def download_images(image_urls, folder_path):
    for image_url in image_urls:
        if download_media(image_url, folder_path, is_video=False):
            continue
        else:
            break

def download_videos(video_urls, folder_path):
    failed_video_count = 0  # Counter for failed videos
    for video_url in video_urls:
        if download_media(video_url, folder_path, is_video=True):
            continue
        else:
            failed_video_count += 1
            if failed_video_count >= 50:
                print("50 failed downloads reached. Stopping video downloads.")
                break

def download_all_media(urls, downloads_path):
    for url in urls:
        username = extract_username(url)
        folder_path = create_directory(downloads_path, username)
        base_url = f"https://fapello.com/content/{username[0]}/{username[1]}/{username}/1000/{username}"
        
        # Get image and video URLs
        image_urls = [get_image_url(base_url, i) for i in range(1, 1000)]
        video_urls = [get_video_url(base_url, i) for i in range(1, 1000)]
        
        # Download images first
        download_images(image_urls, folder_path)
        
        # Then download videos
        download_videos(video_urls, folder_path)

def extract_username(url):
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]
    if url.startswith("www."):
        url = url[len("www."):]
    if url.endswith("/"):
        url = url[:-1]
    parts = url.split('/')
    return parts[-1]

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "urls.txt")
    
    # Read URLs from the text file
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    downloads_path = os.path.join(current_dir, "Downloads")
    download_all_media(urls, downloads_path)

if __name__ == "__main__":
    main()