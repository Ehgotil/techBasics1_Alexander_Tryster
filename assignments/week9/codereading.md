This is my code reading exercise. I chose to focus on this piece of code which attempts to recreate the ELIZA chatbot in python, since my final project follows a similar concept.
This in the link to the project and I chose to analyse the "eliza.py" file.
Even though the file is seven years old, I believe the relevancy makes it applicable for me to analyse.

The code begins with importing the libraries logging(to flexibly log events), random( to generate pseudo-random numbers), re(to make matching operations easier) and Namedtuple from the collections module(to create simple data structures).
Then it uses a try-except function to determine the python version of the user to fix incompatibility.
After that, the classes are defined. The "Key" class is used to determine the keywords that will trigger Elizas next response.
The "Decomp" class checks to see if the input phrase matches a specific structure and is responsible for picking the next reply.
The final class that is established is the "Eliza" class. It contains what is effectively the entire rest of the code. When the class is initialised, there are no values assigned to the containers for memory, keyword dictionaries or word substitutions.
When the user types to Eliza, the respond(self, text) function is called. It begins by converting the entire input string to lowercase and checks it against self.quits, which is a list loaded from the script to make sure there are no termination words in the input.
If one of the termination words is found, the function returns None and the program closes after printing the exit message.
Then the program isolates rogue punctuation marks, like commas, that pythons natural word split would add on to a word, to make the inputs easier for Eliza to read. It does this by isolating commas between empty spaces.
Then it tokenises the string, by first ensuring that double or triple spaces are not counted and then passes the individual words through self._sub and uses the self.pres dictionary. This means that it replaces word with contractions like "dont" with the full version: do not, so the program can more easily understand what is being typed.
After that, the program loops through every word in the cleaned statement, makes the input lowercase and checks if it contains an active keyword from self.keys. If matching keywords are found, they are assembled into a list. The list is sorted using a lambda function. key=lambda k: -k.weight. This weighs the different keywords based upon importance.
Following that, the program iterates through the sorted list of keys. It runs self._match_key(words, key) to check whether the sentence structure matches a rule template.
If no keywords match or the keywords that did match, did not match their structural patterns, Eliza has two more options. It either opts for memory retrieval and uses saved responses from an earlier interaction (if one has taken place) to continue the conversation or resorts to using a keyword called xnone, which makes it cycle through preprogrammed responses that have nothing to do with the users input.
Finally, the program puts the keywords together in a sentence, by using .join(output) to add empty spaces into the phrase to create a final answer.

My main takeaways from reading the code were that even a deceptively simple program like and ELiza chatbot is still very complex to get right, if I want to implement keyword checks and also that all of this complexity was achieved in under 300 lines of code. I also realised the importance of libraries, since they enable a lot more intricate code to work in python. My main approach will still be to make it less complex than this version, by relying on a number of prewritten responses tha trigger based on what keywords are found in the users input. This input should be written to a .csv file and be accessible to the user at the end of a session. My version will also not feature memory, but rather only respond to the individual prompt the user input, since longer prompts are encouraged by the fact that it is effectively a digital journal.

I found the code difficult to understand when it came to the details. I was able to identify general structures, such as what function handles what part of the code, but when it came to the specifics of how the "Key" class works, I was overwhelmed. I used Gemini AI to answer specific questions, but did my best to start on my own. Gemini was especially useful to explain the intricacies of the respond(self, text) function. I am now confident that I understand what the program does, even though the details are still a little nebulous to me, since I do not feel entirely comfortable with python yet.

The link to my code is:
https://github.com/wadetb/eliza/blob/master/eliza.py
