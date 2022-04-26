from game import *

import json
import requests
import webbrowser

# def main():  
#     file = open("rawg.txt", 'w').close()
#     base_url = "https://api.rawg.io/api/games"
#     search = input('what game do you want to search ?')
#     #headers = {'page':1,'page_size':40,'dates':'2022-01-01,2022-04-15','ordering':'-metacritic','key':'5d53699543f048298c19ee28b26eedae'}
#     headers = {'page':1,'page_size':40,'search':search,'key':'5d53699543f048298c19ee28b26eedae'}
#     response = requests.get(base_url,headers)
#     Datalist = response.json()['results']
#     Gamelist=fetchdata(Datalist)
#     savegame(Gamelist, 'rawg.txt')
#     #print(loadgame('rawg.txt'))

def search():
    games = []
    while True:
        if(games==[]):
            term=input('Enter a search term, or "exit" to quit: ')
            if term=="exit":
                print("\nBye!")
                break
            else:
                index=1
                base_url = "https://api.rawg.io/api/games"
                headers = {'page':1,'page_size':10,'search':term,'key':'5d53699543f048298c19ee28b26eedae'}
                response = requests.get(base_url,headers)
                Datalist = response.json()['results']
                games=fetchdata(Datalist)
                savegame(games, 'rawg.txt')
                print("\nSearching results")
                if games==[]:
                    print("No Games found")
                for game in games:
                    print(str(index),game['name'])
                    index+=1
                print("\n")
        else:
            term=input('Enter a number for more info, or another search term, or "exit": ')
            if term=="exit":
                print("\nBye!")
                break
            try:
                index=int(term)
                detail(games[index-1])
            except:
                index=1
                base_url = "https://api.rawg.io/api/games"
                headers = {'page':1,'page_size':10,'search':term,'key':'5d53699543f048298c19ee28b26eedae'}
                response = requests.get(base_url,headers)
                Datalist = response.json()['results']
                games=fetchdata(Datalist)
                print("\nSearching results")
                if games==[]:
                    print("No Games found")
                for game in games:
                    print(str(index),game['name'])
                    index+=1
                print("\n")

def detail(game):
    while True:
        option = input('Which option do you want ? \n1. Game rating\n2. Game description\n3. Game image\n4. Game website\n5. back\n')
        if (option == '1'):
            if(game['rating']!=0):
                print('User Rating: '+str(game['rating']))
            if(game['metacritic']!=0):
                print('Metacritic Score: '+str(game['metacritic']))
            elif(game['rating']==0):
                print('No ratings avaliable.')
            print('\n')
        elif(option == '2'):
            print(game['summary'])
            print('\n')
        elif(option == '3'):
            print("\nLaunching\n"+game['image']+"\nin web browser\n")
            webbrowser.open(game['image'])
        elif(option == '4'):
            print("\nLaunching\n"+game['url']+"\nin web browser\n")
            webbrowser.open(game['url'])
        elif(option == '5'):
            break
def fetchdata(Datalist):
    Gamelist = []
    for game in Datalist:
        Gameinfo = Game(json=game)
        Gameinfo.rating,Gameinfo.url ,Gameinfo.summary = getrate(Gameinfo.name)
        gamedic = {'name':Gameinfo.name,'release_year':Gameinfo.release_year,'metacritic':Gameinfo.metacritic,'image':Gameinfo.image, 'rating':Gameinfo.rating,'summary':Gameinfo.summary,'url':Gameinfo.url}
        Gamelist.append(gamedic)
    return Gamelist

def getrate(name):
    Base_url='https://api.igdb.com/v4/games/'
    headers = {'Client-ID':'wfn7jli2sugg8reuq3nnoar0elrm0l','Authorization': 'Bearer j06sq91d8w6srpzmnbbhft4asbfht7',"Accept": "application/json"}
    query = name
    data = f"search \"{query}\";fields *;"
    response = requests.post(url = Base_url,data=f"search \"{query}\";fields name, total_rating,summary,url;",headers=headers)
    Datalist = response.json()
    Gamelist = []
    for game in Datalist:
        Gameinfo = Game(json=game)
        gamedic = {'name':Gameinfo.name,'rating':Gameinfo.rating,'url':Gameinfo.url,'summary':Gameinfo.summary}
        Gamelist.append(gamedic)
    for game in Gamelist:
        if (game['name'] == name):
            return game['rating'],game['url'],game['summary']
    return 0,0,0

def savegame(Gamelist,filename):
    gameFile = open(filename, 'w',encoding="utf-8")
    for game in Gamelist:
        print(game,file = gameFile)
    gameFile.close()

def loadgame(filename):
    gameFile = open(filename, 'r',encoding="utf-8")
    lines = gameFile.readlines()
    lines = [line.strip() for line in lines]
    gameFile.close()
    return lines

if __name__ == '__main__':
    search()
    #detail({'name': 'The Legend of Zelda: Breath of the Wild', 'release_year': '2017', 'metacritic': 97, 'image': 'https://media.rawg.io/media/games/cc1/cc196a5ad763955d6532cdba236f730c.jpg', 'rating': 94.83972272696695, 'summary': 'In this 3D open-world entry in the Zelda series, Link is awakened from a deep slumber without his past memories in the post-apocalyptic Kingdom of Hyrule, and sets off on a journey to defeat the ancient evil Calamity Ganon. Link treks, climbs and glides through fields, forests and mountain ranges while meeting and helping friendly folk and defeating enemies in order to gather up the strength to face Ganon.', 'url': 'https://www.igdb.com/games/the-legend-of-zelda-breath-of-the-wild'})
