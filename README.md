# 💰 Sistema Bancário em Python

![Status](https://img.shields.io/badge/Projeto-Concluído-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/Licença-MIT-blue.svg)

> Sistema bancário simples desenvolvido em Python, com funcionalidades essenciais como depósitos, saques, extrato, cadastro de usuários e criação de contas. Ideal para iniciantes praticarem conceitos de **lógica de programação**, **funções**, **estruturas condicionais**, **listas** e **manipulação de dados**.

---

## 🧩 Funcionalidades

✅ Menu interativo com as seguintes operações:

- 📥 **Depósito** em conta
- 💸 **Saque** com limite de valor e quantidade diária
- 📄 **Extrato** com histórico detalhado de transações
- 🧑 **Cadastro de usuário** com verificação de CPF único
- 🏦 **Criação de conta bancária** associada a um usuário existente
- 🧾 **Listagem de contas** cadastradas
- ❌ **Encerramento do sistema**

---

## 📌 Regras de Negócio

- ✅ **Depósito**: apenas valores **positivos** são aceitos
- ✅ **Saque**:
  - Máximo de **3 saques diários**
  - Limite de **R$ 500,00 por saque**
  - O valor **não pode exceder o saldo disponível**
- ✅ Cada usuário é identificado unicamente pelo **CPF**
- ✅ Cada conta está associada a **um único usuário**
- ✅ O **extrato** exibe todas as movimentações e o **saldo final**

---

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado (versão 3.10 ou superior).
2. Clone este repositório ou baixe o arquivo `sistema_bancario.py`.
3. Execute o script no terminal:

```bash
python sistema_bancario.py
