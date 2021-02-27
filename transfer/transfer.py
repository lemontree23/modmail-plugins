from discord.ext import commands


class Transfer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Transfer(bot))
