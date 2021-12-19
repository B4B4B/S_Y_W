from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
- اهلا عزيزي {}
أهلا بك {}
يعمل هذا البوت لمساعدتك بطريقة سهله للحصول على كود تيرمكس او كود بايروجرام
    """

    # Home Button
    home_buttons = [        [InlineKeyboardButton("- ابدا بأستخراج كود .", callback_data="generate")],        [InlineKeyboardButton(text="- رجوع .", callback_data="home")]    ]

    generate_button = [        [InlineKeyboardButton("- ابدا بأستخراج كود .", callback_data="generate")]    ]

    # Rest Buttons
    buttons = [        [InlineKeyboardButton("- ابدا بأستخراج كود .", callback_data="generate")],        [InlineKeyboardButton("- قناه السورس .", url="https://t.me/jmthon")],
        [            InlineKeyboardButton("- طريقة الاستخدام ؟ .", callback_data="help"),            InlineKeyboardButton("- حول البوت .", callback_data="about")        ],]

    # Help Message
    HELP = """
** - الاوامر المتوفرة . **

/about - معلومات عن البوت
/help - هذه الرسالة
/start - تشغيل البوت 
/generate - البدا بأستخراج جلسة جديده
/cancel - الغاء العملية
/restart - عملية الالغاء
"""

    # About Message
    ABOUT = """
**- حول هذا البوت .** 

- بوت يساعدك على استخراج كوك تيرمكس و بايروجرام .

- قروب الدعم للمساعدة : [Support](https://t.me/jmthon)

    """
