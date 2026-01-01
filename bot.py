import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    activity=discord.Game(name="FiveM | Karty Bot")
)

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

# ---------------- BAŞLAT ----------------
from config import TOKEN
bot.run(TOKEN)
