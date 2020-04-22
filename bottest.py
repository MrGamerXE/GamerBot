import discord
from discord.ext import commands
import random
import requests
import os
bot = commands.Bot(command_prefix='!')
@bot.command(pass_context=True)
async def ipsetup(ctx, args, versionminec):
 global iplol
 global versionmine
 iplol = args
 versionmine = versionminec
 await ctx.send("IP сервера обновлено.")
@bot.command(pass_context=True)
async def ip(ctx):
    await ctx.send("IP сервера: "+iplol+"\nВерсия: "+versionmine)

@bot.command(pass_context=True)
async def channel(ctx):
    await ctx.send("Создатель сервера: BaDuMoH. Канал: https://www.youtube.com/channel/UCRC-W4FbvsTAaqP3x6pxjAA?view_as=subscriber")

@bot.command(pass_context=True)
async def gamerhelp(ctx):
    await ctx.send("```Команды: \n!ipsetup (IP) - установка IP сервера\n!ip - показ установленного IP\n!say \"текст\" - заставляет бота сказать то что вы пожелаете\n!channel - информация про создателя сервера\n!generatestory - генерация рандомных историй\n!botinfo - информация про бота\n!randomizer (число) - рандомный выбор числа от 0 до вами выбранного числа\n!answer (вопрос) - бот будет отвечать на вопрос \"да\" или \"нет\"\n!rever \"текст\" - реверс текста в обратную сторону\n!rps (твой выбор) - всеми любимая \"камень-ножницы-бумага\"\n!calc (число, действие, число2) - мини-калькулятор, цифры и действия писать через пробелы```")

@bot.command(pass_context=True)
async def generatestory(ctx):

    boyorgirl = random.randint(1, 2)
    
    if boyorgirl == 1:
     newname = random.SystemRandom().choice(["Дима","Вадим","Толик","Паша","Вова","Никита","Даня","Костя","Вова","Денис","Иван","Игорь","Олег","Вася"])   
    if boyorgirl == 2:
     newname = random.SystemRandom().choice(["Даша","Люда","Соня","Лена","Юля","Настя","Карина","Саша"])
    age = random.randint(7, 20)
    marks = random.SystemRandom().choice(["хорошие","плохие"])
    if age < 17 or 17:
     school = "школе"
    if age > 17:
     school = "лицее"
    if age < 14 or 14:
     if boyorgirl == 1:
      agename = "Мальчик"
     if boyorgirl == 2:
      agename = "Девочка"
    if age > 14:
      agename = "Подросток"
    age = str(age)    
    schoolnumber = random.randint(1, 50)
    schoolnumber = str(schoolnumber)
    play = random.SystemRandom().choice(["компьютере","приставке"])
    loseorwin = random.SystemRandom().choice(["проиграл","выиграл"])
    hours = random.randint(5, 9)
    hours = str(hours)
    speed = random.randint(110, 150)
    speed = str(speed)
    game = random.SystemRandom().choice(["CS:GO","DOTA 2","Minecraft","Mortal Combat 11","CS 1.6"])
    if boyorgirl == 1:
     loseorwin = random.SystemRandom().choice(["проиграл","выиграл"])
    if boyorgirl == 2:
     loseorwin = random.SystemRandom().choice(["проиграла","выиграла"])
    if loseorwin == "проиграл":
     angryorno = "от злости"
    if loseorwin == "проиграла":
     angryorno = "от злости"   
    if loseorwin == "выиграл":
     angryorno = "от радости"
    if loseorwin == "выиграла":
     angryorno = "от радости"
    agestory7 = random.randint(7, 15)
    agestory7 = str(agestory7)
    mouseorkeyboard = random.SystemRandom().choice(["мышку","телефон","чашку"])
    motherorfather = random.SystemRandom().choice(["пришла мама и забрала","пришёл папа и забрал"])
    like = random.SystemRandom().choice(["любит","не любит","очень любит","очень не любит"])
    teachers = random.SystemRandom().choice(["нравятся","очень нравятся","не нравятся","очень не нравятся"])
    city = random.SystemRandom().choice(["Санкт-Петербург","Москва","Токио","Лондон","Дубай","Киев","Варшава","Сингапур","Нью-Йорк","Майами","Париж"])
    citylike = random.SystemRandom().choice(["нравится","не нравится","очень нравится","очень не нравится"])
    action = random.SystemRandom().choice(["заниматься физ-культурой","смотреть фильмы и сериалы","гулять на улице","играть в футбол","делать апликации","очень хорошо покушать"])
    story = random.randint(1, 8)
    if story == 1:
     if boyorgirl == 1:
      storylabel = newname+" живет в городе "+city+" и ему "+age+" лет. Он любит "+action+" и ему "+teachers+" учителя в его "+school+"."
     if boyorgirl == 2:
      storylabel = newname+" живет в городе "+city+" и ей "+age+" лет. Она любит "+action+" и ей "+teachers+" учителя в её "+school+"."
    if story == 2:
     if boyorgirl == 1:
      storylabel = age+"-летний "+newname+" живет в городе "+city+"."+newname+" учится в "+school+" номер "+schoolnumber+" и любит "+action+". Ему "+teachers+" его учителя."
     if boyorgirl == 2:
      storylabel = age+"-летняя "+newname+" живет в городе "+city+"."+newname+" учится в "+school+" номер "+schoolnumber+" и любит "+action+". Ей "+teachers+" её учителя." 
    if story == 3:
     if boyorgirl == 1:
      storylabel = newname+". Живет в городе "+city+". Ему "+age+" лет. Учится в "+school+" номер "+schoolnumber+". У него "+marks+" оценки."
     if boyorgirl == 2:
      storylabel = newname+". Живет в городе "+city+". Ей "+age+" лет. Учится в "+school+" номер "+schoolnumber+". У неё "+marks+" оценки."
    if story == 4:
     if boyorgirl == 1:
      storylabel = "В городе "+city+" проживает "+age+"-летний "+newname+". Он любит "+action+". Ему "+citylike+" его город. Он учится в "+school+" под номером "+schoolnumber+"."
     if boyorgirl == 2:
      storylabel = "В городе "+city+" проживает "+age+"-летняя "+newname+". Она любит "+action+". Ей "+citylike+" её город. Она учится в "+school+" под номером "+schoolnumber+"."
    if story == 5:
     if boyorgirl == 1:
      storylabel = "Жил был одинокий "+newname+" и было у него всё нормально. Он любил "+action+" в возрасте "+age+" лет. Ему "+citylike+" город в котором он живёт, называется "+city+". Он учится в "+school+" номер "+schoolnumber+" и ему "+teachers+" учителя там."
     if boyorgirl == 2:
      storylabel = "Жила была одинокая "+newname+" и было у неё всё нормально. Она любила "+action+" в возрасте "+age+" лет. Ей "+citylike+" город в котором она живёт, называется "+city+". Она учится в "+school+" номер "+schoolnumber+" и ей "+teachers+" учителя там."
    if story == 6:
     if boyorgirl == 1:
      storylabel = agename+" по имени "+newname+" любит "+action+". Ему "+age+" лет и он живет в городе "+city+". Он "+like+" свой город. В "+school+" номер "+schoolnumber+" он получает "+marks+" оценки и "+like+" своих учителей."
     if boyorgirl == 2:
      storylabel = agename+" по имени "+newname+" любит "+action+". Ей "+age+" лет и она живет в городе "+city+". Она "+like+" свой город. В "+school+" номер "+schoolnumber+" она получает "+marks+" оценки и "+like+" своих учителей."
    if story == 7:
     if boyorgirl == 1:
      storylabel = newname+" играл на "+play+". Ему "+agestory7+" лет. Он играл в "+game+". Тут вдруг он "+loseorwin+" и поэтому "+angryorno+" кинул "+mouseorkeyboard+" в монитор. После этого "+motherorfather+" шнур питания."
     if boyorgirl == 2:
      storylabel = newname+" играла на "+play+". Ей "+agestory7+" лет. Она играл в "+game+". Тут вдруг она "+loseorwin+" и поэтому "+angryorno+" кинула "+mouseorkeyboard+" в монитор. После этого "+motherorfather+" шнур питания."
    if story == 8:
     if boyorgirl == 1:
      storylabel = newname+" дежурил на дороге уже "+hours+" часов, он собирался уже уезжать. Но когда "+newname+" завёл двигатель, перед ним промчалась машина на "+speed+" км/час.    "+newname+" сразу выехал в след и уведомил по рации, что преследует нарушителя. Менеджер сказал, что к нему едет подмога. Через "+hours+" минут они окружили нарушителя."
     if boyorgirl == 2:
      storylabel = newname+" дежурила на дороге уже "+hours+" часов, она собиралась уже уезжать. Но когда "+newname+" завела двигатель, перед ней промчалась машина на "+speed+" км/час.    "+newname+" сразу выехала в след и уведомила по рации, что преследует нарушителя. Менеджер сказал, что к ней едет подмога. Через "+hours+" минут они окружили нарушителя."
    await ctx.send(storylabel)
@bot.command(pass_context=True)
async def say(ctx, arg):
    if len(arg) > 50:
     await ctx.send("Длинна строки превышает ограничение, операция отменена.")
    if len(arg) < 50:
     await ctx.send(arg)
@bot.command(pass_context=True)
async def botinfo(ctx):
    await ctx.send("Бот написан на Python, создатель - MrGamerX#9121")
@bot.command(pass_context=True)
async def randomizer(ctx, amount=None):
    amount = int(amount)
    randomnumber = random.randint(0, amount)
    randomnumber = str(randomnumber)
    await ctx.channel.send("Бот выбрал число: "+randomnumber+".")
@bot.command(pass_context=True)
async def answer(ctx):
    answerlol = random.SystemRandom().choice(["Да, наверное.","Однозначно да!","Конечно же нет.","Вероятно, нет","Думаю, нет"])
    await ctx.channel.send(answerlol)
@bot.command(pass_context=True)
async def rever(ctx, arg):
    arg = arg[::-1]
    await ctx.channel.send(arg)
@bot.command(pass_context=True)
async def rps(ctx, arg):
    if arg == "ножницы":
     answ = random.SystemRandom().choice(["ножницы","камень","бумага"])
     if answ == "бумага":
      await ctx.channel.send("Бумага! О нет, я проиграл(")
     elif answ == "камень":
      await ctx.channel.send("Камень! О да, я выиграл!)")
     elif answ == "ножницы":
      await ctx.channel.send("Ножницы! Это ничья.")
    elif arg == "камень":
     answ = random.SystemRandom().choice(["ножницы","камень","бумага"])
     if answ == "бумага":
      await ctx.channel.send("Бумага! О да, я выиграл!)")
     elif answ == "камень":
      await ctx.channel.send("Камень! Это ничья.")
     elif answ == "ножницы":
      await ctx.channel.send("Ножницы! О нет, я проиграл")
    elif arg == "бумага":
     answ = random.SystemRandom().choice(["ножницы","камень","бумага"])
     if answ == "бумага":
      await ctx.channel.send("Бумага! Это ничья.")
     elif answ == "камень":
      await ctx.channel.send("Камень! О нет, я проиграл(")
     elif answ == "ножницы":
      await ctx.channel.send("Ножницы! О да, я выиграл!)")
    else:
     await ctx.channel.send("Произошла ошибка, проверь правильность ввода.")
@bot.command(pass_context=True)
async def calc(ctx, number, action, number2):
 if action == "-":
     number = int(number)
     number2 = int(number2)
     answernumber = number - number2
     answernumber = str(answernumber)
     await ctx.send("Ответ: "+answernumber)
 elif action == "+":
     number = int(number)
     number2 = int(number2)    
     answernumber = number + number2
     answernumber = str(answernumber)
     await ctx.send("Ответ: "+answernumber)     
 elif action == "*":
     number = int(number)
     number2 = int(number2)    
     answernumber = number * number2
     answernumber = str(answernumber)
     await ctx.send("Ответ: "+answernumber)      
 elif action == "/":
     number = int(number)
     number2 = int(number2)    
     answernumber = number / number2
     answernumber = str(answernumber)
     await ctx.send("Ответ: "+answernumber)      
 else:
     await ctx.send("Действие не найдено.")

token = os.envirom.get("BOT_TOKEN")
bot.run(str(token))
