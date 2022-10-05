import discord
import os
from keep_alive import keep_alive
from chatFilter import notRacist
from reactionroles import addNotificationRole, removeNotificationRole, ruleAcceptation
from messageCommands import messageCommands
from discord.ext import tasks
from youtubeContent import handleHeppeUploads

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
intent.reactions = True

client = discord.Client(intents=intent)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  checkForVideos.start()


@client.event
async def on_message(message):
  if await notRacist(message):
    await messageCommands(message, client)
  

@client.event
async def on_message_edit(before, after):
  await notRacist(after)


@client.event
async def on_raw_reaction_add(payload):
  await addNotificationRole(payload)
  await ruleAcceptation(payload)


@client.event
async def on_raw_reaction_remove(payload):
  await removeNotificationRole(payload, client)


@tasks.loop(seconds=300)
async def checkForVideos():
  await handleHeppeUploads(client)


keep_alive()
try:
  client.run(os.environ['TOKEN'])
except discord.errors.HTTPException:
    print("BLOCKED BY RATE LIMITS\nRESTARTING NOW\n")
    os.system('kill 1')