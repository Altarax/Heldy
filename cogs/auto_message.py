# Libraries
import discord
import random

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands


class Auto_message(commands.Cog):
    def __init__(self, cli):
        self.cli = cli

        # initializing scheduler
        scheduler = AsyncIOScheduler()

        # sends msg to the channel every day
        scheduler.add_job(self.every_day, 'interval', hours=24, misfire_grace_time=50, start_date='2021-05-17 14:33:00',
                          end_date='2030-05-15 '
                                   '19:00:00')

        # starting the scheduler
        scheduler.start()

    @commands.Cog.listener()
    async def every_day(self):
        general_channel = self.cli.get_channel(835626583045177384)
        announce_channel = self.cli.get_channel(838481170944753704)

        embed = discord.Embed(title="Pour nous soutenir !", colour=discord.Colour(0xF1E6B8),
                              url="https://heldy.fr/accueil/")

        embed.set_thumbnail(
            url="https://cdn.mee6.xyz/guild-images/833680986176225280/512c86165eb21b6bedcedb3aa869138015f9548a8c3ab55b6a2e95d673dadf4f.png")
        embed.set_author(name="Heldy", icon_url="https://emoji.gg/assets/emoji/6286_tada_animated.gif")

        embed.add_field(name="‏‏‎ ‎",
                        value="<a:arrow_rainbow:842899601555193906> **Retrouvez des informations que vous "
                              "auriez ratées sur notre site ! Il "
                              "peut vous être utile : "
                              "https://heldy.fr/accueil/  **\n",
                        inline=False)

        embed.add_field(name="‏‏‎ ‎", value="<a:arrow_rainbow:842899601555193906> **Votez ça nous aide beaucoup : "
                                            "https://discordinvites.net/vote"
                                            "/833680986176225280  **\n",
                        inline=False)

        embed.add_field(name="‏‏‎ ‎", value="<a:arrow_rainbow:842899601555193906> **Nous avons aussi un twitter : "
                                            "https://twitter.com/Heldy_students  **\n",
                        inline=False)

        embed.add_field(name="‏‏‎ ‎",
                        value="<a:arrow_rainbow:842899601555193906> **Merci à ceux qui nous soutiennent**",
                        inline=False)

        general_message = await general_channel.send(embed=embed)
        announce_message = await announce_channel.send(embed=embed)


def setup(cli):
    cli.add_cog(Auto_message(cli))
