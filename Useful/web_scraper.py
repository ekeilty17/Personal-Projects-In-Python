import requests
from bs4 import BeautifulSoup

class Scraper(object):

    blacklist = [   '[document]',
                    'noscript',
                    'html',
                    'meta',
                    'head', 
                    'header',
                    'footer',
                    'input',
                    'script']

    whitelist = [   'h1',
                    'h2',
                    'h3'
                    'p']

    def __init__(self):
        self.html = ""
        self.name = ""
        self.links = []
    
    def get_html_from_url(self, url):
        self.name = url.replace('https://', '').replace('http://', '').replace('/', ':') + '.txt'
        try:
            res = requests.get(url)
            html_page = res.content
            self.html = BeautifulSoup(html_page, 'html.parser')
            self.html.header.decompose()
            self.html.footer.decompose()
            return self.html

        except Exception as e:
            print(f"{url} Failed due to {e}")
            return None
    
    def get_html_from_text(self, file):
        self.name = file.split('.')[0] + "_extracted.txt"
        with open(file, 'r') as f:
            html_page = f.read().replace('\n', '')
        self.html = BeautifulSoup(html_page, 'html.parser')
        self.html.header.decompose()
        self.html.footer.decompose()
        return self.html
    
    def extract(self, relative_links=False, text_file=True, call_recursively=True):
        if self.html == "":
            return ""

        text = self.html.find_all(text=True)
        links_obj = self.html.find_all('a')

        self.links = []
        for link in links_obj:
            try:
                #if url in link['href']:
                #   links.append(link['href'])
                if relative_links:
                    link = self.links.append(url + link['href'])
                else:
                    self.links.append(link['href'])
                
            except Exception:
                pass

        output = ''

        for t in text:
            if t.parent.name not in self.blacklist:
                if t.parent.name in ['h1', 'h2', 'h3']:
                    output += '\nTitle: {}\n'.format(t)
                elif t.parent.name == 'p':
                    output += '{}\n'.format(t)
        
        output += "\n\n\nLinks\n"
        for link in self.links:
            output += str(link) + "\n"

        # It goes 1 layer deep
        if call_recursively:
            for link in self.links:
                S = Scraper()
                S.get_html_from_url(link)
                S.extract(text_file=True, call_recursively=False)

        # Writing to text file
        if text_file:
            with open(self.name, 'w+') as g:
                g.write(output)

        return output

if __name__ == "__main__":
    S = Scraper()
    S.get_html_from_url("https://www.espn.com/nba/")
    S.extract()
