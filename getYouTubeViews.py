import requests
import json 
import pandas  

key = "AIzaSyClKxFwU3KhKD4cI1C-rqe1x4bzA7Wy0Lk"
vidstring="uhBHL3v4d3I,JFAcOnhcpGA,QlF4rhAbwyc,4tdKl-gTpZg,yqIQvE5R1tU,WbxH5S9_A3M,ZChXK2rdr9M,tUVr2xnGIEo,FpF8Wa2yQH0,IkVG-qXRgfo,2Mkq6GFLIsk,m46Z0-HXySo,zaZswCtNmEg"
url = "https://www.googleapis.com/youtube/v3/videos?id=" + vidlist + "&key=" + key + "&part=snippet,contentDetails,statistics"
content = json.loads(requests.get(url).text)

def get_youtoube_content(content):
    id = []
    description = []
    title = []
    time =[]
    for i in content["items"]:
        a=i["id"]
        b=i["snippet"]
        id.append(i["id"])
        description.append(b["description"])
        title.append(b["title"])
        time.append(b["publishedAt"])
    data = pandas.DataFrame({"id":id, "description":description, "title":title, "time":time })
    return(data)

data=get_youtoube_content(content)
stat_url="https://www.googleapis.com/youtube/v3/videos?part=statistics&key="+key+"&maxResults=50&id="+str(list(data["id"])).replace("[","").replace("]","").replace("'","")
stat_content = json.loads(requests.get(stat_url).text)

def get_youtoube_content_stat(content):
    id = []
    commentCount=[]
    dislikeCount = []
    favoriteCount = []
    likeCount=[]
    viewCount=[]
    for i in content["items"]:
        id.append(i["id"])
        b=i["statistics"]
        commentCount.append(b["commentCount"])
        dislikeCount.append(b["dislikeCount"])
        favoriteCount.append(b["favoriteCount"])
        likeCount.append(b["likeCount"])
        viewCount.append(b["viewCount"])
    data = pandas.DataFrame({"id":id, "commentCount":commentCount,"dislikeCount":dislikeCount ,"favoriteCount":favoriteCount,"likeCount":likeCount, "viewCount":viewCount })
    return(data)

data_stat=get_youtoube_content_stat(stat_content)

data=pandas.merge(data, data_stat,"inner", on="id" )

print(data)