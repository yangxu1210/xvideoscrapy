import urllib2
import urllib
import datetime
import re
import os.path

big_path="/Users/yinpengcheng/Desktop/"

def save_file(this_download_url,path = big_path+str(datetime.datetime.now())[:-7]+".mp4"):
    print"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    time1=datetime.datetime.now()
    print str(time1)[:-7],
    if (os.path.isfile(path)):
        file_size=os.path.getsize(path)/1024/1024
        print "File "+path+" ("+ str(file_size)+"Mb) already exists."
        return
    else:
        print "Downloading "+path+"..."
        f = urllib2.urlopen(this_download_url)
        data = f.read()
        with open(path, "wb") as code:
            print "loading"
            code.write(data)
        time2=datetime.datetime.now()
        print str(time2)[:-7],
        print path+" Done."
        use_time=time2-time1
        print "Time used: "+str(use_time)[:-7]+", ",
        file_size=os.path.getsize(path)/1024/1024
        print "File size: "+str(file_size)+" MB, Speed: "+str(file_size/(use_time.total_seconds()))[:4]+"MB/s"

def download_the_av(url):
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()
    while len(content)<100:
        print"try again..."
        content = urllib2.urlopen(req).read()
    print "All length:" +str(len(content))
    titleRe = "setVideoTitle\(\'(.+?)\'\);"
    lowUrlRe = "setVideoUrlLow\(\'(.+?)\'\);"
    patternTitle = re.compile(titleRe)
    patternLowUrl = re.compile(lowUrlRe)
    to_find = content
    matchTitle = patternTitle.search(to_find)
    matchLowUrl = patternLowUrl.search(to_find)
    if matchTitle:
        title = matchTitle.group(1)+".mp4"
        print title

    if matchLowUrl:
        lowUrl = matchLowUrl.group(1)
        print lowUrl
    if len(lowUrl)>0:
        save_file(lowUrl)



urls = ['https://www.xvideos.com/video30678391/star_a.j._creampie_compilation']

for url in urls:
    download_the_av(url)