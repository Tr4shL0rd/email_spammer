from tqdm import tqdm
from time import sleep
from dotenv import load_dotenv
from redmail import gmail
import os
load_dotenv() 
env = os.environ




def send_text(username:str, password:str, receivers:list[str], subject:str,  body:str, attachments:dict[str:str]=None):
    gmail.username = username
    gmail.password = password
    gmail.send(
        subject=subject,
        receivers=receivers,
        text=body,
        attachments=attachments if attachments else None
    )
with open("shrek.txt", "r") as f:
    lines = f.readlines()
    script = []
    for line in lines:
        script.append(line.strip())
script = " ".join(script)
# outlook email storage cap = 15Gb = 298261 emails (with shrek 1 script)  
def spammer(amount:int=101):
    spamMails = env["emails"].split(",")
    print("sending to ")
    for mail in spamMails:
        print(f"\t{mail.split('@')[0]}")
    for i in tqdm(range(amount)):
        send_text(
            username=env["user_mail"],#"scriptsmeme@gmail.com", 
            receivers=spamMails,
            password=env["app_password_mail3"], 
            subject=f"mega awesome email, i swear! ID{i}", 
            body=script,
            attachments=None#{"awesome.txt":"megaAwesomeFile.txt"}
            )
        sleep(1)
    print("DONE!")
try:
    spammer()
except KeyboardInterrupt:
    print("\nExiting...")