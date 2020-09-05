# hellobot

A VERY simple chatbot that learns from you. Written in Python3.

## How to use:

When you run the program, it will ask if you want to load from file. If this is your first time using the program, type "n", and press enter. If you have used the program before, your previous session's statements and responses will be saved in the text files, so type "y" and press enter to load these.
NOTE: choosing "n" will overwrite a previous session.

Now you are speaking directly with the chatbot. If you want to teach it a response, you need to be persistent. The following is a basic conversation example.

```
You: hi there
Bot: hello
You: hi there
Bot: hi there
You: how are you
Bot: hello
You: hi there
Bot: how are you
You: i'm well
Bot: hi there
You: how are you
Bot: i'm well
You: that's good
Bot: how are you
You: i'm well
Bot: that's good
You: yes, it is
Bot: that's good
You: yes, it is
Bot: yes, it is
You: hello
Bot: hi there
You: how are you
Bot: i'm well
You: that's good
Bot: yes, it is
```

Notice how by the end of the conversation, the chatbot mimics what you were inputting as your responses to create a somewhat coherent conversation.
Hello, hi there, how are you, i'm well, that's good, yes, it is.
When you want to stop talking to the bot, type "/exit" or "/quit". This will save your session to the textfiles. If you want to exit without save, you'll have to use a keyboard interrupt (CTRL+C).

Enjoy!

## Changelog

 - v0.2 (Current): Optimized code.
 - v0.1: Base release.
