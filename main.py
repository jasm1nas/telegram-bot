import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN as token
from botton import *



bot=Bot(token=token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp=Dispatcher()

@dp.message(Command('start'))
async def CommandStart(message: Message):
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!",reply_markup=menyu)



@dp.message(F.text=='Arab Harflari')
async def echo_handler(message: Message) -> None:
    await message.answer_photo(photo="https://t.me/arab_alifbosi_Tajvid_darslari/4",caption='Мазкур 28 ҳарфнинг барчаси ундош ҳарфлар ҳисобланиб, улар мабоний (ўзгармайдиган) ҳарфлар деб айтилади.', reply_markup=menyu)
    await message.answer_video(video="https://t.me/arab_tili_alifbosi/48", reply_markup=menyu)


@dp.message(F.text=='Arab Harflari Oqilishi')
async def namoz2(message:Message):
  await message.answer(text='Arab alifbosi',reply_markup=oqish)    

@dp.message(F.text=='ا alif')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/49',reply_markup=oqish)    

@dp.message(F.text=='ب ba')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/56',reply_markup=oqish) 

@dp.message(F.text=='ت ta')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/53',reply_markup=oqish)   

@dp.message(F.text=='ث fa')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/65',reply_markup=oqish)   

@dp.message(F.text=='ج jim')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/68',reply_markup=oqish)   

@dp.message(F.text=='ح ha')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/70',reply_markup=oqish)   

@dp.message(F.text=='خ xo')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/69',reply_markup=oqish)   

@dp.message(F.text=='د dal')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/73',reply_markup=oqish)   

@dp.message(F.text=='ذ zal')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/75',reply_markup=oqish)   

@dp.message(F.text=='ر ro')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/50',reply_markup=oqish)   

@dp.message(F.text=='ز za')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/51',reply_markup=oqish)   

@dp.message(F.text=='س sin')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/64',reply_markup=oqish)
@dp.message(F.text=='ش shin')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/63',reply_markup=oqish)   

@dp.message(F.text=='ص sod')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/66',reply_markup=oqish)   

@dp.message(F.text=='ض dod')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/74',reply_markup=oqish)   

@dp.message(F.text=='ط to')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/67',reply_markup=oqish)   

@dp.message(F.text=='ظ za')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/76',reply_markup=oqish)

@dp.message(F.text=='ع ayn')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/72',reply_markup=oqish)

@dp.message(F.text=='غ g`ayn')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/71',reply_markup=oqish)   

@dp.message(F.text=='ف fa')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/61',reply_markup=oqish)   

@dp.message(F.text=='ق qof')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/62',reply_markup=oqish)   

@dp.message(F.text=='ك kaf')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/57',reply_markup=oqish)   

@dp.message(F.text=='ل lam')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/58',reply_markup=oqish)   

@dp.message(F.text=='م mim')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/52',reply_markup=oqish)   

@dp.message(F.text=='ن nun')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/54',reply_markup=oqish)   

@dp.message(F.text=='ه ha')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/60',reply_markup=oqish)   

@dp.message(F.text=='و vov')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/59',reply_markup=oqish)   

@dp.message(F.text=='ي ya')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/55',reply_markup=oqish)   


@dp.message(F.text =='Arabcha Kitoblar')
async def namoz2(message:Message):
    await message.answer_document(
        document="https://t.me/arabtilibotu/98",
        caption="",
        reply_markup=oqish)
    
@dp.message(F.text =='books📕')
async def namoz2(message:Message):
    await message.answer_document(


        document="https://t.me/arabtilibotu/99",
        caption="",
        reply_markup=menyu)
    

@dp.message(F.text == 'Tongi duolar✨')
async def namoz2(message:Message):
    await message.answer(f'''Аллоҳумма бика асбаҳнаа ва бика амсайнаа ва бика наҳйаа ва бика намууту ва илайкан нушуур»  дер эдилар.
Маъноси: Аллоҳим, Сенинг номинг ила тонг оттирдик, Сенинг номинг ила кеч киргиздик. Сенинг номинг ила тириламиз ва Сенинг номинг ила ўламиз. Va Сенга қайтажакмиз. ''',reply_markup=menyu)



@dp.message(F.text=='Juma kuni oqiladigan suralar')
async def namoz2(message:Message):
  await message.answer(f'''1. Kahf surasi.

Rasululloh sollallohu alayhi vasallam: "Kim juma kuni Kahf surasini o'qisa, qiyomat kuni uning qadami ostidan nur chiqib, osmonu falakni yoritadi va uning ikki juma orasidagi gunohlari kechiriladi", dedilar (Abu Bakr ibn Marduyah rivoyat qilgan).

 
2. Duxan surasi.

Rasululloh sollallohu alayhi vasallam: "Kim juma kechasi "Ha mim" (Duxon surasi)ni qiroat qilsa, mag'firat qilinadi", dedilar.

Nabiy alayhissalom: "Kim juma kechasi "Ha mim"ni o'qisa, etmish ming farishta tonggacha uning haqqiga istig'for aytib chiqadi", deganlar.


3. Oli Imran surasi.

Hazrati Usmon ibn Affon roziyallohu anhu aytadilar: "Kimki kechasi "Oli Imron" surasini o'qisa, unga kechani bedor o'tkazganlik savobi yoziladi".

Bir asarda: "Kim juma kuni Oli Imron surasini o'qisa, 70 ming farishta kechgacha istig'for aytadi".


4. Hud surasi.

Rasululloh sollallohu alayhi vasallam: "Hud surasini juma kuni o'qinglar", deganlar.

                       
5. Yasin surasi.
                       

                       
6. Ixlos, falaq va naas surasi.

Rasululloh sollallohu alayhi vasallam: «Kim juma namozidan keyin "Qul huvallohu ahad", "Qul a'uzu birobbil falaq" va "Qul a'uzu birobbin naas" suralarini etti marta o'qisa, Alloh taolo uni keyingi jumagacha yomonlikdan saqlaydi», dedilar (Ibn Sunniy rivoyati).

  ''',reply_markup=menyu)  


   

@dp.message(F.text == 'Ortga <-')
async def namoz2(message:Message):
  await message.answer(text='Asosiy Menyu',reply_markup=menyu)

@dp.message()

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Tugadi")
