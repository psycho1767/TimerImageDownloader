from telethon import TelegramClient

api_id = '26510241'
api_hash = '9cdd43c4ab4598c0aac613693cab1574'
chatID = 7018412152
client = TelegramClient('helloworldnewapp', api_id, api_hash)

async def main():
    await client.start()
    async for message in client.iter_messages(chatID, limit=1):
        # if message.photo:
        #     await client.download_media(message.photo, 'downloads/')
        print(message)
    print('ok shod')
with client:
    client.loop.run_until_complete(main())
