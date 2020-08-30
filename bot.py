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

        elif message.content.startswith('!api-category business'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=business&https=true').text)

        elif message.content.startswith('!api-category calendar'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=calendar&https=true').text)

        elif message.content.startswith('!api-category cloudstorage&filesharing'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=cloud&https=true').text)

        elif message.content.startswith('!api-category continuousintegration'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=continuous&https=true').text)

        elif message.content.startswith('!api-category cryptocurrency'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=cryptocurrency&https=true').text)

        elif message.content.startswith('!api-category currencyexchange'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=currency&https=true').text)

        elif message.content.startswith('!api-category datavalidation'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=data&https=true').text)

        elif message.content.startswith('!api-category development'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=development&https=true').text)

        elif message.content.startswith('!api-category dictionaries'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=dictionaries&https=true').text)

        elif message.content.startswith('!api-category documents&productivity'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=documents&https=true').text)

        elif message.content.startswith('!api-category environment'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=environment&https=true').text)

        elif message.content.startswith('!api-category events'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=events&https=true').text)

        elif message.content.startswith('!api-category finance'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=finance&https=true').text)

        elif message.content.startswith('!api-category food&drink'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=food&https=true').text)

        elif message.content.startswith('!api-category games&comics'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=games&https=true').text)

        elif message.content.startswith('!api-category geocoding'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=geocoding&https=true').text)

        elif message.content.startswith('!api-category government'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=government&https=true').text)

        elif message.content.startswith('!api-category health'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=health&https=true').text)

        elif message.content.startswith('!api-category jobs'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=jobs&https=true').text)

        elif message.content.startswith('!api-category machinelearning'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=machine&https=true').text)

        elif message.content.startswith('!api-category music'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=music&https=true').text)

        elif message.content.startswith('!api-category news'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=news&https=true').text)

        elif message.content.startswith('!api-category opendata'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=open&https=true').text)

        elif message.content.startswith('!api-category opensourceprojects'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=projects&https=true').text)

        elif message.content.startswith('!api-category patent'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=patent&https=true').text)

        elif message.content.startswith('!api-category personality'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=personality&https=true').text)

        elif message.content.startswith('!api-category photography'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=photography&https=true').text)

        elif message.content.startswith('!api-category science&math'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=science&https=true').text)

        elif message.content.startswith('!api-category security'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=security&https=true').text)

        elif message.content.startswith('!api-category shopping'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=shopping&https=true').text)

        elif message.content.startswith('!api-category social'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=social&https=true').text)

        elif message.content.startswith('!api-category sports&fitness'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=sports&https=true').text)

        elif message.content.startswith('!api-category testdata'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=test&https=true').text)

        elif message.content.startswith('!api-category textanalysis'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=text&https=true').text)

        elif message.content.startswith('!api-category tracking'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=tracking&https=true').text)

        elif message.content.startswith('!api-category transportation'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=transportation&https=true').text)

        elif message.content.startswith('!api-category urlshorteners'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=url&https=true').text)

        elif message.content.startswith('!api-category vehicle'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=vehicle&https=true').text)

        elif message.content.startswith('!api-category video'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=video&https=true').text)

        elif message.content.startswith('!api-category weather'):
            await message.channel.send(
                requests.get('https://api.publicapis.org/entries?category=weather&https=true').text)

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

    if message.content.startswith('!api-random'):
        await message.channel.send(requests.get('https://api.publicapis.org/random?auth=null').text)
        
    if message.content.startswith('!api-search'):
        desc = message.content
        minus = '!api-search '
        desc = desc.replace(minus, '')
        url = 'https://api.publicapis.org/entries?description=' + desc + '&https=true'
        await message.channel.send(requests.get(url).text)
           
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
