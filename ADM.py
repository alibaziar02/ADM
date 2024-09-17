import requests , threading
from bs4 import BeautifulSoup
from tkinter import * 
from tkinter import messagebox as msg
from tkinter import ttk
import os , getpass


os.chdir("C:\\Users\\{}\\Downloads".format(getpass.getuser()))

def t1(chunk,file):
    global progressbar
    if chunk:
        try:
         progressbar.step((390/len(chunk)) * 0.001)
         file.write(chunk)
        except:
            file.write(chunk)

def download_video(video_url, output_file):
    # ارسال درخواست برای دانلود ویدیو
    response = requests.get(video_url, stream=True)
    threads=[]
    if response.status_code == 200:
        with open(output_file, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                t1(chunk,file)
        msg.showinfo("Alert",f"{output_file} Downloaded")
        progressbar.step(0)
    else:
        msg.showerror("Error",f"Error Code:{response.status_code}")
root = Tk()
progressbar = ttk.Progressbar(length=390)
label1 = Label(root,text="URL: ")
entry1 = Entry(root,width=70)
entry2 = Entry(root)
def download():
    global button
    url = entry1.get()
    if not (url is None):
        newurl = url.strip("https://")
        newurl = newurl.strip("http://")
        newurl = newurl.split("/")
        ext = newurl[-1]
        if ext.find("?") != -1:
            index = ext.find("?")
            ext = ext[:index]
            output_name = ext
            button["state"] = "disabled"
            download_video(url, output_name)
            button['state'] = "normal"
button = Button(root,text="Download",fg="white",bg="green",command=threading.Thread(target=download).start)
def main():
    global progressbar
    root.title("Ali Download Manager(ADM)")
    root.geometry("500x500")
    label1.grid(column=3,row=2)
    entry1.grid(column=4,row=2)
    button.grid(column=4,row=5)
    progressbar.grid(column=4,row=6)
    # page_url = input("Enter a URL:")
    # output = input("Enter a Output File:")
    # download_video(page_url, output)
    root.mainloop()
if __name__ == '__main__':
    main()

