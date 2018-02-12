#!/usr/bin/python3
import discord
client = discord.Client();
chan_map = {}
try:
	with open("o7.dat", "r") as f:
		chan_map = eval(f.read())
except:
	chan_map = {}
@client.event
async def on_member_join(M):
	await client.send_message(M.server.get_channel(chan_map[M.server.id]), M.mention + "  o7")
@client.event
async def on_message(M):
	if(M.content == "/o7"):
		if(M.author.server_permissions.administrator == True or M.author.id == "247841704386756619"):
			chan_map[M.server.id] = M.channel.id
			await client.send_message(M.channel, "Done.")
			with open("o7.dat", "w") as f:
				print(chan_map, file=f)
client.run("token")
