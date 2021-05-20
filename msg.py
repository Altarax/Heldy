import discord
from discord.ext import commands
from main import client

'''
User	                    <@USER_ID>	    <@80351110224678912>	
User (Nickname)	            <@!USER_ID>	    <@!80351110224678912>	
Channel	                    <#CHANNEL_ID>	<#103735883630395392>	
Role	                    <@&ROLE_ID>	    <@&165511591545143296>	
Custom Emoji	            <:NAME:ID>	    <:mmLol:216154654256398347>	
Custom Emoji (Animated)	    <:a:NAME:ID>	<a:b1nzy:392938283556143104>
'''


@client.event
async def on_raw_reaction_add(payload):
    # Guide Message
    roles_msg_ID = 837302849448312852

    if roles_msg_ID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        if emoji == '🏈':
            role = discord.utils.get(guild.roles, name="Staps")
        elif emoji == '🌎':
            role = discord.utils.get(guild.roles, name="Histoire-géographie")
        elif emoji == '🏫':
            role = discord.utils.get(guild.roles, name="Lycée")
        elif emoji == '🔎':
            role = discord.utils.get(guild.roles, name="Philosophie")
        elif emoji == '🏠':
            role = discord.utils.get(guild.roles, name="Architecture")
        elif emoji == '✈':
            role = discord.utils.get(guild.roles, name="Aviation")
        elif emoji == '💻':
            role = discord.utils.get(guild.roles, name="Informatique")
        elif emoji == '➕':
            role = discord.utils.get(guild.roles, name="Mathématiques")
        elif emoji == '🏛':
            role = discord.utils.get(guild.roles, name="Droit")
        elif emoji == '🎵':
            role = discord.utils.get(guild.roles, name="Musique")
        elif emoji == '💶':
            role = discord.utils.get(guild.roles, name="Economie")
        elif emoji == '🍃':
            role = discord.utils.get(guild.roles, name="Ecologie")
        elif emoji == '🔨':
            role = discord.utils.get(guild.roles, name="BTP")
        elif emoji == '⌚':
            role = discord.utils.get(guild.roles, name="Gestion")
        elif emoji == '💉':
            role = discord.utils.get(guild.roles, name="Médecine")
        elif emoji == '🏨':
            role = discord.utils.get(guild.roles, name="Hôtellerie-et-restauration")
        elif emoji == '🈴':
            role = discord.utils.get(guild.roles, name="Langues")
        elif emoji == '🏢':
            role = discord.utils.get(guild.roles, name="Immobilier")
        elif emoji == '⚙':
            role = discord.utils.get(guild.roles, name="Industriel")
        elif emoji == '🧳':
            role = discord.utils.get(guild.roles, name="Tourisme")
        await member.add_roles(role)

    # Guide Message 2
    roles_msg_ID = 840983022232797184

    if roles_msg_ID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        if emoji == '🔌':
            role = discord.utils.get(guild.roles, name="Electronique")
        elif emoji == '🆘':
            role = discord.utils.get(guild.roles, name="Social")
        elif emoji == '🛏️':
            role = discord.utils.get(guild.roles, name="Psychologie")
        elif emoji == '💱':
            role = discord.utils.get(guild.roles, name="Commerce")
        elif emoji == '🎨':
            role = discord.utils.get(guild.roles, name="Arts & Spectacles")
        await member.add_roles(role)

    # Level Msg
    level_msg_ID = 835984389232918558

    if level_msg_ID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        if emoji == '1️⃣':
            role = discord.utils.get(guild.roles, name="BAC ou Equivalent")
        elif emoji == '2️⃣':
            role = discord.utils.get(guild.roles, name="BAC +2")
        elif emoji == '3️⃣':
            role = discord.utils.get(guild.roles, name="BAC +3")
        elif emoji == '4️⃣':
            role = discord.utils.get(guild.roles, name="BAC +4")
        elif emoji == '5️⃣':
            role = discord.utils.get(guild.roles, name="BAC +5")
        elif emoji == '*️⃣':
            role = discord.utils.get(guild.roles, name="BAC >5")
        await member.add_roles(role)

    # Statut Msg
    stats_msg_ID = 837270721834647563

    if stats_msg_ID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        if emoji == '📒':
            role = discord.utils.get(guild.roles, name="Alternant")
        elif emoji == '📙':
            role = discord.utils.get(guild.roles, name="Etudiant")
        elif emoji == '📕':
            role = discord.utils.get(guild.roles, name="Boursier")
        elif emoji == '📘':
            role = discord.utils.get(guild.roles, name="Diplômé.e")

        await member.add_roles(role)

    # Regions Message
    regions_msg_ID = 835632955689926656

    if regions_msg_ID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        if emoji == '💘':
            role = discord.utils.get(guild.roles, name="Auvergne-Rhône-Alpes")
        elif emoji == '💝':
            role = discord.utils.get(guild.roles, name="Bourgogne-Franche-Comté")
        elif emoji == '🤍':
            role = discord.utils.get(guild.roles, name="Bretagne")
        elif emoji == '💖':
            role = discord.utils.get(guild.roles, name="Centre-Val-de-Loire")
        elif emoji == '💗':
            role = discord.utils.get(guild.roles, name="Corse")
        elif emoji == '❤️':
            role = discord.utils.get(guild.roles, name="Grand-Est")
        elif emoji == '🧡':
            role = discord.utils.get(guild.roles, name="Hauts-de-France")
        elif emoji == '💛':
            role = discord.utils.get(guild.roles, name="Île-de-France")
        elif emoji == '💚':
            role = discord.utils.get(guild.roles, name="Normandie")
        elif emoji == '💙':
            role = discord.utils.get(guild.roles, name="Nouvelle-Aquitaine")
        elif emoji == '💜':
            role = discord.utils.get(guild.roles, name="Occitanie")
        elif emoji == '🤎':
            role = discord.utils.get(guild.roles, name="Pays-de-la-Loire")
        elif emoji == '🖤':
            role = discord.utils.get(guild.roles, name="Provence-Alpes-Côte-d'Azur")
        await member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    # Guide Message
    roles_msg_ID = 837302849448312852

    if roles_msg_ID == payload.message_id:
        guild = await(client.fetch_guild(payload.guild_id))

        emoji = payload.emoji.name

        if emoji == '🏈':
            role = discord.utils.get(guild.roles, name="Staps")
        elif emoji == '🌎':
            role = discord.utils.get(guild.roles, name="Histoire-géographie")
        elif emoji == '🏫':
            role = discord.utils.get(guild.roles, name="Lycée")
        elif emoji == '🔎':
            role = discord.utils.get(guild.roles, name="Philosophie")
        elif emoji == '🏠':
            role = discord.utils.get(guild.roles, name="Architecture")
        elif emoji == '✈':
            role = discord.utils.get(guild.roles, name="Aviation")
        elif emoji == '💻':
            role = discord.utils.get(guild.roles, name="Informatique")
        elif emoji == '➕':
            role = discord.utils.get(guild.roles, name="Mathématiques")
        elif emoji == '🏛':
            role = discord.utils.get(guild.roles, name="Droit")
        elif emoji == '🎵':
            role = discord.utils.get(guild.roles, name="Musique")
        elif emoji == '💶':
            role = discord.utils.get(guild.roles, name="Economie")
        elif emoji == '🍃':
            role = discord.utils.get(guild.roles, name="Ecologie")
        elif emoji == '🔨':
            role = discord.utils.get(guild.roles, name="BTP")
        elif emoji == '⌚':
            role = discord.utils.get(guild.roles, name="Gestion")
        elif emoji == '💉':
            role = discord.utils.get(guild.roles, name="Médecine")
        elif emoji == '🏨':
            role = discord.utils.get(guild.roles, name="Hôtellerie-et-restauration")
        elif emoji == '🈴':
            role = discord.utils.get(guild.roles, name="Langues")
        elif emoji == '🏢':
            role = discord.utils.get(guild.roles, name="Immobilier")
        elif emoji == '⚙':
            role = discord.utils.get(guild.roles, name="Industriel")
        elif emoji == '🧳':
            role = discord.utils.get(guild.roles, name="Tourisme")

        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            pass

    # Guide Message 2
    roles_msg_ID = 840983022232797184

    if roles_msg_ID == payload.message_id:
        guild = await(client.fetch_guild(payload.guild_id))

        emoji = payload.emoji.name

        if emoji == '🔌':
            role = discord.utils.get(guild.roles, name="Electronique")
        elif emoji == '🆘':
            role = discord.utils.get(guild.roles, name="Social")
        elif emoji == '🛏️':
            role = discord.utils.get(guild.roles, name="Psychologie")
        elif emoji == '💱':
            role = discord.utils.get(guild.roles, name="Commerce")
        elif emoji == '🎨':
            role = discord.utils.get(guild.roles, name="Arts & Spectacles")

        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            pass

    # Level Msg
    level_msg_ID = 835984389232918558

    if level_msg_ID == payload.message_id:
        guild = await(client.fetch_guild(payload.guild_id))

        emoji = payload.emoji.name

        if emoji == '1️⃣':
            role = discord.utils.get(guild.roles, name="BAC ou Equivalent")
        elif emoji == '2️⃣':
            role = discord.utils.get(guild.roles, name="BAC +2")
        elif emoji == '3️⃣':
            role = discord.utils.get(guild.roles, name="BAC +3")
        elif emoji == '4️⃣':
            role = discord.utils.get(guild.roles, name="BAC +4")
        elif emoji == '5️⃣':
            role = discord.utils.get(guild.roles, name="BAC +5")
        elif emoji == '*️⃣':
            role = discord.utils.get(guild.roles, name="BAC >5")

        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            pass

    # Statut Msg
    stats_msg_ID = 837270721834647563

    if stats_msg_ID == payload.message_id:
        guild = await(client.fetch_guild(payload.guild_id))

        emoji = payload.emoji.name

        if emoji == '📒':
            role = discord.utils.get(guild.roles, name="Alternant")
        elif emoji == '📙':
            role = discord.utils.get(guild.roles, name="Etudiant")
        elif emoji == '📕':
            role = discord.utils.get(guild.roles, name="Boursier")
        elif emoji == '📘':
            role = discord.utils.get(guild.roles, name="Diplômé.e")

        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            pass

    # Regions Message
    regions_msg_ID = 835632955689926656

    if regions_msg_ID == payload.message_id:
        guild = await(client.fetch_guild(payload.guild_id))

        emoji = payload.emoji.name

        if emoji == '💘':
            role = discord.utils.get(guild.roles, name="Auvergne-Rhône-Alpes")
        elif emoji == '💝':
            role = discord.utils.get(guild.roles, name="Bourgogne-Franche-Comté")
        elif emoji == '🤍':
            role = discord.utils.get(guild.roles, name="Bretagne")
        elif emoji == '💖':
            role = discord.utils.get(guild.roles, name="Centre-Val-de-Loire")
        elif emoji == '💗':
            role = discord.utils.get(guild.roles, name="Corse")
        elif emoji == '❤️':
            role = discord.utils.get(guild.roles, name="Grand-Est")
        elif emoji == '🧡':
            role = discord.utils.get(guild.roles, name="Hauts-de-France")
        elif emoji == '💛':
            role = discord.utils.get(guild.roles, name="Île-de-France")
        elif emoji == '💚':
            role = discord.utils.get(guild.roles, name="Normandie")
        elif emoji == '💙':
            role = discord.utils.get(guild.roles, name="Nouvelle-Aquitaine")
        elif emoji == '💜':
            role = discord.utils.get(guild.roles, name="Occitanie")
        elif emoji == '🤎':
            role = discord.utils.get(guild.roles, name="Pays-de-la-Loire")
        elif emoji == '🖤':
            role = discord.utils.get(guild.roles, name="Provence-Alpes-Côte-d'Azur")

        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("Test")


# -------------------------------------------
# --------- Messages with the bots ---------
# -------------------------------------------


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def role_msg(ctx):
    embed = discord.Embed(title="Votre guide !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Guide des rôles : \n"
                                     "\n🏈 <@&836877338577731634>\n"
                                     "\n🌎 <@&836876629087223829>\n"
                                     "\n🏫 <@&836876683436228628>\n"
                                     "\n🔎 <@&836876686569766912>\n"
                                     "\n🏠 <@&836876690230870056>\n"
                                     "\n🧳 <@&837276081576214528>\n"
                                     "\n✈ <@&836876692190003220>\n"
                                     "\n💻 <@&835488905766764584>\n"
                                     "\n➕ <@&835488905766895616>\n"
                                     "\n🏛 <@&835488906346233896>\n"
                                     "\n🎵 <@&835522419787038730>\n"
                                     "\n💶 <@&835520809015574549>\n"
                                     "\n🍃 <@&835520809904767037>\n"
                                     "\n🔨 <@&835521516082823178>\n"
                                     "\n⌚ <@&835520811842273290>\n"
                                     "\n💉 <@&835520812387663913>\n"
                                     "\n🏨 <@&835520911204810803>\n"
                                     "\n🈴 <@&835520926912348180>\n"
                                     "\n🏢 <@&835522774817832991>\n"
                                     "\n⚙ <@&835521441280557057>\n**")

    embed.add_field(name="🌈", value="**Explications : \n"
                                     "\nLe but étant de choisir le diplôme dans lequel vous êtes et dans celui ou "
                                     "ceux qui vous intéresse.nt. "
                                     "\nDe ce fait, vous aurez accès aux channels correspondants.\n"
                                     "\n Pour choisir vos rôles, vous pouvez le faire avec les emojis "
                                     "associés à ce message dans le même ordre que la liste à gauche.\n"
                                     "\nSi vous pensez qu'il en manque, n'hésitez pas à nous prévenir**")

    message = await ctx.send(embed=embed)
    await message.add_reaction('🏈')
    await message.add_reaction('🌎')
    await message.add_reaction('🏫')
    await message.add_reaction('🔎')
    await message.add_reaction('🏠')
    await message.add_reaction('🧳')
    await message.add_reaction('✈')
    await message.add_reaction('💻')
    await message.add_reaction('➕')
    await message.add_reaction('🏛')
    await message.add_reaction('🎵')
    await message.add_reaction('💶')
    await message.add_reaction('🍃')
    await message.add_reaction('🔨')
    await message.add_reaction('⌚')
    await message.add_reaction('💉')
    await message.add_reaction('🏨')
    await message.add_reaction('🈴')
    await message.add_reaction('🏢')
    await message.add_reaction('⚙')


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def role_msg2(ctx):
    embed = discord.Embed(title="Votre guide !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Guide des rôles : \n"
                                     "\n🔌 <@&835521379297132544> \n"
                                     "\n🆘 <@&838083198755405854> \n"
                                     "\n🛏️ <@&838397499643002891> \n"
                                     "\n💱 <@&840902562018492426> \n"
                                     "\n🎨 <@&840982404033150986> \n"
                                     "**")

    embed.add_field(name="🌈", value="**Explications : \n"
                                     "\nLe but étant de choisir le diplôme dans lequel vous êtes et dans celui ou "
                                     "ceux qui vous intéresse.nt. "
                                     "\nDe ce fait, vous aurez accès aux channels correspondants.\n"
                                     "\n Pour choisir vos rôles, vous pouvez le faire avec les emojis "
                                     "associés à ce message dans le même ordre que la liste à gauche.\n"
                                     "\nSi vous pensez qu'il en manque, n'hésitez pas à nous prévenir**")

    message = await ctx.send(embed=embed)
    await message.add_reaction('🔌')
    await message.add_reaction('🆘')
    await message.add_reaction('🛏️')
    await message.add_reaction('💱')
    await message.add_reaction('🎨')


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def level_msg(ctx):
    embed = discord.Embed(title="Votre guide !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Guide des rôles : \n"
                                     "\n<@&835983953201725450>\n"
                                     "\n<@&835485799263764491>\n"
                                     "\n<@&835485868574769152>\n"
                                     "\n<@&835485870051164170>\n"
                                     "\n<@&835485870563917874>\n"
                                     "\n<@&835485871091613726>**\n")

    embed.add_field(name="🌈", value="**Explications : \n"
                                     "\nLe but étant de choisir le niveau dans lequel vous êtes et dans celui ou "
                                     "ceux qui vous intéresse.nt. "
                                     "\nDe ce fait, vous aurez accès aux channels correspondants.\n"
                                     "\n Pour choisir vos rôles, vous pouvez le faire avec les emojis "
                                     "associés à ce message dans le même ordre que la liste à gauche.\n"
                                     "\nSi vous pensez qu'il en manque, n'hésitez pas à nous prévenir**")

    message = await ctx.send(embed=embed)
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')
    await message.add_reaction('4️⃣')
    await message.add_reaction('5️⃣')
    await message.add_reaction('*️⃣')


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def stat_msg(ctx):
    embed = discord.Embed(title="Votre guide !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Guide des rôles : \n"
                                     "\n<@&835488903808024618>\n"
                                     "\n<@&835488904412659712>\n"
                                     "\n<@&835488904772845618>\n"
                                     "\n<@&837269089549680680>**\n")

    embed.add_field(name="🌈", value="**Explications : \n"
                                     "\nLe but étant de choisir le statut dans lequel vous êtes et dans celui ou "
                                     "ceux qui vous intéresse.nt. "
                                     "\nDe ce fait, vous aurez accès aux channels correspondants.\n"
                                     "\n Pour choisir vos rôles, vous pouvez le faire avec les emojis "
                                     "associés à ce message dans le même ordre que la liste à gauche.\n"
                                     "\nSi vous pensez qu'il en manque, n'hésitez pas à nous prévenir**")

    message = await ctx.send(embed=embed)
    await message.add_reaction('📒')
    await message.add_reaction('📙')
    await message.add_reaction('📕')
    await message.add_reaction('📘')


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def region_msg(ctx):
    embed = discord.Embed(title="Votre guide !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Guide des rôles : \n"
                                     "\n💘 <@&835485871456387094>\n"
                                     "\n💝 <@&835485871779217451>\n"
                                     "\n🤍 <@&835485872659890176>\n"
                                     "\n💖 <@&835485873138171944>\n"
                                     "\n💗 <@&835485873633230888>\n"
                                     "\n❤️ <@&835488317696901200>\n"
                                     "\n🧡 <@&835488319198593065>\n"
                                     "\n💛 <@&835488320321486849>\n"
                                     "\n💚 <@&835488320447447080>\n"
                                     "\n💙 <@&835488321718321252>\n"
                                     "\n💜 <@&835488325724799036>\n"
                                     "\n🤎 <@&835488326161137694>\n"
                                     "\n🖤 <@&835488326483836929>**")

    embed.add_field(name="🌈", value="**Explications : \n"
                                     "\nLe but étant de choisir la région dans lequel vous êtes et dans celle ou "
                                     "celles qui vous intéresse.nt. "
                                     "\nDe ce fait, vous aurez accès aux channels correspondants.\n"
                                     "\n Pour choisir vos rôles, vous pouvez le faire avec les emojis "
                                     "associés à ce message dans le même ordre que la liste à gauche.**\n")

    message = await ctx.send(embed=embed)
    await message.add_reaction('💘')
    await message.add_reaction('💝')
    await message.add_reaction('🤍')
    await message.add_reaction('💖')
    await message.add_reaction('💗')
    await message.add_reaction('❤️')
    await message.add_reaction('🧡')
    await message.add_reaction('💛')
    await message.add_reaction('💚')
    await message.add_reaction('💙')
    await message.add_reaction('💜')
    await message.add_reaction('🤎')
    await message.add_reaction('🖤')


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def prop_msg(ctx):
    embed = discord.Embed(title="Votre guide !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Guide des ressources : \n"
                                     "\nEn fonction des channels dont vous avez accès, "
                                     "vous pouvez retrouver des ressources liés aux domaines qui vous intéressent.\n"
                                     "\nSi vous souhaitez proposer des ressources faites par vous-même ou trouvées "
                                     "sur internet, "
                                     "n'hésitez pas à nous en parler dans le channel <#835622649936871484>\n"
                                     "\nSi ce sont des fichiers personnels, veuillez créer des archives .zip et nous"
                                     "vous contacterons par message privé le plus rapidement possible pour les "
                                     "récupérer.**")

    await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def links_msg(ctx):
    embed = discord.Embed(title="Le site web !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Liens utiles : \n"
                                     "\n🌐 Site web : https://heldy.fr/accueil \n"
                                     "\n🌐 Ambassadeurs : https://heldy.fr/accueil/index.php/ambassadeurs/ \n"
                                     "\n💶 Aides financières : https://heldy.fr/accueil/index.php/aides-financieres/ \n"
                                     "\n💶 Aides candidatures : https://heldy.fr/accueil/index.php/aides-candidatures/ \n"
                                     "\n#️⃣ Notre instagram :  https://www.instagram.com/heldy_students/ \n"
                                     "\n📰 Formations : "
                                     "**")
    await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def rules_msg(ctx):
    embed = discord.Embed(title="Nos règles !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="1️⃣", value="**Il est très important pour vous de choisir un rôle ! N'hésitez pas à le faire "
                                      "^^**\n")
    embed.add_field(name="2️⃣", value="**Traitez tout le monde avec respect. Aucun harcèlement, chasse aux sorcières, "
                                      "sexisme, racisme ou discours de haine ne sera toléré. "
                                      "**\n")
    embed.add_field(name="3️⃣", value="**Pas de spam ni d'autopromotion (invitations de serveurs, publicités, "
                                      "etc.) sans l'autorisation d'un modérateur du serveur, y compris via les MP "
                                      "envoyés aux autres membres.**\n")
    embed.add_field(name="4️⃣", value="**Pas de contenu violent, obscène ou NSFW, qu'il s'agisse de texte, d'images "
                                      "ou de liens mettant en scène de la nudité, du sexe, de l'hyperviolence ou un "
                                      "quelconque contenu dérangeant.**\n")
    embed.add_field(name="5️⃣", value="**Si tu remarques quelque chose de contraire aux règles ou qui te met dans un "
                                      "sentiment d'insécurité, informe-en les modérateurs. Nous voulons que ce "
                                      "serveur soit accueillant pour tout le monde !**\n")

    message = await ctx.send(embed=embed)
    await message.add_reaction('✅')


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def suggests_msg(ctx):
    embed = discord.Embed(title="Faire une suggestion !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Pour faire une suggestion vous pouvez utiliser : \n"
                                     "\n> La commande !suggest VOTRE_SUGGESTION\n"
                                     "\n> Aucun autre message ne pourra être posté ici ^^**")

    message = await ctx.send(embed=embed)
    await message.add_reaction('✅')


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def ambassadeurs_msg(ctx):
    embed = discord.Embed(title="Devenir un embassadeur !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Vous souhaitez devenir ambassadeur ou ambassadrice ?\n"
                                     "\nPouvoir aider bénévolement à la réussite de tous et toutes ?\n"
                                     "\n> Il te faut alors envoyer un message privé à <@270670173059547136>"
                                     "\n> En présisant d'où tu viens, ton diplôme et ton niveau et surtout, un petit "
                                     "message pour parler de toi ne peut que t'aider !**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def links_msg2(ctx):
    embed = discord.Embed(title="Pour partager le discord !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**https://discord.gg/q2Kv3qAdbp\n**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def questions_msg(ctx):
    embed = discord.Embed(title="Questions récurrentes !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Ici vous pouvez poser toutes les questions que vous voulez. \nChaque "
                                     "semaine nous ferons un tri et garderons toutes celles qui ont été les plus"
                                     "posées pour les ajouter au site et sur le discord ainsi que leur réponse.\n**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def entretien(ctx):
    embed = discord.Embed(title="Ressources utiles !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Un entretien en vue ? Ce PDF est fait pour vous ! \n"
                                     "**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def informatique(ctx):
    embed = discord.Embed(title="Ressources utiles !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Un site qui regroupe des pdf en anglais d'une superbe qualité ! \n"
                                     "https://books.goalkicker.com/ \n"
                                     "\nBesoin d'apprendre des langages de programmation ? Suis ce lien : \n"
                                     "https://www.learndev.info/ \n"
                                     "\n Beaucoup de choses qui peuvent vous intéresser : \n"
                                     "https://sites.google.com/view/newecligne/accueil?authuser=0"
                                     "**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def electronique(ctx):
    embed = discord.Embed(title="Ressources utiles !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Un site qui regroupe des pdf en anglais d'une superbe qualité ! \n"
                                     "https://books.goalkicker.com/ \n"
                                     "\nBesoin d'apprendre des langages de programmation ? Suis ce lien : \n"
                                     "https://www.learndev.info/fr \n"
                                     "\nPour faire du VHDL : \n"
                                     "https://www.unilim.fr/pages_perso/vahid.meghdadi-neyshabouri/vhdl.html \n"
                                     "\nPour faire de l'électronique et bien d'autres : \n"
                                     "https://www.enib.fr/~kerhoas/index.html\n"
                                     "\n Beaucoup de choses qui peuvent vous intéresser : \n"
                                     "https://sites.google.com/view/newecligne/accueil?authuser=0"
                                     "**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def maths(ctx):
    embed = discord.Embed(title="Ressources utiles !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Besoin d'annales et de corrections ? \n"
                                     "https://cristofari.pagesperso-orange.fr/ecrits.html \n"
                                     "\n Beaucoup de choses qui peuvent vous intéresser : \n"
                                     "https://sites.google.com/view/newecligne/accueil?authuser=0"
                                     "**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def industriel(ctx):
    embed = discord.Embed(title="Ressources utiles !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Tout sur les liaisons ! \n"
                                     "http://bboy78.free.fr/Cours%20TN01/C9_SolutionsTechnologiques.pdf \n"
                                     "\n Beaucoup de choses qui peuvent vous intéresser : \n"
                                     "https://sites.google.com/view/newecligne/accueil?authuser=0"
                                     "**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def medecine(ctx):
    embed = discord.Embed(title="Ressources utiles !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**Reminder pour les débutants (des images) ! \n"
                                     "Lien drive à venir : \n"
                                     "\nUn référentiel d'anatomie humaine : \n"
                                     "https://drive.google.com/file/d/1Xz-OPjPl57JSw5OOkBE48yI1HiTDe85O/view?usp=sharing \n"
                                     "**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def lycee(ctx):
    embed = discord.Embed(title="Ressources utiles !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**\n Vous aider à réussir le bac: \n"
                                     "http://www.gecif.net/#ab\n"
                                     "https://www.bacdefrancais.net/deroulement-oral-bac-francais.php"
                                     "**")

    message = await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role(835886105131352115, 835957850178060318)
async def hebergement(ctx):
    embed = discord.Embed(title="Catégorie hébergement !", colour=discord.Colour(0xF1E6B8),
                          url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526"
                              "/logo_H_color.png")

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/833680986176225283/835302356253802526/logo_H_color.png")
    embed.set_author(name="Heldy", icon_url="https://cdn.discordapp.com/emojis/482704428512706583.gif?v=1")

    embed.add_field(name="🌈", value="**\n 🌍 Aides sur l'hébergement : 🌍 \n"
                                     "\n Dans cette catégorie vous trouverez des salons vous permettant "
                                     "de discuter avec différents étudiants dans les régions qui vous "
                                     "intéressent et demander par exemple pour les aides spécifiques aux régions "
                                     "et surtout parler des hébergements et pourquoi pas de proposer des collocations "
                                     "ou en demander ! Soyez créatifs et n'hésitez pas à demander de l'aide !\n "
                                     "\n Voici tous les salons à votre disposition : \n"
                                     "\n> <#839827549814915073>	\n"
                                     "> <#839828900976656414>	\n"
                                     "> <#839827800386961410>	\n"
                                     "> <#839827866152861706>	\n"
                                     "> <#839828367480979457>	\n"
                                     "> <#839828241681743903>	\n"
                                     "> <#839828856315052063>	\n"
                                     "> <#839828282655768616>	\n"
                                     "> <#839828320283262987>	\n"
                                     "> <#839828216356929547>	\n"
                                     "> <#839828403552649216>	\n"
                                     "> <#839827812109123648>	\n"
                                     "> <#839828179836600320>	\n"
                                     "**")

    message = await ctx.send(embed=embed)
