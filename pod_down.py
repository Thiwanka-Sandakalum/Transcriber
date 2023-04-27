import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

class PodcastDownloader:
    def __init__(self, url):
        self.url = url
        self.episodes = {}
        self.soup = None

    def get_soup(self):
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, 'html.parser')

    def get_episodes(self):
        divs = self.soup.find_all('div', attrs={'class': 'oD3fme'})
        for ix, div in enumerate(divs[::-1]):
            date = div.find('div', attrs={'class': 'OTz6ee'}).text
            name = div.find('div', attrs={'class': 'e3ZUqe'}).text
            name = re.sub('[\/:*?"<>|]+', '', name)
            url = div.find('div', attrs={'jsname': 'fvi9Ef'}).get('jsdata').split(';')[1]
            file_name = f'EP {ix:03d} - {name} ({date})'
            self.episodes[ix] = {'url': url, 'file_name': file_name}
            print(file_name)

    def download_episode(self, episode_number):
        selected_episode = self.episodes[episode_number]
        url = selected_episode['url']
        file_name = selected_episode['file_name']
        podcast = requests.get(url, stream=True)

        # get the file size from the content-length header
        file_size = int(podcast.headers.get('Content-Length', 0))

        # create a progress bar using tqdm
        progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)

        # iterate over the content and write it to the file
        with open(f'{file_name}.mp3', 'wb') as out:
            for chunk in podcast.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    out.write(chunk)
                    progress_bar.update(len(chunk))

        # close the progress bar
        progress_bar.close()
        return f'{file_name}.mp3'

if __name__ == '__main__':
    url = main.podcast_url
    podcast = PodcastDownloader(url)
    podcast.get_soup()
    podcast.get_episodes()
    selected_episode = int(input("Enter episode number you want to download: "))
    podcast.download_episode(selected_episode)
