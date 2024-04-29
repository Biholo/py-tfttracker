import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members =True

bot = commands.Bot(command_prefix='!', intents=intents)

api_key = os.getenv("API_KEY")
discord_key = os.getenv("DISCORD_KEY")

user_data = {}

# Faire help et init

# @bot.command()
# async def help(ctx):
    

@bot.command()
async def ping(ctx):
  await ctx.send('TftTracker est bien opérationnel !')

@bot.command()
async def define(ctx, member: discord.Member, riot_name: str, region: str):
    user_data[member.id] = {"riot_name": riot_name, "region": region}
    await ctx.send(f"{member.display_name} : Riot username = {riot_name}; Region = {region}")

@bot.command()
async def display(ctx):
    await ctx.send(user_data)

@bot.command()
async def stats(ctx, member: discord.Member):
    # rank = "Challenger"
    # lp = 250
    # current_game = True
    # game_info = "ID de la partie : 12345, Top 4, Gain de LP : +20"
    # composition = "Blaster/Brawler"

    # if current_game:
    #     response = f"**{summoner_name}** est actuellement en partie !\n{game_info}\nComposition : {composition}"
    # else:
    #     response = f"**{summoner_name}** est {rank} avec {lp} LP.\nComposition préférée : {composition}"

    # await ctx.send(response)
    if member.id in user_data:
        data = user_data[member.id]
        await ctx.send(f"Informations pour {member.display_name} : Nom d'utilisateur Riot = {data['riot_name']}, Région = {data['region']}")
    else:
        await ctx.send(f"Aucune information trouvée pour {member.display_name}.")
        await ctx.send(f"Merci de l'ajouter via la commande suivante :")
        await ctx.send(f"!define @Mention RiotUsername Region @TeamTracker")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!help"))
    print(f"Bot connecté en tant que {bot.user.name} ({bot.user.id})")

bot.run(discord_key)