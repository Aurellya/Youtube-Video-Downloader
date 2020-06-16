import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def find_source():
    global my_entry

    link = str(my_entry.get())
    split_link = link.split('www.')[1]
    final_url = link.split('www.')[0] + "www.ss" + split_link

    driver = webdriver.Chrome()

    driver.get(final_url)
    driver.refresh()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "def-btn-box")))

    parser = BeautifulSoup(driver.page_source, "html.parser")
    download_link = parser.find(title="video format: 360")['href']

    driver.close()
    return str(download_link)


def download_video():
    try:
        download_link = find_source()

        driver = webdriver.Chrome()
        driver.get(download_link)

        urllib.request.urlretrieve(download_link, 'download.mp4')

        driver.close()

        success_message()

    except:
        missing_input()


def missing_input():
    tk.messagebox.showinfo(title="Missing Input", message="No Link Detected!")


def success_message():
    tk.messagebox.showinfo(title="Successful Download", message="The Videos Has Been Downloaded")


root = tk.Tk()
root.geometry('650x420')
root.resizable(0, 0)

# Image
path = "youtube_downloader.jpg"
img = Image.open(path)
img = img.resize((450, 220), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Label
window1 = tk.Label(root, image=img)
window1.pack()

window = tk.Label(root, text="Youtube Video Downloader\n", font="Helvetica 24 bold")
window.pack()

# Input Area
my_entry = tk.Entry(root, bd=5, width=60)
my_entry.insert(0,'##--put your link here--##')
my_entry.pack()

window = tk.Label(root, text="")
window.pack()

# Download button
button = tk.Button(root, text="Download", font="Helvetica 20 bold", fg="red",
                   activeforeground="green", height=2, width=15, command=download_video)
button.pack()

window = tk.Label(root, text="")
window.pack()

root.mainloop()
