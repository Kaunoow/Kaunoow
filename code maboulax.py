import discord
from discord.ext import commands, tasks 
from discord import Intents

import asyncio
import random
import time
import typing
import upsidedown

bot = commands.Bot(command_prefix = "+", description = "...", help_command = None, intents = Intents.all())

#Event
	
@bot.event
async def on_ready():
	print("------------")
	print("Prêt !")
	print("Bot :")
	print(bot.user.name)
	print("ID :")
	print(bot.user.id)
	print("------------")
	print("Console :")
	changeStatus.start()

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"> {ctx.author.mention} vous devez indiquez un argument pour effectuer cette commande.")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send(f"> {ctx.author.mention} vous n'avez pas les permissions nécessaires pour effectuer cette commande.")

@bot.listen('on_member_join')
async def on_member_join(member : discord.Member):
	channel = member.guild.get_channel(876552551187759155)
	embed = discord.Embed(title = "🧳 __**Arrivée**__", description = f"Bienvenue {member.mention} ! Merci d'aller voir le règlement.", color = 0x235370)
	embed.set_author(name = f"{member}", icon_url = member.avatar_url)
	
	await channel.send(embed = embed)

@bot.event
async def on_member_remove(member : discord.Member):
	channel = member.guild.get_channel(878375123625865226)
	embed = discord.Embed(title = "__**Départ**__", description = f"A bientôt {member.mention} !", color = 0x235370)
	embed.set_author(name = f"{member}", icon_url = member.avatar_url)

	await channel.send(embed = embed)

@bot.listen('on_message') 
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel): #Check if message in DM
        guild = bot.get_guild(875771903799877683)
        channel = guild.get_channel(876553804861034496)
        await channel.send(f"> {message.author.mention} m'a mp en disant : {message.content}")
        return

#Task

@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await bot.change_presence(activity = game)

#Miscellaneous 

@bot.command()
async def embed(ctx, title, *, description):
	embed = discord.Embed(title = title, description = description, color = 0x9400D3)
	embed.set_footer(text = "Modèle Embed")
	await ctx.message.delete()
	await ctx.send(embed = embed) 

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

@say.error 
async def say_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Vous devez écrire quelque chose !")

@bot.command()
async def chinois(ctx, *text):
	chineseChar = "丹书ㄈ力已下呂廾工丿片乚爪ㄇ口尸厶尺ㄎ丁凵人山父了乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a") 
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append(" ") 	 
	await ctx.send("".join(chineseText))

@bot.command()
async def russe(ctx, *text):
	russeChar = "абцдЕфгхийклмнопqрстувшщыз"
	russeText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = russeChar[index]
				russeText.append(transformed)
			else: 
				russeText.append(char)
		russeText.append(" ")
	await ctx.send("".join(russeText))

@bot.command()
async def reverse(ctx, *, sentence : str):
    await ctx.send(sentence[::-1])

#Fun

@bot.command()
async def poids(ctx):
	var = random.randint(30, 250)
	if var > 100:
		message = "Tu connais les légumes ?"
	if var < 100:
		message = "Tu dois être musclé !"
	embed = discord.Embed(title = "⚖️  **Poids**", description = f"{ctx.author.mention} Tu fais {var} kg ! {message}", color = 0x9400D3)

	await ctx.send(embed = embed)

@bot.command()
async def gay(ctx):
	gay = random.randint(0, 100)
	if gay > 50: 
		message = "Oula.."
	if gay < 50: 
		message = "Ca peut aller.."
	if gay < 5:
		message = "Giga chad à énorme queue"
	embed = discord.Embed(title = "🏳️‍🌈 **Gayomètre**", description = f"{ctx.author.mention} Tu es gay à {gay} % ! {message} ", color = 0x9400D3)

	await ctx.send(embed = embed)

@bot.command()
async def disquette(ctx):
	embed = discord.Embed(title = "✉️ **Disquette**", description = f"{ctx.author.mention} {random.choice(disquettes)}", color = 0x9400D3)

	await ctx.send(embed = embed)

@bot.command()
async def blague(ctx):
	embed = discord.Embed(title = "🤣 **Blague**", description = f"{ctx.author.mention} {random.choice(blagues)}", color = 0x9400D3)

	await ctx.send(embed = embed)

@bot.command()
async def meme(ctx):
	await ctx.send(f"> {ctx.author.mention} : Clique sur le lien pour télécharger la vidéo ! {random.choice(memes)}")

@bot.command()
async def nombrerandom(ctx):
	nombre = random.randint(0, 1000)
	embed = discord.Embed(title = "1️⃣  **Nombre**", description = f"{ctx.author.mention} {nombre} !", color = 0x9400D3)

	await ctx.send(embed = embed)

@bot.command()
async def pileouface(ctx):
	embed = discord.Embed(title = "❔ **Pile ou face**", description = f"{ctx.author.mention} {random.choice(pileouface)} !", color = 0x9400D3)
	
	await ctx.send(embed = embed)

@bot.command()
async def mention(ctx, member : discord.Member):
	await ctx.send(f"{member.mention}")
	await ctx.message.delete()

#Images 

@bot.command()
async def cursed(ctx):
	await ctx.send("Soit patient batard")

@bot.command()
async def random(ctx):
	await ctx.send("Soit patient batard")

@bot.command()
async def dog(ctx):
	await ctx.send("Soit patient batard")

@bot.command()
async def cat(ctx):
	await ctx.send("Soit patient batard")

#Informations

@bot.command()
async def serveurInfo(ctx):
    server_description = ctx.guild.description
    embed = discord.Embed(title = "🧾**Informations du serveur**", color = 0xE4A425)
    embed.add_field(name = "🧍🏻 Population :", value = f"Il y a actuellement **{ctx.guild.member_count}** personnes dans le serveur.")
    embed.add_field(name = "📢 Description :", value = server_description)
    embed.add_field(name = "🗨️ Salons :", value = f"Il y a actuellement **{len(ctx.guild.text_channels)}** salons écrits et **{len(ctx.guild.voice_channels)}** salons vocaux.", inline = True)

    await ctx.send(embed = embed)

@bot.command()
async def documentation(ctx): 
	embed = discord.Embed(title = "📖 **Documentation**", description = "Toute ma documentation, au possible actualisée aussi vite que possible est disponible sur Github. Vous avez le droit de vous en aider pour vos projets. Mon code est en Python.", color = 0xE4A425)
	embed = set_thumbnail(name = " ", url = )

@bot.command()
async def ping(ctx):
  the_ping = bot.latency * 1000
  rounded_ping = round(the_ping)
  embed = discord.Embed(title = "🏓  **Pong ! **", description = f"{ctx.author.mention} {rounded_ping} ms !", color = 0xE4A425)

  await ctx.send(embed = embed)

@bot.command()
async def help(ctx):
	embed = discord.Embed(title = "📚 **Listes des commandes**", description = "Je suis un bot discord polyvalent qui fait de la modération et d'autres choses amusantes et utiles.\n\n **🔨 Modération : ** \n\n `+ban`, `+unban`, `+mute`, `+unmute`, `+clear`, `+kick`\n\n **ℹ️ Informations :** \n\n `+help`, `serveurInfo`, `+ping`, `+documentation`\n\n ** 🎉 Fun : ** \n\n `+meme`, `+blague`, `+disquette`, `+poids`, `+gay`, `+nombrerandom`, `+pileouface`\n\n **📷 Images :** \n\n `+cursed`, `+random`, `+dog`, `+cat`\n\n **❓ Divers :** \n\n `+say`, `+chinois`, `+russe`, `+reverse`, `+embed`, `+mention`\n\n **🎶 Musique :** \n\n `Bientôt`\n\n **🏯 Pokémon :** \n\n `Bientôt`", color = 0xE4A425)
	embed.set_author(name = "Maboulax", icon_url = "https://media.discordapp.net/attachments/947914445693263932/947945558713184377/SPOILER_03-drunk-monkey.png?width=507&height=676", )
	embed.set_footer(text = "➞ Besoin d'aide ? Envoyez moi un message ou contactez Dr Maboule#4456 !")

	await ctx.send(embed = embed)

#Administrator

async def createMutedRole(ctx):
	mutedRole = await ctx.guild.create_role(name = "Muted", 
											permissions = discord.Permissions(
												send_messages = False,
												speak = False),
											reason = "Création du role Muted")

	for channel in ctx.guild.channels:
		await channel.set_permissions(mutedRole, send_messages = False, speak = False)
	return mutedRole

async def getMutedRole(ctx):
	roles = ctx.guild.roles
	for role in roles:
		if role.name == "Muted":
			return role

	return await createMutedRole(ctx)

@bot.command()
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member : discord.Member, *, reason = "Aucune"):
	mutedRole = await getMutedRole(ctx)  
	await member.add_roles(mutedRole, reason = reason)
	await member.send(f"> Tu as été mute du serveur **{ctx.guild.name}**. Si tu penses que c'est une erreur, ouvre un **ticket**.")
	embed = discord.Embed(title = "**Mute**", description = f"{member.mention} a été mute !", url = "https://youtu.be/dQw4w9WgXcQ", color = 0xba1206)
	embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/2912-peperee.png")
	embed.add_field(name = "Raison", value = reason)
	embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)

	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_messages = True)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune"):
	mutedRole = await getMutedRole(ctx)
	await member.remove_roles(mutedRole, reason = reason)
	await member.send(f"> Tu as été unmute du serveur **{ctx.guild.name}**. Merci de respecter le règlement pour éviter une éventuelle **sanction**.")
	embed = discord.Embed(title = "**Unmute**", description = f"{member.mention} a été unmute !", url = "https://youtu.be/dQw4w9WgXcQ", color = 0x008000)
	embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/4923-peepo-ok-admins.png")
	embed.add_field(name = "Raison", value = reason)
	embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)

	await ctx.send(embed = embed)
	
@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,nombre : int):
	await ctx.channel.purge(limit = nombre +1)

@bot.command()
@commands.has_permissions(manage_messages = True)
async def kick(ctx, user : discord.User , *, reason = "Aucune"):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	embed = discord.Embed(title = "**Kick**", description = "Quelqu'un a été kick !", url = "https://youtu.be/dQw4w9WgXcQ", color = 0xba1206)
	embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/6132-pepe-high.png")
	embed.add_field(name = "Membre kick", value = user.name, inline = True) 
	embed.add_field(name = "Raison", value = reason)
	embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)

	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *, reason = "Aucune"):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	embed = discord.Embed(title = "**Bannisement**", description = "Le marteau du ban a frappé !", url = "https://youtu.be/dQw4w9WgXcQ", color = 0xba1206)	
	embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/6623_banhammer.png")
	embed.add_field(name = "Membre banni", value = user.name, inline = True)
	embed.add_field(name = "Raison", value = reason)
	embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
	
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *reason):
		reason = " ".join(reason)
		userName, userId = user.split("#")
		bannedUsers = await ctx.guild.bans()
		for i in bannedUsers : 
			if i.user.name == userName and i.user.discriminator == userId:
				await ctx.guild.unban(i.user, reason = reason)
				await ctx.send(f"{user} a été unban.")
				return
		await ctx.send(f"{user} n'a pas été trouvé dans la liste des bans. Veuillez chercher dans la liste des bans **Discord**.")

@bot.command()
@commands.is_owner()
async def changeIntervalle(ctx, secondes = 5):
	changeStatus.change_interval(seconds = secondes)
	embed = discord.Embed(title = " **Intervalle du status**")

	await ctx.send("L'intervalle a bien été changé")

#Messages 

@bot.command()
@commands.has_permissions(manage_roles = True)
async def regles(ctx):
	embed = discord.Embed(title = "📘 __**Règlement du serveur**__", description = "I. __Informations Personnelles__ \n\n Il est formellement interdit de divulger les informations personnelles de quiconque dans le serveur. Les prénoms, noms, adresse, numéro de téléphone, ainsi que la divulgation des membres familiaux et d'images personnelles sont interdits. \n\n II. __Discrimination__ \n\n Il est formellement interdit de discriminer une personne sur sa religion, son sexe et sa couleur de peau. \n\n III. __Contenu NSFW__ \n\n Le contenu NSFW est formellement interdit sur l'ensemble du serveur. Cela comprend le contenu à caractère pornographique et gore. \n\n IV. __Insultes et Menaces__ \n\n Les insultes sont autorisés à condition que celles-ci ne prennent pas des proportions trop grosses. Les menaces de quelconque natures sont interdites. \n\n V. __Soundboard__ \n\n Il est formellement interdit de soundboard en masse. Vous pouvez soundboard, mais ceci doit garder des proportions normales. \n\n VI. __TOS de discord__ \n\n Vous êtes dans l'obligation de respecter les TOS de discord : https://discord.com/terms", color = 0x12E67)
	await ctx.message.delete()
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_roles = True)
async def deban(ctx):
	embed = discord.Embed(title = "✏️ __**Formulaire de débannissement**__", description = "Pour être débanni du serveur :\n ➜ https://forms.gle/2xWLAFCBh7PscQSw5\n :warning: Tout **troll** sera **supprimé** :warning:", color = 0x12E67)
	embed.set_footer(text = "Les demandes sont étudiées dans les plus brefs délais")
	await ctx.message.delete()
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_roles = True)
async def candid(ctx):
	embed = discord.Embed(title = "📄 __**Candidature**__", description = ":man_technologist: Vous voulez devenir modérateur sur notre serveur ?\n ➜ https://forms.gle/JkXJ3wQ4C8k4AQAF6\n :warning: Tout **troll** sera **supprimé** :warning:", color = 0x12E67)
	embed.set_footer(text = "Les candidatures sont étudiées dans les plus brefs délais")
	await ctx.message.delete()	
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_roles = True)
async def candidopen(ctx):
	embed = discord.Embed(title = "🟢 __**Status des candidatures**__", description = "Les candidatures sont **ouvertes**, vous pouvez déposer votre candidature", color = 0x08000)
	embed.set_footer(text = "Les candidatures sont étudiées dans les plus brefs délais")
	await ctx.message.delete()
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_roles = True)
async def candidclose(ctx):
	embed = discord.Embed(title = "🔴 __**Status des candidatures**__", description = "Les candidatures sont **fermées**, vous pourrez déposer votre candidature lorsque celles-ci réouvriront", color = 0xFF0000)
	embed.set_footer(text = "Munissez vous de patience !")
	await ctx.message.delete()
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_roles = True)
async def work(ctx):
	embed = discord.Embed(title = "🚧 **Salon en cours de création** 🚧", description = "Revenez plus tard", color = 0xFFFFFF)
	await ctx.message.delete()
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_roles = True)
async def ticket(ctx):
	embed = discord.Embed(title = "📃 __**Système de ticket**__", description = "__Vous pouvez créer un ticket si__ :\n\n I. Vous voulez **signaler** un membre\n\n II. Vous voulez nous faire parvenir **quelque chose**\n\n III. Vous voulez nous faire un **don**\n\n IV. Vous voulez avoir un bot **personnalisé**\n\n ⚠️ **Pas de ticket troll ou pour toute autre demande sous peine d'un ban** ⚠️", color = 0x12E67)
	embed.set_footer(text = "Les tickets sont traitées dans les plus brefs délais")
	await ctx.message.delete()
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_roles = True)
async def faq(ctx):
	embed = discord.Embed(title = "📌 __**Foire aux questions**__", description = f"I. __Comment avoir son propre bot discord ?__\n\n Vous pouvez demander à avoir un bot discord en créant un ticket ➜")
	await ctx.message.delete()
	await ctx.send(embed = embed)

@bot.command()
@commands.has_any_role(876409350741164032, 876549851595276318)
async def botperso(ctx):
	embed = discord.Embed(title = "🤖 __**Bot personnalisé**__", description = "I. __Indiquez vos envies dans un message__\n\n Cela peut-être un bot administrateur, fun etc..\nUne fois votre commande validée, nous vous expliquerons comment votre bot sera mis **au point**.\n\n II. __Tarifs__\n\n Les tarifs peuvent variés selon la complexité du bot. Vous devez avoir les **fonds nécessaires** au préalable et vous devez payer la **moitié du prix** au préalable pour éviter toute **arnaque**.\n\n III. __Durée d'attente__\n\n L'attente peut variée selon le **nombre de commande** et la **disponibilité** de nos développeurs.\n\n IV. __Hébergement__\n\n Vous devrez héberger votre bot vous **même**.\n\n ⚠️**Toute arnaque sera puni d'un ban non révoquable**⚠️", color = 0x12E67)
	embed.set_footer(text = "Les demandes de bots sont traitées dans les plus brefs délais")
	await ctx.message.delete()
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_roles = True)
async def bvn(ctx):
	embed = discord.Embed(title = "📘 __**Merci de m'avoir ajouté !**__", description = "Je suis un bot discord développé en Python !\n Je suis en cours de développement et par conséquent mon code n'est pas encore disponible. Je peux être offline vu que je ne suis pas hébergé.\n Pour tout problème ➞ Dr Maboule#4456", color = 0x12E67)
	await ctx.message.delete()
	await ctx.send(embed = embed)

#Others

status = ["+help | Dr Maboule#4456", "Beta 1.1"]

memes = ["https://cdn.discordapp.com/attachments/861324771752935445/880155053632147466/video0.mov", "https://cdn.discordapp.com/attachments/861324771752935445/880155024943104021/video0.mov","https://cdn.discordapp.com/attachments/861324771752935445/877952783221932032/VID_20210221_061317.mp4","https://cdn.discordapp.com/attachments/861324771752935445/877711907631558696/video0-33-2.mp4",
  			"https://cdn.discordapp.com/attachments/861324771752935445/880152679718977599/video0-7-2.mov", "https://cdn.discordapp.com/attachments/861324771752935445/879782103175286834/aK51is9Fd4z-4sVk-1.mp4", "https://cdn.discordapp.com/attachments/606446464062717952/869918832033148928/je-te-propose-30eur-si-tu-suces-mon-biberon-meme-chatelet.mp4",
  			"https://cdn.discordapp.com/attachments/871322514985472020/871325021547687957/cramed.mp4", "https://cdn.discordapp.com/attachments/871322514985472020/871323491830480926/J.mp4", "https://cdn.discordapp.com/attachments/807255777470709811/879529571660218378/7789b96079d7a4e4b9441adf9d337238.mp4", "https://cdn.discordapp.com/attachments/835870618422870057/877406952303513640/video0_97.mov",
  			"https://cdn.discordapp.com/attachments/861324771752935445/878427964872724510/ssstiktok_1629503879.mp4", "https://cdn.discordapp.com/attachments/815902111895650314/877906000781410355/video-1629379363.mp4", "https://cdn.discordapp.com/attachments/861324771752935445/877582956577849364/video0-70.mp4", "https://cdn.discordapp.com/attachments/861324771752935445/878427964872724510/ssstiktok_1629503879.mp4",
  			"https://cdn.discordapp.com/attachments/861324771752935445/881649966685237319/video0.mp4","https://cdn.discordapp.com/attachments/861324771752935445/881204585799229440/video0-27-1.mp4", "https://cdn.discordapp.com/attachments/861324771752935445/881141293600866324/Rat_stare.mp4", "https://cdn.discordapp.com/attachments/861324771752935445/880953176805748796/video0_7-2.mp4",
  			"https://cdn.discordapp.com/attachments/861324771752935445/880944204304502844/video0.mp4", "https://cdn.discordapp.com/attachments/861324771752935445/880585870279860234/video1_1.mov", "https://cdn.discordapp.com/attachments/861324771752935445/880551653579845672/video0.mp4","https://cdn.discordapp.com/attachments/861324771752935445/880556247345156106/stinkysunstep_20210826_9.mp4", 
  			"https://cdn.discordapp.com/attachments/739569670339952660/880406833024610374/trisorun.mp4", "https://cdn.discordapp.com/attachments/715910745614712974/880082587756941322/video1.mp4", "https://cdn.discordapp.com/attachments/861324771752935445/880211045883457586/League_of_Legends_players_going_outside.mp4",
  			"https://cdn.discordapp.com/attachments/861324771752935445/880152679718977599/video0-7-2.mov", "https://cdn.discordapp.com/attachments/861324771752935445/875127332451532840/starfoullah.mp4", "https://cdn.discordapp.com/attachments/834078658083815534/878719915270500392/video0_56.mov", "https://cdn.discordapp.com/attachments/857388315565097000/878616741138272256/Fy9u8XpxRmJTHMB.mp4"
  			"https://cdn.discordapp.com/attachments/737427076872929371/947141749032235028/video0.mp4"]

disquettes = ["Ton père fait des biscottes? Parce que t'es super craquante !", "Ton père c'est un voleur. Il a volé toutes les étoiles du ciel pour les mettre dans tes yeux.","Tu serais pas (a+b)² par hasard ? Parceque t'es remarquable",
				"Ton père est terroriste ? Parce que tu es une vraie bombe !", "Ton père travaille chez Nintendo ? Parce tu as un corps de DS !", "Salut tu serais pas HTTPS ? Parceque sans toi je suis ://"]

blagues = ["Il y a un arabe et un noir dans une voiture, qui conduit ? || La police ! || "]

pileouface = ["Pile", "Face"]

cursed = []

random = []

dog = []

cat = []

#Token			

bot.run('#')

# My code is free to use - Mon code est gratuit à utiliser. Try my bot on add in your server with : https://discord.com/api/oauth2/authorize?client_id=876767268774748180&permissions=8&scope=bot !
