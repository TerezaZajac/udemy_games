import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

first_url = 'http://quotes.toscrape.com/'

def read_quotes(filename):
    with open(filename, 'r') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def scrape_quotes():
    quotes_complete = []
    url = '/page/1'
    while url:
        res = requests.get(f'{first_url}{url}')
        print(f'Scraping{first_url}{url}')
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.find_all(class_='quote')
        
        for quote in quotes:
            quotes_complete.append({'text':quote.find(class_='text').get_text(),'author':quote.find(class_='author').get_text(), 'about author':quote.find('a')['href']})
        #print(quotes_complete)     
    
        next_button = soup.find(class_='next')
        url = next_button.find('a')['href'] if next_button else None
    return quotes_complete

#print(quotes_complete)
def quote_game(quotesgame):
    quote = choice(quotesgame)
    remaining_guesses = 4
    print('Here is a quote: ')
    print(quote['text'])
    #print(quote['author'])
    guess = ''
    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
        guess = input(f'Who said this quote (whole name please) Guesses remaining: {remaining_guesses}\n')
        if guess.lower() == quote['author'].lower():
            print('CORRECT! Clever you!')
            break
        remaining_guesses -= 1
        hints(quote, remaining_guesses)
        
    play_again = ''
    while play_again.lower() not in ('y','n', 'yes', 'no'):
        play_again = input('Do you want to play again (y/n)? ')
    if play_again.lower() in ('yes', 'y'):
        print('Ok, you play again')
        return quote_game(quotesgame)
    else:
        print('Ok, goodbye')

def hints(quote, remaining_guesses):
    if remaining_guesses == 3:
        res = requests.get(f'{first_url}{quote["about author"]}')
        soup = BeautifulSoup(res.text, 'html.parser')
        birth_date = soup.find(class_='author-born-date').get_text()
        birth_place = soup.find(class_='author-born-location').get_text()
        print(f'Here is first hint: The author was born on {birth_date} {birth_place}')
    elif remaining_guesses == 2:
        print(f'Here is second hint: The author first name starts with: {quote["author"][0]}')
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(' ')[-1][0]
        print(f'Here is third hint: The author last name starts with: {last_initial}')
    else:
        print(f'Sorry, you lost. The answer was {quote["author"]}')

quotesgame = read_quotes('/Users/user/Desktop/programovani/quotes.csv')
quote_game(quotesgame)


