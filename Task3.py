try:
    from transformers import pipeline
    import importlib.util

    chatterbot_spec = importlib.util.find_spec("chatterbot")
    if chatterbot_spec is None:
        raise ModuleNotFoundError("chatterbot")
    else:
        from chatterbot import ChatBot
        from chatterbot.trainers import ChatterBotCorpusTrainer
except ModuleNotFoundError as e:
    print(f"Missing module: {e.name}. Please install it using 'pip install {e.name}' and try again.")
    chatterbot_available = False
    transformers_available = e.name != "chatterbot"
else:
    chatterbot_available = True
    transformers_available = True

def create_chatbot():
    if not chatterbot_available:
        print("ChatterBot module is not available. Using a fallback response system.")
        return None
    
    chatbot = ChatBot("AI Assistant")
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    return chatbot

def get_response(chatbot, query):
    if chatbot:
        return chatbot.get_response(query)
    return "I'm sorry, but I can't process that request right now."

def main():
    chatbot = create_chatbot()
    qa_pipeline = None
    
    if transformers_available:
        try:
            qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
        except Exception as e:
            print("Error initializing NLP model:", e)
    
    print("Chatbot is ready! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = get_response(chatbot, user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
