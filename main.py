import discord
from discord.ext import commands
from discord_secret import *
import asyncio
import msg

client = commands.Bot(command_prefix="!")


roles = None


@client.event
async def on_ready():
    print("Présent")

    # Get roles
    global roles

    roles = client.get_guild(833680986176225280).roles
    client.loop.create_task(rainbow_role())


# Auto change color for role "Ambassadeur" for fun
async def rainbow_role():
    global roles

    colours = [discord.Color.dark_orange(), discord.Color.orange(), discord.Color.dark_gold(), discord.Color.gold(),
               discord.Color.dark_magenta(), discord.Color.magenta(), discord.Color.red(), discord.Color.dark_red(),
               discord.Color.blue(), discord.Color.dark_blue(), discord.Color.teal(), discord.Color.dark_teal(),
               discord.Color.green(), discord.Color.dark_green(), discord.Color.purple(), discord.Color.dark_purple()]

    while True:
        for role in roles:
            if role.id == 835876045273038919:
                for colour in colours:
                    await role.edit(color=colour)
                    await asyncio.sleep(1)


@client.event
async def on_message(message):
    # Verify if it's an other msg than !suggest in suggestion channel
    if message.channel.id == 835648274353618974:
        if str(message.content)[0:8] != "!suggest":
            if str(message.author) != "Heldy#3856":
                await message.channel.purge(limit=1)
        else:
            await message.channel.purge(limit=1)
    else:
        if str(message.content)[0:8] == "!suggest":
            await message.channel.purge(limit=1)

    await client.process_commands(message)


# Load
@client.command()
@commands.has_any_role(835886105131352115, 835957850178060318)
async def load(ctx, name=None):
    if name:
        client.load_extension(name)
        await ctx.send("Extension chargée")


# Unload
@client.command()
async def unload(ctx, name=None):
    if name:
        client.unload_extension(name)
        await ctx.send("Extension déchargée")


# Reload
@client.command()
async def reload(ctx, name=None):
    if name:
        try:
            client.reload_extension(name)
            await ctx.send("Extension rechargée")
        except:
            client.load_extension(name)


# Delete message
@client.command()
@commands.has_any_role(835886105131352115, 835957850178060318)
async def d(ctx, amount):
    if str(amount) == "all":
        await ctx.channel.purge(limit=1000)
    else:
        await ctx.channel.purge(limit=int(amount) + 1)


@client.command()
async def suggest(ctx, *, suggestion):
    channel = client.get_channel(835648274353618974)

    suggestEmbed = discord.Embed(colour=0xF1E6B8)
    suggestEmbed.set_author(name=f'Auteur : {ctx.message.author}', icon_url=f'{ctx.author.avatar_url}')
    suggestEmbed.add_field(name='> Nouvelle suggestion : \n', value=f'\n{suggestion}')

    message = await channel.send(embed=suggestEmbed)
    await message.add_reaction('✅')
    await message.add_reaction('❎')

client.run(token)