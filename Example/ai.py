from ancient import  AncientScriptAI

# وارد کردن توکن API خود
api_key = ""
ai_bot =  AncientScriptAI(api_key=api_key)

# متن ورودی کاربر
text = "سلام باستانی"
script = "cuneiform"


# گرفتن پاسخ AI
response = ai_bot.get_ancient_response(text, script)
print(response)