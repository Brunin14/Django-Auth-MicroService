# 🚀 Django Auth Microservice

Microserviço de autenticação moderno construído com **Django + Django Rest Framework**, utilizando **JWT**, **verificação de e-mail**, **rate limiting**, **refresh tokens** e estrutura pronta para **2FA**.

Ideal para ser usado como **serviço central de autenticação** em aplicações SaaS, APIs e sistemas modernos.

---

## ✨ Funcionalidades

- ✅ Registro por e-mail  
- ✅ Login JWT (Access + Refresh)  
- ✅ Refresh automático de token  
- ✅ Logout com blacklist  
- ✅ Endpoint autenticado `/me`  
- ✅ Verificação de e-mail  
- ✅ Rate limit contra brute-force  
- ✅ Estrutura pronta para 2FA (OTP)  
- ✅ Swagger automático  
- ✅ Arquitetura modular  
- ✅ Custom User Model  

---

## 🧠 Arquitetura

Fluxo de autenticação desacoplado:

Frontend (Web / Mobile)
|
↓
Django Auth Microservice
|
↓
JWT + Refresh Tokens


Compatível com:

- React
- React Native
- Next.js
- Flutter
- APIs externas
- Microserviços

---

## 🛠 Stack Tecnológica

| Tecnologia | Uso |
----------|-------
Django 5 | Backend principal
Django Rest Framework | API REST
SimpleJWT | Autenticação JWT
dj-rest-auth | Endpoints de autenticação
django-allauth | Registro + verificação de e-mail
drf-spectacular | Swagger / OpenAPI
SQLite | Banco dev
JWT Blacklist | Logout seguro
Django OTP | Base para 2FA

---

## 📦 Instalação

### 1️⃣ Clone o projeto

```bash
git clone https://github.com/Brunin14/Django-Auth-MicroService
cd django-auth-microservice

2️⃣ Crie o ambiente virtual
Windows: python -m venv .venv
        .venv\Scripts\activate
Linux/Mac: python3 -m venv .venv
           source .venv/bin/activate
    
3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Rode as migrations
python manage.py migrate

5️⃣ Inicie o servidor
python manage.py runserver
🚀 Servidor disponível em: http://127.0.0.1:8000

🌐 Demo Online (Produção)

Teste a API agora mesmo sem precisar instalar nada:

👉 **[Acessar Documentação Swagger (Live)](https://django-auth-microservice.onrender.com/api/docs/)**

*Base URL: `https://django-auth-microservice.onrender.com`*


📄 Documentação Swagger

Interface visual da API: https://django-auth-microservice.onrender.com/api/docs/
Schema OpenAPI: https://django-auth-microservice.onrender.com/api/schema/

---

🔐 Autenticação JWT

Login - POST: /api/auth/login/
Body: {
  "email": "user@email.com",
  "password": "StrongPass123!"
}   
Resposta: {
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}

---

Refresh Token - POST: /api/auth/token/refresh/
Body: {
  "refresh": "JWT_REFRESH_TOKEN"
}

---

Logout - POST: /api/auth/logout/
Header: Authorization: Bearer ACCESS_TOKEN

---

Usuário Autenticado - GET: /api/auth/me/
Authorization: Bearer ACCESS_TOKEN

---

📝 Registro de Usuário

Criar conta - POST: /api/auth/registration/
Body: {
  "email": "novo@email.com",
  "password1": "StrongPass123!",
  "password2": "StrongPass123!"
}

---

📧 Confirmação de Email (Modo Desenvolvimento)
Configuração atual: EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

O link de confirmação aparece diretamente no terminal
Exemplo: https://django-auth-microservice.onrender.com/accounts/confirm-email/XXXX/

🛡 Segurança & Proteções
 -   🔒 JWT com expiração curta
 -   🔁 Refresh Token rotativo
 -   🚫 Blacklist no logout
 -   📧 Email obrigatório
 -   🧠 Validação forte de senha
 -   🛑 Rate limit contra ataques
 -   🔐 Middleware OTP pronto

📂 Estrutura do Projeto

backend/
│
├── .venv/                   <-- Ambiente Virtual
├── config/                  <-- Configurações Globais (settings, urls)
├── templates/               <-- Templates de E-mail Personalizados
├── users/                   <-- App Principal
│   ├── migrations/          <-- Histórico do Banco de Dados
│   ├── tests/               <-- Testes Automatizados
│   ├── jwt_login.py         <-- View Modular: Login
│   ├── jwt_refresh.py       <-- View Modular: Refresh
│   ├── register.py          <-- View Modular: Registro
│   ├── models.py            <-- Custom User Model
│   └── serializers.py       <-- Validações
│
├── .env                     <-- Variáveis de Ambiente (Ignorado pelo Git)
├── .gitignore
├── db.sqlite3               <-- Banco de Dados Local
├── manage.py
├── requirements.txt
└── README.md

🚀 Roadmap

Funcionalidades futuras:
    - SMTP produção (SendGrid / Gmail)
    - Login social Google
    - 2FA completo
    - Docker
    - PostgreSQL
    - Redis Rate Limit
    - Deploy produção

👨‍💻 Autor

    - Projeto desenvolvido com foco em:
    - Backend moderno
    - Arquitetura desacoplada
    - Segurança JWT
    - APIs profissionais
    - Microserviços



🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

Developed by Bruno 🚀
