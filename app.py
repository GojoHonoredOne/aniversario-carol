import streamlit as st
import os
import sqlite3
from datetime import datetime

# ==========================================
# 1. BANCO DE DADOS (SQLite Avançado)
# ==========================================
DB_NAME = "festa.db"

def init_db():
    """Cria o banco de dados e as tabelas se não existirem"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Tabela de Presença
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS presenca (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            status TEXT NOT NULL,
            bebida TEXT,
            data_envio TEXT
        )
    """)
    
    # Tabela do Mural de Recados
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mural (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            texto TEXT NOT NULL,
            data_envio TEXT
        )
    """)
    
    # Tabela de Músicas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            musica TEXT NOT NULL,
            artista TEXT NOT NULL,
            sugerido_por TEXT
        )
    """)
    
    conn.commit()
    conn.close()

init_db()

# ==========================================
# 2. CONFIGURAÇÃO VISUAL (Contraste e Legibilidade)
# ==========================================
st.set_page_config(
    page_title="Aniversário da Carol 🎉",
    page_icon="🐕",
    layout="centered"
)

# Estilização focada em leitura fácil para a família
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a0033 0%, #2e004d 40%, #4a0080 100%);
    }
    .titulo-principal {
        color: #ffcc00;
        text-align: center;
        font-size: 2.8rem;
        font-weight: 900;
        margin-bottom: 5px;
        text-shadow: 3px 3px 12px rgba(255, 204, 0, 0.4);
        font-family: 'Arial Black', Gadget, sans-serif;
    }
    .subtitulo {
        color: #ffffff;
        text-align: center;
        font-size: 1.3rem;
        line-height: 1.6;
        background-color: rgba(74, 0, 128, 0.6);
        padding: 22px;
        border-radius: 20px;
        border: 2px solid #6600cc;
        margin-bottom: 35px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    .card-festa {
        background-color: rgba(255, 255, 255, 0.98);
        padding: 35px;
        border-radius: 25px;
        box-shadow: 0 20px 45px rgba(0,0,0,0.4);
        border: 4px solid #6600cc;
        margin-bottom: 30px;
    }
    .info-titulo {
        color: #2e004d;
        text-align: center;
        margin-top: 0;
        font-weight: 800;
        font-size: 1.6rem;
        border-bottom: 2px solid #e6ccff;
        padding-bottom: 10px;
    }
    .detalhe-linha {
        font-size: 1.25rem;
        color: #1a0033;
        margin-bottom: 18px;
    }
    .alerta-peruca {
        font-size: 1.4rem;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        background: linear-gradient(45deg, #6600cc, #9933ff);
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(102, 0, 204, 0.4);
        margin: 25px 0;
    }
    .card-salsicha {
        background-color: #f3ebff;
        padding: 18px;
        border-radius: 15px;
        border-left: 6px solid #4a0080;
        color: #1a0033;
        font-size: 1.1rem;
        text-align: center;
    }
    .texto-final {
        font-size: 2.1rem;
        font-weight: bold;
        color: #ffcc00;
        text-align: center;
        margin-top: 45px;
        margin-bottom: 25px;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.6);
    }
    
    /* GLOBAIS DE FORMULÁRIO (Garante cor branca nos textos e labels) */
    h2, h3 {
        color: #ffcc00 !important;
        font-weight: 700 !important;
    }
    label {
        color: #ffffff !important;
        font-size: 1.15rem !important;
        font-weight: bold !important;
    }
    p {
        color: #ffffff;
    }
    
    /* Botão Principal de Entrada */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #7b2cbf, #9d4edd);
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
        padding: 15px 45px;
        border-radius: 50px;
        border: 3px solid #ffcc00;
        box-shadow: 0 10px 30px rgba(157, 78, 221, 0.6);
        transition: all 0.3s ease;
        display: block;
        margin: 40px auto;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Nova data atualizada da festa: 26 de Julho de 2026 às 15:30
DATA_DO_ANIVERSARIO = datetime(2026, 7, 26, 15, 30)

# ==========================================
# 3. CONTROLE DE ESTADO DA INTERFACE
# ==========================================
if 'convite_aberto' not in st.session_state:
    st.session_state.convite_aberto = False

# --- TELA INICIAL ---
st.markdown('<h1 class="titulo-principal">🎉 CONVITE ESPECIAL 🎉</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitulo">Você foi convidado para comemorar o aniversário '
    'da pessoa mais linda, memorável e apaixonada por salsichas: <b>Ana Carol</b>! 👑💜</p>', 
    unsafe_allow_html=True
)

if not st.session_state.convite_aberto:
    if st.button("Abrir convite especial... 🎫"):
        st.session_state.convite_aberto = True
        st.rerun()

# --- TELA DO CONVITE ABERTO ---
if st.session_state.convite_aberto:
    st.balloons()
    
    # CARD 1: Detalhes Fundamentais Atualizados
    st.markdown('<div class="card-festa">', unsafe_allow_html=True)
    st.markdown('<h2 class="info-titulo">🗓️ INFORMAÇÕES DA FESTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="detalhe-linha">📅 <b>Quando:</b> Domingo, 26 de Julho de 2026</p>', unsafe_allow_html=True)
    st.markdown('<p class="detalhe-linha">⏰ <b>Horário:</b> A partir das 15h30</p>', unsafe_allow_html=True)
    st.markdown('<p class="detalhe-linha">📍 <b>Local:</b> Raul bispo dos santos, 311</p>', unsafe_allow_html=True)
    st.markdown('<div class="alerta-peruca">🎭 DRESS CODE: De peruca, claro que sim! 🎭</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="card-salsicha">🐕 Todo mundo bem alegre e de peruca para deixar a comemoração da Carol ainda mais divertida! 🐾</div>', 
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # CARD 2: Cronômetro Atualizado
    agora = datetime.now()
    if DATA_DO_ANIVERSARIO > agora:
        faltam = DATA_DO_ANIVERSARIO - agora
        col1, col2, col3 = st.columns(3)
        col1.metric("Dias Corridos", faltam.days)
        col2.metric("Horas Restantes", faltam.seconds // 3600)
        col3.metric("Minutos Finais", (faltam.seconds % 3600) // 60)
    else:
        st.success("🔥 A FESTA COMEÇOU! 🎉")

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # CARD 3: Confirmação de Presença Limpa
    st.markdown("<h3 style='text-align:center;'>📝 Confirme sua Presença</h3>", unsafe_allow_html=True)
    with st.form("form_evento", clear_on_submit=True):
        nome_convidado = st.text_input("Seu Nome e Sobrenome:")
        opcao_presenca = st.radio("Você vai conseguir ir?", [
            "Sim! Vou e com certeza estarei lá de peruca.",
            "Infelizmente não vou poder ir."
        ])
        opcao_bebida = st.selectbox("O que você prefere beber?", [
            "Apenas Refri/Água 🥤", "Suco 🧃"
        ])
        
        btn_enviar = st.form_submit_button("Confirmar Presença 🐾")
        
        if btn_enviar:
            if nome_convidado:
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO presenca (nome, status, bebida, data_envio) VALUES (?, ?, ?, ?)",
                    (nome_convidado, opcao_presenca, opcao_bebida, datetime.now().strftime("%d/%m/%Y %H:%M"))
                )
                conn.commit()
                conn.close()
                st.toast(f"Confirmação salva, obrigado {nome_convidado}!", icon="💜")
            else:
                st.error("Por favor, digite seu nome para confirmar.")

    st.markdown("<hr>", unsafe_allow_html=True)

    # CARD 4: Playlist Colaborativa
    st.markdown("<h3 style='text-align:center;'>🎵 Sugira Músicas para a Festa</h3>", unsafe_allow_html=True)
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        musica_sug = st.text_input("Nome da Música:")
    with col_m2:
        artista_sug = st.text_input("Nome do Cantor/Banda:")
    nome_dj = st.text_input("Quem está sugerindo? (Seu nome completo):")
    
    if st.button("Sugerir Música 💿"):
        if musica_sug and artista_sug and nome_dj:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO playlist (musica, artista, sugerido_por) VALUES (?, ?, ?)",
                (musica_sug, artista_sug, nome_dj)
            )
            conn.commit()
            conn.close()
            st.success(f"'{musica_sug}' enviada com sucesso!")
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    # CARD 5: Mural de Recados Eterno
    st.markdown("<h3 style='text-align:center;'>💬 Mural de Recados para a Carol</h3>", unsafe_allow_html=True)
    nome_mural = st.text_input("Seu nome:")
    texto_mural = st.text_area("Deixe uma mensagem carinhosa:", max_chars=140)
    
    if st.button("Deixar Recado 📌"):
        if nome_mural and texto_mural:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO mural (nome, texto, data_envio) VALUES (?, ?, ?)",
                (nome_mural, texto_mural, datetime.now().strftime("%d/%m/%Y %H:%M"))
            )
            conn.commit()
            conn.close()
            st.rerun()

    # Exibe os recados na tela
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, texto FROM mural ORDER BY id DESC")
    todos_recados = cursor.fetchall()
    conn.close()

    if todos_recados:
        for r in todos_recados:
            st.markdown(f"<div style='background-color:rgba(255,255,255,0.1); padding:15px; border-radius:12px; margin-bottom:12px; border-left:4px solid #ffcc00; color:#fff;'><b>{r[0]}</b>: {r[1]}</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # CARD 6: Painel de Controle Secreto da Carol
    st.markdown("<h3 style='text-align:center;'>🔑 Espaço da Carol</h3>", unsafe_allow_html=True)
    senha_carol = st.text_input("Senha para ver a lista de confirmados:", type="password")
    
    if senha_carol == "carol123":
        st.subheader("📊 Relatórios em Tempo Real:")
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT nome, status, bebida FROM presenca")
        dados_presenca = cursor.fetchall()
        
        cursor.execute("SELECT musica, artista, sugerido_por FROM playlist")
        dados_musica = cursor.fetchall()
        conn.close()
        
        st.write("**Lista de Presença:**")
        st.dataframe(dados_presenca)
        
        st.write("**Músicas Sugeridas:**")
        st.dataframe(dados_musica)

    # ==========================================
    # 4. EXIGÊNCIA DA IMAGEM E TEXTO
    # ==========================================
    st.markdown('<p class="texto-final">"Carol se vc n for de peruca"</p>', unsafe_allow_html=True)
    
    foto_encontrada = False
    extensoes = ["foto_carol.jpg", "foto_carol.jpeg", "foto_carol.JPG", "foto_carol.JPEG"]
    
    for ext in extensoes:
        if os.path.exists(ext):
            st.image(ext, use_container_width=True)
            foto_encontrada = True
            break
            
    if not foto_encontrada:
        st.warning("⚠️ Lembrete: Coloque a foto dela na pasta 'sitemano' com o nome 'foto_carol.jpg' para ela aparecer aqui no final!")
