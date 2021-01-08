from qbittorrent import Client
import re

qb = Client ("@ de redirection du client") #à modifier  
qb.login("username", "password") #à modifier

txt = "torrentName.torrent" #à modifier
torrent_file =open(txt, "rb")

qb.download_from_file(torrent_file)

x = txt.split(".torrent")
torrents = qb.torrents()

for torrent in torrents:
    if(torrent["name"]==x[0]):
        torrent_hash = torrent["hash"]

x.clear()

r=qb.get_torrent_files(torrent_hash)    

nb_file=0
print(type(r))
for i in r:
    x.append(i["name"])
    nb_file+=1

x.sort()
r.clear()
 
qb.resume(torrent_hash)
j=0

while(j<nb_file):
    r=qb.get_torrent_files(torrent_hash)   
    i=0
    finish = False
    for t in x:
        if(t==r[i]["name"] and r[i]["progress"]<1):
            print("i : "+str(i))
            qb.set_file_priority(torrent_hash,i,7)
            
            while (finish==False):
                r=qb.get_torrent_files(torrent_hash) 
                print(str(r[i]["name"])+" : "+str(int(r[i]["progress"]*100))+"%",end="\r", flush=True)
                
                if(r[i]["progress"]>=1):
                    finish=True
                    
            if(finish==True):
                j+=1
                break
        else:
            qb.set_file_priority(torrent_hash,i,1)
            i+=1
print("Torrent complete")