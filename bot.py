import discord
import requests

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!api-category'):
        search = message.content
        search = search.replace('!api-category ', '')
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
            if len(r)>2000:
                for i in range(0, 1999):
                    msg += r[i]
            else:
                msg = r
            await message.channel.send(msg)

    if message.content.startswith('!api-random'):
        await message.channel.send(requests.get('https://api.publicapis.org/random?auth=null').text)

    if message.content.startswith('!api-search'):
        desc = message.content
        minus = '!api-search '
        desc = desc.replace(minus, '')
        url = 'https://api.publicapis.org/entries?description=' + desc + '&https=true'
        await message.channel.send(requests.get(url).text)

    if message.content.startswith('!stack-search'):
        msg = ''
        searchterms = message.content
        searchterms = searchterms.replace('!stack-search ', '')
        r = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=' + searchterms + '&site=stackoverflow').text
        if len(r) > 2000:
            for i in range(0, 1999):
                msg += r[i]
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
