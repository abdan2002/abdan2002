import streamlit as st
from streamlit_option_menu import option_menu
import math
from math import pi
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

with st.sidebar :
    selected = option_menu ("Kalkulator Penghitung LOW FREQUENCY RESPONSE BJT AMPLIFIER dan ANALISIS DC",
    ["Home",
    "Rangkaian Low Frequency Response-BJT Amplifier",],
    default_index=0)

if(selected == "Home") :
    st.header("Kalkuator Perhitungan LOW FREQUENCY RESPONSE BJT AMPLIFIER dan ANALISIS DC")
    st.subheader("By Abdan Reza Raihan (11-2021-006) dari ITENAS Program Studi Teknik Elektro")
    st.write("Program ini dibuat untuk memenuhi Tugas Besar Elektronika Analog\nDosen Pengampu : Ir. Rustamaji M.T")
   

if(selected == "Rangkaian Low Frequency Response-BJT Amplifier") :
    st.title("Contoh Rangkaian Low Frequency Response-BJT Amplifier")
    st.image("IMG-20230624-WA0011.jpg", width = 500)
    st.subheader("Perhitungan Rangkaian Low Frequency Response-BJT Amplifier dan Analisis DC")

    Vcc = st.number_input("Masukkan Nilai Vcc (Volt)")
    vi = st.number_input("Masukkan Nilai Vin (Volt)")
    f = st.number_input("Masukkan Nilai Frekuensi Tegangan Input (Hz)")
    B = st.number_input("Masukkan Nilai β ")
    Cs = st.number_input("Masukkan Nilai Cs (μF)")
    Ce = st.number_input("Masukkan Nilai Ce (μF)")
    Cc = st.number_input("Masukkan Nilai Cc (μF)")
    R1 = st.number_input("Masukkan Nilai R1 (Ω)")
    R2 = st.number_input("Masukkan Nilai R2 (Ω)")
    Re = st.number_input("Masukkan Nilai Re (Ω)")
    Rc = st.number_input("Masukkan Nilai Rc (Ω)")
    Rl = st.number_input("Masukkan Nilai Rl (Ω)") 
    tr = st.selectbox("Transistor" , ['ideal','Silikon' , 'Germanium'])

    if tr == 'ideal':
        hitung = st.button("Hitung Nilai Respon Frekuensi")
    
        if hitung:
            Vb = (R2 * Vcc) / (R2 + R1)
            Ie = Vb / Re
            re = (26 * (10 ** -3)) / Ie
            Bre = B * re
            R = (Rc * Rl) / (Rc + Rl)
            Av = (-1 * R) / re
            Ri1 = (R1 * R2) / (R1 + R2)
            Ri = (Ri1 * Bre) / (Ri1 + Bre)
            Rp = (R1 * R2) / (R1 + R2)
            Rq = (Rp / B) + re
            Ra = (Re * Rq) / (Re + Rq)
            vo = Av * vi
            fls = 1 / (2 * pi * Ri * (Cs * (10 ** -6)))
            flc = 1 / (2 * pi * (Rc + Rl) * (Cc * (10 ** -6)))
            fle = 1 / (2 * pi * Ra * (Ce * (10 ** -6)))
            st.success(f"Nilai VB  adalah = {Vb} Volt")
            st.success(f"Nilai IE  adalah = {Ie} Ampere")
            st.success(f"Nilai penguatannya (Av) adalah = {Av}")
            st.success(f"Nilai Vout adalah = {vo} Volt ")
            st.success(f"Nilai Frekuensi Cut-off yang ditentukan oleh Cs (fLs) adalah = {fls} Hz")
            st.success(f"Nilai Frekuensi Cut-off yang ditentukan oleh Cc (fLc) adalah = {flc} Hz")
            st.success(f"Nilai Frekuensi Cut-Off yang ditentukan oleh Ce (fLe) adalah = {fle} Hz")
            
            def sinusoidal():
                t = np.linspace(-0.05, 0.05, 1000)
                phase_shift = 180  # Phase shift in degrees
            
                # Calculate the sinusoidal signals
                hasil_Vi = vi * np.sin(2 * np.pi * f * t + np.deg2rad(phase_shift))
                hasil_Vo = -1 * Av * vi * np.sin(2 * np.pi * f * t )

                if hitung:
                    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                    ax1.plot(t, hasil_Vi)
                    ax1.set_xlabel('Waktu (s)')
                    ax1.set_ylabel('Amplitudo (V)')
                    ax1.set_title('Sinyal Vi')
                    ax1.grid(True)
                    ax1.set_xlim(-0.05,0.05)

                    ax2.plot(t, hasil_Vo)
                    ax2.set_xlabel('Waktu (s)')
                    ax2.set_ylabel('Amplitudo (V)')
                    ax2.set_title('Sinyal Vo')
                    ax2.grid(True)
                    ax2.set_xlim(-0.05,0.05)

                    plt.xlim(-0.05, 0.05)
                    plt.tight_layout()
                    st.pyplot(fig)

            sinusoidal()

    if tr == 'Silikon':
        hitung = st.button("Hitung Nilai Respon Frekuensi")
    
        if hitung:
            Vb = (R2 * Vcc) / (R2 + R1)
            Ie = (Vb - 0.7) / Re
            re = (26 * (10 ** -3)) / Ie
            Bre = B * re
            R = (Rc * Rl) / (Rc + Rl)
            Av = (-1 * R) / re
            Ri1 = (R1 * R2) / (R1 + R2)
            Ri = (Ri1 * Bre) / (Ri1 + Bre)
            Rp = (R1 * R2) / (R1 + R2)
            Rq = (Rp / B) + re
            Ra = (Re * Rq) / (Re + Rq)
            vo = Av * vi
            fls = 1 / (2 * pi * Ri * (Cs * (10 ** -6)))
            flc = 1 / (2 * pi * (Rc + Rl) * (Cc * (10 ** -6)))
            fle = 1 / (2 * pi * Ra * (Ce * (10 ** -6)))
            st.success(f"Nilai VB  adalah = {Vb} Volt")
            st.success(f"Nilai IE  adalah = {Ie} Ampere")
            st.success(f"Nilai penguatannya (Av) adalah = {Av}")
            st.success(f"Nilai Vout adalah = {vo} Volt ")
            st.success(f"Nilai Frekuensi Cut-off yang ditentukan oleh Cs (fLs) adalah = {fls} Hz")
            st.success(f"Nilai Frekuensi Cut-off yang ditentukan oleh Cc (fLc) adalah = {flc} Hz")
            st.success(f"Nilai Frekuensi Cut-Off yang ditentukan oleh Ce (fLe) adalah = {fle} Hz")

            def sinusoidal():
                t = np.linspace(-0.05, 0.05, 1000)
                phase_shift = 180  # Phase shift in degrees
            
                # Calculate the sinusoidal signals
                hasil_Vi = vi * np.sin(2 * np.pi * f * t + np.deg2rad(phase_shift))
                hasil_Vo = -1 * Av * vi * np.sin(2 * np.pi * f * t )

                if hitung:
                    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                    ax1.plot(t, hasil_Vi)
                    ax1.set_xlabel('Waktu (s)')
                    ax1.set_ylabel('Amplitudo (V)')
                    ax1.set_title('Sinyal Vi')
                    ax1.grid(True)
                    ax1.set_xlim(-0.05,0.05)

                    ax2.plot(t, hasil_Vo)
                    ax2.set_xlabel('Waktu (s)')
                    ax2.set_ylabel('Amplitudo (V)')
                    ax2.set_title('Sinyal Vo')
                    ax2.grid(True)
                    ax2.set_xlim(-0.05,0.05)

                    plt.xlim(-0.05, 0.05)
                    plt.tight_layout()
                    st.pyplot(fig)

            sinusoidal()
    

    elif tr == 'Germanium':
        hitung = st.button("Hitung nilai Respon Frekuensi")   

        if hitung :
            Vb = (R2 * Vcc) / (R2 + R1)
            Ie = (Vb - 0.3) / Re
            re = (26 * (10 ** -3)) / Ie
            Bre = B * re
            R = (Rc * Rl) / (Rc + Rl)
            Av = (-1 * R) / re 
            Ri1 = (R1 * R2) / (R1 + R2)
            Ri = (Ri1 * Bre) / (Ri1 + Bre)
            Rp = (R1 * R2) / (R1 + R2)
            Rq = (Rp / B) + re
            Ra = (Re * Rq) / (Re + Rq)
            vo = Av * vi
            fls = 1 / (2 * pi * Ri * (Cs * (10 ** -6)))
            flc = 1 / (2 * pi * (Rc + Rl) * (Cc * (10 ** -6)))
            fle = 1 / (2 * pi * Ra * (Ce * (10 ** -6)))
            st.success(f"Nilai VB  adalah = {Vb} Volt")
            st.success(f"Nilai IE  adalah = {Ie} Ampere")
            st.success(f"Nilai penguatannya (Av) adalah = {Av}")
            st.success(f"Nilai Vout adalah = {vo} Volt ")
            st.success(f"Nilai Frekuensi Cut-off yang ditentukan oleh Cs (fLs) adalah = {fls} Hz")
            st.success(f"Nilai Frekuensi Cut-off yang ditentukan oleh Cc (fLc) adalah = {flc} Hz")
            st.success(f"Nilai Frekuensi Cut-Off yang ditentukan oleh Ce (fLe) adalah = {fle} Hz")

            def sinusoidal():
                t = np.linspace(-0.05, 0.05, 1000)
                phase_shift = 180  # Phase shift in degrees
            
                # Calculate the sinusoidal signals
                hasil_Vi = vi * np.sin(2 * np.pi * f * t + np.deg2rad(phase_shift))
                hasil_Vo = -1 * Av * vi * np.sin(2 * np.pi * f * t )

                if hitung:
                    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                    ax1.plot(t, hasil_Vi)
                    ax1.set_xlabel('Waktu (s)')
                    ax1.set_ylabel('Amplitudo (V)')
                    ax1.set_title('Sinyal Vi')
                    ax1.grid(True)
                    ax1.set_xlim(-0.05,0.05)

                    ax2.plot(t, hasil_Vo)
                    ax2.set_xlabel('Waktu (s)')
                    ax2.set_ylabel('Amplitudo (V)')
                    ax2.set_title('Sinyal Vo')
                    ax2.grid(True)
                    ax2.set_xlim(-0.05,0.05)

                    plt.xlim(-0.05, 0.05)
                    plt.tight_layout()
                    st.pyplot(fig)

            sinusoidal()
