from ancient import AncientImageGenerator,AncientScriptAI,AncientScripts,AncientTimeline



api_key = ""


converter = AncientScripts()
script="cuneiform"
timeline = AncientTimeline(script=script)

ai_bot = AncientScriptAI(api_key=api_key)

generator = AncientImageGenerator(script=script)
output_image = generator.generate_image("از کتابخانه منحصرفرد ما استفاده کنید")
text = input("enter the text :>")


print("welcome to AncientLinesOfTheWorld Project ")

print("="*60)


print("Supported Ancient Scripts:")
for name,desc in converter.get_supported_scripts().items():
    print(f" - {name:<12} → {desc}")
    
print("="*60)

print("\n🪶 Converted Texts:")
print(f"  🔸 Pahlavi:       {converter.pahlavi(text)}")
print(f"  🔸 Akkadian:      {converter.akkadian(text)}")
print(f"  🔸 Avestan:       {converter.avestan(text)}")
print(f"  🔸 Manichaean:    {converter.manichaean(text)}")
print(f"  🔸 Linear B:      {converter.linear_b(text)}")
print(f"  🔸 Hebrew:        {converter.hebrew(text)}")
print(f"  🔸 Hieroglyph:    {converter.hieroglyph(text)}")
print(f"  🔸 Sanskrit:      {converter.sanskrit(text)}")
print(f"  🔸 Oracle Bone:   {converter.oracle_bone(text)}")
print(f"  🔸 Cuneiform:     {converter.cuneiform(text)}")

print("="*60)


print(f"📜 Real-time Ancient Timeline ({script} Script):")
timeline.show()
print("=" * 60)


print(f"📜 تصویر آماده شد و در این مسیر ذخیره شد:\n{output_image}")
print("=" * 60)


result = ai_bot.get_ancient_response(text,script=script)



print(f"🤖 AI Response in {script}: {result}")
print("=" * 60)


print("💫 Project completed using AncientLinesOfTheWorld")
print("💫 All classes  AncientScripts, AncientTimeline, AncientImageGenerator, AncientScriptAI")

