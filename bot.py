from discord.ext import commands
from discord import utils as discord_utils

DISCORD_TOKEN  = "{TOKEN}"
DISCORD_SERVER = "EventServer"
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    if DISCORD_SERVER not in map(lambda x: x.name, bot.guilds):
        print(f"{DISCORD_SERVER} not found in the bot's guilds")
    else:
        print(f"{bot.user.name} bot successfully logged into the {DISCORD_SERVER} guild.")

@bot.command(name="hello")
async def hello(ctx):
    if ctx.author.id == bot.user.id: # the bot does not reply to itself
        return
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()f
    for each_message in messages:
        await each_message.delete()

@bot.command("poll")
async def show_poll(ctx, *args):
    # polls can only be sent from the 'admins' channel
    if ctx.channel.name != "admins":
        return
    # poll command:
    # !poll event_name event_date
    event_name = args[0]
    event_date = args[1]
    # retrieving the 'events' channel
    events_channel = discord_utils.get(ctx.guild.channels, name="events")
    # sending the poll
    message = await events_channel.send(f"@everyone Will you come to the **{event_name}** event the **{event_date}**?")
    # adding reactions to the poll
    await message.add_reaction('U00002705')
    await message.add_reaction('U0000274C')

bot.run(DISCORD_TOKEN)