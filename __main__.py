update_title = """
Update v2.2.5 Cat.bot 
2023-11-24 11:29 v2.2:
+ fix lỗi bot chào mừng bot join
2023-11-24 1:57 v2.2.5:
+ áp dụng hàm global cho better code
2023-11-25 7:53 v2.3:
+ thêm chat gpt khi mention bot thì bot sẽ reply trả lời bằng gpt
"""
"""
all code made by ÂnNguyễn2008
p/s: 200 lines dài thật sự, đương nhiên là luôn phải mò chức năng mới mà!
"""
#------------------------------------------------------------------------
import requests
import urllib.parse
import discord
import json
from discord.ext import commands
from discord import app_commands
import datetime
from datetime import *
import random
import psutil
from keep_alive import keep_alive
import os
import openai
import requests
#------------------------------------------------------------------------
with open('config.json') as f:
  config = json.load(f)
#------------------------------------------------------------------------
bot = commands.Bot(command_prefix=config["command_prefix"], intents=discord.Intents.all())
openai.api_key = config["openai_token"]
#------------------------------------------------------------------------
class color():
  green = '\033[92m'
  pink = '\033[95m'
  red = '\33[91m'
  yellow = '\33[93m'
  blue = '\33[94m'
  gray = '\33[90m'
  reset = '\33[0m'
  bold = '\33[1m'
  italic = '\33[3m'
  unline = '\33[4m'
#------------------------------------------------------------------------
channel_rule = bot.get_channel()
channel_welcome = bot.get_channel()
channel_out = bot.get_channel()
dev_id = 
#------------------------------------------------------------------------
def get_ram_usage():
  ram = psutil.virtual_memory()
  ram_total = round(ram.total / (1024**3), 2)
  ram_used = round(ram.used / (1024**3), 2)
  ram_percent = ram.percent
  return f'Memory ``{ram_total}GB / {ram_used}GB | {ram_percent}%``'

#------------------------------------------------------------------------
def get_storage_usage():
  storage = psutil.disk_usage('.')
  storage_total = round(storage.total / (1024**3), 2)
  storage_used = round(storage.used / (1024**3), 2)
  storage_percent = storage.percent
  return f'Storage ``{storage_total}GB / {storage_used}GB | {storage_percent}%``'

#------------------------------------------------------------------------
@bot.event
async def on_ready():
  print(f'{color.gray+ color.bold}{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {color.blue}CONSOLE{color.reset}  {color.pink}discord.on_ready{color.reset} Đã đăng nhập bot {color.bold}{bot.user}{color.reset}')
  try:
      sync = await bot.tree.sync()
      print(f'{color.gray+ color.bold}{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {color.blue}CONSOLE{color.reset}  {color.pink}discord.command{color.reset} {len(sync)} commands')
  except Exception as e:
      print(e)
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name='Đen\'s playlist'))

#------------------------------------------------------------------------
@bot.event
async def on_member_join(member):
  if not member.bot:
    global channel_welcome, channel_rule
    embed = discord.Embed(
        title=f"Chào mừng {member.name}",
        description=f"{member.mention} bạn là member thứ #{member.guild.member_count}! nhớ đọc rule ở kênh {channel_rule.mention}.",
        color=0x97ffde)
    embed.add_field(name="Vào lúc",
                    value=member.joined_at.strftime("%d/%m/%Y %H:%M"),
                    inline=False)
    embed.set_thumbnail(url=member.avatar)
    await channel_welcome.send(embed=embed)

#------------------------------------------------------------------------
@bot.event
async def on_member_remove(member):
  if member.bot:
    global channel_out
    await channel_out.send(f'**{member.name}** đã rời server...')
#------------------------------------------------------------------------
@bot.event
async def on_member_ban(guild, member):
  global channel_out
  await channel_out.send(f'**{member.name}** đã bị ăn bonk khỏi **{guild.name}**!')
#------------------------------------------------------------------------
@bot.tree.command(name="ping", description="kiểm tra trạng thái kết nối bên host")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(f"📡Ping {round(bot.latency*1000)}ms", delete_after=30
                                          )

#------------------------------------------------------------------------
@bot.tree.command(name="cat", description="tìm ảnh mèo")
async  def cat(interaction:discord.Interaction):
  embed = discord.Embed(color= discord.Color.random())
  response = requests.get('https://api.thecatapi.com/v1/images/search')
  embed.set_image(url = response.json()[0]['url'])
  await interaction.response.send_message(embed=embed)
#------------------------------------------------------------------------
@bot.tree.command(name="help", description="xem hướng dẫn sử dụng")
async def ping(interaction: discord.Interaction):
  embed = discord.Embed(
      title=f"Hướng dẫn dùng lệnh",
      color=0x00FFFF)
  embed.add_field(name="```/ping```",
                  value="Kiểm tra trạng thái mạng bên bot host.", inline=False)
  embed.add_field(name="```/help <member>```",
                  value="Thông tin của member.", inline=False)
  embed.add_field(name="```/info_bot```",
                  value="thông tin của bot.", inline=False)
  embed.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/1092067471638397020/1123878937475432538/d78619e3249e33e58ff16d6f52de9848.jpg"
  )
  await interaction.response.send_message(embed=embed, delete_after=60)

#------------------------------------------------------------------------
@bot.tree.command(name="info_bot", description="Thông tin bot")
async def ping(interaction: discord.Interaction):
  embed = discord.Embed(
      title="Thông tin bot",
      description="Nếu bot có bug thì hãy liên hệ ``annguyen2k8#0`` !\n\👇Look me hoạt động in...\nhttps://replit.com/@Bao-AnAn14/hostbot247?v=1",
      color=0x00ffff
  )
  embed.add_field(name='HostCloud replit',
                  value=f'{get_ram_usage()}\n{get_storage_usage()}\nPing ``{round(bot.latency*1000)}ms``')
  embed.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/1102415304312758322/1115966756066971749/Untitled.png"
  )
  await interaction.response.send_message(embed=embed, delete_after=30)

#------------------------------------------------------------------------
@bot.tree.command(name="say", description="!say LMAO")
async def say_message(interaction: discord.Interaction, say: str):
  global dev_id
  if interaction.user.id == dev_id:
    channel = bot.get_channel(interaction.channel.id)
    await interaction.response.send_message('đã nhắn tin nhắn!', ephemeral=True, delete_after=3)
    await channel.send(say)
  else:
    await interaction.response.send_message('xin lỗi, bạn không có **quyền sử dụng lệnh**!', ephemeral=True, delete_after=3)
#------------------------------------------------------------------------
@bot.tree.command(name="update", description="update!")
async def update(interaction: discord.Interaction):
  global update_title,dev_id
  if interaction.user.id == dev_id:
    channel = bot.get_channel(interaction.channel.id)
    await interaction.response.send_message('Pong!', ephemeral=True, delete_after=3)
    await channel.send(content = ('```'+update_title+'```'))
  else:
    await interaction.response.send_message('xin lỗi, bạn không có **quyền sử dụng lệnh**!', ephemeral=True, delete_after=3)
#------------------------------------------------------------------------
@bot.tree.command(name="avatar", description="xem avatar của mọi người")
async def get_avatar(interaction: discord.Interaction, member:discord.Member):
  embed = discord.Embed(title=f"{member.name}'s avatar", url= member.avatar, color=0x00FFFF)
  embed.set_image(url = member.avatar)
  await interaction.response.send_message(embed = embed, ephemeral=True, delete_after = 60)
#------------------------------------------------------------------------
@bot.tree.command(name="info", description="xem thông tin người dùng bằng cách gõ /info <@username>")
async def info(interaction: discord.Interaction, member: discord.Member):
  roles = ''
  for role in member.roles:
      if role.name != '@everyone':
          roles += f'{role.mention}'
  if member.nick != None:
      embed = discord.Embed(title=f"{member.nick}\'s info",
                            description=f"id: {member.id}", color=0x00FFFF)
      embed.add_field(name='Nickname',
                      value=member.nick, inline=False)
  else:
      embed = discord.Embed(title=f"{member.name}\'s info",
                            description=f"id: {member.id}", color=0x00FFFF)
  embed.add_field(name='Username',
                  value=member, inline=False)
  embed.add_field(name="Created at",
                  value=member.created_at.strftime('%d/%m/%Y %H:%M'), inline=True)
  embed.add_field(name="Joined at",
                  value=member.joined_at.strftime('%d/%m/%Y %H:%M'), inline=True)
  embed.add_field(name="Roles",
                  value=roles, inline=False)
  embed.set_thumbnail(url=member.avatar)
  await interaction.response.send_message(embed=embed, delete_after=30)
#------------------------------------------------------------------------
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        message_reply = await message.channel.send('Bot đang suy nghĩ...')
        msg = openai.Completion.create(model = 'text-davinci-003', prompt = str(message.content), max_tokens = 3000, temperature=0.7)["choices"][0]["text"]
        await message_reply.edit(content = msg)
#------------------------------------------------------------------------
#ở đây nếu host bot ở máy tính thì xóa cái dòng này, vì dòng này là để khi host trên replit.com thì nó sẽ giữ code luôn chạy
keep_alive()
#------------------------------------------------------------------------
bot.run(config["token_bot"])
