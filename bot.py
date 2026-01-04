import os
import discord
from discord.ext import commands
from discord import app_commands
import asyncio
from aiohttp import web


# -------- INTENTS --------
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    activity=discord.Game(name="FiveM | Karty Bot")
)

# -------- SABİTLER --------
SIPARIS_KANAL_ID = 1456358667438784542
VARLIK_KANAL_ID = 1457172366114164893

GALERI_KANALLARI = [
    1456089461573292033,
    1456089948129067038
]

async def start_web():
    port = int(os.environ.get("PORT", 10000))
    app = web.Application()

    async def health(request):
        return web.Response(text="Karty Bot aktif")

    app.router.add_get("/", health)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()


# -------- READY (TEK) --------
@bot.event
async def on_ready():
    await bot.tree.sync()
    bot.loop.create_task(start_web())
    print(f"{bot.user} aktif!")



# ---------------- PING ----------------
@bot.tree.command(name="ping", description="Karty Bot çalışıyor mu?")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🟢 **Karty Bot aktif!**")

# ---------------- HESAP ----------------
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
    await interaction.response.send_message(
        "🔧 **Karty Oto Servis** 🔧\n"
        "**Aracınız Emin Ellerde!**\n\n"
        "🚗 Motor – Şanzıman – Kaporta\n"
        "⚙️ Bakım, onarım ve performans yükseltme\n"
        "🎨 Modifiye & kişiselleştirme\n"
        "⏱️ Hızlı servis, güvenilir işçilik\n"
        "💸 Uygun fiyat, kaliteli hizmet\n\n"
        "📍 Detaylı bilgi ve randevu için bize ulaşın!"
    )

# ---------------- GALERİ (TEK KOMUT) ----------------
@bot.tree.command(name="galeri", description="Galeri işlemleri")
@app_commands.describe(
    islem="ekle / temizle / sipariş",
    arac="Araç adı",
    fiyat="Fiyat",
    telefon="Telefon numarası"
)
async def galeri(
    interaction: discord.Interaction,
    islem: str,
    arac: str = None,
    fiyat: int = None,
    telefon: str = None
):

    # ---- GALERİ EKLE (sadece mesaj döner) ----
    if islem.lower() == "ekle":
        if not arac or not fiyat:
            await interaction.response.send_message(
                "❌ Kullanım: `/galeri ekle AraçAdı Fiyat`",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"✅ **Galeriye eklendi**\n🚗 {arac}\n💰 {fiyat:,}$",
            ephemeral=True
        )

    # ---- GALERİ TEMİZLE ----
    elif islem.lower() == "temizle":
        await interaction.response.send_message(
            "🧹 **Galeri ilanları sıfırlandı.**",
            ephemeral=True
        )

    # ---- GALERİ SİPARİŞ ----
    elif islem.lower() == "sipariş":
        if not telefon or not fiyat:
            await interaction.response.send_message(
                "❌ Kullanım: `/galeri sipariş Telefon Fiyat`",
                ephemeral=True
            )
            return

        kanal = interaction.guild.get_channel(SIPARIS_KANAL_ID)
        if not kanal:
            await interaction.response.send_message(
                "❌ Sipariş kanalı bulunamadı.",
                ephemeral=True
            )
            return

        await kanal.send(
            "🛒 **Yeni Galeri Siparişi**\n\n"
            f"👤 **Siparişi Veren:** {interaction.user.mention}\n"
            f"📞 **Telefon:** `{telefon}`\n"
            f"💰 **Alınacak Fiyat:** `{fiyat:,}$`"
        )

        await interaction.response.send_message(
            "✅ Sipariş galeriye iletildi.",
            ephemeral=True
        )

    else:
        await interaction.response.send_message(
            "❌ Geçersiz işlem.\n`ekle / temizle / sipariş`",
            ephemeral=True
        )

# ---------------- GALERİ İLAN (KANALLARDAN OKUR) ----------------
@bot.tree.command(name="galeri_ilan", description="Galerideki araçları listeler")
async def galeri_ilan(interaction: discord.Interaction):

    ilan = "🚘 **Karty Galeri** 🚘\n**Öne Çıkan Araçlar:**\n\n"

    for kanal_id in GALERI_KANALLARI:
        kanal = bot.get_channel(kanal_id)
        if not kanal:
            continue

        async for msg in kanal.history(limit=3):
            if msg.content:
                ilan += f"• {msg.content}\n"

    ilan += "\n📍 Detaylı bilgi için iletişime geçin!"
    await interaction.response.send_message(ilan)

# ---------------- VARLIK ----------------
@bot.tree.command(name="varlık", description="Çetenin elindeki varlıkları gösterir")
async def varlik(interaction: discord.Interaction):

    kanal = bot.get_channel(VARLIK_KANAL_ID)
    if not kanal:
        await interaction.response.send_message("Varlık bilgisi bulunamadı.")
        return

    mesajlar = [msg.content async for msg in kanal.history(limit=10) if msg.content]

    if not mesajlar:
        await interaction.response.send_message("Varlık bilgisi yok.")
        return

    await interaction.response.send_message(
        "**Çete Varlıkları:**\n" + "\n".join(reversed(mesajlar))
    )

# ---------------- YIKAMA ----------------
@bot.tree.command(name="yıkama", description="Yıkama hesaplama (1/80)")
@app_commands.describe(miktar="Yıkanacak para miktarı")
async def yikama(interaction: discord.Interaction, miktar: int):
    sonuc = miktar // 80
    await interaction.response.send_message(
        f"🧼 **Yıkama Hesaplaması**\n\n"
        f"💰 Girilen: `{miktar:,}$`\n"
        f"📉 Sonuç (1/80): `{sonuc:,}$`",
        ephemeral=True
    )

# -------- TOKEN --------
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise Exception("TOKEN bulunamadı!")

bot.run(TOKEN)
