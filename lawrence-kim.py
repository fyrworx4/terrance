import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('OTQ4ODQwNDkyMzE2MTE5MTEw.YiBqkQ.UWTvbNsbdYfI_JPm8l1aBBokKSU')