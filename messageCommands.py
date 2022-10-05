async def messageCommands(message, client):
  if message.author == client.user:
    return
  msg = message.content.lower()
  if (msg.startswith('subscribe to heppe')):
    await message.channel.send('Subscribe to Heppe')
  if msg.startswith('.links'):
    await message.channel.send('Youtube: https://www.youtube.com/c/HeppeGaming')
  if msg.startswith('.call saul'):
    await message.channel.send('Hi, I’m Saul Goodman. Did you know that you have rights? The Constitution says you do. And so do I. I believe that until proven guilty, every man, woman, and child in this country is innocent. And that’s why I fight for you, Albuquerque! Better call Saul!')
  if 'bot' in msg:
    await message.channel.send('https://tenor.com/view/my-reaction-to-that-information-saul-goodman-saul-goodman3d-better-call-saul-breaking-bad-gif-25801565')
  #if msg.startswith('speak'):
  #  await message.channel.send('If you want to get notified, when Heppe uploads, react to this message with: \n 🇻 for videos, \n 🇸 for shorts \n 🇱 for livestreams')
  #if msg.startswith('ok'):
  #  await message.channel.send('me watching everyone suddenly get racist for no reason https://tenor.com/view/3d-saul-saul-goodman-adamghik-gif-23876766')
  #if msg.startswith('cope'):
  #  await message.channel.send('https://tenor.com/view/cope-cope-harder-saul-goodman3d-better-call-saul-saul-goodman-gif-24033192')