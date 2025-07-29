# 📰 Notificador de Concursos Públicos por Filtros

Este projeto é um **notificador automático de concursos públicos**, com foco em extração inteligente de informações relevantes (salário, cargo, local) a partir de editais em PDF publicados por bancas examinadoras. O usuário define seus filtros, e o sistema envia notificações somente quando encontrar concursos compatíveis.

---

## 🚀 Funcionalidades

- 🕸️ Coleta automática de editais diretamente de sites oficiais
- 📄 Leitura de arquivos PDF com extração textual
- 🔍 Filtros personalizados por região, cargo e salário
- 💾 Armazenamento estruturado em banco de dados (SQLite)
- ✉️ Notificações por email
- ⏱️ Execução automática via GitHub Actions

---

## ⚙️ Como Usar

1. **Clone o projeto:**
   ```bash
   git clone https://github.com/seu-usuario/notificador-concursos.git
   cd notificador-concursos