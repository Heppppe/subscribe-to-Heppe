async def notRacist(message):
  """
  bannedWords = ["nigg", "n!gg", "n1gg", "ni🇬"]
  msg = message.content
  for word in bannedWords:
    if word in msg.lower():
      await message.delete()
      await message.channel.send("That's what the kids call EPIC FAIL " + message.author.mention)
      return 0
  """
  msg = message.content.lower()
  string = 'n'
  for i in range(len(msg)):
    if msg[i] == 'n':
      shorter = 12
      if len(msg)-i < shorter:
        shorter = len(msg)-i
      for j in range(shorter):
        if msg[i+j] == 'i' or msg[i+j] == '!' or msg[i+j] == '1' or msg[i+j]=='j':
          string+='i'
        if msg[i+j] == 'g' or msg[i+j] == '🇬':
          string+='g'
      if 'nigg' in string:
        await message.delete()
        await message.channel.send("That's what the kids call EPIC FAIL " + message.author.mention)
        return 0
    string = 'n'
  return 1