# -*- coding: utf-8 -*-
#
# Pastikan Anda telah menginstal library 'rich': pip install rich
# Library ini digunakan untuk membuat tampilan konsol yang jauh lebih menarik dan profesional.

from typing import Final
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Inisialisasi objek Console dari 'rich'
# Objek ini akan menangani semua pencetakan berformat
console = Console()

# --- DATA NARASI ---
# Cerita disimpan dalam string multi-baris (triple quotes)
FULL_STORY_TEXT: Final[str] = """
Malam itu, hawa dingin menggigit seperti pengkhianatan. Aku sudah tersandung mengelilingi 
blok apartemen ini entah sudah berapa kali—sebuah kebiasaan bodoh yang kumulai sejak kau 
pergi. Kaki-kaki ini mendambakan kilasanmu, sementara mereka hanya menemukan keheningan. 
Kau melewatkan setiap panggilan yang kucoba—bukan karena kau tidak mendengarnya, tapi 
karena kau sudah memutuskan frekuensiku.
Maka, selesai. Sekarang aku menyerah.

Sebuah patah hati di pertengahan Desember—seberapa ironisnya, ketika seharusnya ini adalah 
musim untuk kehangatan. Kau tahu, bagian yang paling menyayat adalah menyadari: kau tidak 
peduli sedikit pun. Dalam hidupmu yang baru, yang bergerak maju tanpa celah, aku tahu 
kau tidak akan pernah mengingatku.

Di suatu tempat, jauh dari sini, aku membayangkanmu. Kau pasti tengah menarik celana jinnya, 
terserap dalam keramaian kota besar yang kau dambakan—tempat yang selalu kita bicarakan, 
tapi kau capai tanpa aku.

Sementara itu, aku terpaku. Aku memandang ke luar jendela kecil kita, mengamati semua mobil 
berlalu seperti waktu yang tak bisa kuraih kembali. Aku bertanya-tanya, apakah aku akan 
pernah mengejar impian yang dulu kita susun bersama? Melihat cakrawala yang luas atau senja 
di ujung negeri? Atau akankah aku mati dalam kedinginan ini, merasa biru dan sendirian?
Aku sering bertanya, akankah suatu hari, suara ini, pengakuan yang kutuangkan dalam melodi 
sepi, akan sampai ke telingamu, diputar di stereo-mu?

Aku sungguh berharap, kau mendapatkan segala yang kau impikan. Lantai dansa yang gemerlap, 
rumah sempurna dengan pintu merah mawar—lambang dari kestabilan dan kebahagiaan yang tak 
bisa kuberikan. Aku tahu pasti, aku hanyalah hal terakhir yang akan kau ingat. Sebab, 
ini telah menjadi Desember yang panjang dan sepi bagiku.

Jika saja aku bisa memutar waktu.
Aku berharap aku tahu bahwa 'kurang itu lebih'. Bahwa cinta tidak perlu selalu mendesak. 
Tapi aku, yang terlalu rapuh, berakhir dengan terkapar di lantai karena keracunan oleh 
diri sendiri. Dan itu adalah hal terakhir yang kuingat dari malam-malam tanpa kamu. 
Desember yang panjang, sepi, dan menghapuskan memori.

Kau dengan mudah menyingkirkanku, untuk menunjukkan dirimu dalam cahaya yang lebih baik—
sebagai seseorang yang akhirnya membuat pilihan yang benar. Kau muncul dari perpisahan ini 
dengan baik-baik saja, seolah ini hanya pergantian bab. Sementara aku, aku keluar meratap, 
nyaris tidak bernapas, sebuah jiwa yang compang-camping.
Aku yakin kau akan menggandeng tangannya. Dan dengan kepahitan yang bercampur harapan tulus, 
aku berdoa semoga dia lebih baik dari yang pernah kulakukan.

Kesalahanku hanyalah kebodohan, bukan niat jahat. Dan ini adalah daftar pengakuanku yang 
tak bisa kusampaikan secara langsung—pengakuan yang kini membebani udara di sekitarku. 
Aku tahu, secara filosofis:
Rasa sakit tidak pernah permanen, tapi malam ini, rasa sakit itu membunuhku.
Aku merindukan wajahmu. Kau ada di kepalaku, sebuah rekaman yang tak henti diputar. 
Ada begitu banyak hal yang seharusnya kukatakan saat kita masih punya waktu. Setahun 
penderitaan, sebuah pelajaran yang sangat pahit.

Pergilah, dan dapatkan lantai dansamu. Dapatkan rumah berdaun pintu merah mawar itu.
Aku akan tetap di sini, bayangan di bulan Desember, menjadi kenangan terakhir yang terlupakan.

Desember ini—selalu Desember yang panjang dan sepi.
"""

def create_title_panel() -> Panel:
    """Membuat panel untuk judul dengan gaya menarik."""
    title_text = Text(
        "Desember yang Panjang dan Sepi", 
        style="bold white on blue", 
        justify="center"
    )
    return Panel(
        title_text, 
        border_style="bold blue",
        padding=(1, 2)
    )

def create_story_panel(story: str) -> Panel:
    """Membuat panel untuk konten cerita dengan gaya melankolis."""
    # Mengubah teks cerita menjadi objek Text
    story_text = Text(story, style="italic dim white on black")
    
    # Menemukan dan memberi warna khusus pada beberapa kata kunci yang menonjol
    # Contoh: 'Desember' diberi warna merah muda (magenta)
    story_text.highlight_regex(r"Desember", "bold magenta")
    story_text.highlight_regex(r"patah hati|kedinginan|sendirian|keracunan", "red")
    
    return Panel(
        story_text,
        title="[yellow]Surat Pengakuan di Malam Dingin[/yellow]",
        border_style="dim yellow",
        padding=(2, 4)
    )

def main():
    """Fungsi utama untuk menjalankan program dan menampilkan narasi."""
    try:
        # 1. Tampilkan Judul Utama
        console.print(create_title_panel(), justify="center")
        console.print("\n")
        
        # 2. Tampilkan Panel Cerita
        story_panel = create_story_panel(FULL_STORY_TEXT)
        console.print(story_panel, justify="center")
        
        console.print("\n")
        # 3. Tampilkan Pesan Penutup
        console.print("[bold green]-- Narasi Berhasil Ditampilkan dengan Gaya Profesional --[/bold green]", justify="center")
        
    except Exception as e:
        console.print(f"[bold red]TERJADI KESALAHAN:[/bold red] Pastikan Anda telah menginstal 'rich'. Detail: {e}")

if __name__ == "__main__":
    main()