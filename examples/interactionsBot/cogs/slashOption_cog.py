import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.commands import slash_command
from discord.commands import Option

class SlashOptionExample(commands.Cog):
    def __init__(self,client):
        self.client = client    

    # slash commands with options
    @slash_command(guild_ids=[...],name="avatar",description="check someones avatar!")
    async def av(self,ctx,
                 # <discord.commands.Option>
                 member: Option(discord.Member,description="the user you want the avatar of.")
                ):
        """
        ephemeral makes "Only you can see this" message

        `await ctx.respond(embed=discord.Embed().set_image(url=str(member.avatar.url)),ephemeral=True)`

        embed docs - https://docs.pycord.dev/en/master/api.html#embed
        member docs - https://docs.pycord.dev/en/master/api.html#discord.Member
        """
        return await ctx.respond(embed=discord.Embed().set_image(url=str(member.avatar.url)))

    @av.error
    async def av_error(self, ctx:Context ,error):
        return await ctx.respond(error,ephemeral=True) # ephemeral makes "Only you can see this" message

def setup(client):
    client.add_cog(SlashOptionExample(client))