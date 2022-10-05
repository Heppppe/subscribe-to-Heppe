import json
import re
import aiohttp

async def handleHeppeUploads(client):
  discord_channel = client.get_channel(1023337024318603305)
  livestream_playlist = "https://www.youtube.com/playlist?list=PL81lWxumu43VY1duQ9c7CJrp2rm3WFIp0"
  sharts_playlist = "https://www.youtube.com/playlist?list=PL81lWxumu43X19SdMcHyWr4Ss20KOnTS8"
  video_url_prefix = "https://www.youtube.com/watch?v="
  
  with open("youtubeData.json", "r") as f:
    data=json.load(f)
  async with aiohttp.ClientSession() as session:
    async with session.get("https://www.youtube.com/c/HeppeGaming/videos") as resp:  
      html= await resp.text()
  try:
    latest_url = video_url_prefix + re.search('(?<="videoId":").*?(?=")', html).group()
  except:
    return
  if str(data["youtube_info"]["latest_video_url"]) != latest_url: #did I upload a new video?
    
    async with aiohttp.ClientSession() as session:
      async with session.get(sharts_playlist) as resp:
        html= await resp.text()
    try:
      latest_short_url = video_url_prefix + re.search('(?<="videoId":").*?(?=")', html).group()
    except:
      return
    if str(latest_url) == latest_short_url: # anything new in sharts playlist?
      msg = f"Heppe just made a New Short: {latest_short_url}"
      await discord_channel.send(msg)

    else:
      async with aiohttp.ClientSession() as session:
        async with session.get(livestream_playlist) as resp:
          html= await resp.text()
      try:
        latest_live_url = video_url_prefix + re.search('(?<="videoId":").*?(?=")', html).group()
      except:
        return
      
      if str(latest_url) == latest_live_url: # anything new in livestream playlist?
        msg = f"live started: {latest_short_url}"
        await discord_channel.send(msg)
        1==1

      else:  # So it has to be a video
        discord_channel = client.get_channel(1023337024318603305)
        msg = f"Heppe just made a video: {latest_url}"
        await discord_channel.send(msg)
  
    data[str("youtube_info")]["latest_video_url"] = latest_url
    with open("youtubeData.json", "w") as f:
      json.dump(data, f)