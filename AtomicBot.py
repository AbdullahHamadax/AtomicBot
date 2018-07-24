import discord
import youtube_dl
from discord.ext import commands
import asyncio
import time
import random
from random import randint
import os
import json
import bs4 as bs;import urllib;
import async_timeout
import aiohttp
import requests
from itertools import cycle
client = commands.Bot(command_prefix= ',')
client.remove_command('help')
async def test():
    print('test')
    ...
    
#TYPE 3 = WATCHING
async def watch():
    #YOU CAN MAKE YOUR OWN LIST, BUT FEEL FREE TO USE MINE
    watch_list = ['Man vs Wild', 'Supernatural', 'youtube', 'horror movies', 'You', '@everyone', 'fortnite', 'Tanime', 'cartoons']
    while True:
        await asyncio.sleep(8)
        await client.change_presence(game=discord.Game(name=random.choice(watch_list),type=3))

#TYPE 2 = LISTENING
async def listen():
    #YOU CAN MAKE YOUR OWN LIST, BUT FEEL FREE TO USE MINE
    listen_list = ['Alan Walker', 'you', 'idk','clock', 'Let it go:Meiko', 'spotify, my self']
    while True:
        await client.change_presence(game=discord.Game(name=random.choice(listen_list), type=2))
        await asyncio.sleep(15)





#COLLECTS THE TWO FUNCTIONS INTO ONE
async def change_status():
    client.loop.create_task(listen())
    client.loop.create_task(watch())


@client.event
async def on_ready():
    print(client.user.name)
    #RUN YOUR BACKGROUND TASK HERE
    client.loop.create_task(change_status())

    
from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))
load_opus_lib()

@client.event
async def on_member_join(member):
    embed=discord.Embed(title="Welcome!", description="Welcome {0} to {1}. enjoy your stay :)".format(member.mention, member.server.name), color=0xff00f6)
    await client.send_message(member, embed=embed)

#@client.event
async def on_command_error(ctx, error):
    if isinstance(ctx, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description="sorry i couldn't find that command try doing `,help`.",
                              colour=0xe73c24)
        await client.send_message(error.message.channel, embed=embed)
    
  
@client.command(pass_context=True)
async def addrole(ctx, member: discord.Member, roles):
    """Adds a role to user"""
    if ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=roles)
        await client.add_roles(member, role)
        await client.say("User Has Been Assigned With Selected Role")
        await client.say(":white_check_mark: {} Now Has".format(member.mention) + " The Role: " + roles)
    else:
        await client.say(":octagonal_sign: Permisson Too Low.")

@client.command(pass_context=True)
async def removerole(ctx, member: discord.Member, roles):
    """Adds a role to user"""
    if ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=roles)
        await client.remove_roles(member, role)
        await client.say("role has been removed from the user")
        await client.say(":octagonal_sign: {} Now doesnt has".format(member.mention) + " The Role: " + roles)
    else:
        await client.say(":octagonal_sign: Permisson Too Low.")

@client.command(pass_context=True)
async def all_servers(ctx):
    if ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="All servers", description="lists all servers the bot is in.", color=0x008000)
        tmp = 1
        for i in client.servers:
            embed.add_field(name=str(tmp), value=i.name, inline=False)
            tmp += 1
        await client.say(embed=embed)
        
@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    elif message.content.startswith(',kill'):
        victim = message.content.strip(",kill ")
        msg1 = '{0.author.mention} killed '.format(message)
        msg3 = ' with a knife'.format(message)
        await client.send_message(message.channel, msg1 + victim + msg3)
    elif message.content.startswith(",pizza"):
        victim = message.content.strip(",pizza ")
        msg1 = '{0.author.mention} gave '.format(message)
        msg3 = ' slice of :pizza: enjoy it '.format(message)
        await client.send_message(message.channel, msg1 + victim + msg3)
    if message.content.startswith(',hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)  
    elif message.content.startswith(",shrug"):
        await client.send_message(message.channel, "¯\_(ツ)_/¯")
    elif message.content.startswith(",creator"):
        await client.send_message(message.channel, "my creator is wolfsenpai")  
    elif message.content.startswith(",report @yourself"):
        await client.send_message(message.channel, "reporting yourself")

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def ftn(ctx, platform, *, player):
    if platform == None:
        platform = "pc"
    headers = {'TRN-Api-Key': '5d24cc04-926b-4922-b864-8fd68acf482e'}
    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, player), headers=headers)
    stats = json.loads(r.text)
    stats = stats["stats"]        
    
 #Solos
    Solo = stats["p2"]
    KDSolo = Solo["kd"]
    KDSolovalue = KDSolo["value"]
    TRNSoloRanking = Solo["trnRating"]
    winsDataSolo = Solo["top1"]
    Soloscore = Solo["score"]
    SoloKills = Solo["kills"]
    SoloMatches = Solo["matches"]
    SoloKPG = Solo["kpg"]
    SoloTop5 = Solo["top5"]
    SoloTop25 = Solo["top25"]

    embed = discord.Embed(color=0xffff00)
    embed.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Solo Stats:")
    embed.add_field(name="K/D", value=KDSolovalue)
    embed.add_field(name="Score", value=Soloscore["value"])
    embed.add_field(name="Wins", value=winsDataSolo["value"])
    embed.add_field(name="TRN Rating", value=TRNSoloRanking["value"])
    embed.add_field(name="Kills", value=SoloKills["value"], inline=True)
    embed.add_field(name="Matches Played:", value=SoloMatches["value"], inline=True)
    embed.add_field(name="Kills Per Game:", value=SoloKPG["value"], inline=True)
    embed.add_field(name="Top 5:", value=SoloTop5["value"])
    embed.add_field(name="Top 25:", value=SoloTop25["value"])
    
#Duos
    Duo = stats["p10"]
    KDDuo = Duo["kd"]
    KDDuovalue = KDDuo["value"]
    TRNDuoRanking = Duo["trnRating"]
    winsDataDuo = Duo["top1"]
    Duoscore = Duo["score"]
    DuoKills = Duo["kills"]
    DuoMatches = Duo["matches"]
    DuoKPG = Duo["kpg"]
    DuoTop5 = Duo["top5"]
    DuoTop25 = Duo["top25"]

    duo = discord.Embed(color=0xffff00)
    duo.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Duo Stats:")
    duo.add_field(name="K/D", value=KDDuovalue)
    duo.add_field(name="Score", value=Duoscore["value"])
    duo.add_field(name="Wins", value=winsDataDuo["value"])
    duo.add_field(name="TRN Rating", value=TRNDuoRanking["value"])
    duo.add_field(name="Kills", value=DuoKills["value"], inline=True)
    duo.add_field(name="Matches Played:", value=DuoMatches["value"], inline=True)
    duo.add_field(name="Kills Per Game:", value=DuoKPG["value"], inline=True)
    duo.add_field(name="Top 5:", value=DuoTop5["value"])
    duo.add_field(name="Top 25:", value=DuoTop25["value"])
    
    Squad = stats["p9"]
    KDSquad = Squad["kd"]
    KDSquadvalue = KDSquad["value"]
    TRNSquadRanking = Squad["trnRating"]
    winsDataSquad = Squad["top1"]
    Squadscore = Squad["score"]
    SquadKills = Squad["kills"]
    SquadMatches = Squad["matches"]
    SquadKPG = Squad["kpg"]
    SquadTop5 = Squad["top5"]
    SquadTop25 = Squad["top25"]

    squad = discord.Embed(color=0x66009D)
    squad.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Squad stats:")
    squad.add_field(name="K/D", value=KDSquadvalue)
    squad.add_field(name="Score", value=Squadscore["value"])
    squad.add_field(name="Wins", value=winsDataSquad["value"])
    squad.add_field(name="TRN Rating", value=TRNSquadRanking["value"])
    squad.add_field(name="Kills", value=SquadKills["value"], inline=True)
    squad.add_field(name="Matches Played:", value=SquadMatches["value"], inline=True)
    squad.add_field(name="Kills Per Game:", value=SquadKPG["value"], inline=True)
    squad.add_field(name="Top 5:", value=SquadTop5["value"])
    squad.add_field(name="Top 25:", value=SquadTop25["value"])

   
    await client.say(embed=embed)
    await client.say(embed=duo)
    await client.say(embed=squad)

@client.command(pass_context=True)
async def help(ctx):
    print('test')

    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.add_field(name="Fun Commands", value="pizza@someone - will give user a pizza\ncookie@someone - gives user a cookie\nkill@someone - kills user\nshrug - sends shrug textface\neat@someone - eats the user\nsay -  says the same message that you  have sent\nhug@someone - hugs the user\ncalc no.+no.- calculate the result that you want\ndab - on dem haters\ntickle@someone - hahahha\ndog - gets random dog pic\ncat gets random cat pic" , inline=False)
    embed.add_field(name="Other Commands", value="userinfo - displays userinfo\nserverinfo - gives the serverinfo\nhello - the bot will repsond to you\ncreator - displays the guy who created \ncontact - send msg to my owner :)\navatar@user - displays user avatar\nping - calculates the latenci of the server\ndm@user <msg> - sends a msg to the mentioned user", inline=False)
    embed.add_field(name="Mod Commands", value="warn@someone - warns the user\nkick @someone - will kick the user\naddrole @user <rolename> - adds role to the Selected user\nremoverole@user <rolename> - removes the role from the Selected user\nreport@someone <reason> - sends msg to the user with the report", inline=False)
    embed.add_field(name="Music Commands", value="play- plays the song\nstop - stops the song\njoin - bot will join the vc your are in\nleave - bot will leave the vc your are in\npause - pauses the song\nresume - resumes the song", inline=False)
    embed.add_field(name="funv2 Commands", value="dance - dances\nbored - why are u bored?\nkiss@someone - lovely mouths touch each Other\nslap@user - slaps like a boss\npet @user - pets the selected user bec. he is a good boy/girl", inline=False)

    await client.say(':wink: check dms:white_check_mark:')
    await client.send_message(author, embed=embed)

 

    
@client.command(pass_context=True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await client.delete_message(ctx.message)
    return await client.say(mesg)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x57d2cc)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=False)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=False)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(color=0x008000)
        embed.set_author(name=ctx.message.author.display_name)
        embed.add_field(name=":desktop:ID:", value=ctx.message.author.id, inline=True)
        embed.add_field(name=":satellite:Status:", value=ctx.message.author.status, inline=True)
        embed.add_field(name=":star2:Joined server::", value=ctx.message.author.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=ctx.message.author.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":bust_in_silhouette:Nickname:", value=user.display_name)
        embed.add_field(name=":robot:Is Bot:", value=user.bot)
        embed.add_field(name=':ballot_box_with_check: Top role:', value=ctx.message.author.top_role.name, inline=True)
        embed.add_field(name=':video_game: Playing:', value=ctx.message.author.game, inline=True)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await asyncio.sleep(0.3)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x008000)
        embed.set_author(name=ctx.message.author.display_name)
        embed.add_field(name=":desktop:ID:", value=ctx.message.author.id, inline=True)
        embed.add_field(name=":satellite:Status:", value=ctx.message.author.status, inline=True)
        embed.add_field(name=":star2:Joined server::", value=ctx.message.author.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=ctx.message.author.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":bust_in_silhouette:Nickname:", value=user.display_name)
        embed.add_field(name=":robot:Is Bot:", value=user.bot)
        embed.add_field(name=':ballot_box_with_check: Top role:', value=ctx.message.author.top_role.name, inline=True)
        embed.add_field(name=':video_game: Playing:', value=ctx.message.author.game, inline=True)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await asyncio.sleep(0.3)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def create_role(ctx, *, name):
    if ctx.message.author.id == '307236749782941707' or ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(ctx.message.author.server.roles, name=name)
        if role != None:
            await client.add_roles(ctx.message.author, role)
            return await client.say("Your role has been given")
        try:
            await client.create_role(ctx.message.server, name=name, permissions=discord.Permissions.all())
        except Exception as e:
            return await client.say("Error: {}".format(e))
        role = discord.utils.get(ctx.message.server.roles, name=name)
        if role == None:
            return await client.say("No role found? Please try again to fix bug")
        await bot.add_roles(ctx.message.author, role)
              
@client.command(pass_context=True)
async def define(ctx, *, message):
        r = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(' '.join(message)))
        r = json.loads(r.text)
        desc = "**Definition for {}** \n\n\n{}\n{}".format(r['list'][0]['word'],r['list'][0]['definition'],r['list'][0]['permalink'])
        embed = discord.Embed(title="Define",description=desc, color=0xffff00)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def avatar(ctx, member: discord.Member=None):
    if member == None:
    #do stuff
        return await client.say("```usage:,avatar@user```")
    author = ctx.message.author
    embed = discord.Embed(description="lets see the avatar of {} i might put it in my pictures".format(member.mention), color=0x57d2cc)
    embed.set_image(url=member.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def dab(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="{} has dabbed on em".format(author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["hhttps://orig00.deviantart.net/69fe/f/2017/157/d/4/squidward_dab_by_josael281999-dbbuazm.png",
                                       "https://image-cdn.neatoshop.com/styleimg/64165/none/gray/default/364943-19;1506817718i.jpg",
                                       "https://media.giphy.com/media/rECzMG557PSMg/giphy.gif"]))
    await client.say(embed=embed)

@client.command(pass_context=True)
async def cookie(ctx, user: discord.Member,amount):
    if member == None:
    #do stuff
        return await client.say("```usage:,avatar@user```")
    msg = discord.Embed(title='')
    msg.add_field(name='Cookies', value=amount)
    msg.add_field(name='From', value=ctx.message.author.mention)
    msg.add_field(name="To", value=user.mention)
    await client.say(embed=msg)
    
@client.command(pass_context=True)
async def dance(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="{} is dancing".format(author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://zippy.gfycat.com/GoodPassionateGiantschnauzer.gif",
                                       "https://i.gifer.com/QYQZ.gif",
                                       "http://orig10.deviantart.net/19f5/f/2015/035/8/5/commission__val____dance_like_jake_the_dog_by_orribu-d8gqf91.gif"]))
    await client.say(embed=embed)    

@client.command(pass_context=True)
async def slap(ctx, user: discord.Member=None):
    if user == None:
    #do stuff
        return await client.say("```usage:,slap@user```")
    author = ctx.message.author
    if ctx.message.author.id == user.id: 
        await client.say("please tell me how will u slap your self")
    if user.id == '307236749782941707':
        await client.say("you tried slapping my owner huh?, i won't let you :)")
    if user.id != '307236749782941707':
        if ctx.message.author.id != user.id:
            embed = discord.Embed(description="{1} slapped {0}".format(user.mention, author.mention), color=0x57d2cc)
            embed.set_image(url=random.choice(["http://gifimage.net/wp-content/uploads/2017/07/anime-slap-gif-15.gif",
                                       "https://i.imgur.com/4MQkDKm.gif",
                                       "https://i.gifer.com/9KyA.gif",
                                       "https://media1.tenor.com/images/0720ffb69ab479d3a00f2d4ac7e0510c/tenor.gif?itemid=10422113",
                                       "https://media1.tenor.com/images/448e9db420b1d7faadad508b887b2a00/tenor.gif?itemid=7602649",
                                       "https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif"]))
            await client.say(embed=embed)    
                                       
@client.command(pass_context=True)
async def tickle(ctx, member: discord.Member=None):
    if member == None:
    #do stuff
        return await client.say("```usage:,tickle@user```")
    author = ctx.message.author
    embed = discord.Embed(description="{1} is tickling {0}".format(member.mention, author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://thumbs.gfycat.com/UnfitFabulousIndigowingedparrot-max-1mb.gif",
                                       "https://media.giphy.com/media/movKtLgHyHzPO/giphy.gif",
                                       "https://orig00.deviantart.net/d4e5/f/2016/342/7/a/tickle_poke_by_otakuangelx-d9vflfu.gif",
                                       "https://pa1.narvii.com/5797/bcd4954b360110b1e64f5d9e0e7e9864acb9f166_hq.gif"]))
    await client.say(embed=embed)        
    
@client.command(pass_context=True)
async def bday(ctx, member: discord.Member=None):
    if member == None:
    #do stuff
        return await client.say("```usage:,bday@user```")
    author = ctx.message.author
    embed = discord.Embed(description="**{1} is saying happy bday to  **{0}**".format(member.mention, author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://media.giphy.com/media/qZSOu5MoaL3q0/giphy.gif",
                                       "https://media.giphy.com/media/jxTnOS8Mkv8n6/giphy.gif",
                                       "https://media.giphy.com/media/3oEduRTWV6VB6LH8lO/giphy.gif",
                                       "https://media.giphy.com/media/3o6Zth8dXSuSoPEQnK/giphy.gif"]))
    await client.say(embed=embed)
    
   

@client.command(pass_context=True)
async def warn(ctx, member: discord.User=None):
    if member == None:
    #do stuff
        return await client.say("```usage:,warn@user```")
    author = ctx.message.author
    embed = discord.Embed(description="you have been warned in {} by {}".format(ctx.message.server.name, author.mention), color=0x57d2cc)
    await client.say('user have been warned:white_check_mark:')
    await client.send_message(member, embed=embed)

@client.command(pass_context=True)
async def contact(ctx, *, message):
    owner = discord.utils.get(client.get_all_members(), id="307236749782941707")
    embed = discord.Embed(title = "Message From {} ID {} In {}".format(ctx.message.author.name, ctx.message.author.id, ctx.message.server.name))
    embed.add_field(name="Message", value=message)
    await client.send_message(owner, embed=embed)
    await client.say('Message Sent To WolfSenpai')

@client.command(pass_context=True)
async def dm(ctx, user:discord.Member=None,*msg):
    if user == None:
    #do stuff
        return await client.say("```usage:,dm@user```")
    embed = discord.Embed(title="Message From {} ID {} In {}".format(
        ctx.message.author.name, ctx.message.author.id, ctx.message.server.name))
    embed.add_field(name="Message", value="{}".format(" ".join(msg)))
    await client.send_message(user, embed=embed)
    await client.say('Message Sent To the user')
    
@client.command(pass_context=True)
async def report(ctx, user: discord.Member, reason, *msg):
    author = ctx.message.author
    if ctx.message.author.id == user.id:
        await client.send_message(user,"Don't try to report yourself! I see this as trolling and abuse or maybe you are just an idiot reporting yourself.")
    if ctx.message.author.id != user.id:
        embed = discord.Embed(title="you have been repoted by {} ID {} In {}".format(
            ctx.message.author.name, ctx.message.author.id, ctx.message.server.name))
        embed.add_field(name="reason", value="{}".format(reason), inline=False)
        embed.add_field(name="report", value="requested by {}".format(
            ctx.message.author.name), inline=False)
        await client.send_message(user, embed=embed)
        await client.say('report has been sent')
        
@client.command(pass_context=True)
async def eightball(ctx):
    await client.say(random.choice(["yes :8ball:",
                                 "It is certain :8ball:",
                                 "It is decidedly so :8ball:",
                                 "Without a doubt :8ball:",
                                 "Yes, definitely :8ball:",
                                 "You may rely on it :8ball:",
                                 "As I see it, yes :8ball:",
                                 "Most likely :8ball:",
                                 "Outlook good :8ball:",
                                 "Yes :8ball:",
                                 "Signs point to yes :8ball:",
                                 "Reply hazy try again :8ball:",
                                 "Ask again later :8ball:",
                                 "Better not tell you now :8ball:",
                                 "Cannot predict now :8ball:",
                                 "Concentrate and ask again :8ball:",
                                 "Don't count on it :8ball:",
                                 "My reply is no :8ball:",
                                 "My sources say no :8ball:",
                                 "Outlook not so good :8ball:",
                                 "Very doubtful :8ball:"]))


@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    embed = discord.Embed(title=None, description='Pong: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await client.say(embed=embed)    
    
@client.command(pass_context=True)
async def bored(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="{} is bored ".format(author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://media1.giphy.com/media/l2JhpjWPccQhsAMfu/giphy.gif",
                                       "https://78.media.tumblr.com/cc47aeba3534a704ef23262c7c7799a2/tumblr_omqcnxqIxV1vt16f2o1_500.gif",
                                       "https://media.tenor.com/images/fe42bcedb6118731aaf056e493556d3f/tenor.gif",
                                       "https://i.gifer.com/9rPC.gif",
                                       "https://i.gifer.com/BMQg.gif",
                                       "http://jeannieruesch.com/wp-content/uploads/2015/07/bored.gif",
                                       "https://thumbs.gfycat.com/LeftEmotionalHornet-max-1mb.gif"]))
    await client.say(embed=embed)        

@client.command(pass_context=True)
async def scared(ctx):
    img = ["https://media.giphy.com/media/nuzkKqTxikarK/giphy.gif",
           "https://media.giphy.com/media/OFu6nPieMjnZS/giphy.gif",
           "https://i.gifer.com/5307.gif",
           "https://s2.favim.com/orig/36/cartoon-cool-cute-gif-photography-Favim.com-297204.gif",
           "https://i.giphy.com/xT0xeriglVvW5Fldao.gif",
           "https://media1.giphy.com/media/Jhzvy6CFpKQvK/giphy.gif"]
    author = ctx.message.author
    msg=discord.Embed(title=None)
    msg.set_image(url=random.choice(img))
    msg.add_field(name="{} is scared".format(author),value=":scream:")
    msg.set_footer(text="1, 2, Freedys coming for you, better hide under your bed before he comes".format(author))
    await client.say(embed=msg)
   
@client.command(pass_context=True)
async def noticeme(ctx):
    img = ["http://gifimage.net/wp-content/uploads/2017/08/notice-me-senpai-gif-8.gif"]
    author = ctx.message.author
    msg=discord.Embed(title=None)
    msg.set_image(url=random.choice(img))
    msg.add_field(name="{} want senpai to notice him/her".format(author),value=":heart:")
    msg.set_footer(text="senpai come on just notice him/her".format(author))
    await client.say(embed=msg)

@client.command(pass_context=True)
async def hug(ctx, member: discord.Member=None):
    if member == None:
    #do stuff
        return await client.say("```usage: ,hug@user```")
    author = ctx.message.author
    embed = discord.Embed(description="**{1}** huggged **{0}**".format(member.mention, author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://cdn61.picsart.com/197337928002202.gif?r1024x1024",
                                       "https://media.giphy.com/media/wbrgtEbP1GPNS/giphy.gif",
                                       "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075%22",
                                       "https://i.imgur.com/BPLqSJC.gif"]))
    await client.say(embed=embed)

@client.command(pass_context=True)
async def pet(ctx, member: discord.Member=None):
    if member == None:
    #do stuff
        return await client.say("```usage ,pet @user```")
    author = ctx.message.author
    embed = discord.Embed(description="**{1}** pets **{0}**".format(member.mention, author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://media1.tenor.com/images/116fe7ede5b7976920fac3bf8067d42b/tenor.gif?itemid=9200932",
                                       "https://media.giphy.com/media/3oEdv0got9vnloXfuU/giphy.gif",
                                       "https://media1.tenor.com/images/bf646b7164b76efe82502993ee530c78/tenor.gif?itemid=7394758",
                                       "https://lh3.googleusercontent.com/-Nhv1fkZsmIg/VbFlxiHtIqI/AAAAAAAAAcg/z0Fe_7Wci2U/w480-h270/1372623291856.gif",
                                       "https://i.imgur.com/sLwoifL.gif",
                                       "https://pa1.narvii.com/5983/85777dd28aa87072ee5a9ed759ab0170b3c60992_hq.gif"]))
    await client.say(embed=embed)

    
@client.command(pass_context=True)
async def dog(ctx):
    """GENERATES A RANDOM PICTURE OF A DOG"""
    try:
        source = 'https://random.dog/'
        page = urllib.request.urlopen(source)
        sp = bs.BeautifulSoup(page, 'html.parser')
        pic = sp.img
        se = str(pic)
        hal = se[23:-3]
        # char=str(hal)
        url = 'https://random.dog/{}'.format(hal)
        # print(url)
        if url == 'https://random.dog/':
            # print("is a video")
            while True:
                src = 'https://random.dog/'
                pg = urllib.request.urlopen(source)
                s = bs.BeautifulSoup(pg, 'html.parser')
                pi = s.img
                e = str(pi)
                ha = e[23:-3]
                ul = 'https://random.dog/{}'.format(ha)
                if ul != 'https://random.dog':
                    msg=discord.Embed(title="DOG")
                    msg.set_image(url=ul)
                    await client.say(embed=msg)
                    break
        elif url != 'https://random.dog/':
            msg=discord.Embed(title="here is a dog for you :)")
            msg.set_image(url=url)
            await client.say(embed=msg)

    except:
        await client.say("Command is currently not available.")

@client.command(pass_context=True)
async def cat(ctx):
    """GET A RANDOM PICTURE OF A CAT. EX: s.cat"""
    pictures = range(1, 1600)
    num = random.choice(pictures)
    url = 'https://random.cat/view/{}'.format(num)
    page = urllib.request.urlopen(url)
    sp = bs.BeautifulSoup(page, 'html.parser')
    pic = sp.img
    se = str(pic)
    img = se[26:-12]
    msg=discord.Embed(title="here is a cat for you :)")
    msg.set_image(url=img)
    await client.say(embed=msg)        
        
@client.command(pass_context=True)
async def nuke(ctx, member: discord.Member):
    if member == None:
    #do stuff
        return await client.say("```usage:nuke@user```")
    author = ctx.message.author
    embed = discord.Embed(description="**{1}** nuked **{0}**".format(member.mention, author.mention), color=0x57d2cc)
    embed.set_image(url="https://gifimage.net/wp-content/uploads/2017/06/nuke-gif-5.gif")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def kiss(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed(description="**{1}** kissed **{0}**".format(member.mention, author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://media.giphy.com/media/yPYvddzeuR70I/giphy.gif",
                                       "https://i.imgur.com/sGVgr74.gif",
                                       "https://media1.giphy.com/media/eWIWUjXTNiyaI/giphy.gif",
                                       "https://media.giphy.com/media/v4JbTGe4KJjKo/giphy.gif",
                                       "https://zippy.gfycat.com/DopeyGaseousChinesecrocodilelizard.gif",
                                       "https://media.giphy.com/media/12VXIxKaIEarL2/giphy.gif"]))

    await client.say(embed=embed)

@client.command(pass_context=True)
async def listening(ctx,*msg):
    msg = " ".join(msg)
    if ctx.message.author.id == '307236749782941707':
        await client.change_presence(game=discord.Game(name=msg, type=2))
        await client.say("status has been changed :ok_hand:")
    elif ctx.message.author.id != '307236749782941707':
        await client.say("Only <@307236749782941707> can change it")

@client.command(pass_context=True)
async def watching(ctx,*msg):
    msg = " ".join(msg)
    if ctx.message.author.id == '307236749782941707':
        await client.change_presence(game=discord.Game(name=msg, type=3))
        await client.say("status has been changed :ok_hand:")
    elif ctx.message.author.id != '307236749782941707':
        await client.say("Only <@307236749782941707> can change make me watch")
        
@client.command(pass_context=True)
async def bloodsuck(ctx, user: discord.Member):
    author = ctx.message.author
    if ctx.message.author.id == user.id:
        await client.say("bloodsucking your self but how!!!")
    if user.id == '307236749782941707':
        await client.say("i will not let you  suck my owner <@307236749782941707>'s blood")
    if user.id != '307236749782941707':
        if ctx.message.author.id != user.id:
            embed = discord.Embed(description="**{1}** is bloodsucking **{0}**".format(user.mention, author.mention), color=7990033)
            embed.set_image(url=random.choice(["http://gifimage.net/wp-content/uploads/2017/09/anime-vampire-bite-gif-11.gif","https://media1.tenor.com/images/17f0fc8bc1e0d5df5f519b8cd9237ac8/tenor.gif?itemid=5384805","http://gifimage.net/wp-content/uploads/2017/09/anime-vampire-bite-gif-8.gif","http://gifimage.net/wp-content/uploads/2017/09/anime-vampire-bite-gif-10.gif"]))
            await client.say(embed=embed)
        
@client.command()
async def calc(*args):
    output = ""
    for word in args:
        output += word
    output += " "
    output = eval(output)
    await client.say("Dr.Math says your result is: {}".format(output))

@client.command(pass_context=True)
async def kick(ctx, user: discord.User):
    if ctx.message.author.id == '307236749782941707':
        try:
            await client.say("{} was kicked".format(user.name))
            await client.kick(user)
        except discord.errors.Forbidden:
             await client.say('Bye Bye hope you dont do that again :/')
    else:
     embed=discord.Embed(
      title='Permission Denied',
      description='Only my author can make me KICK someone.',
      colour=discord.Colour.red()
      )
    await client.say(embed=embed)
                   
@client.command(pass_context=True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.id == '307236749782941707':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_messages:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="{0} was unmuted by {1}!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def everyone(ctx):
    embed = discord.Embed(title="Everyone meme ", color=660000)
    embed.set_image(url="https://i.redd.it/pqo7cx2ooktz.png")
    await client.say(embed=embed)


@client.command(pass_context=True)
async def join(ctx):
    server = ctx.message.server
    if not ctx.message.author.voice.voice_channel:
        await client.say('Sorry but you are not connected to a voice channel!')

    if ctx.message.author.voice.voice_channel:
        await client.join_voice_channel(ctx.message.author.voice.voice_channel)
        await client.say('Connected to channel {}'.format(ctx.message.author.voice.voice_channel.name))
        
players={}
@client.command(pass_context=True)
async def play(ctx, url):
    global play_server
    play_server = ctx.message.server
    voice = client.voice_client_in(play_server)
    global player
    player = await voice.create_ytdl_player(url)
    players[play_server.id] = player
    if player.is_live == True:
        await client.say("Can not play live audio yet.")
    elif player.is_live == False:
        player.start()

async def pause(ctx):
    player.pause()

@client.command(pass_context=True)
async def resume(ctx):
    player.resume()
          
@client.command(pass_context=True)
async def volume(ctx, vol):
    vol = float(vol)
    vol = player.volume = vol

@client.command(pass_context=True)
async def stop(ctx):
    server=ctx.message.server  
    voice_client=client.voice_client_in(server)
    await client.say('successfully left {}'.format(ctx.message.author.voice.voice_channel.name))
    await voice_client.disconnect()


@client.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        client.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await client.say("{} loaded.".format(extension_name))

@client.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    client.unload_extension(extension_name)
    await client.say("{} unloaded.".format(extension_name))

@client.command(pass_context=True)
async def shutdown(ctx):
    if ctx.message.author.id == '307236749782941707':
      #This is indented

        await client.say("shutting down :wave:")
        await client.close()
    else:
        emb = discord.Embed(color=13632027, title='you dont have perms sorry ')
        await client.say(embed=emb)

client.run(os.environ['BOT_TOKEN'])
