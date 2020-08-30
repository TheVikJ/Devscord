import discord
import requests

import re 
  
def Find(string): 
  
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url] 
      

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!api-category'):
        searchX = message.content
        search = searchX.replace('!api-category ', '')
        searchterms = ''.join([i for i in search if not i.isdigit()])

        if searchterms == '':
            await message.channel.send(
                'Please use ```!api-category [name]```to get APIs of that category. The current categories'
                'are Animals, Anime, Anti-Malware, Art&Design, Books, Business, Calendar, Cloud Storage'
                '&FileStorage, ContinuousIntegration, Cryptocurrency, CurrencyExchange, Data'
                'Validation, Development, Dictionaries, Documents&Productivity, Environment, '
                'Events, Finance, Food&Drink, Games&Comics, Geocoding, Government, Health, Jobs, '
                'MachineLearning, Music, News, OpenData, OpenSourceProjects, Patent, Personality, '
                'Photography, Science&Math, Security, Shopping, Social, Sports&Fitness, TestData'
                'TextAnalysis, Tracking, Transportation, URLShorteners, Vehicle, Video, Weather.')
        else:
            url = 'https://api.publicapis.org/entries?category=' + searchterms + '&https=true'
            r = requests.get(url).text
            msg = ''
            for i in range(0, 1999):
                    msg += r[i]
                AllA = Find(msg)
                
            outputstring = "Here are some APIs from the "
            outputstring += searchX
            outputstring += " category: "
            for i in range (len(AllA)-1):
                index  = str(i+1)                
                  outputstring += "Link " 
                  outputstring += index 
                  outputstring += ":" 
                  outputstring += str(AllA[i])
            await message.channel.send(outputstring)
            
    if message.content.startswith('!api-random'):
        await message.channel.send(requests.get('https://api.publicapis.org/random?auth=null').text)

    if message.content.startswith('!api-search'):
        desc = message.content
        minus = '!api-search '
        desc = desc.replace(minus, '')
        url = 'https://api.publicapis.org/entries?description=' + desc + '&https=true'
        await message.channel.send(requests.get(url).text)

    if message.content.startswith('!stack-search'):
        searchterm = message.content
        searchterms = searchterm.replace('!stack-search ', '')
        r = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=' + searchterms + '&site=stackoverflow').text
        if len(r) > 2000:
            msg = ''
            for i in range(0, 1999):
                msg += r[i]
              AllQ = Find(msg)
              AllQ = [i for i in AllQ if 'questions' in i]             
                  
              outputstring = "For your search for the following search terms: " 
              outputstring += searchterm 
              outputstring += " , we could find the following related links: "
              for i in range (len(AllQ)-1):
                index  = str(i+1)                
                outputstring += "Link " 
                outputstring += index 
                outputstring += ":" 
                outputstring += str(AllQ[i])
                
        await message.channel.send(outputstring)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
