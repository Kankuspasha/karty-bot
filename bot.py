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

# ---------------- HESAPLAMA ----------------
@bot.tree.command(name="hesap", description="Girilen sayının 1/3'ünü alır")
async def hesap(interaction: discord.Interaction, sayi: float):
    sonuc = sayi / 3
    await interaction.response.send_message(
        f"🧮 Girilen sayı: **{sayi:,.0f}**\n"
        f"📊 Sonuç (1/3): **{sonuc:,.0f}**"
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

        async for msg in kanal.history(limit=3):
            if msg.content:
                ilan += f"• {msg.content}\n"

    ilan += "\n📍 Detaylı bilgi için bizimle iletişime geçin!"
    await interaction.response.send_message(ilan)

# ---------------- VARLIK ----------------
@bot.tree.command(name="varlık", description="Çetenin elindeki varlıkları gösterir")
async def varlik(interaction: discord.Interaction):
    kanal = bot.get_channel(1457172366114164893)

    if not kanal:
        await interaction.response.send_message("Varlık bilgisi bulunamadı.")
        return

    mesajlar = []
    async for msg in kanal.history(limit=10):
        if msg.content:
            mesajlar.append(msg.content)

    if not mesajlar:
        await interaction.response.send_message("Varlık bilgisi yok.")
        return

    await interaction.response.send_message(
        "**Çete Varlıkları:**\n" + "\n".join(reversed(mesajlar))
    )

# ---------------- YIKAMA (İNATİF) ----------------
@bot.tree.command(name="yıkama", description="Şu anda aktif değil")
async def yikama(interaction: discord.Interaction):
    await interaction.response.send_message(
        "⛔ Bu özellik şu anda aktif değil."
    )

# -------- TOKEN --------
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise Exception("TOKEN bulunamadı!")

bot.run(TOKEN)
