# management/commands/import_champions.py

import requests
from django.core.management.base import BaseCommand
from draft.models import Champion, Archetype

class Command(BaseCommand):
    help = 'Import champions data from Riot API'

    def handle(self, *args, **kwargs):
        api_key = 'ton_api_key_riot'
        region = 'euw1'  # Region (ex: EUW)

        url = f'https://{region}.api.riotgames.com/lol/static-data/v3/champions'
        headers = {'X-Riot-Token': api_key}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()

            for champ in data['data'].values():
                # Créer un objet Champion
                champion = Champion.objects.create(
                    name=champ['id'],
                    image_url=f"http://ddragon.leagueoflegends.com/cdn/11.22.1/img/champion/{champ['id']}.png",
                    type='Range' if champ['tags'][0] == 'Marksman' else 'Melee',  # Déterminer le type en fonction des tags
                    ap_ratio=champ['info'].get('AP', 0),
                    ad_ratio=champ['info'].get('AD', 0),
                )

                # Associer des archétypes selon des critères, par exemple : Poke, Front-to-back, etc.
                for archetype_name in champ['tags']:
                    archetype, created = Archetype.objects.get_or_create(name=archetype_name)
                    champion.archetypes.add(archetype)
            
            self.stdout.write(self.style.SUCCESS('Champions imported successfully!'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data from Riot API: {response.status_code}'))
