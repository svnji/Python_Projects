from pytube import YouTube


url = input("your url video : ")

print('wait for it')

y = YouTube(url).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()


print("done!")