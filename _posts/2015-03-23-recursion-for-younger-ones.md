---
layout: post
tags: [programming, python, kids]
---
This evening, my daughter read a book that ctually had a recursive element - it referenced itself. The book was about being able to step into books and meet the characters,with the character in the book suggesting the reader, if they could, would be able to step in and meet him. And then he was holding the book that she was holding. She found it quite amusing, and exciting -the idea that the book, in the book would have him holding the book again and so on.

This lead us to playing with the idea - she learned a new word - recursion. And then I linked it to code.
She has done simple programming - turtle stuff and some drawing in a pygame loop or on Khan Academy, but she'd not seen functions.

So I introduced a simple function for printing stuff, using python:

    def train():
      print "Choo choo!"
      
    print "The train is coming."
    train()
    print "The train is going."
    train()
    
She had seen how `import` let her pull in rules for drawing and other things, so I explained that `def` means she can make her own rules - called functions. I then got her to dry run this code - tell me what it would do, and then run it.

    The train is coming.
    Choo choo!!
    The train is going.
    Choo choo!!
    

She then wanted the train to say "chugga chugga". This was good - she got to change the code in one place, and see it effect the output twice.

    def train():
      print "Chugga chugga!"
      
This was fun, but I wanted to introduce a couple of other concepts now she was playing with that. 
Lets get it to say something to her. She'd seen variables before, and used parameters with other functions, but not ones she'd seen defined yet:

    def hello(person):
	    print "Hello", person
	    
    >>> hello("stinky")
    Hello stinky
    
She liked that. She played with it a bit trying different words for person - and she understood what it did. Yes she was also getting a little cheeky with her wording - I decided to roll with it if it worked - 5 year olds love toilet humour, partially because its the only joke structure she seemed to know, but I digress...
We then changed hello to do somehting a bit different:

    >>> def hello(person):
	    print "Hi there my old buddy", person

    >>> hello("stink")
    Hi there my old buddy stink
    
She played a bit - different persons, different greetings. So we worked on another bit of code to play with:

    >>> def smelly_wee(a_silly_number):
	    print "you silly sausage, the answer is"
	    print a_silly_number + 5

I did have to explain the underscore and how to type it at this point - sorry if it offends you, but this is definitely the height of 5 year old humour. She was quickly able to get what would happen here though - I again got her to tell me what an example would do, before pressing enter to run it:

    >>> smelly_wee(10)
    you silly sausage, the answer is
    15
    
Getting her to anticipate the real answer was tricky (she was desperate to run it), but when she saw she could predict the results well, it meant she started to get what was going on there.

Now came the big trick. Recursion. I am very pleased she got this and it wasn't a brain melter for her, although I will have to show her the more conventionalway of looping later. I wrote a "putting it all together" type function, and again let her guide naming and style - which means it came out toilet humour again.
First I made a mistake - and it gave mean opportunity to explain it too:

    >>> def down_the_toilet(big_stinky_number):
	    if big_stinky_number > 3:
		    print a_big_stinky_number, "is too big"
		    down_the_toilet(a_big_stinky_number - 1)
	    else:
		    print a_big_stinky_number, "is small enough"
    
    >>> down_the_toilet(1)

I got her to explain what this bit would do - she had understood that big_stinky_number would be 1 here, and that it is not more than 3 (she has seen more than in Khan Academy maths before), but neither her nor I spotted the fact that I'd named it differently yet - so after predicting that it would output "1 is small enough" and pressing enter, we got this:

    Traceback (most recent call last):
      File "<pyshell#25>", line 1, in <module>
        down_the_toilet(1)
      File "<pyshell#24>", line 6, in down_the_toilet
        print a_big_stinky_number, "is small enough"
    NameError: global name 'a_big_stinky_number' is not defined

I had made an opportunity to explain this - that the computer is stupid - it doesn't know that a_big_stinky_number meant big_stinky_number, so it couldn't find the one we meant, and gave a NameError because it didn't know anything with that name. She got a laugh at how dump the computer is. We then fixed the code (I let her type some, and I fixed one she missed in the else). 

    >>> def down_the_toilet(big_stinky_number):
    	if big_stinky_number > 3:
    		print big_stinky_number, "is too big"
    		down_the_toilet(big_stinky_number - 1)
    	else:
    		print big_stinky_number, "is small enough"
    
    		
    >>> down_the_toilet(1)
    1 is small enough

This wasn the output we expected. I then posed a question on what a number larger than 3, say 4 would do. 

    >>> down_the_toilet(4)
    
She followed the if, the print, and then asked me what is going on there. I said recursion - this function calls itself. She got the arithmetic, and asked about big_stinky_number now being different in the next call. A good sign that she was getting it. She was able to get to big_stinky_number being 3, made silly face when I asked her if 3 is more than 3 (of course its not more its the same you silly!), and then predicted the other output. We ran it - and again she got to see her prediction was correct.

    >>> down_the_toilet(4)
    4 is too big
    3 is small enough
    
I let her play with numbers - but told her don't put anything greater than 10 in. I am sure she will by herself later, let her see what happens then, it'll probably cope for fairly big numbers though.

    >>> down_the_toilet(8)
    8 is too big
    7 is too big
    6 is too big
    5 is too big
    4 is too big
    3 is small enough

She had one last question. "The code makes it smaller, but the story doesn't make sense. How does it get smaller?" We added one line to make the story make more sense, and be even funnier to her:

    >>> def down_the_toilet(big_stinky_number):
    	if big_stinky_number > 3:
		    print big_stinky_number, "is too big"
		    print "flushing..."
		    down_the_toilet(big_stinky_number - 1)
	    else:
		    print big_stinky_number, "is small enough"
    
    		
    >>> down_the_toilet(8)
    8 is too big
    flushing...
    7 is too big
    flushing...
    6 is too big
    flushing...
    5 is too big
    flushing...
    4 is too big
    flushing...
    3 is small enough

I think I'll need to refresh conventional loops with her too - just so she knows that this is perhaps a bit of an odd way to approach this problem, but now she has seen that this is possible, she can play with it.
