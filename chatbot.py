from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
import speak as sp

chatbot = ChatBot('Thermo')

# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english") 
# trainer.export_for_training("./data.json")

def respone(query):
        
    if ("exit" in query or 'stop' in query
        or 'stop talking' in query or 'no response' in query):
        sp.speak('it was nice to talk to you!')
        print('Bot said : it was nice to talk to you!')
        return False
    else:
        Query = chatbot.get_response(query)
        sp.speak(Query)
        print(f"Bot said : {Query}")
            
        # if len(Query)>0:
        #     return Query      

# respone()