import asyncio
import aiohttp
import json


class Session:
    @staticmethod
    async def _start_session(query_type, name_or_id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://pokeapi.co/api/v2/{query_type}/{name_or_id}/") as response:
                # print("status", response.status)
                # print("content-type", response.headers['content-type'])

                json_data = await response.text()
                # print("Body:", json_data[:50], "...")
                json_data = json.loads(json_data)
                # print(json_data['effect_changes'][0]['effect_entries'][1]['effect'])
                # print(json_data)
                return json_data

    @staticmethod
    def query_info(query_type, name_or_id):
        loop = asyncio.get_event_loop()
        json_data = loop.run_until_complete(Session()._start_session(query_type, name_or_id))
        return json_data

    @staticmethod
    async def query_url(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                json_data = await response.text()
                json_data = json.loads(json_data)
                return json_data
