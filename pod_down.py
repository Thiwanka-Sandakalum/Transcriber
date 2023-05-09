import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from converter import convert_audio_to_wav
import os

class PodcastDownloader:
    def __init__(self, url):
        self.url = url
        self.episodes = {}
        self.soup = None
        self.get_soup()

    def get_soup(self):
        try:
            r = requests.get(self.url)
            r.raise_for_status()  # Raise an exception if the request was not successful
            self.soup = BeautifulSoup(r.content, 'html.parser')
            self.get_episodes()
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to retrieve the webpage - {e}")
            raise

    def get_episodes(self):
        try:
            divs = self.soup.find_all('div', attrs={'class': 'oD3fme'})
            for ix, div in enumerate(divs[::-1]):
                date = div.find('div', attrs={'class': 'OTz6ee'}).text
                name = div.find('div', attrs={'class': 'e3ZUqe'}).text
                name = re.sub('[\/:*?"<>|]+', '', name)
                url = div.find('div', attrs={'jsname': 'fvi9Ef'}).get('jsdata').split(';')[1]
                file_name = f'EP {ix:03d} - {name} ({date})'
                self.episodes[ix] = {'url': url, 'file_name': file_name}
                print(file_name)

            selected_episode = int(input("Enter the episode number you want to download: "))
            self.download_episode(selected_episode)
        except Exception as e:
            print(f"Error: Failed to retrieve the episodes - {e}")
            raise

    def download_episode(self, episode_number):
        try:
            selected_episode = self.episodes[episode_number]
            url = selected_episode['url']
            file_name = selected_episode['file_name']
            podcast = requests.get(url, stream=True)
            podcast.raise_for_status()  # Raise an exception if the download request was not successful

            # get the file size from the content-length header
            file_size = int(podcast.headers.get('Content-Length', 0))

            # create a progress bar using tqdm
            progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)

            # iterate over the content and write it to the file
            with open(f'{file_name}.mp3', 'wb') as out:
                for chunk in podcast.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        out.write(chunk)
                        progress_bar.update(len(chunk))

            print(f'{file_name} downloaded')

            # convert .mp3 to .wav
            print("Converting...")
            output_path = "model/output.wav"
            convert_audio_to_wav(f'{file_name}.mp3',output_path)

            # remove downloaded mp3 file
            os.remove(f'{file_name}.mp3')

            # close the progress bar
            progress_bar.close()

            return f'{file_name}.wav'
        except Exception as e:
            print(f"Error: Failed to download the episode - {e}")
            raise

