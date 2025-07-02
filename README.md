# 💰 Sistema Bancário em Python

![Status](https://img.shields.io/badge/Projeto-Concluído-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/Licença-MIT-blue.svg)

> Sistema bancário simples desenvolvido em Python, com funcionalidades essenciais como depósitos, saques, extrato, cadastro de usuários e criação de contas. Ideal para iniciantes praticarem conceitos de lógica, funções, listas e controle de fluxo.

---

## 🧩 Funcionalidades

✅ Menu interativo com as seguintes opções:

- 📥 **Depósito** em conta
- 💸 **Saque** com limite de valor e quantidade
- 📄 **Extrato** com histórico de movimentações
- 🧑 **Cadastro de usuário** com CPF único
- 🏦 **Criação de conta bancária** associada ao CPF
- ❌ **Encerramento do sistema**

---

## 📌 Regras do Sistema

- ✅ **Depósito**: apenas valores positivos
- ✅ **Saque**:
  - Máximo de **3 saques diários**
  - Limite de **R$500,00 por saque**
  - Não pode ultrapassar o **saldo disponível**
- ✅ **Usuários** identificados unicamente por **CPF**
- ✅ Cada conta está associada a **um único usuário**
- ✅ O **extrato** mostra todas as transações realizadas e o saldo atual

---

## 📂 Estrutura do Projeto

```bash
sistema-bancario/
│
├── sistema_bancario.py       # Arquivo principal com toda a lógica
├── README.md                 # Este arquivo de documentação
