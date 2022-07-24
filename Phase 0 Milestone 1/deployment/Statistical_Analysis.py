import streamlit as st
import numpy as np

def app ():
    st.title ('Statistical Analysis')
    st.write ('This is Page For Statistical Analysis Dashboard')

    st.header ('Sample Case')
    st.subheader ('Explanation Will Be in Indonesian')
    st.write ('''Anggaplah politisi tersebut memutuskan untuk menggunakan Google Ads jenis IMAGE
    karena dirasa biaya yang dikeluarkan relatif lebih murah dibandingkan dengan Google Ads jenis yang lain.
    Namun untuk meningkatkan kampanye, politisi tersebut merasa jika menggunakan Google Ads jenis IMAGE saja tidak cukup,
    maka dari itu sang politisi memutuskan untuk menambah menggunkan Google Ads jenis yang lain. Sebagai seorang data science di tim sukses,
    kita diminta menentukan Google Ads apakah yang akan dipakai untuk meningkatkan kampanye.''')

    st.header ('Descriptive Statistics')
    st.subheader ('Explanation Will Be in Indonesian')
    st.write ('Analisa Central Tendency')
    st.write ('''Untuk Mengetahui Google Ads Apa Yang Akan Dipakai Nantinya,
    Ada Baiknya Kita Mengetahui Rata - Rata Biaya an Rata - Rata Biaya Per Hari Untuk Google Ads Jenis VIDEO & IMAGE 
    ''')
    st.image ('centraltendency.png')
    st.write ('KESIMPULAN : ')
    st.write ('Rata - rata biaya untuk setiap jenis TEXT lebih murah daripada VIDEO')
    st.write ('Rata - rata biaya yang dikeluarkan per hari untuk VIDEO lebih murah daripada TEXT')
    st.write ('''Dari sini kita bisa melihat bahwa ads jenis TEXT lebih banyak daripada ads jenis VIDEO karena 
    biarpun rata - rata biaya jenis TEXT lebih murah tetapi biaya yang dikeluarkan per hari untuk ads jenis TEXT lebih besar daripada ads jenis VIDEO''')

    st.header ('Inferential Statistics')
    st.subheader ('Explanation Will Be in Indonesian')
    st.write ('Hipotesis Testing - Two Samples Independent Two Tailed Hypothesis Testing')
    st.write ('Untuk Mengecek Apakah Rata - Rata Biaya Yang Dikeluarkan / Hari Untuk Jenis Iklan VIDEO & TEXT Berbeda Secara Signifikan Atau Tidak')
    st.write ('Hipotesis Kita Dalam Kasus Ini: ')
    st.write ('H0: μ_video = μ_text')
    st.write ('H1: μ_video != μ_text')
    st.image ('hipotesistesting.png')
    st.write ('KESIMPULAN : ')
    st.write ('Berdasarkan hasil di atas, kita dapat menyimpulkan bahwa kita gagal untuk merejek H0 / hipotesis nol di mana di antara VIDEO dan TEXT tidak berbeda secara signifikan dalam hal rata - rata biaya per hari')

    st.header ('Rate This Page')
    st.select_slider('Anwer', ['Awesome', 'Outstanding', 'Magnificent'])

    if st.button('Submit'):
        st.write('Thanks For Rating')
