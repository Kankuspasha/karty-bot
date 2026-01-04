import os
import discord
from discord.ext import commands
from discord import app_commands
import math

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


# ---------------- Yıkama ----------------

@bot.tree.command(name="yıkama", description="Yıkama hesaplama (1/80)")
@app_commands.describe(miktar="Yıkanacak para miktarı")
async def yikama(interaction: discord.Interaction, miktar: int):

    sonuc = miktar // 80

    await interaction.response.send_message(
        f"🧼 **Yıkama Hesaplaması**\n\n"
        f"💰 Girilen miktar: `{miktar:,}$`\n"
        f"📉 Yıkama sonucu (1/80): `{sonuc:,}$`",
        ephemeral=True
    )

# ---------------- Galeri2v ----------------

    # 🔹 GALERİ EKLE
    if islem.lower() == "ekle":
        if not arac or not fiyat:
            await interaction.response.send_message(
                "❌ Kullanım: `/galeri ekle AraçAdı Fiyat`",
                ephemeral=True
            )
            return

        galeri_ilanlari.append(f"🚗 **{arac}** — 💰 `{fiyat:,}$`")

        await interaction.response.send_message(
            "✅ Araç galeriye eklendi.",
            ephemeral=True
        )

    # 🔹 GALERİ TEMİZLE
    elif islem.lower() == "temizle":
        galeri_ilanlari.clear()
        await interaction.response.send_message(
            "🧹 Tüm galeri ilanları temizlendi.",
            ephemeral=True
        )

    # 🔹 GALERİ SİPARİŞ
    elif islem.lower() == "sipariş":
        if not telefon or not fiyat:
            await interaction.response.send_message(
                "❌ Kullanım: `/galeri sipariş TelefonNumarası Fiyat`",
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
            "✅ Siparişiniz galeriye iletildi.",
            ephemeral=True
        )

    else:
        await interaction.response.send_message(
            "❌ Geçersiz işlem.\nKullanım: `ekle / temizle / sipariş`",
            ephemeral=True
        )

BASVURU_KATEGORI_ID = 1457177637356044349
LOG_KANAL_ID = 1457177708478861342

ONAY_ROLLERI = [
    1456071388493381675,
    1456088696444158088
]

GORUCU_ROLLER = [
    1456071388493381675,
    1456088696444158088,
    1456999721355841744
]

VERILECEK_ROL = 1456090311834206370


# ---------- BUTON ----------
class BasvuruView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Başvuru Oluştur", style=discord.ButtonStyle.green, emoji="🧾")
    async def basvuru(self, interaction: discord.Interaction, button: discord.ui.Button):

        guild = interaction.guild
        user = interaction.user
        kategori = guild.get_channel(BASVURU_KATEGORI_ID)

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            user: discord.PermissionOverwrite(view_channel=True, send_messages=True)
        }

        for rid in GORUCU_ROLLER:
            role = guild.get_role(rid)
            if role:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True)

        kanal = await guild.create_text_channel(
            name=f"basvuru-{user.name}",
            category=kategori,
            overwrites=overwrites
        )

        mesaj = await kanal.send(
            "**🧾 Aile Başvuru Formu**\n\n"
            "Fivem saati:\n"
            "Aile geçmişi var mı:\n"
            "Yetenekleri:\n"
            "Silah kullanmayı biliyor musun:\n"
        )
        await mesaj.add_reaction("✅")

        log = guild.get_channel(LOG_KANAL_ID)
        if log:
            await log.send(f"📥 **Yeni başvuru:** {user.mention} | {kanal.mention}")

        await interaction.response.send_message(
            f"Başvurun oluşturuldu: {kanal.mention}",
            ephemeral=True
        )


# ---------- BOT HAZIR ----------
@bot.event
async def on_ready():
    bot.add_view(BasvuruView())
    print("Karty Bot aktif.")


# ---------- ONAY ----------
@bot.event
async def on_raw_reaction_add(payload):

    if str(payload.emoji) != "✅":
        return

    guild = bot.get_guild(payload.guild_id)
    channel = guild.get_channel(payload.channel_id)
    member = guild.get_member(payload.user_id)

    if not member or member.bot:
        return

    if not any(r.id in ONAY_ROLLERI for r in member.roles):
        return

    basvuran = next((m for m in channel.members if not m.bot and m != member), None)
    if not basvuran:
        return

    rol = guild.get_role(VERILECEK_ROL)
    if rol:
        await basvuran.add_roles(rol)
        await channel.send(f"✅ {basvuran.mention} **başvurusu onaylandı.**")        

# -------- TOKEN --------
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise Exception("TOKEN bulunamadı!")

bot.run(TOKEN)
