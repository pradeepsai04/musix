from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import upload


import os
from django.conf import settings
from moviepy.editor import VideoFileClip

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import UploadVideo

import moviepy.video.fx.all as vfx
from moviepy.editor import  *

"""
from .forms import faderange2
from .forms import speedfactor
from .forms import volumefactor
from .forms import rotateangle
from .forms import gammavalue
from .forms import faderange

"""

#parsing a url
from urllib.parse import urlparse



# Create your views here.
def handle_uploaded_file(f):
 print("filename f#####",f)
 print("type of file is %%%%",type(f))
 global vname
 vname = f.name
 print("@@@@@",vname)
 
 print("$$$$$$$",vname)

 with open(os.path.join(settings.MEDIA_ROOT,f.name),'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)


"""
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        handle_uploaded_file(uploaded_file)
        return HttpResponse('File uploaded successfully!')
    return render(request, 'upload.html')

"""

# using simple form
   
def edit_video(request,*args):
 if request.method=="POST":
  form = UploadVideo(request.POST,request.FILES)
  if form.is_valid():
  
   handle_uploaded_file(request.FILES['video']) 
   print("all are done successfully")
   return HttpResponseRedirect('/homepage/',{'form':form})
  # args ={'form':form,'vname':vname}
  # return render(request,'coralpage.html',args)
   
 else:
  form = UploadVideo()
  try:
     print(vname,"########")
     args ={'form':form,'vname':vname}
  except: args = {'form':form};print("commited a error")
 return render(request,'coralpage.html',args)

 

##########################################################################################################

# using model form
"""
def edit(request):
 if request.method=="POST":
      form= UploadVideo(data=request.POST,files=request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse("<h1>hello everyone</h1>")
 else:
   form=UploadVideo()
   obj=upload.objects.all()
   args={"form":form,"obj":obj}   


   return render(request,'coralpage.html',args)

def show(request):
  obj=upload.objects.all()
  args={"obj":obj}
  return render(request,'start.html',args)


"""
######################################################################

def black(request):
 global vname
 
 
 file_path = os.path.join(settings.MEDIA_ROOT, vname)
 myclip = VideoFileClip(file_path)
 mynewclip = myclip.fx(vfx.blackwhite,RGB=None, preserve_luminosity=True)
 vname="1%s"%(vname)
 
 file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
 mynewclip.write_videofile(file_path1)
 print("it is helpfull")
 return HttpResponseRedirect('/homepage/')
 ########################################################################
def paint(request):
 global vname
 
 
 file_path = os.path.join(settings.MEDIA_ROOT, vname)
 myclip = VideoFileClip(file_path)
 mynewclip = myclip.fx(vfx.painting,saturation=1.5,black=0.009)
 vname="1%s"%(vname)
 file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
 mynewclip.write_videofile(file_path1)

 return HttpResponseRedirect('/homepage/')
##################################################################

def mirrorx(request):
 global vname
 
 file_path = os.path.join(settings.MEDIA_ROOT, vname)
 myclip = VideoFileClip(file_path)
 mynewclip = myclip.fx(vfx.mirror_x,apply_to="mask")
 vname="1%s"%(vname)
 file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
 mynewclip.write_videofile(file_path1)
 
 return HttpResponseRedirect('/homepage/')

 ###########################################################################
def mirrory(request):
 global vname
 
 file_path = os.path.join(settings.MEDIA_ROOT, vname)
 myclip = VideoFileClip(file_path)
 mynewclip = myclip.fx(vfx.mirror_y,apply_to="mask")
 vname="1%s"%(vname)
 file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
 mynewclip.write_videofile(file_path1)
 return HttpResponseRedirect('/homepage/')

###############################################################################
 
 
#################################################################################
 
def invertcolors(request):
 global vname
 
 file_path = os.path.join(settings.MEDIA_ROOT, vname)
 myclip = VideoFileClip(file_path)

 mynewclip = myclip.fx(vfx.invert_colors)
 vname="1%s"%(vname)
 
 file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
 mynewclip.write_videofile(file_path1)
 
 return HttpResponseRedirect('/homepage/') 


########################################################################################

 
def lumcontrast(request):
 global vname
 
 file_path = os.path.join(settings.MEDIA_ROOT, vname)
 myclip = VideoFileClip(file_path)

 mynewclip = myclip.fx(vfx.lum_contrast,lum=0,contrast=0,contrast_thr=127)
 vname="1%s"%(vname) 
 file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
 mynewclip.write_videofile(file_path1)

 return HttpResponseRedirect('/homepage/')

############################################################################################
  
def evensize(request):
 global vname


 
 file_path = os.path.join(settings.MEDIA_ROOT, vname)
 myclip = VideoFileClip(file_path)

 
 mynewclip = myclip.fx(vfx.even_size)
 vname="1%s"%(vname)
 file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
 mynewclip.write_videofile(file_path1)
 return HttpResponseRedirect('/homepage/')
 #######################################################################
def timemirror(request):
 global vname
 
 file_path = os.path.join(settings.MEDIA_ROOT, vname)
 myclip = VideoFileClip(file_path)


 mynewclip = myclip.fx(vfx.time_mirror,self)
 vname="1%s"%(vname)
 file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
 mynewclip.write_videofile(file_path1)
 return HttpResponseRedirect('/homepage/')
  



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from .forms import uploadAudio
from moviepy.editor import CompositeAudioClip

def trim_edit(request):
      global vname
      if request.method=='POST':
       form=uploadAudio(request.POST,request.FILES)
       if form.is_valid():
         global vname
         audio=form.cleaned_data['audio']
         with open(os.path.join(settings.MEDIA_ROOT,audio.name),'wb+') as destination:
          for chunk in audio.chunks():
           destination.write(chunk)
         

         audio_file_path=os.path.join(settings.MEDIA_ROOT,audio.name)
         audioclip=AudioFileClip(audio_file_path)
        
         video_file_path = os.path.join(settings.MEDIA_ROOT, vname)
         myclip = VideoFileClip(video_file_path).subclip(form.cleaned_data['start'],form.cleaned_data['end']).without_audio()
         


         duration=myclip.duration
         temp_audio=audioclip.set_duration(duration)
         final_audio=CompositeAudioClip([temp_audio])
         final_video=myclip.set_audio(final_audio)
         vname="1%s"%(vname)
         file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
         final_video.write_videofile(file_path1)
         return HttpResponseRedirect('/homepage/')
      else:
       form=uploadAudio()
       return render(request,'start.html',{'form':form}) 


"""

from .forms import *          
def addwatermark(request):
  global vname
  if request.method=="POST":
    form=uploadAudio(request.POST,request.FILES)
    if form.is_valid():
         global vname
         text=form.cleaned_data['text']

         file_path = os.path.join(settings.MEDIA_ROOT, vname)
         myclip = VideoFileClip(file_path)

         txt_clip=TextClip(text,fontsize=50,color="Black")
         txt_clip=txt_clip.set_position('center').set_duration(10)
         
         video=CompositeVideoClip([myclip,txt_clip])
         vname="1%s"%(vname)
         file_path1 = os.path.join(settings.MEDIA_ROOT, vname)
         video.write_videofile(file_path1)

         return HttpResponseRedirect('/homepage/')


  else:
   form=watermark()
   return render(request,'start.html',{"form":form})
  
  
"""



import base64
import requests

# Set your Spotify API credentials
SPOTIFY_CLIENT_ID = "51901700aff74af18d2a63ea34a15ef4"
SPOTIFY_CLIENT_SECRET ="473bb5cfc4c947489475be6cacaabe01"

# Spotify Accounts service URL to get the access token
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

def get_spotify_access_token():
    # Base64 encode the client_id and client_secret
    auth_str = f'{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}'
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    # Set the headers and payload for the POST request
    headers = {
        'Authorization': f'Basic {b64_auth_str}',
    }
    data = {
        'grant_type': 'client_credentials',
    }

    # Make the POST request to get the access token
    response = requests.post(SPOTIFY_TOKEN_URL, headers=headers, data=data)

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        return access_token
    else:
        print(f"Error: {response.status_code}")
        return None

# Get the access token
#access_token = get_spotify_access_token()
#print("Access token:", access_token)

########################################################################################################



######################################################################
preview_url=[]
def fetch_song_preview_url(album_id, access_token):
    spotify_api_url = f'https://api.spotify.com/v1/albums/{album_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(spotify_api_url, headers=headers)
    #print("song response",response)
    #print(response)
    if response.status_code == 200:
        data = response.json()
        #print("the data",data)
        total_tracks=len(data['tracks']['items'])
        print("total lenght",total_tracks)
        preview_url=[]
        
        for i in range(total_tracks):
            print("%%%%%% SUCCESS")


            url = data['tracks']['items'][i]['preview_url']
            preview_url.append(url)
            print(len(preview_url))
            if len(preview_url)==total_tracks:
                print("total urls",preview_url)
                return preview_url
    else:
        return None
    





def show(request):
  if request.method=="GET":
  
     
    album_id = '4aawyAB9vmqN3uQ7FjRGTy'   
    result=fetch_song_preview_url(album_id,access_token=get_spotify_access_token())  
  
    return render(request,'spotify.html',{"result":result})

#####################################################

#@@@@@@@@@@@@@@@@@@@
import requests

SPOTIFY_API_URL = 'https://api.spotify.com/v1/search'

def search_spotify(query, search_type='track', artist=None, album=None, access_token=None):
    if not access_token:
        raise ValueError("Access token is required for Spotify API authentication.")
    
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    params = {
        'q': query,
        'type': search_type,
    }

    if artist:
        params['q'] += f' artist:{artist}'
    
    if album:
        params['q'] += f' album:{album}'

    response = requests.get(SPOTIFY_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('tracks', {}).get('items', [])
    else:
        print(f"Error: {response.status_code}")
        return None

#@@@@@@@@@@@@@@@
tracks_url = 'https://api.spotify.com/v1/tracks'

def fetch_multiple_tracks(track_ids):
    access_token = get_spotify_access_token()

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    params = {
        'ids': ','.join(track_ids),  # Convert the list of track IDs to a comma-separated string
    }

    response = requests.get(tracks_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['tracks']
    else:
        print(f"Error: {response.status_code}")
        return None
    
















#@@@@@@@@@@@@@@@@
def sid(request):
  if request.method=="GET":
    access_token = get_spotify_access_token()
    search_query = 'Sid Sriram'  # Replace with your desired search query

    # Search for tracks by the artist 'Imagine Dragons'
    results_artist = search_spotify(search_query, search_type='track', artist='Sid Sriram', access_token=access_token)


    # Search for tracks from the album 'Night Visions' by 'Imagine Dragons'
    results_album = search_spotify(search_query, search_type='track', album='Night Visions', access_token=access_token)
    artist_tracks_ids=[]
    
    for i in results_artist:
        artist_tracks_ids.append(i['id'])
        print(i['id'])
    
    tracks_data = fetch_multiple_tracks(artist_tracks_ids)
    final_tracks=[]
    for i in range(len(artist_tracks_ids)):
        print("track preview_url",tracks_data[i]['preview_url'])
        final_tracks.append(tracks_data[i]['preview_url'])
    print("len",len(final_tracks))    
    for i in range(len(artist_tracks_ids)):
           print("tracks_ popularity",tracks_data[i]['popularity'])

    result=final_tracks
    
    return render(request,'spotify.html',{'result':result})

from .forms import uform
from  .models import data

def form(request):
   if request.method=='POST':
      form=uform(data=request.POST,files=request.FILES)
      if form.is_valid(): 
          name=form.cleaned_data['name']
          age=form.cleaned_data['age']
          data1=data.objects.create(name=name,age=age)
          data1.save()
           

          return render(request,'spotify.html',{"form":uform})
         
      
   return render(request,'spotify.html',{"form":uform})






