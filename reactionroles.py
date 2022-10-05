import discord

async def addNotificationRole(payload):
  ourMessageID = 1023205195343204413
  if ourMessageID == payload.message_id:
    member = payload.member
    guild = member.guild
    emoji = payload.emoji.name
    if(emoji == '🇱'):
      role = discord.utils.get(guild.roles, name="Live Enjoyer")
      await member.add_roles(role)
    if(emoji == '🇸'):
      role = discord.utils.get(guild.roles, name="Shorts Enjoyer")
      await member.add_roles(role)
    if(emoji == '🇻'):
      role = discord.utils.get(guild.roles, name="Video Enjoyer")
      await member.add_roles(role)

async def removeNotificationRole(payload, client):
  ourMessageID = 1023205195343204413
  if ourMessageID == payload.message_id:
    guild = await(client.fetch_guild(payload.guild_id))
    member = await(guild.fetch_member(payload.user_id))
    emoji = payload.emoji.name
    if(emoji == '🇱'):
      role = discord.utils.get(guild.roles, name="Live Enjoyer")
      await member.remove_roles(role)
    if(emoji == '🇸'):
      role = discord.utils.get(guild.roles, name="Shorts Enjoyer")
      await member.remove_roles(role)
    if(emoji == '🇻'):
      role = discord.utils.get(guild.roles, name="Video Enjoyer")
      await member.remove_roles(role)

async def ruleAcceptation(payload):
  ourMessageID = 1023863591801208872
  if ourMessageID == payload.message_id:
    member = payload.member
    guild = member.guild
    emoji = payload.emoji.name
    if(emoji == '✅'):
      role = discord.utils.get(guild.roles, name="Intellectual")
      await member.add_roles(role)