
# Encrypted Ocean Sensors

## 🌊 Projeto: Comunicação Criptografada para Sensores de Detecção de Lixo Oceânico

### 📜 Descrição

Este projeto foi realizado para a matéria **Cognitive Cybersecurity** do Professor **Leonardo Ruiz Orabona** na FIAP. O objetivo é desenvolver um sistema de comunicação criptografada para transmitir dados de sensores e dispositivos utilizados na detecção de lixo nos oceanos. Utilizando criptografia simétrica, o sistema garante que as mensagens não sejam interceptadas ou alteradas durante a transmissão, proporcionando segurança e integridade dos dados.

### 📝 Problema Proposto

**Comunicação Criptografada para Sensores de Detecção de Lixo Oceânico**

**Objetivo:**
Desenvolver um sistema de comunicação criptografada para transmitir dados de sensores e dispositivos utilizados na detecção de lixo nos oceanos. O sistema deverá utilizar criptografia simétrica para garantir que as mensagens não sejam interceptadas ou alteradas durante a transmissão, proporcionando segurança e integridade dos dados.

**Descrição:**
O trabalho consiste na criação de um sistema em Python capaz de enviar e receber dados de sensores oceânicos de forma segura. Utilizando técnicas de criptografia simétrica, os dados serão protegidos contra interceptações e alterações. Os alunos deverão implementar a criptografia e a descriptografia das mensagens, além de garantir a eficiência e a segurança da comunicação.

**Itens que serão considerados para a nota:**
- Implementação da Criptografia Simétrica
- Segurança da Comunicação
- Documentação do Código

**Ferramentas Recomendadas:**
- Python: Linguagem de programação principal.
- PyCryptodome: Biblioteca para implementação de criptografia.
- Socket: Biblioteca para comunicação de rede.
- Pandas: Biblioteca para manipulação de dados.

### 🎯 Objetivos do Projeto

- **Implementação da Criptografia Simétrica**: Garantir que os dados transmitidos sejam protegidos contra interceptações.
- **Segurança da Comunicação**: Assegurar que a comunicação entre sensores e servidores seja segura.
- **Documentação do Código**: Fornecer uma documentação detalhada para facilitar a compreensão e replicação do projeto.

### 🛠 Ferramentas Utilizadas

- **Python**: Linguagem de programação principal.
- **PyCryptodome**: Biblioteca para implementação de criptografia.
- **Socket**: Biblioteca para comunicação de rede.
- **Pandas**: Biblioteca para manipulação de dados.
- **Pytest**: Ferramenta para testes automatizados.

### 📂 Estrutura do Projeto

```plaintext
encrypted-ocean-sensors/
├── README.md
├── requirements.txt
├── main.py
├── crypto_utils.py
├── network_utils.py
├── tests/
│   ├── __init__.py
│   └── test_crypto_utils.py
```

### 🚀 Como Usar

1. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Execute o Servidor**:
    ```bash
    python main.py server --key mysecretkey
    ```

3. **Execute o Cliente**:
    ```bash
    python main.py client --key mysecretkey --message "Hello, Ocean!" --host 127.0.0.1 --port 65432
    ```

### 🧪 Testes

Para rodar os testes automatizados, execute:
```bash
pytest tests/
```

### 📋 Funcionalidades

- **Criptografia Simétrica com AES**: Protege a integridade e confidencialidade dos dados transmitidos.
- **Comunicação Segura com Sockets**: Garante uma transmissão segura dos dados entre cliente e servidor.
- **Manipulação de Dados com Pandas**: Permite a análise e visualização dos dados recebidos.

### 🔍 Exemplos de Uso

Exemplo de execução do servidor:
```bash
python main.py server --key mysecretkey
```

Exemplo de execução do cliente:
```bash
python main.py client --key mysecretkey --message "Hello, Ocean!" --host 127.0.0.1 --port 65432
```

### 🌟 Impacto e Importância

Este projeto é uma demonstração prática de como a criptografia pode ser aplicada para proteger dados sensíveis transmitidos por sensores, especialmente em um contexto ambiental como a detecção de lixo oceânico. A segurança dos dados é crucial para garantir a integridade das informações coletadas e apoiar iniciativas de preservação ambiental.

### 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorar este projeto.

### 📞 Contato

Para mais informações ou perguntas, entre em contato:
- **LinkedIn**: [Leonardozgf](https://www.linkedin.com/in/leonardozgf/)
- **Email**: leonardozgf@gmail.com

---

**Nota:** Este projeto foi desenvolvido como parte de um estudo sobre comunicação segura e criptografia aplicada a sensores ambientais.
