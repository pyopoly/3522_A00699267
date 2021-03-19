import asyncio
import aiohttp
import json


class Session:
    async def start(self):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://pokeapi.co/api/v2/ability/magic-guard/") as response:

                print("status", response.status)
                print("content-type", response.headers['content-type'])

                json_data = await response.text()
                print("Body:", json_data[:50], "...")
                y = json.loads(json_data)
                # print(y)
                print(y['effect_changes'][0]['effect_entries'][1]['effect'])


loop = asyncio.get_event_loop()
loop.run_until_complete(Session().start())
