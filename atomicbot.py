import discord
import youtube_dl
from discord import Game
from discord.ext import commands
import asyncio
import time
import random
from random import randint
import os
import json
import async_timeout
import aiohttp
import requests
import checks
import urllib.parse
import urllib.request
from itertools import cycle
client = commands.Bot(command_prefix= ',')
status = ["dont forget to", "do ,help", "to see all the commands :)"]
client.remove_command('help')
async def test():
    print('test')
    ...

players = {}

api = str(os.environ.get('RIOT_KEY'))

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)

@client.event
async def on_ready():
   print("Logged in as " + client.user.name)
     
@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return 
    elif message.content.startswith("ping"):
        await client.send_message(message.channel, "Pong!:ping_pong:")
    elif message.content.startswith(',kill'):
        victim = message.content.strip(",kill ")
        msg1 = '{0.author.mention} killed '.format(message)
        msg3 = ' with a knife'.format(message)
        await client.send_message(message.channel, msg1 + victim + msg3)
    elif message.content.startswith(',cookie'):
        victim = message.content.strip(",cookie ")
        msg1 = '{0.author.mention} gave '.format(message)
        msg3 = ' a cookie:cookie:'.format(message)
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
        await client.send_message(message.channel, "my creator is wolfsnepai")    

@client.command(pass_context=True)
async def help(ctx):
    print('test')

    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.add_field(name="Fun Commands", value="pizza@someone - will give user a pizza\ncookie@someone - gives user a cookie\nkill@someone - kills user\nshrug - sends shrug textface\neat@someone - eats the user\nsay -  says the same message that you  have sent\nhug@someone - hugs the user\ncalc no.+no.- calculate the result that you want\ndab - on dem haters" , inline=False)
    embed.add_field(name="Other Commands", value="userinfo - displays userinfo\nserverinfo - gives the serverinfo\nhello - the bot will repsond to you\ncreator - displays the guy who created \nprefix - displays the prefix of the bot", inline=False)
    embed.add_field(name="Mod Commands", value="warn@someone - warns the user\nkick @someone - will kick the user", inline=False)
    embed.add_field(name="Music Commands", value="play- plays the song\nstop - stops the song\njoin - bot will join the vc your are in\nleave - bot will leave the vc your are in\npause - pauses the song\nresume - resumes the song", inline=False)
    embed.add_field(name="funv2 Commands", value="dance - dances\nbored - why are u bored?\nkiss@someone - lovely mouths touch each Other\nslap@user - slaps like a boss", inline=False)

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
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I found.", color=0x57d2cc)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role,)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
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
async def dance(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="{} is dancing".format(author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://zippy.gfycat.com/GoodPassionateGiantschnauzer.gif",
                                       "https://i.gifer.com/QYQZ.gif",
                                       "http://orig10.deviantart.net/19f5/f/2015/035/8/5/commission__val____dance_like_jake_the_dog_by_orribu-d8gqf91.gif"]))
    await client.say(embed=embed)    

@client.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed(description="{1} slapped {0}".format(member.mention, author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["http://gifimage.net/wp-content/uploads/2017/07/anime-slap-gif-15.gif",
                                       "https://i.imgur.com/4MQkDKm.gif",
                                       "https://i.gifer.com/9KyA.gif",
                                       "https://media1.tenor.com/images/0720ffb69ab479d3a00f2d4ac7e0510c/tenor.gif?itemid=10422113",
                                       "https://media1.tenor.com/images/448e9db420b1d7faadad508b887b2a00/tenor.gif?itemid=7602649",
                                       "https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif"]))
    await client.say(embed=embed)    


@client.command(pass_context=True)
async def warn(ctx, member: discord.User):
    author = ctx.message.author
    embed = discord.Embed(description="you have been warned in {} by {}".format(ctx.message.server.name, author.mention), color=0x57d2cc)
    await client.send_message(member, embed=embed)

@client.command(pass_context=True)
async def prefix (ctx):
 await client.say("my prefix is ,")

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
async def bored(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="{} is bored ".format(author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://media1.giphy.com/media/l2JhpjWPccQhsAMfu/giphy.gif",
                                       "https://78.media.tumblr.com/cc47aeba3534a704ef23262c7c7799a2/tumblr_omqcnxqIxV1vt16f2o1_500.gif",
                                       "https://media.tenor.com/images/fe42bcedb6118731aaf056e493556d3f/tenor.gif",
                                       "https://thumbs.gfycat.com/LeftEmotionalHornet-max-1mb.gif"]))
    await client.say(embed=embed)        

@client.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed(description="**{1}** huggged **{0}**".format(member.mention, author.mention), color=0x57d2cc)
    embed.set_image(url=random.choice(["https://cdn61.picsart.com/197337928002202.gif?r1024x1024",
                                       "https://media.giphy.com/media/wbrgtEbP1GPNS/giphy.gif",
                                       "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075%22",
                                       "https://i.imgur.com/BPLqSJC.gif"]))
    await client.say(embed=embed)

@client.command(pass_context=True)
async def nuke(ctx, member: discord.Member):
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
                                       "https://media.giphy.com/media/12VXIxKaIEarL2/giphy.gif"]))

    await client.say(embed=embed)


@client.command(pass_context=True)
async def bloodsuck(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed(description="**{1}** is bloodsucking **{0}**".format(member.mention, author.mention), color=7990033)
    embed.set_image(url=random.choice(["http://gifimage.net/wp-content/uploads/2017/09/anime-vampire-bite-gif-11.gif",
                                       "https://media1.tenor.com/images/17f0fc8bc1e0d5df5f519b8cd9237ac8/tenor.gif?itemid=5384805",
                                       "http://gifimage.net/wp-content/uploads/2017/09/anime-vampire-bite-gif-8.gif",
                                       "http://gifimage.net/wp-content/uploads/2017/09/anime-vampire-bite-gif-10.gif"]))
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
     if ctx.message.author.id == '365797140448018443':
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
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play  (ctx, *, song):
      opts = { 'default_search': 'auto','quiet':True, }
      voice_client = client.voice_client_in(ctx.message.server)
      player = await voice_client.create_ytdl_player(song, ytdl_options=opts)
      players[ctx.message.server.id] = player
      player.start()
      emb = discord.Embed(color=13632027, title='Now Playing: ' + player.title )
      await client.say(embed = emb)

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

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

client.loop.create_task(change_status())
client.run("TOKEN")
