from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
- مرحبا بك في بوت جمثون

من هذا البوت يمكنك استخراج كود تيرمكس او كود بايروجرام بسهولة وبسرعة و بدون مشاكل اختر امر الاستخراج في الاسفل واكمل العملية  ، 

@JMTHON
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" • بدء الاستخراج  •", callback_data="generate")],
        [InlineKeyboardButton(text="• الواجهة الرئيسية •", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("• بدء الاستخراج  •", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("• بدء الاستخراج  •", callback_data="generate")
            InlineKeyboardButton("• كيفية الاستخدام  •", callback_data="help"),
        ],
        [InlineKeyboardButton(" • قناة السورس •", url="https://t.me/JMTHON")],
    ]

    # Help Message
    HELP = """ 
✨ الاوامر المتوفرة التي يمكنك مساعدة استخدام البوت بسلاسة هي : ✨

/about 
لعـرض معلومـات البـوت
/help 
 لعـرض اوامـر البوت
/start 
 لتشغـيل البـوت
/generate 
لبـدء استخـراج كود بايروجرام او تيرمكس
"""

    # About Message
    ABOUT = """
بوت استخراج كود تيرمكس او كود بايروجرام

وهـو عبـارة عن بوت بسيط للمساعـدة في استخـراج كـود تيرمكس/بايروجرام بسهولة وبأمان تام  ومساعدك في عمليه تنصيب سورس جمثون 

قناة السورس  : 
@Jmthon
>    """
