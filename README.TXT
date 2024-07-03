This are the instructions for this app

prerequisites:

Install python version 3.10.4
Install node version 14.16
Install npm version 6.14.11

For importing the project, go to a terminal and paste

	git clone https://github.com/Jotaeme55/MMCAccessTest.git

Once installed, go to the backend 

cd backend
then create a virtual environment,

py -m venv env1  	#The name of the environment is not really that important
./env1/Scripts/activate
py -m pip install -r requirements.txt
py app.py 	#Once everything is installed 

Now go back to the frontend
cd frontend

npm install 	#Just wait for the installation
npm run serve 	#Wait for the deployment

after that, just go to http://localhost:8000 or http://localhost:8001
It depends on what is on the frontend terminal right after you run the command npm run serve
