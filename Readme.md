# ChatbotRashi
## Chatbot Link: https://t.me/TestRasMiner_bot or https://console.dialogflow.com/api-client/demo/embedded/57044841-2f83-4c5c-887f-19a6c385d376
## Task:
Create a chatbot (RashiMiners) deployed on Telegram for small talk and currency conversion.
## IDE: PyCharm
## Steps:
* Create an API for currency conversion using https://www.currencyconverterapi.com/.
* Create an account/signup on Dialogflow platform by Google Cloud.
* Create a new project rashiminers.
* Go to Dialogflow ES and then create an agent RashiMiners.
* Create and train 3 intents:
1. currency-converter: For Currency Conversion - Add few training phrases, 2 action parameters and a default text response
2. Default Fallback Intent: Display fallback message if chatbot can't understand user - Add few default text responses for action input.unknown + Enable and save intent
3. Default Welcome Intent: Display welcome message for user - Add few training phrases and few default text responses for event Welcome + Save intent
* Fill small talk section completely. (Keep saving partwise and enable small talk)
* Create a new project with venv (Python 3.7). .idea and venv folder will be automatically created.
* In terminal having (venv), pip install flask. (Just install once in venv)
* Create app.py file for creating app.
* To run the app, use play button for app.py or in terminal write python app.py.
* To stop the app, use stop button for app.py or in terminal, click on cross at top and then Terminate.
* Do API testing via Postman software.
* Open cmd as administrator and install ngrok -> choco install ngrok -> ngrok. (Ngrok needs antivirus to be disabled - Software + Firewall Settings)
* After email-verification (create temporary email for safety), type the command from connect section (only once) & ngrok http 5000.
* Open the obtained https link in browser (valid for limited time => complete this step quickly) and then copy it. In fulfillment section, enable webhook and paste copied link in webhook URL. Enable and save the option enable webhook call for this intent in currency-converter intent's fulfillment part.
* Now try the change statement in right pane.
* You can see data below.
* Open json viewer in web browser and copy raw response from diagnostic info there to understand currency-converter's intent call.
* To see output,
1. In terminal having (venv), pip install requests. (Just install once in venv)
2. Test on local system by removing methods, commenting everything in index function except return statement and run the app.
3. Add methods + uncomment above lines, save and rerun app.
4. Try change statement in dialogflow and see the output in PyCharm's terminal.
5. Now, keep repeating step 4 for implementing any changes done further.
* Deploy on Telegram: In Dialogflow,
1. Go to integrations -> Telegram.
2. Proceed as asked.
3. Copy and paste the code in a new notepad file in PyCharm project folder on system.
4. Save it as chatbot.html.
5. Check the app on web browser by using the link in chatbot.html through chatting.
6. Check the app on system by opening chatbot.html file in folder through chatting.
7. Now, go to Telegram app.
8. Search and open BotFather. (Blue Tick One)
9. To get the token to be used on Dialogflow, execute these:
/start
/newbot
TestRasMiner
TestRasMiner_bot
10. In Dialogflow, insert the obtained token in the ‘Telegram Token’ field and then click start.
11. Search for TestRashiMiner and then /start to proceed with chatting.
12. Click on stop in Dialogflow once done with chatting.

Note: Free currency conversion API key may not always work well and is for one month only.
## Tools:
* PyCharm
* Dialogflow
* Postman
* Ngrok API Gateway
* Telegram (Web or Desktop Version)
