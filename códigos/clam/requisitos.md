# Instalação de packages
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install python-pip
sudo pip install virtualenv
sudo snap install heroku --classic


virtualenv venv
source venv/bin/activate

pip install -r requirements.txt


# Setando o heroku
heroku git:remote -a 'nome-do-seu-app-heroku'

# Criar um banco de dados 

sudo -u postgres -i

# A flag -W força a pedir uma senha pro usuário (donododb/newpassword)
createuser donododb

# cria o db com um nome
createdb nomedodb

# erro do psycopg2
pip uninstall psycopg2
pip install --no-binary :all: psycopg2

# Para subir
python manage.py migrate
python manage.py collectstatic


# Para subir e rodar no heroku
git commit -m 'Mensagem do commit'
git push heroku master
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py shell
