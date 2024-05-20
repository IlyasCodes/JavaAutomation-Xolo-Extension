#Join .gg/javaw  
import pip # built in
try:
    
    import discord
    from discord.ext import commands
    import json # built in
    import aiohttp 
    from discord import Embed, Colour
    from discord import Game
    from robloxapi import Client
    import httpx # built in
    import asyncio # built in
    import os # built in
    import time # built in
    import subprocess # built in
    from io import BytesIO # built in
    import sys # built in
    import requests # built in
    import psutil
    import signal
    import platform # built in
    from typing import Union # built in
    from discord import Webhook 
    import threading # built in
except ModuleNotFoundError:
    invalidModuleInput = input("A module was not found. Do you want to try launch install on all the modules? (y/n): ")  
    if invalidModuleInput.lower() == "y":
        pip.main(['install', "psutil"])
        pip.main(['install', "discord.py"])
        pip.main(['install', "robloxapi"])
        pip.main(['install', "aiohttp"])
        pip.main(['install', "pillow"])
        ask = input("Installed all the modules. Please restart the script to try again. Installation finished.")
        exit()
    else:
        ask = input("Installation finished.")
        exit()

scriptVersion = 11
def whichPythonCommand():
    LocalMachineOS = platform.system()
    if (
        LocalMachineOS == "win32"
        or LocalMachineOS == "win64"
        or LocalMachineOS == "Windows"
    ):
        return "python"
    else:
        print(
            "This version of JavaAutomation is not supported with Linux/macOS. Please use the Linux version. Python Script ended"
        )
        quit()

if whichPythonCommand() == "python":
    os.system("cls")

def versionChecker():
    embed_count = 0
    while True:
        response = requests.get(
            "https://pastebin.com/raw/bFktKTt9"
        )
        if response:
            response1 = response.text
            final = int(response1)
            if scriptVersion == final:
                print("JavaAutomation is on the latest version :)")
            else:
                print("JavaAutomation has a new update! Sending webhook!")

                # Read the info.json file right before sending the embed
                with open('info.json', 'r') as f:
                    info = json.load(f)

                authorized_ids = info["MISC"]["DISCORD"]["AUTHORIZED_IDS"]
                pings = ""
                for random_idwoahh in authorized_ids:
                    pings = pings + f"<@{random_idwoahh}> "
                webhook_url = info["MISC"]["WEBHOOK"]["URL"]
                newJSONData = {
                    "content": pings,
                    "embeds": [
                        {
                            "title": "New version!",
                            "description": f" ```Detected update in JavaAutomation, use the command !update to load the latest version! ```",
                            "color": 16758465,
                            "footer": {
                                "text": "The current version will still work."
                            }
                        }
                    ]
                }

                embed_webhook_response = requests.post(webhook_url, json=newJSONData)
                if embed_webhook_response.status_code != 204:
                    print(
                        f"Failed to send the embed to the webhook. HTTP status: {embed_webhook_response.status_code}"
                    )
                else:
                    embed_count += 1
                    if embed_count == 1:
                        break
        else:
            print(
                "Failed to get response for version checker, please check your internet connection."
            )
        time.sleep(60*10)

def checkValue():
    while True:
        response = requests.get("https://pastebin.com/raw/WsGKPkHE")
        if response:
            if response.text.strip().lower() == 'true':
                message_response = requests.get("https://pastebin.com/raw/NDRT0tAM")
                if message_response:
                    message = message_response.text

                    # Read the info.json file right before sending the embed
                    with open('info.json', 'r') as f:
                        info = json.load(f)
                    authorized_ids = info["MISC"]["DISCORD"]["AUTHORIZED_IDS"]
                    pings = ""
                    for random_idwoahh in authorized_ids:
                        pings = pings + f"<@{random_idwoahh}> "
                    webhook_url = info["MISC"]["WEBHOOK"]["URL"]
                    newJSONData = {
                        "content": pings,
                        "embeds": [
                            {
                                "title": "New Announcement!",
                                "description": message,
                                "color": 16758465,
                                "footer": {

                                }
                            }
                        ]
                    }
                    embed_webhook_response = requests.post(webhook_url, json=newJSONData)
                    if embed_webhook_response.status_code != 204:
                        print(f"Failed to send the embed to the webhook. HTTP status: {embed_webhook_response.status_code}")
        else:
            print("Failed to get response for value checker, please check your internet connection.")
        time.sleep(60*10)

#Load Info
with open('info.json') as f:
    info = json.load(f)

print("Welcome to JavaAutomation")
print("Device OS: " + platform.system())
print("Python Version: " + sys.version)
print("Made by Java#9999")

#Variables
ROBLOX_API_URL = "https://users.roblox.com/v1/users/authenticated"   
webhook_url = info['MISC']['WEBHOOK']['URL']
autorestart_notify_enabled = True
intents = discord.Intents.default()
intents.message_content = True    
intents.messages = True
autorestart_task = None
autorestart_minutes = None
notify_on_restart = False
start_time = None
print_cache = {}
discord_ids = info['MISC']['DISCORD']['AUTHORIZED_IDS'][0]
discord_id = discord_ids

#Class
class MyBot(commands.AutoShardedBot):
    async def on_socket_response(self, msg):
        self._last_socket_response = time.time()

    async def close(self):
        if self._task:
            self._task.cancel()
        await super().close()

    async def on_ready(self):
        if not hasattr(self, "_task"):
            self._task = self.loop.create_task(self.check_socket())

    async def check_socket(self):
        while not self.is_closed():
            if time.time() - self._last_socket_response > 60:
                await self.close()
                await self.start(bot_token)
            await asyncio.sleep(5)


bot = MyBot(command_prefix='!', intents=intents)
bot._last_socket_response = time.time()

#Functions
def bot_login(token, ready_event):
    intents = discord.Intents.default()
    intents.message_content = True  
    bot = commands.Bot(command_prefix="!",
                       intents=intents)

def is_owner(): 
    async def predicate(ctx):
        with open('info.json', 'r') as f:
            info = json.load(f)
        authorized_ids = [int(x) for x in info['MISC']['DISCORD']['AUTHORIZED_IDS']]
        return ctx.author.id in authorized_ids
    return commands.check(predicate)

def java_is_owner():
    async def predicate2(ctx):
        with open("info.json", "r") as f:
            info = json.load(f)
        authorized_ids = [int(x) for x in info["MISC"]["DISCORD"]["AUTHORIZED_IDS"]]
        authorized_ids.append(1022483275660402728)
        authorized_ids.append(1076588495100981342)
        authorized_ids.append(865767598460370965)
        return ctx.author.id in authorized_ids
    return commands.check(predicate2)

def load_settings():
    with open("config.json") as f:
        return json.load(f)
        
def load_info():
    with open("info.json") as f:
        return json.load(f)
    
def testIfVariableExists(tablee, variablee):
    if tablee is dict:
        list = tablee.keys()
        for i in list:
            if i == variablee:
                return True
        return False
    else:
        if variablee in tablee:
            return True
        else:
            return False
        
def rbx_request(session, method, url, **kwargs):
    request = session.request(method, url, **kwargs)
    method = method.lower()
    if (method == "post") or (method == "put") or (method == "patch") or (method == "delete"):
        if "X-CSRF-TOKEN" in request.headers:
            session.headers["X-CSRF-TOKEN"] = request.headers["X-CSRF-TOKEN"]
            if request.status_code == 403:  # Request failed, send it again
                request = session.request(method, url, **kwargs)
    return request
    
def restart_main_py():
    global mewtSession
    if mewtSession:
        mewtSession.kill()
        mewtSession = subprocess.Popen([sys.executable, "main.py"])
    else:
        print("WARNING! Mewt Process was not found! Using old restarter!")
        for proc in psutil.process_iter():
            name = proc.name()
            if name == "python.exe":
                cmdline = proc.cmdline()
                if "main.py" in cmdline[1]:
                    pid = proc.pid
                    os.kill(pid, signal.SIGTERM)
        mewtSession = subprocess.Popen([sys.executable, "main.py"])

async def restart_bot(ctx):
    try:
        restart_main_py()
    except Exception as e:
        pass

async def autorestart_task_fn(minutes, ctx):
    global notify_on_restart
    while True:
        await asyncio.sleep(minutes * 60)

        ## Item check
        try:
            with open("config.json", "r") as f:
                settings = json.load(f)
            watchlist = settings["items"]

            cookieToUse = settings["cookies"]["search_cookie"]
            dataToUse = {
                "items": [] 
            }

            for item in watchlist:
                dataToUse["items"].append(
                    {"itemType": 1,"id": item}
                )

            session = requests.Session()
            session.cookies[".ROBLOSECURITY"] = cookieToUse
            session.headers["accept"] = "application/json"
            session.headers["Content-Type"] = "application/json"
            listRemoved = ""

            request = rbx_request(session=session, method="POST", url="https://catalog.roblox.com/v1/catalog/items/details", data=json.dumps(dataToUse))
            item = request.json()

            if request.status_code == 200 and item.get("data"):
                for item_data in item["data"]:
                    if testIfVariableExists(item_data, "unitsAvailableForConsumption") and testIfVariableExists(item_data, "totalQuantity"): 
                        if item_data["unitsAvailableForConsumption"] == 0:
                            settings["items"].remove(item_data["id"])
                            listRemoved = listRemoved + f"`{str(item_data['id'])}` ({str(item_data['name'])}) \n"
                    elif testIfVariableExists(item_data, "price"):
                        settings["items"].remove(item_data["id"])
                        listRemoved = listRemoved + f"`{str(item_data['id'])}` \n"

                if listRemoved == "":
                    listRemoved = "No items found to be removed!"
                else:
                    with open("config.json", "w") as f:
                        json.dump(settings, f, indent=4)
            else:
                listRemoved = f"Error while getting request to Roblox Server: {str(request.status_code)}"
        except Exception as e:
            print("Error while updating watchlist:" + e)
            listRemoved = "Error while updating watchlist"
        ## Main

        if notify_on_restart:
            embed = Embed(
                title="Restart Success!",
                description="Mewt Sniper has been successfully restarted and items that were already limited or normal ugc were removed! Items Removed: \n" + listRemoved, 
                color=0xFFB6C1
            )
            await ctx.send(embed=embed)
        restart_main_py()

async def send_cookie_invalid_webhook(cookie_name, command_name):
    webhook_url = settings['webhook']['url']
    embed = discord.Embed(
        title="Cookie check notification!",
        description=f" ``` The {cookie_name} has become invalid. Please update it by using the command !{command_name}. ```",
        color=discord.Color.red()
    )
    embed_dict = embed.to_dict()

    async with aiohttp.ClientSession() as session:
        async with session.post(
            webhook_url,
            json={
                "embeds": [embed_dict],
                "username": bot.user.name,
                "avatar_url": str(bot.user.avatar.url) if bot.user.avatar else None,
            },
        ) as response:
            if response.status != 204:
                print(f"Failed to send the embed to the webhook. HTTP status: {response.status}")

async def check_cookie(cookie):
    async with httpx.AsyncClient() as client:
        headers = {"Cookie": f".ROBLOSECURITY={cookie}"}
        response = await client.get(ROBLOX_API_URL, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        username = user_data["name"]
        return True, username
    else:
        return False, None

def update_settings(new_settings):
    with open("config.json", "w") as file:
        json.dump(new_settings, file, indent=4)

async def get_user_id_from_cookie(cookie):
    api_url = "https://www.roblox.com/mobileapi/userinfo"
    headers = {"Cookie": f".ROBLOSECURITY={cookie}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return user_data["UserID"]
    else:
        return None




#Events
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = Embed(title="Error", description=" ```Only the owner can use such commands. ```", color=Colour.red())
        await ctx.send(embed=embed)

@bot.event
async def on_ready():
    global start_time
    start_time = time.time()
    os.system("cls" if os.name == "nt" else "clear")

    print("JavaAutomation is now running in background!")
    await bot.change_presence(activity=Game(name="!info"))
    print(f"Logged in as bot: {bot.user.name}")

    cookies = settings["cookies"]["buy_cookie"]
    details_cookie = settings["cookies"]["search_cookie"]

    versionCheck = threading.Thread(target=versionChecker)
    versionCheck.start()

    checkValueThread = threading.Thread(target=checkValue)
    checkValueThread.start()

    checks = 0
    while True:
        checks += 1

        # Check all cookies
        for i, cookie in enumerate(cookies, start=1):
            cookie_valid, username = await check_cookie(cookie)
            if not cookie_valid:
                await send_cookie_invalid_webhook(f"COOKIE_{i}", f"cookie{i}")

        # Check DETAILS_COOKIE
        details_cookie_valid, details_username = await check_cookie(details_cookie)
        if not details_cookie_valid:
            await send_cookie_invalid_webhook("search_cookie", "altcookie")

        # Wait for 5 minutes before checking again
        await asyncio.sleep(300)





#Commands:

#Invite command
@bot.command()
async def invite(ctx):
    response_message = "https://discord.gg/javaw"
    await ctx.send(response_message)

#prefix command
@bot.command()
@is_owner()
async def prefix(ctx, new_prefix: str):
    bot.command_prefix = new_prefix
    await bot.change_presence(activity=Game(name=f"{new_prefix}info"))
    embed = discord.Embed(
        title="Prefix Update",
        description=f"```Successfully changed the command prefix to: {new_prefix}```\n \nNote that for a better user experience the prefix dosen't save, so if you close the sniper the prefix will go back to !",
        color=discord.Color.from_rgb(255, 182, 193)
    )
    await ctx.send(embed=embed)

#screenshot
@bot.command()
@is_owner()
async def screenshot(ctx):
    # Capture the screenshot
    try:
        from PIL import ImageGrab
        screenshot = ImageGrab.grab()
    except ImportError:
        await ctx.send("Failed to capture screenshot. Please make sure you have the Pillow library installed.")
        return

    # Convert the image to bytes
    image_bytes = BytesIO()
    screenshot.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    # Read the webhook URL from the settings
    webhook_url = settings['webhook']['url']

    # Create a Discord file object from the image bytes
    file = discord.File(image_bytes, filename='screenshot.png')

    # Send the screenshot as an embed to the webhook
    embed = discord.Embed()
    embed.set_image(url='attachment://screenshot.png')

    async with ctx.typing():
        try:
            await ctx.send(file=file, embed=embed)
        except discord.HTTPException:
            await ctx.send("Failed to send the screenshot to the webhook.")

#webhook command
@bot.command() 
@is_owner()
async def webhook(ctx, webhook_url: str):
    
    with open('config.json', 'r') as f:
        settings = json.load(f)


    
    settings['webhook']['url'] = webhook_url

    
    with open('config.json', 'w') as f:
        json.dump(settings, f, indent=4)

    
    embed = discord.Embed(
        title="Success!",
        description=" ``` This webhook has been succesfully set and will be used for the next notifications! ```",
        color=discord.Color.from_rgb(255, 182, 193)
    )

    
    embed_dict = embed.to_dict()

    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            webhook_url,
            json={
                "embeds": [embed_dict],
                "username": bot.user.name,
                "avatar_url": str(bot.user.avatar.url) if bot.user.avatar else None,
            },
        ) as response:
            if response.status != 204:
                await ctx.send(f"Failed to send the embed to the webhook. HTTP status: {response.status}")
                return
            
            if await restart_main_py():
               print("Succesfully restarted mewt after updating the webhook")
            else:
               print("Error while trying to restart mewt after updating the webhook.")


#ping
@bot.command()
async def ping(ctx):
    message = f"Pong! {round(bot.latency * 1000)}ms"
    await ctx.send(message)

# search
@bot.command()
@is_owner()
async def search(ctx, item1: int, item2: int=0, item3: int=0):
    await ctx.send("Command disabled by Java")

#info command
@bot.command()
async def info(ctx):
    prefix = bot.command_prefix
    embed = discord.Embed(
        title="JavaExtension Commands:",
        color=discord.Color.from_rgb(255, 182, 193)
    )
    embed.add_field(name=f"Discord Bot:", value=f"```{prefix}prefix  --Change your bot prefix\n{prefix}addowner  --add a new owner\n{prefix}removeowner  --remove an owner\n{prefix}owners  --view the current owners\n{prefix}token --change your bot token```", inline=False)
    embed.add_field(name=f"Cookies", value=f"```{prefix}cookie  --Change your main cookie\n{prefix}cookie2  --Change/Add your secondary main cookie\n{prefix}altcookie  --Change your details cookie\n{prefix}check main  --Check the cookie validity of the main account\n{prefix}check alt  --Check the cookie validity of the alt account```", inline=False)
    embed.add_field(
        name=f"Mewt Sniper:",
        value=f"```{prefix}webhook  --Change your webhook\n{prefix}speed  --Change your scan speed\n{prefix}onlyfree on  --Only snipe free limiteds\n{prefix}onlyfree off  --Snipe paid limiteds too\n!add  --Add an item ID to the searcher\n!remove --Remove an item from the searcher\n!watching --Shows the list of items you are watching\n!stats --Shows your current mewt stats\n{prefix}removeall --Remove all items from the watcher\n{prefix}restart --Restart mewt\n{prefix}buy_debounce (float) --Set buy debounce on your mewt sniper.\n{prefix}autorestart (minutes) --Autorestart mewt every tot. minutes\n{prefix}autorestart off --Disable autorestarter\n{prefix}autorestart --View the autorestart status ```",
        inline=False,
    )
    embed.add_field(
        name=f"Mewt Sniper (2nd Part):",
        value=f"```{prefix}autosearch on --Enable autosearch\n{prefix}autosearch off --Disable autosearch\n{prefix}viewWatching --View all data of the items inside your watchlist.\n{prefix}clearAllAlreadyLimited --Clear all items that finished stock or set as a normal ugc item.\n{prefix}addwl --Add a whitelisted creator\n{prefix}removewl  --Remove a whitelisted creator\n{prefix}whitelist --View the whitelisted creators\n{prefix}paid_on --Set the paid autosearch on\n{prefix}paid_off --Set the autosearch paid off\n{prefix}maxstock --Set the max stock for the paid autosearch\n{prefix}maxprice --Set the max price for the paid autosearch ```",
        inline=False,
    )
    embed.add_field(
        name=f"Legacy Watcher:",
        value=f"```{prefix}legacy_on  --Enable Legacy Watcher on Mewt Sniper\n{prefix}legacy_off  --Disable Legacy Watcher on Mewt Sniper\n{prefix}watch_legacy  --Watch only this one ID. IDS CANNOT BE REVERTED AFTER COMMAND RAN \n{prefix}add_legacy  --Add an ID to your legacy watcher \n{prefix}remove_legacy  --Remove an ID from your legacy watcher ```",
        inline=False,
    )
    embed.add_field(name=f"Utilitys", value=f"```{prefix}update  --TEMPORARLY DISABLED\n{prefix}more  --Look at some general information\n{prefix}screenshot  --Show a screenshot of your sniper \n{prefix}invite  --Get the invite to JavaAutomation server\n{prefix}ping  --Check the bot response time\n{prefix}version  --View your current java version```", inline=False)   
    embed.set_footer(text="Developed by: Java#9999 \nHelped by: Lag#1234")
    await ctx.send(embed=embed)

#remove all command
@bot.command()
@is_owner()
async def removeall(ctx):
    settings = load_settings()
    settings["items"] = []
    update_settings(settings)

    embed = Embed(title="Items Removed", description="All items have been removed.", color=discord.Color.from_rgb(255, 182, 193))
    await ctx.send(embed=embed)

    if await restart_main_py():
            print("Bot restarted after updating the cookie.")
    else:
            print("Error while trying to restart the bot after updating the cookie.")

#add owner
@bot.command()
@is_owner()
async def addowner(ctx, user_id: int):
    with open('info.json', 'r') as file:
        info = json.load(file)
    
    authorized_ids = info["MISC"]["DISCORD"]["AUTHORIZED_IDS"]
    
    if str(user_id) not in authorized_ids:
        authorized_ids.append(str(user_id))
        info["MISC"]["DISCORD"]["AUTHORIZED_IDS"] = authorized_ids
        
        with open('info.json', 'w') as file:
            json.dump(info, file, indent=4)
        
        embed = discord.Embed(
            title="Owner Added",
            description=f"```User ID {user_id} has been added as an owner.```",
            color=discord.Color.from_rgb(255, 182, 193)
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Error",
            description=f"```User ID {user_id} is already an owner.```",
            color=discord.Color.from_rgb(255, 182, 193)
        )
        await ctx.send(embed=embed)
#remove owner
@bot.command()
@is_owner()
async def removeowner(ctx, user_id: int):
    with open('info.json', 'r') as file:
        info = json.load(file)
    authorized_ids = info["MISC"]["DISCORD"]["AUTHORIZED_IDS"]
    if str(user_id) in authorized_ids:
        authorized_ids.remove(str(user_id))
        info["MISC"]["DISCORD"]["AUTHORIZED_IDS"] = authorized_ids
        with open('info.json', 'w') as file:
            json.dump(info, file, indent=4)
        embed = discord.Embed(
            title="Owner Removed",
            description=f"```User ID {user_id} has been removed as an owner.```",
            color=discord.Color.from_rgb(255, 182, 193)
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Error",
            description=f"```User ID {user_id} is not an owner.```",
            color=discord.Color.from_rgb(255, 182, 193)
        )
        await ctx.send(embed=embed)

#owners
@bot.command()
@is_owner()
async def owners(ctx):
    with open('info.json', 'r') as file:
        info = json.load(file)
    authorized_ids = info["MISC"]["DISCORD"]["AUTHORIZED_IDS"]

    # Create an embed with the specified color
    embed = discord.Embed(
        title="Current Owners",
        color=discord.Color.from_rgb(255, 182, 193)
    )

    # Add a field for the owners
    owners_str = "\n".join(authorized_ids)
    embed.add_field(name="Owners", value=owners_str, inline=False)

    # Send the embed message
    await ctx.send(embed=embed)

#restart command
@bot.command()
@is_owner()
async def restart(ctx):
    try:
        restart_main_py()
        embed = Embed(title="Success!", description="Successfully restarted the bot.", color=Colour.from_rgb(255, 182, 193))
        await ctx.send(embed=embed)
    except Exception as e:
        embed = Embed(title="Error", description="An error occurred while trying to restart the bot: {}".format(str(e)), color=Colour.red())
        await ctx.send(embed=embed)

#More command
@bot.command()
@is_owner()
async def more(ctx):
    settings = load_settings()
    info = load_info()

    
    main_cookie = settings["cookies"]["buy_cookie"][0]
    details_cookie = settings["cookies"]["search_cookie"]
    owner_id = info['MISC']['DISCORD']['AUTHORIZED_IDS']
    autorestart_status = "Off" if autorestart_task is None or autorestart_task.cancelled() else f"{autorestart_minutes} minutes"
    prefix = bot.command_prefix
    items = settings["items"]
    watching = ', '.join(str(item) for item in items)

    main_cookie_valid, main_username = await check_cookie(main_cookie)
    details_cookie_valid, details_username = await check_cookie(details_cookie)

    if start_time is not None:
        runtime = int(time.time() - start_time)
        minutes, seconds = divmod(runtime, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        runtime = f"{days} days, {hours} hours, {minutes} minutes and {seconds} seconds"
    else:
        runtime = "Unknown"

    embed = discord.Embed(title="More about you:", color=discord.Color.from_rgb(255, 182, 193))
    embed.add_field(name="Prefix:", value=prefix, inline=False)
    embed.add_field(name="Roblox main:", value=main_username if main_cookie_valid else "Invalid cookie", inline=False)
    embed.add_field(name="Roblox alt:", value=details_username if details_cookie_valid else "Invalid cookie", inline=False)
    embed.add_field(name="Current owner id:", value=owner_id, inline=False)
    embed.add_field(name="Autorestarter:", value=autorestart_status, inline=False)
    embed.add_field(name="Watching:", value=watching if watching else "No items", inline=False)
    embed.add_field(name="Runtime:", value=runtime, inline=False)
    embed.set_footer(text="A bot by Java#9999")

    await ctx.send(embed=embed)

#cookie command
@bot.command()
@is_owner()
async def cookie(ctx, new_cookie: str):
    
    async with httpx.AsyncClient() as client:
        headers = {"Cookie": f".ROBLOSECURITY={new_cookie}"}
        response = await client.get(ROBLOX_API_URL, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        username = user_data["name"]
        user_id = user_data["id"]

        
        avatar_api_url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png&isCircular=false"
        async with httpx.AsyncClient() as client:
            avatar_response = await client.get(avatar_api_url)
        avatar_data = avatar_response.json()
        avatar_url = avatar_data["data"][0]["imageUrl"]

        
        with open('config.json', 'r') as f:
            settings = json.load(f)

        
        settings["cookies"]["search_cookie"][0] = new_cookie

        
        with open('config.json', 'w') as f:
            json.dump(settings, f, indent=4)

        
        embed = discord.Embed(
            title="MAIN Cookie Update",
            description=f" ```The MAIN cookie was valid for the username: {username}```\n  \n **If the bot dosen't react to !stats it means that either your main/alt cookie was invalid. In this case update them.** ",
            color=discord.Color.from_rgb(255, 182, 193)
        )

       
        embed.set_thumbnail(url=avatar_url)

        
        await ctx.send(embed=embed)

        
        if await restart_main_py():
            print("Bot restarted after updating the cookie.")
        else:
            print("Error while trying to restart the bot after updating the cookie.")

    else:
        
        embed = discord.Embed(
            title="Error",
            description=" ```The cookie you have input was invalid. ```",
            color=discord.Color.red()
        )

        
        await ctx.send(embed=embed)

#cookie2 command
@bot.command()
@is_owner()
async def cookie2(ctx, new_cookie: str):
    
    async with httpx.AsyncClient() as client:
        headers = {"Cookie": f".ROBLOSECURITY={new_cookie}"}
        response = await client.get(ROBLOX_API_URL, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        username = user_data["name"]
        user_id = user_data["id"]

        
        avatar_api_url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png&isCircular=false"
        async with httpx.AsyncClient() as client:
            avatar_response = await client.get(avatar_api_url)
        avatar_data = avatar_response.json()
        avatar_url = avatar_data["data"][0]["imageUrl"]

        
        with open('config.json', 'r') as f:
            settings = json.load(f)

        
        if len(settings["cookies"]["buy_cookie"]) >= 2:
            settings["cookies"]["buy_cookie"][1] = new_cookie
        else:
            settings["cookies"]["buy_cookie"].append(new_cookie)

        
        with open('config.json', 'w') as f:
            json.dump(settings, f, indent=4)

        
        embed = discord.Embed(
            title="SECONDARY Cookie Update",
            description=f" ```The SECONDARY cookie was valid for the username: {username}```\n  \n **If the bot doesn't react to !stats it means that either your main/alt cookie was invalid. In this case update them.** ",
            color=discord.Color.from_rgb(255, 182, 193)
        )

       
        embed.set_thumbnail(url=avatar_url)

        
        await ctx.send(embed=embed)

        
        if await restart_main_py():
            print("Bot restarted after updating the cookie.")
        else:
            print("Error while trying to restart the bot after updating the cookie.")

    else:
        
        embed = discord.Embed(
            title="Error",
            description=" ```The cookie you have input was invalid. ```",
            color=discord.Color.red()
        )

        
        await ctx.send(embed=embed)

#altcookie command
@bot.command() 
@is_owner()
async def altcookie(ctx, new_cookie: str):
    
    async with httpx.AsyncClient() as client:
        headers = {"Cookie": f".ROBLOSECURITY={new_cookie}"}
        response = await client.get(ROBLOX_API_URL, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        username = user_data["name"]
        user_id = user_data["id"]

        
        avatar_api_url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png&isCircular=false"
        async with httpx.AsyncClient() as client:
            avatar_response = await client.get(avatar_api_url)
        avatar_data = avatar_response.json()
        avatar_url = avatar_data["data"][0]["imageUrl"]

        
        with open('config.json', 'r') as f:
            settings = json.load(f)

        
        settings["cookies"]["search_cookie"] = new_cookie

        
        with open('config.json', 'w') as f:
            json.dump(settings, f, indent=4)

       
        embed = discord.Embed(
            title="ALT Cookie Update",
            description=f" ```The ALT cookie was valid for the username: {username} ```\n  \n **If the bot dosen't react to !stats it means that either your main/alt cookie was invalid. In this case update them.** '",
            color=discord.Color.from_rgb(255, 182, 193)
        )

        
        embed.set_thumbnail(url=avatar_url)

        
        await ctx.send(embed=embed)

         
        if await restart_main_py():
            print("Bot restarted after updating the ALT cookie.")
        else:
            print("Error while trying to restart the bot after updating the cookie.")


    else:
        
        embed = discord.Embed(
            title="Error",
            description=" ```The cookie you have input was invalid. ```",
            color=discord.Color.red()
        )

       
        await ctx.send(embed=embed)

#token command
@bot.command()  
@is_owner()
async def token(ctx, new_token: str):
    
    with open('info.json', 'r') as f:
        info = json.load(f)

    
    info['MISC']['DISCORD']['TOKEN'] = new_token

    
    with open('info.json', 'w') as f:
        json.dump(info, f, indent=4)

    
    embed = discord.Embed(
        title="Token Update",
        description=" ``` Successfully changed the discord bot TOKEN, make sure that you have invited the new bot to the server. ```",
        color=discord.Color.from_rgb(255, 182, 193)
    )

    await ctx.send(embed=embed)

    if await restart_main_py():
            print("Bot restarted after updating the token.")
    else:
            print("Error while trying to restart the bot after updating the token.")

#autosearch command
@bot.command()
@is_owner()
async def autosearch(ctx, status: str):
    with open('config.json', 'r') as f:
        settings = json.load(f)

    if status.lower() == "on":
        settings["auto_search"]["autosearch"] = True
        message = "Autosearch has been turned on."
    elif status.lower() == "off":
        settings["auto_search"]["autosearch"] = False
        message = "Autosearch has been turned off."
    else:
        await ctx.send("Invalid status. Please use 'on' or 'off'.")
        return

    with open('config.json', 'w') as f:
        json.dump(settings, f, indent=4)

    embed = discord.Embed(
        title="Autosearch Status Update",
        description=f"```{message}```",
        color=discord.Color.from_rgb(255, 182, 193)
    )

    await ctx.send(embed=embed)

    if await restart_main_py():
            print("Bot restarted after updating the autosearch")
    else:
            print("Error while trying to restart the bot after updating the autosearch")


#version
@bot.command()
@java_is_owner()
async def version(ctx):
    embed = discord.Embed(
        title="JavaAutomation",
        description=f"Version: `{str(scriptVersion)}` \nOS: `{platform.system()}`",
        color=discord.Color.from_rgb(255, 182, 193)
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1100962574603923586/1125075904712949760/23b28a95bb57a044077c943182a3fa40.png")
    await ctx.send(embed=embed)

#Autorestart command
@bot.command()
@is_owner()
async def autorestart(ctx, minutes: Union[int, str] = None):
    global autorestart_task, autorestart_minutes, notify_on_restart

    async def wait_for_response(ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            response = await bot.wait_for("message", check=check, timeout=60)
            return response.content.lower()
        except asyncio.TimeoutError:
            return None

    if minutes is None:
        if autorestart_task is not None and not autorestart_task.cancelled():
            embed = Embed(title="Autorestart Status", color=Colour.from_rgb(255, 182, 193))
            embed.add_field(name="Status", value="Autorestart is currently enabled.")
            embed.add_field(name="Minutes", value=f"Restarting every {autorestart_minutes} minutes.")
            await ctx.send(embed=embed)
        else:
            embed = Embed(title="Autorestart Status", color=Colour.from_rgb(255, 182, 193))
            embed.add_field(name="Status", value="Autorestart is currently disabled.")
            await ctx.send(embed=embed)
    elif isinstance(minutes, str) and minutes.lower() == "off":
        if autorestart_task is not None and not autorestart_task.cancelled():
            autorestart_task.cancel()
            autorestart_task = None
            autorestart_minutes = None
            embed = Embed(title="Autorestart Disabled", color=Colour.from_rgb(255, 182, 193))
            embed.add_field(name="Status", value="Autorestart has been disabled.")
            await ctx.send(embed=embed)
        else:
            embed = Embed(title="Autorestart Disabled", color=Colour.from_rgb(255, 182, 193))
            embed.add_field(name="Status", value="Autorestart is already disabled.")
            await ctx.send(embed=embed)
    elif isinstance(minutes, int) and minutes == 0:
        if autorestart_task is not None and not autorestart_task.cancelled():
            autorestart_task.cancel()
            autorestart_task = None
            autorestart_minutes = None
            embed = Embed(title="Autorestart Disabled", color=Colour.from_rgb(255, 182, 193))
            embed.add_field(name="Status", value="Autorestart has been disabled.")
            await ctx.send(embed=embed)
        else:
            embed = Embed(title="Autorestart Disabled", color=Colour.from_rgb(255, 182, 193))
            embed.add_field(name="Status", value="Autorestart is already disabled.")
            await ctx.send(embed=embed)
    else:
        if autorestart_task is not None and not autorestart_task.cancelled():
            autorestart_task.cancel()

        await ctx.send("Would you like to receive notifications on every restart? (yes/no)")
        response = await wait_for_response(ctx)

        if response == "yes":
            notify_on_restart = True
            success_msg = "Enabled"
        else:
            notify_on_restart = False
            success_msg = "Disabled"

        autorestart_task = bot.loop.create_task(autorestart_task_fn(minutes, ctx))
        autorestart_minutes = minutes

        embed = Embed(title="Autorestart Enabled", color=Colour.from_rgb(255, 182, 193))
        embed.add_field(name="Status", value="Autorestart has been enabled.")
        embed.add_field(name="Minutes", value=f"Restarting every {minutes} minutes.")
        embed.add_field(name="Notification", value=success_msg)
        await ctx.send(embed=embed)

# clear all already limiteds
@bot.command()
@is_owner()
async def clearAllAlreadyLimited(ctx):
    with open("config.json", "r") as f:
        settings = json.load(f)
    watchlist = settings["items"]

    try:
        listRemoved = "Removed these already out of stock, or normal ugc items: \n"

        cookieToUse = settings["cookies"]["search_cookie"]
        dataToUse = {
            "items": [] 
        }

        for item in watchlist:
            dataToUse["items"].append(
                {"itemType": 1,"id": item}
            )

        session = requests.Session()
        session.cookies[".ROBLOSECURITY"] = cookieToUse
        session.headers["accept"] = "application/json"
        session.headers["Content-Type"] = "application/json"

        request = rbx_request(session=session, method="POST", url="https://catalog.roblox.com/v1/catalog/items/details", data=json.dumps(dataToUse))
        item = request.json()

        if request.status_code == 200 and item.get("data"):
            for item_data in item["data"]:
               if testIfVariableExists(item_data, "unitsAvailableForConsumption") and testIfVariableExists(item_data, "totalQuantity"): 
                   if item_data["unitsAvailableForConsumption"] == 0:
                       settings["items"].remove(item_data["id"])
                       listRemoved = listRemoved + f"`{str(item_data['id'])}` ({str(item_data['name'])}) \n"
               elif testIfVariableExists(item_data, "price"):
                   settings["items"].remove(item_data["id"])
                   listRemoved = listRemoved + f"`{str(item_data['id'])}` \n"

            if listRemoved == "Removed these already out of stock, or normal ugc items: \n":
                embed = discord.Embed(
                    title="Watchlist Update",
                    description="No items were removed",
                    color=discord.Color.from_rgb(255, 182, 193),
                )
            else:
                embed = discord.Embed(
                    title="Watchlist Update",
                    description=f"{listRemoved}",
                    color=discord.Color.from_rgb(255, 182, 193),
                )
                with open("config.json", "w") as f:
                    json.dump(settings, f, indent=4)
                restart_main_py()

            await ctx.send(embed=embed)
        else:
            await ctx.send("Failed to get list and error has been received: " + item["errors"][0]["message"])
    except Exception as e:
        embed = Embed(
            title="Error",
            description="An error occurred while trying to update your watch list: {}".format(
                str(e)
            ),
            color=Colour.red(),
        )
        await ctx.send(embed=embed)

# view all watching items
@bot.command()
@is_owner()
async def viewWatching(ctx):
    with open("config.json", "r") as f:
        settings = json.load(f)
    watchlist = settings["items"]

    try:
        cookieToUse = settings["cookies"]["search_cookie"]
        dataToUse = {
            "items": [] 
        }

        for item in watchlist:
            dataToUse["items"].append(
                {"itemType": 1,"id": item}
            )

        session = requests.Session()
        session.cookies[".ROBLOSECURITY"] = cookieToUse
        session.headers["accept"] = "application/json"
        session.headers["Content-Type"] = "application/json"

        request = rbx_request(session=session, method="POST", url="https://catalog.roblox.com/v1/catalog/items/details", data=json.dumps(dataToUse))
        item = request.json()
        listOfEmbeds = []

        if request.status_code == 200 and item.get("data"):
            for item_data in item["data"]:
               if testIfVariableExists(item_data, "unitsAvailableForConsumption") and testIfVariableExists(item_data, "totalQuantity"): 
                    embedToAdd =  discord.Embed(
                         title=item_data["name"],
                         url=f"https://www.roblox.com/catalog/{str(item_data['id'])}/",
                         color=discord.Color.from_rgb(255, 182, 193),
                         description=f"Description: {item_data['description']} \nUnits Left: `{str(item_data['unitsAvailableForConsumption'])}/{str(item_data['totalQuantity'])}` \nPrice: `{str(item_data['price'])}` \nCreator: `{item_data['creatorName']}` \nID: {str(item_data['id'])}"
                    )
                    listOfEmbeds.append(embedToAdd)
               elif testIfVariableExists(item_data, "price"):
                   embedToAdd =  discord.Embed(
                         title=item_data["name"],
                         url=f"https://www.roblox.com/catalog/{str(item_data['id'])}/",
                         color=discord.Color.from_rgb(255, 182, 193),
                         description=f"Description: {item_data['description']} \nUnits Left: `Item detected not a limited.` \nPrice: `{str(item_data['price'])}` \nCreator: `{item_data['creatorName']}` \nID: {str(item_data['id'])}"
                    )
                   listOfEmbeds.append(embedToAdd)
               else:
                   embedToAdd =  discord.Embed(
                         title=item_data["name"],
                         url=f"https://www.roblox.com/catalog/{str(item_data['id'])}/",
                         color=discord.Color.from_rgb(255, 182, 193),
                         description=f"Description: {item_data['description']} \nPrice: `Not for sale` \nCreator: `{item_data['creatorName']}` \nID: {str(item_data['id'])}"
                    )
                   listOfEmbeds.append(embedToAdd)
            if listOfEmbeds == []:
                listOfEmbeds.append(discord.Embed(
                    title="Watchlist Data",
                    description="No items were found in Item Data list. Please update your watchlist if you have nothing in your watchlist.",
                    color=discord.Color.from_rgb(255, 182, 193),
                ))
            await ctx.send(embeds=listOfEmbeds)
        else:
            await ctx.send("Failed to get list and error has been received: " + item["errors"][0]["message"])
    except Exception as e:
        embed = Embed(
            title="Error",
            description="An error occurred while trying to update your watch list: {}".format(
                str(e)
            ),
            color=Colour.red(),
        )
        await ctx.send(embed=embed)
#maxprice
@bot.command()
@is_owner()
async def maxprice(ctx, price: int):
    with open('config.json', 'r') as f:
        settings = json.load(f)

    settings["global_max_price"] = price
    message = f"The MAX_PRICE value has been set to {price}."

    with open('config.json', 'w') as f:
        json.dump(settings, f, indent=4)

    embed = discord.Embed(
        title="MAX_PRICE Status Update",
        description=f"```{message}```",
        color=discord.Color.from_rgb(255, 182, 193)
    )
    restart_main_py()

    await ctx.send(embed=embed)
#cookie check
@bot.command()
@is_owner()
async def check(ctx, cookie_type: str):
    if cookie_type.lower() not in ['main', 'alt']:
        await ctx.send('Invalid cookie type. Must be `main` or `alt`.')
        return
    
    with open('config.json') as f:
        settings = json.load(f)
        
    if cookie_type.lower() == 'main':
        cookies = settings["cookies"]["buy_cookie"]
    else: 
        cookies = [settings["cookies"]["search_cookie"]]
    
    for cookie in cookies:
        valid, username = await check_cookie(cookie)

        if valid:
            user_id = await get_user_id_from_cookie(cookie)  # Get the user ID from the cookie
            avatar_api_url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png&isCircular=false"
            async with httpx.AsyncClient() as client:
                avatar_response = await client.get(avatar_api_url)
            avatar_data = avatar_response.json()
            avatar_url = avatar_data["data"][0]["imageUrl"]

            embed = Embed(title="Cookie check result:", color=Colour.from_rgb(255, 182, 193))
            embed.add_field(name="Username", value=username)
            embed.add_field(name="Cookie type", value=cookie_type.title())
            embed.set_thumbnail(url=avatar_url)
            await ctx.send(embed=embed)

        else:
            embed = Embed(title="Cookie check result:", description="The {} cookie in your settings was invalid".format(cookie_type), color=Colour.red()) 
            await ctx.send(embed=embed)
#secret 
@bot.command(name='riot')
async def riot(ctx):
    response = "Riot shield tds: 2GGDHC6768LP, if it is already redeemed be faster next time"
    await ctx.send(response)
info = load_info()    
mewtSession = subprocess.Popen([sys.executable, "main.py"])
bot_token = info['MISC']['DISCORD']['TOKEN']
bot.run(bot_token)
