# Fapello Downloader

## Description
This Python script is designed to download images and videos from user pages on fapello.com. The script reads a list of URLs from a file `urls.txt` and downloads all available images and up to 50 videos from each user's page.

## Usage
1. Add desired URLs to user pages on fapello.com in the file `urls.txt`, one URL per line.
2. Run `Fapello.py`.
3. The script creates a folder for each user and downloads the images and up to 50 videos to their respective folders.

## Prerequisites
- Python 3.x
- Libraries: requests, tqdm

## Installation of Dependencies
```
pip install -r requirements.txt
```

## Configuration
No configuration is required. Make sure to have a file `urls.txt` with desired URLs to user pages on fapello.com.

## Structure
```
.
├── main.py
├── README.md
├── requirements.txt
├── urls.txt
└── Downloads/
```

- `Fapello.py`: The main script for downloading images and videos.
- `README.md`: This file, containing description and instructions for the project.
- `requirements.txt`: List of required Python libraries.
- `urls.txt`: The file with URLs to user pages on fapello.com.
- `Downloads/`: The folder where downloaded images and videos are saved.

## Contributions
Contributions are welcome! Feel free to open an issue to discuss major changes or create a pull request directly if you have minor changes to suggest.

## License
This project is licensed under the [MIT License](LICENSE).