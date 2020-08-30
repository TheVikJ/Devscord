## Devscord
A Discord bot where you can collaboratively search for APIs and common questions via Stack Overflow.

## Add the bot to your server
https://discord.com/api/oauth2/authorize?client_id=749386272388284426&permissions=8&scope=bot

## Inspiration
We were inspired to make Devscord because we've done a lot of Hackathons (18+ between the two of us), and we realized it was getting really annoying to do one part: the idea planning. We all ended up researching independently, coming up with random links and debating which to use. This process used up a lot of valuable time which could've been used actually coding. Inspired by this, Devscord was born.
## What it does
Devscord is a Discord bot which you can use to collaboratively search for APIs and common questions via Stack Overflow. 

Commands:

!api-category to get the names of all the catergories

!api-category [category_name] to get the names of APIs in a category

!api-search [search_term] to get the APIs with that search term

!api-random to get a random API

!stack-search [search_tag1],[search_tag2],[search_tag3], etc. to get Stack Overflow questions that match your tags


## How we built it
We built Devscord with Python and discord.py for the bot part. For the searching of Stack Overflow and APIs, we use the public-APIs API and the StackExchange API. We access these using the requests package and then use an algorithm to extract the links from the JSON and format the message.

## Challenges we ran into
1. Teammates dropping out 2 hours before the Hackathon started

Our teammates dropped out 2 hours before the start of the Hackathon, and we didn't have enough manpower or time to finish our project in javascript as we had initially wanted. We actually learnt Javascript in the 24 hours before the Hackathon for preparation, but since our teammates who already knew Javascript dropped out, we had to switch our language to Python, our plan entirely and prepare for having two fewer people. 

2. APIs in Python

If you've ever used the requests package, you know that the APIs usually return JSON text. We were getting really cryptic messages on Discord initially, but we used an algorithm to extract whatever we needed from the JSON string which was really difficult for us.

3. Never having used re and requests packages

We used these two packages for the first time in this Hackathon, which was actually pretty hard. After debugging a lot, we ended up choosing these packages instead of Python wrappers for the APIs that we chose. This was taking our knowledge a step further and really pushed us to our limit.

4. Accidentally almost ruining our entire project on GitHub because of 4+ wrong commits

We used GitHub properly this Hackathon and used more complex stuff than just commits. We accidentally committed like 5 buggy commits and they almost ruined our project because that was 1 hour before the deadline. Luckily, we had some code leftover and we could restore our changes and continue with our project.

## Accomplishments that we're proud of
1. That our code actually works

Our code wasn't working just one hour before the deadline and it was extremely stressful. Luckily, we somehow managed to make our code work, and add all of our intended features and commands.

2. That we learnt Javascript

As mentioned above, we were initially planning on making our project in Javascript with discord.js, but our teammates dropped out, and we had already learned Javascript for a long time. We had to switch to Python to actually make a somewhat complex product, but we still learnt Javascript this weekend, and we are extremely proud of that.

3. requests package

Both of us haven't worked with the requests package before to its true extent, so it was enlightening to see how it can be used, and we are planning on using it for future Hackathons.

4. Complexity

This was the most complex project that we have undertaken and actually managed to finish to a good extent during a Hackathon. It was immensely gratifying to see our project unfold with only our hands and lines of code.

## What we learned
1. **Javascript**

We learnt a decent amount of Javascript this weekend before switching to Python, but that's still something we learnt, so, yay!

2. **RegEx** and **requests** packages

We actually had never used these packages to their true extent before and it was actually very stressful, yet rewarding to see them work in our project.

## What's next for Devscord
We have one plan that we wanted to achieve this weekend but didn't have enough time to. That was searching GitHub for repositories that would pertain to your topic. We also would've liked to add a chatbot that could act as a mentor or helper for your Hackathon journey.
