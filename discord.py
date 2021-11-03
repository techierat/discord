import requests
import random
from time import sleep
import discum
from discum.gateway.session import guild
channel_id='903951269444599868'
token='ODI2Nzk1NjI4NDE1NTQ5NDUx.YYIZpg.HHOxavwcU9_6-0TMlSdnlYb6q9E'

bot = discum.Client(token=token)

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

members = get_members('900286053565472778', '903951269444599868')
memberslist = []

for memberID in members:
    memberslist.append(memberID)
    print(memberID)


def sendMessage(token, channel_id, message):
    try:
        url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
        data = {"content": message}
        header = {"authorization": token}

        r = requests.post(url, data=data, headers=header)
        if r.status_code == 200:
            print(f'quote sent: {message} \n')
        else:
            print(r.raise_for_status())
    except Exception as e:
        print(e)

    
    sleep(random.randint(200,680))



LIST=[]

while True:
    try:
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
            json_data = response.json()
            data = json_data['data']
            message=data[0]['quoteText']
        else:
            print(requests.status_codes)
            message=['who dey zuzu','whats up guys', 'spap nice one', 'comrades how far', 'how far', 'whats popping', 'wetin dey sup', 'WAGMI']

        for line in memberslist:
            for word in line.split():
                LIST.append(word)
        answer = random.choice(LIST)
        answer=int(answer)
        userid= f'<@!{answer}>'
        taguser=userid+message

        
        sendMessage(token,channel_id,taguser)
    except Exception as e:
        sleep(360)
        print(e)
    
