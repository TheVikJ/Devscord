import discord
import requests

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))

    if message.content.startswith('!api-category'):
        if message.content.startswith('!api-category animals'):
            await message.channel.send(requests.get('https://api.publicapis.org/entries?category=animals&https=true').text)
        elif message.content.startswith('!api-category anime'):
            await message.channel.send(requests.get('https://api.publicapis.org/entries?category=anime&https=true').text)
        elif message.content.startswith('!api-category anti-malware'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=anti-malware&https=true').text)
        elif message.content.startswith('!api-category art&design'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=art&https=true').text)
        elif message.content.startswith('!api-category books'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=books&https=true').text)
        else:
            await message.channel.send(
                'Please use ```!api-category [name]```to get APIs of that category. The current categories'
                'are Animals, Anime, Anti-Malware, Art&Design, Books, Business, Calendar, Cloud Storage'
                '&FileStorage, ContinuousIntegration, Cryptocurrency, CurrencyExchange, Data'
                'Validation, Development, Dictionaries, Documents&Productivity, Environment, '
                'Events, Finance, Food&Drink, Games&Comics, Geocoding, Government, Health, Jobs, '
                'MachineLearning, Music, News, OpenData, OpenSourceProjects, Patent, Personality, '
                'Photography, Science&Math, Security, Shopping, Social, Sports&Fitness, TestData'
                'TextAnalysis, Tracking, Transportation, URLShorteners, Vehicle, Video, Weather.')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
