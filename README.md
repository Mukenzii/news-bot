# Boshlanish

Yangiliklarni parsing qilib jo'natadigan telegram-bot
## Proyekt haqida
Bu proyekt telegramdan chiqmagan holda yangiliklarni o'qish uchun yaratilgan. Proyektni yaratishda Python, Django,DRF,bs4 texnologiyalaridan foydalanilgan.

## O'rnatish uchun qo'llanma

Birinchi bo'lib environment yaratiladi va [pip](https://pip.pypa.io/en/stable/) orqali barcha kerakli kutubxonalar o'rnatilinadi.Requriements.txt fileda barcha kerakli kutubxonalar bor. Shuni o'zini terminalga yozamiz.

```bash
pip install -r requriements.txt
```
Birinch navbatda parcingfile.py filega o'tiladi hamda uni run qilinadi.Run bo'lgandan keyin data.json nomlik file datalar bilan birgalikda paydo bo'ladi.

## Terminal
Terminal o'tib mana shu 3 ta buyruqni berish kerak bo'ladi.
```bash
py manage.py makemigrations
py manage.py makemigrate
py manage.py import_news.py
```

## Telegram-Bot
Telegram-botni ulash uchun [bot](https://t.me/BotFather)ga o'tamiz va u yerdan yangi bot yaratib tokenini olamiz va mana shu yerga qo'yamiz.
```python
bot = TeleBot('Bu yerni token uchun qoldirib ketaman.')
```

Telegram-botni ishlatishimizdan avval serverni ishlatib olamiz.
```bash
py manage.py runserver
```
Server ishlagandan so'ng parcing/bot.py filega o'tamiz va uni run qilamiz.Run qilganimizdan so'ng telegrambotga o'tib avval /start buyrug'ini beramiz. Keyin /latest buyrug'i berilgandan so'ng bot bizga bazadan yangiliklarni tashlashni boshlaydi.
