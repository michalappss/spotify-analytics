import os
import json
from datetime import datetime
class Data():
    def __init__(self):
        pass
    def join_data(self, raw_data_path:str):
        join_list=[]
        entries=os.scandir(raw_data_path)
        for entry in entries:
            f=(open(entry, encoding="utf8"))
            lista=json.load(f)
            join_list.extend(lista)
        data_list=[x for x in join_list if x["skipped"] != True]
        return data_list
    

    def filter(self, data_list):
        min_date_obj, max_date_obj = self.find_dates(data_list)

        fil = input('Filter dates? (T/N): ').lower()
        if fil[0] == 'n':
            pass
        else: 
            new_min_date_obj, new_max_date_obj = self.set_dates(min_date_obj, max_date_obj)
                
            for x in data_list:
                x['ts']=datetime.strptime(x['ts'], '%Y-%m-%dT%H:%M:%SZ')
            data_list = [x for x in data_list if x['ts']>=new_min_date_obj and x['ts']<= new_max_date_obj]
        print(f'Great. Your new list has {len(data_list)} entries')
        return data_list

    def set_dates(self, min_date_obj, max_date_obj):
        new_min_date_obj=""
        new_max_date_obj=""
        
        while isinstance(new_min_date_obj, datetime) == False:
            new_min_date = input('Set minimum date in format dd/mm/rrrr: ')
            try:
                new_min_date_obj=datetime.strptime(new_min_date, "%d/%m/%Y")  
            except:
                print("Expected date format is dd/mm/rrrr")     
        
        while isinstance(new_max_date_obj, datetime) == False:
            new_max_date = input('Set maximum date in format dd/mm/rrrr: ') 
            try:
                new_max_date_obj = datetime.strptime(new_max_date, "%d/%m/%Y")
            except:
                print("Expected date format is dd/mm/rrrr")

        if new_min_date_obj<min_date_obj:
            new_min_date_obj=min_date_obj
        if new_max_date_obj>max_date_obj:
            new_max_date_obj=max_date_obj
        return new_min_date_obj,new_max_date_obj

    def find_dates(self, data_list):
        min_date_obj=datetime.strptime(min(data_list, key=lambda x:x['ts'])['ts'], '%Y-%m-%dT%H:%M:%SZ')
        max_date_obj=datetime.strptime(max(data_list, key=lambda x:x['ts'])['ts'], '%Y-%m-%dT%H:%M:%SZ')
        
        print(f"Your list contains {len(data_list)} entries. Dates from {min_date_obj.strftime('%d/%m/%Y')} to {max_date_obj.strftime('%d/%m/%Y')}")
        return min_date_obj,max_date_obj

    def clear_and_save(self, data_list):
        for slownik in data_list:
            del slownik['ts']
            # del slownik["username"]
            # del slownik["platform"]
            # del slownik["conn_country"]
            # del slownik["ip_addr_decrypted"]
            # del slownik["user_agent_decrypted"]
            # del slownik["episode_name"]
            # del slownik["episode_show_name"]
            # del slownik["spotify_episode_uri"]
            # del slownik["shuffle"]
            # del slownik["offline"]
            # del slownik["offline_timestamp"]
            # del slownik["incognito_mode"]
            del slownik["skipped"]
            # del slownik["reason_start"]
            # del slownik["reason_end"]
            # del slownik["ms_played"]
            # del slownik["spotify_track_uri"]
            json.dumps(slownik)
        json.dumps(data_list)
        #write to file 
        with open("data.json", 'w', encoding="utf-8") as file:
            file.write(str(data_list))
        with open("data.json", 'w') as file:
            json.dump(data_list, file)