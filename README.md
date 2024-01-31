# ALLRIGHT LANDING PAGE

---
## 🧪 Tecnologias utilizadas neste projeto

Este projeto foi desenvolvido utilizando:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)


## 🚀 Como executar

O primeiro passo é ter o Git instalado no seu PC. Se você ainda não baixou, pode fazê-lo [com este link](https://git-scm.com/downloads). Para verificar se você tem git, use o seguinte comando:

```bash
$ git --version # Se você tiver git, o número da versão deverá aparecer no seu console
```

Clone o projeto utilizando a url HTTPS, em uma pasta de sua preferência, clicando em "clone" na página do repositório, selecionando a opção HTTPS e utilizando o seguinte comando:

```bash
$ git clone <URL HTTPS>
```

Alternativamente, você pode baixar o repositório em .zip

Tendo o repositório em seu ambiente local, garanta que possui o [Docker e Docker-Compose](https://www.docker.com/) instalados e configurados em sua máquina.
Em seguida, para executar localmente a API do projeto, basta reproduzir o seguinte comando:

```bash
$ docker-compose up --build # Sobe o servidor utilizando o docker-compose.yml
```

Em produção, deve-se configurar corretamente as variáveis .env, e se utilizar o comando:

```bash
$ docker-compose -f docker-compose.prod.yml up --build # Sobe o servidor utilizando o docker-compose.prod.yml
```

Atenção: O comando para produção somente funcionará corretamente caso as variáveis estejam corretamente configuradas.

Se tudo der certo, ao acessar [esta url](http://localhost:8000) você deve de ver o servidor funcionando.