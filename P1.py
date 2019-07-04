urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

def extract_filename(urls):
    filenames = {}
    
    for i in range(len(urls)):
        j = -1
        nameindex = ""
        while nameindex != "/":
            nameindex = urls[i][j]
            j = j -1
        
        if urls[i][j+2:] not in filenames.keys():
            filenames[urls[i][j+2:]] = 1
        else:
            filenames[urls[i][j+2:]] += 1
    
    sorted(filenames.items())
    key = list(filenames.keys())
    
    for i in key[:3]:
        print(i,filenames[i])
        
   
extract_filename(urls)        
    
        
    



    

