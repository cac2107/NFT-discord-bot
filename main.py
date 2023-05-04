import discord
from discord.embeds import Embed
import constants
import sel_scraper
import my_parser
import filemanager
import asyncio
import sol_parser

bot = discord.Client()

@bot.event
async def on_ready():
    print(f"{bot.user} has connected succesfully!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    elif message.content.startswith("!upcoming"):
        nfts = upcoming()
        await upcoming_msg_maker(nfts)

    elif message.content == "!solsea":
        channel = message.channel
        nfts = solsea(False)
        await solsea_msg_maker(nfts, channel)

    elif message.content == "!solsea verified":
        channel = message.channel
        nfts = solsea(True)
        await solsea_msg_maker(nfts, channel)

def upcoming():
    page = sel_scraper.get_page(constants.UPCOMING)
    areas = my_parser.get_list(page)
    original = filemanager.get_upcoming()
    nfts = {}
    for area in areas:
        currency = "other"
        if len(area) < 10:
            continue
        try:
            name = my_parser.get_name(area)
        except Exception as e:
            print(e)
        if name in original:
            continue
        try:
            image = my_parser.get_image(area)
        except Exception as e:
            print(e)
        try:
            price = my_parser.get_price(area)
        except Exception as e:
            print(e)
        try:
            total = my_parser.get_total(area)
        except Exception as e:
            print(e)
        try:
            twitter = my_parser.get_twitter(area)
        except Exception as e:
            print(e)
        try:
            disc = my_parser.get_discord(area)
        except Exception as e:
            print(e)
        try:
            website = my_parser.get_website(area)
            website = website.replace(" ", "")
            if website[:4] != "http":
                website = "https://" + website
        except Exception as e:
            print(e)
        try:
            date = my_parser.get_date(area)
        except Exception as e:
            print(e)
        
        if "ADA" in price:
            currency = "ADA"
        elif "ETH" in price:
            currency = "ETH"
        elif "SOL" in price:
            currency = "SOL"
        nfts[name] = {"image": image, "price": price, "twitter": twitter, "disc": disc, "website": website, "date": date, "total": total, "currency": currency}
        original[name] = {"image": image, "price": price, "twitter": twitter, "disc": disc, "website": website, "date": date, "total": total, "currency": currency}
    filemanager.upcoming_writer(original)
    return nfts

def solsea(verified):
    page = sel_scraper.get_page(constants.SOLSEA)
    rows = sol_parser.get_content(page)
    if verified:
        original = filemanager.get_verified_sol()
    else:
        original = filemanager.get_sol()
    nfts = {}
    for row in rows:
        price = "--"
        supply = "--"
        price = row.find("div", class_="listed-floor__CalendarItem_3HFd1")
        items = price.findAll("h6")
        item2 = row.find("div", class_="like-view__CalendarItem_16zcx")
        items2 = item2.findAll("h6")
        name = sol_parser.get_name(row)
        date = sol_parser.get_date(row)
        is_verified = sol_parser.is_verified(row)
        img = sol_parser.get_image(row)
        website = sol_parser.get_website(row)
        try:
            pricee = sol_parser.get_price(items[1])
        except Exception as e:
            print("No price found")
            price = "--"
        try:
            supply = sol_parser.get_supply(items[0])
        except Exception as e:
            print("No supply found")
            supply = "--"
        likes = sol_parser.get_likes(items2)
        views = sol_parser.get_views(items2)
        if verified and is_verified and name not in original:
            nfts[name] = {"date": date, "verified": is_verified, "image": img, "website": website, "price": pricee, "supply": supply, "likes": likes, "views": views}
            original[name] = {"date": date, "verified": is_verified, "image": img, "website": website, "price": pricee, "supply": supply, "likes": likes, "views": views}
        elif name not in original and not verified:
            nfts[name] = {"date": date, "verified": is_verified, "image": img, "website": website, "price": pricee, "supply": supply, "likes": likes, "views": views}
            original[name] = {"date": date, "verified": is_verified, "image": img, "website": website, "price": pricee, "supply": supply, "likes": likes, "views": views}
    if verified:
        filemanager.sol_verified_writer(original)
    else:
        filemanager.sol_writer(original)
    return nfts

async def upcoming_msg_maker(nfts):
    for name in nfts:
        embed = discord.Embed(title=name, url=nfts[name]["website"])
        embed.add_field(name = "Discord", value = nfts[name]["disc"], inline=True)
        embed.add_field(name = "Twitter", value = nfts[name]["twitter"], inline=True)
        embed.add_field(name = "Release Date", value = nfts[name]["date"], inline=False)
        embed.add_field(name = "Price", value = nfts[name]["price"], inline=True)
        embed.add_field(name = "Quantity", value = nfts[name]["total"], inline=True)
        embed.color = discord.Color(7)
        currency = nfts[name]["currency"]
        if currency == "other":
            channel = bot.get_channel(constants.OTHER_ID)
        elif currency == "ADA":
            channel = bot.get_channel(constants.ADA_ID)
        elif currency == "ETH":
            channel = bot.get_channel(constants.ETH_ID)
        elif currency == "SOL":
            channel = bot.get_channel(constants.SOL_ID)

        if nfts[name]["image"][:5] == "https":
            embed.set_image(url=nfts[name]["image"])
        else:
            print("Invalid image")
        try:
            await channel.send(embed=embed)
        except Exception as e:
            print(e)
            print(f"{name} failed to send. Likely an invalid website")
            await channel.send(f"{name}")
        await asyncio.sleep(3)

async def solsea_msg_maker(nfts, channel):
    for name in nfts:
        embed = discord.Embed(title=name, url=nfts[name]["website"])
        embed.add_field(name = "Release Date", value=nfts[name]["date"], inline=False)
        embed.add_field(name="Likes", value=nfts[name]["likes"], inline=True)
        embed.add_field(name="Views", value=nfts[name]["views"], inline=True)
        embed.add_field(name="Quantity", value=nfts[name]["supply"], inline=False)
        embed.add_field(name="Price", value=nfts[name]["price"], inline=True)
        embed.add_field(name="Verified", value = nfts[name]["verified"], inline=True)
        embed.color = discord.Color(7)
        if nfts[name]["image"][:5] == "https" and " " not in nfts[name]["image"]:
            embed.set_image(url=nfts[name]["image"])
        else:
            print("Invalid image")

        try:
            await channel.send(embed=embed)
        except Exception as e:
            print(e)
            await channel.send(f"{name}")
            print(f"Failed to send {name}, Website is likely invalid")
        await asyncio.sleep(3)


bot.run(constants.TOKEN)
