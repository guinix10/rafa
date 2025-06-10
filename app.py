import streamlit as st

st.set_page_config(page_title="Carta especial para minha rafa 💌", page_icon="💖", layout="centered")

# --- CSS personalizado e animação dos corações ---
st.markdown("""
<style>
.stApp {
    background-image: linear-gradient(135deg, #ffe4e1, #fff0f5);
    color: #8B0000;
    font-family: 'Comic Sans MS', cursive;
}
.big-font {
    font-size: 28px !important;
}
.heart {
    font-size: 50px;
    text-align: center;
    animation: pulse 1.5s infinite;
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}

/* Corações flutuantes */
.floating-hearts {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 9999;
    overflow: hidden;
}

.heart-float {
    position: absolute;
    bottom: -50px;
    color: pink;
    font-size: 30px;
    animation: float 4s infinite ease-in;
}

@keyframes float {
    0% { transform: translateY(0) scale(1); opacity: 1; }
    100% { transform: translateY(-100vh) scale(1.5); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# Cabeçalho com coração
st.markdown("<div class='heart'>💖</div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>PARA A MINHA RAFA!</h1>", unsafe_allow_html=True)

# Nome
nome = "keller"

# Sessão
if "mostrar_carta" not in st.session_state:
    st.session_state.mostrar_carta = False
if "filme_index" not in st.session_state:
    st.session_state.filme_index = 0

# Botão
if st.button("Ler a carta 💌"):
    st.session_state.mostrar_carta = True

# Conteúdo
if st.session_state.mostrar_carta:
    # Corações flutuantes em forma de animação
    st.markdown("""
    <div class="floating-hearts">
        <div class="heart-float" style="left: 10%;">💖</div>
        <div class="heart-float" style="left: 25%;">💘</div>
        <div class="heart-float" style="left: 40%;">💝</div>
        <div class="heart-float" style="left: 60%;">💓</div>
        <div class="heart-float" style="left: 80%;">💕</div>
    </div>
    """, unsafe_allow_html=True)

    # Carta
    st.markdown(f"""
    <div class="big-font">
    minha {nome},<br><br>
    meu amor, vc sabe que minha letra é arábica mas resolvi escrever um texto pra vc desse jeito! desde a primeira vez que vc me elogiou, eu já consegui me sentir uma pessoa incrível, e ao decorrer do tempo vc me fez sentir melhor ainda, eu estou muito muito feliz e sinto que eu posso ser quem realmente sou quando estou junto com vc!! obrigado meu amor de vdd!! tenho que agradecer demais vc por tudo isso, eu realmente não tenho palavras pra descrever o quanto vc me faz ter vontade de viver e curtir a vida, vc é uma pessoa incrível, vc é PERFEITA, seu cabelo é lindo, seus olhos, seu rostinho, amo ver o seu sorriso quando consigo te deixar rindo ou feliz E PRINCIPALMENTE seu jeito de ser, amo te agradar e sempre que eu puder vou fazer qualquer coisa por vc, EU TE AMO KELLER OBRIGADO POR TUDO VC MERECE TUDO DE BOM!!<br><br>
    com muito carinho do seu namorado.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("lembranças que vou guardar com carinho.")

    # Música
    st.markdown("#### sua música fav 💘")
    st.components.v1.iframe("https://open.spotify.com/embed/track/4RvWPyQ5RL0ao9LPZeSouE", height=80)

    # Imagens
    st.markdown("#### comida fav 💘")
    st.image("sushi.jpg", width=400)

    st.markdown("#### sua cor fav 💘")
    st.image("rosa2.jpg", width=400)

    st.markdown("#### nossos filhos 💘")
    st.image("snoopy.jpg", width=400)

    st.markdown("#### MINHA NENEM 💘")
    st.image("BEBE.jpg", width=400)

    st.markdown("#### NOS 💘")
    st.image("nos.jpg", width=400)

    # Filmes
    st.markdown("#### SEUS FILMES 💘")
    filmes = [
        ("Para Todos os Garotos que Já Amei", "para_todos_os_garotos.webp"),
        ("Amizade Colorida", "amizade_colorida.jpg"),
        ("Casamento Sangrento", "casamento_sangrento2.jpg"),
        ("O Pequenino", "o_pequenino.webp"),
        ("As Branquelas", "as_branquelas.webp"),
        ("Ela e os Caras", "ela_e_os_caras.jpg"),
        ("Stitch", "stitch.jpg"),
        ("Amor com data marcada", "amor_com_data_marcada.jpg" ),
        ("Norbit", "norbit.jpg")
    ]

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅ Anterior") and st.session_state.filme_index > 0:
            st.session_state.filme_index -= 1
    with col3:
        if st.button("Próximo ➡") and st.session_state.filme_index < len(filmes) - 1:
            st.session_state.filme_index += 1

    titulo, imagem = filmes[st.session_state.filme_index]
    st.image(imagem, caption=titulo, use_container_width=True)




   




  

