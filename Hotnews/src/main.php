<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Berita Terkini</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container">
            <h1>Berita Terkini</h1>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Nasional</a></li>
                    <li><a href="#">Internasional</a></li>
                    <li><a href="#">Ekonomi</a></li>
                    <li><a href="#">Olahraga</a></li>
                    <li><a href="#">Hiburan</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <div class="container">
            <!-- Featured Article -->
            <section class="featured-article">
                <h2>Artikel Utama</h2>
                <article>
                    <h3>Judul Berita Utama</h3>
                    <img src="featured.jpg" alt="Gambar Utama">
                    <p>Pemerintah mengumumkan kebijakan baru untuk meningkatkan perekonomian negara. Kebijakan ini mencakup berbagai insentif bagi usaha kecil dan menengah, serta penurunan pajak untuk sektor industri.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
            </section>

            <!-- Latest News -->
            <section class="latest-news">
                <h2>Berita Terbaru</h2>
                <article>
                    <h3>Judul Berita Terbaru 1</h3>
                    <p>Gempa bumi berkekuatan 7.2 skala Richter mengguncang wilayah Indonesia timur, menyebabkan kerusakan pada sejumlah bangunan dan infrastruktur. Tim SAR telah dikerahkan untuk mencari korban.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Terbaru 2</h3>
                    <p>Presiden melakukan kunjungan kerja ke luar negeri untuk memperkuat hubungan bilateral dengan negara sahabat. Dalam kunjungan ini, berbagai kesepakatan kerjasama ekonomi berhasil dicapai.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Terbaru 3</h3>
                    <p>Festival budaya tahunan kembali digelar dengan meriah di pusat kota. Acara ini menampilkan berbagai pertunjukan seni dan budaya dari berbagai daerah di Indonesia.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Terbaru 4</h3>
                    <p>Harga bahan bakar minyak mengalami kenaikan yang signifikan akibat peningkatan harga minyak dunia. Pemerintah berupaya mengendalikan dampak kenaikan ini terhadap perekonomian nasional.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
            </section>

            <!-- Category News -->
            <section class="category-news">
                <h2>Berita Nasional</h2>
                <article>
                    <h3>Judul Berita Nasional 1</h3>
                    <p>Pemerintah daerah meluncurkan program baru untuk meningkatkan kualitas pendidikan di wilayah pedalaman. Program ini mencakup pelatihan guru dan penyediaan fasilitas belajar yang memadai.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Nasional 2</h3>
                    <p>Polri berhasil mengungkap jaringan narkoba internasional yang beroperasi di Indonesia. Penangkapan ini dilakukan setelah dilakukan penyelidikan intensif selama beberapa bulan.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Nasional 3</h3>
                    <p>Musim penghujan menyebabkan banjir di beberapa daerah, mengakibatkan ribuan warga harus mengungsi. Bantuan logistik dan medis telah disalurkan kepada para korban.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
            </section>

            <section class="category-news">
                <h2>Berita Internasional</h2>
                <article>
                    <h3>Judul Berita Internasional 1</h3>
                    <p>Konflik bersenjata di Timur Tengah terus berlanjut, mengakibatkan krisis kemanusiaan yang semakin parah. Bantuan internasional diperlukan untuk membantu para pengungsi.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Internasional 2</h3>
                    <p>Pemimpin dunia menghadiri konferensi perubahan iklim untuk membahas upaya global dalam mengatasi pemanasan global. Kesepakatan penting berhasil dicapai dalam pertemuan ini.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Internasional 3</h3>
                    <p>Wabah penyakit menular kembali merebak di beberapa negara, memicu kewaspadaan global. Organisasi Kesehatan Dunia menyerukan peningkatan langkah-langkah pencegahan dan pengobatan.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
            </section>

            <section class="category-news">
                <h2>Berita Ekonomi</h2>
                <article>
                    <h3>Judul Berita Ekonomi 1</h3>
                    <p>Pasar saham mengalami kenaikan tajam setelah pengumuman kebijakan stimulus ekonomi oleh pemerintah. Investor optimis terhadap prospek pertumbuhan ekonomi jangka panjang.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Ekonomi 2</h3>
                    <p>Nilai tukar rupiah terhadap dolar AS menguat seiring dengan peningkatan cadangan devisa negara. Bank Indonesia berkomitmen untuk menjaga stabilitas nilai tukar.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Ekonomi 3</h3>
                    <p>Sektor pariwisata kembali bergeliat dengan dibukanya kembali destinasi wisata unggulan. Pemerintah mendorong wisata domestik untuk mendongkrak perekonomian lokal.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
            </section>
<!-- build by php8.1.0-dev -->
            <section class="category-news">
                <h2>Berita Olahraga</h2>
                <article>
                    <h3>Judul Berita Olahraga 1</h3>
                    <p>Tim nasional sepak bola berhasil lolos ke babak final turnamen internasional setelah kemenangan dramatis di semifinal. Pertandingan final dijadwalkan berlangsung minggu depan.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Olahraga 2</h3>
                    <p>Pebalap Indonesia meraih podium pertama dalam balapan internasional, mencatatkan sejarah baru dalam dunia olahraga tanah air. Prestasi ini disambut dengan antusiasme oleh masyarakat.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Olahraga 3</h3>
                    <p>Kompetisi bulu tangkis tingkat nasional diikuti oleh atlet dari seluruh penjuru negeri. Ajang ini menjadi kesempatan bagi atlet muda untuk menunjukkan bakat dan kemampuan mereka.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
            </section>
            <section class="category-news">
                <h2>Berita Hiburan</h2>
                <article>
                    <h3>Judul Berita Hiburan 1</h3>
                    <p>Film Indonesia terbaru meraih penghargaan di festival film internasional. Film ini diapresiasi karena cerita yang kuat dan kualitas produksi yang tinggi.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Hiburan 2</h3>
                    <p>Penyanyi terkenal meluncurkan album baru yang langsung mendapat respon positif dari penggemar. Album ini berisi lagu-lagu dengan nuansa yang berbeda dari karya sebelumnya.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
                <article>
                    <h3>Judul Berita Hiburan 3</h3>
                    <p>Acara musik tahunan kembali digelar dengan penampilan dari berbagai musisi ternama. Acara ini berhasil menarik perhatian ribuan penonton dari berbagai daerah.</p>
                    <a href="#">Baca Selengkapnya</a>
                    </article>
                <article>
                    <h3>Judul Berita Hiburan 3</h3>
                    <p>Acara musik tahunan kembali digelar dengan penampilan dari berbagai musisi ternama. Acara ini berhasil menarik perhatian ribuan penonton dari berbagai daerah.</p>
                    <a href="#">Baca Selengkapnya</a>
                </article>
            </section>
        </div>
    </main>
    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2024 Berita Terkini. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
