## 📜 Elijah's Rise

🔹 *Um jogo 2D em Python/Pygame inspirado na história bíblica do profeta Elias, seus feitos impulsionados por sua fé em Deus e coragem em ousar ser um homem de valor em um tempo de crise.*

---

### 📌 Sobre o Projeto

**Elijah's Rise** é um jogo educativo e interativo com narrativa cristã (inicialmente em pt-br). 

O jogador assume o controle de um corvo enviado por Deus para alimentar o profeta Elias com pão e carne no deserto. O objetivo é coletar os alimentos enquanto desvia de obstáculos e enfrenta a força do vento, com tempo limitado.

---

### 🎯 Objetivo da Fase 1 (Única desenvolvida até o momento)

- Controlar o **corvo** (player) usando as teclas direcionais.
- Coletar **5 "meat breads"** antes que o tempo acabe ou o 'health' do player chegue a zero.
- **Evitar obstáculos**: árvores, hienas e ventos aleatórios.
- Ao vencer, o jogo exibe um vídeo de Elias sendo alimentado e o jogador seta seu score.
- Se o tempo acabar, um vídeo de falha é mostrado.

---

### 🧹 Tecnologias e Padrões Utilizados

- 🐍 **Python 3**
- 🎮 **Pygame**
- 🧪 **Design Patterns**:
  - **Proxy** – Registro do score do jogador
  - **Mediator** – Coordenação de colisões, vida e score
  - **Factory** – Criação dinâmica de entidades e fases

---

### 🧠 Estrutura do Projeto

```bash
ElijahsRise/
│
├── code/
│   ├── Entity.py          # Classe base de entidades
│   ├── Player.py          # Corvo controlado pelo jogador
│   ├── Enemy.py           # Pássaros e obstáculos móveis
│   ├── Wind.py            # Movimento aleatório e desafiante
│   ├── Tree.py            # Obstáculo fixo (background)
│   ├── MeatBread.py       # Itens coletáveis
│   ├── Const.py           # Constantes globais (dimensões, velocidade, tempo)
│   └── ...
│
├── asset/                # Sprites, vídeos e sons
│   ├── player_sprite_sheet.png
│   ├── MedievalSharp.ttf
│   └── success_video.mp4
│
├── main.py                # Loop principal e entrada do jogo
├── README.md
└── requirements.txt       # Dependências do projeto
```

---

### ⏳ Tempo de Jogo

- Tempo total: **80 segundos**
- Contagem regressiva exibida na tela
- A fase termina com sucesso ao coletar 5 itens antes do tempo esgotar

---

### 🖼️ Imagem do Profeta Elias

![Profeta Elias](https://github.com/ranieriiuri/ElijahsRiseGame/tree/main/asset/elijah.png)

---

### ⚒️ Como Rodar o Projeto com auxilio de IDE

1. Clone o repositório:
```bash
git clone https://github.com/ranieriiuri/ElijahsRiseGame.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode o jogo:
```bash
python main.py
```

---
### ⚒️ Como Instalar o Game em sistemas windows

- Executar o arquivo '.exe' em:  
```bash
ElijahsRise/
│
├── dist/
│   ├── elijahs_rise.exe          # executável gerado

```

---

### ✨ Créditos e Agradecimentos

- Desenvolvido por **Ranieri Iuri**
- Sprites e sons: fontes livres (OpenGameArt, etc.)
- Inspiração bíblica: 1 Reis cap 17 a 2 Reis cap 2 
- Agradecimentos especiais à ![Vecteezy](https://www.vecteezy.com/), Por parte da arte utilizada!

---

### 📖 Versículo Inspirador

> *“Os corvos lhe traziam pão e carne de manhã e de tarde, e ele bebia do riacho.”*  
> **– 1 Reis 17:6 (NVI)**

