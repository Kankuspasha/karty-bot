import os
import discord
from discord.ext import commands

# -------- INTENTS --------
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    activity=discord.Game(name="FiveM | Karty Bot")
)

# -------- READY --------
@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Karty Bot aktif!")

# ---------------- KONTROL ----------------
@bot.tree.command(name="ping", description="Karty Bot çalışıyor mu?")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🟢 **Karty Bot aktif!**")

# ---------------- MATEMATİK ----------------
@bot.tree.command(name="topla", description="İki sayıyı toplar")
async def topla(interaction: discord.Interaction, a: float, b: float):
    await interaction.response.send_message(f"🧮 Sonuç: **{a + b}**")

@bot.tree.command(name="cikar", description="İki sayıyı çıkarır")
async def cikar(interaction: discord.Interaction, a: float, b: float):
    await interaction.response.send_message(f"🧮 Sonuç: **{a - b}**")

@bot.tree.command(name="carp", description="İki sayıyı çarpar")
async def carp(interaction: discord.Interaction, a: float, b: float):
    await interaction.response.send_message(f"🧮 Sonuç: **{a * b}**")

@bot.tree.command(name="bol", description="İki sayıyı böler")
async def bol(interaction: discord.Interaction, a: float, b: float):
    if b == 0:
        await interaction.response.send_message("❌ Sıfıra bölünemez")
    else:
        await interaction.response.send_message(f"🧮 Sonuç: **{a / b}**")

@bot.tree.command(name="yuzde", description="Bir sayının yüzdesini hesaplar")
async def yuzde(interaction: discord.Interaction, sayi: float, oran: float):
    sonuc = sayi * oran / 100
    await interaction.response.send_message(
        f"📊 **{sayi}** sayısının **%{oran}**'i = **{sonuc}**"
    )

# ---------------- MEKANİK ----------------
@bot.tree.command(name="mekanik", description="Karty Oto Servis ilanı")
async def mekanik(interaction: discord.Interaction):
    mesaj = (
        "🔧 **Karty Oto Servis** 🔧\n"
        "**Aracınız Emin Ellerde!**\n\n"
        "🚗 Motor – Şanzıman – Kaporta\n"
        "⚙️ Bakım, onarım ve performans yükseltme\n"
        "🎨 Modifiye & kişiselleştirme\n"
        "⏱️ Hızlı servis, güvenilir işçilik\n"
        "💸 Uygun fiyat, kaliteli hizmet\n\n"
        "📍 Detaylı bilgi ve randevu için bize ulaşın!"
    )
    await interaction.response.send_message(mesaj)

# ---------------- GALERİ ----------------
@bot.tree.command(name="galeri", description="Galeri ilanı hazırlar")
async def galeri(interaction: discord.Interaction):
    kanal_idleri = [
        1456089461573292033,
        1456089948129067038
    ]

    ilan = "🚘 **Karty Galeri** 🚘\n**Galerimizden Öne Çıkan Araçlar:**\n\n"

    for kanal_id in kanal_idleri:
        kanal = bot.get_channel(kanal_id)
        if not kanal:
            continue

        ilan += f"📂 <#{kanal_id}>\n"
        async for msg in kanal.history(limit=3):
            if msg.content:
                ilan += f"• {msg.content}\n"
        ilan += "\n"

    ilan += "📍 Detaylı bilgi için bizimle iletişime geçin!"

    await interaction.response.send_message(ilan)

# -------- TOKEN --------
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise Exception("TOKEN bulunamadı!")

bot.run(TOKEN)
