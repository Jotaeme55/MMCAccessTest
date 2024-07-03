# Project Setup Instructions
## Prerequisites
Before you begin, ensure you have the following installed:

Python version 3.10.4
Node.js version 14.16
npm version 6.14.11
Clone the Repository
Open a terminal and run the following command to clone the project:

sh
git clone https://github.com/Jotaeme55/MMCAccessTest.git

# Backend Setup
## Navigate to the backend directory:

sh
cd backend
Create a virtual environment:

sh
py -m venv env1  # The name of the environment is not important
Activate the virtual environment:

sh
./env1/Scripts/activate
Install the required Python packages:

sh
py -m pip install -r requirements.txt
Run the backend application:

sh
py app.py

# Frontend Setup
Navigate to the frontend directory:

sh
cd ../frontend
Install the required npm packages:

sh
npm install
Start the frontend server:

sh
npm run serve
Once the server is running, open your web browser and go to:

In a browser go to:
http://localhost:8000 or http://localhost:8001
The exact port depends on the output shown in the frontend terminal after running npm run serve.

## Considerations
This project uses a free LLM API, so make sure you have internet access while using it.
