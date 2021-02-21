from instabot import Bot

bot=Bot()

print("\nWRITE YOUR USERNAME: \n")

usr = input()

print("\nWRITE YOUR PASSWORD: \n")

pwd = input()

print("\nGIVE THE FILE NAME IN .jpg or .png FORMAT: \n")

pic = input()

print("\nWRITE THE CAPTION THAT YOU WANT ON YOUR PHOTO'S DESCRIPTION: \n")

cap = input()

bot.login(username=usr,password=pwd)
bot.upload_photo(pic,caption=cap)