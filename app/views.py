# from django.shortcuts import render
#
# # Create your views here.
# from django.shortcuts import render
# from nltk.chat.util import Chat, reflections
#
# patterns = [
#     (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
#     (r'how are you', ['I am doing well, thank you!', "I'm fine, thanks!"]),
#     (r'what is your name', ['I am a chatbot. You can call me ChatGPT.']),
#     (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
#     (r'your age|how old are you', ['I don\'t have an age. I\'m just a computer program.']),
#     (r'what do you do', ['I\'m here to chat and assist you. Ask me anything!']),
#     (r'where are you from', ['I exist in the digital realm, so I don\'t have a specific location.']),
#     (r'how can you help me', ['I can answer questions, provide information, or just chat with you.']),
# ]
#
# chatbot = Chat(patterns, reflections)
#
# def home(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input', '')
#         response = chatbot.respond(user_input)
#         return render(request, 'app/home.html', {'user_input': user_input, 'response': response})
#     return render(request, 'app/home.html')
from django.shortcuts import render
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', "I'm fine, thanks!"]),
    (r'what is your name', ['I am a chatbot. i don\'t have a name.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'your age|how old are you', ['I don\'t have an age. I\'m just a computer program.']),
    (r'what do you do', ['I\'m here to chat and assist you. Ask me anything!']),
    (r'where are you from', ['I exist in the digital realm, so I don\'t have a specific location.']),
    (r'how can you help me', ['I can answer questions, provide information, or just chat with you.']),
]

chatbot = Chat(patterns, reflections)


def home(request):
    default_response = "I'm sorry, I didn't understand that. Please ask me something else."

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = chatbot.respond(user_input) or default_response
        return render(request, 'app/home.html', {'user_input': user_input, 'response': response})

    return render(request, 'app/home.html')
