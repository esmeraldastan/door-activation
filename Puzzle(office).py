import random
import sys

print "Figure out the password in order to open the door."

password = ["3546", "5515", "1651"] #passwords to open up the doors 
wordIndex = random.randint(0,len(password)-1)
code_rip = password[wordIndex]
user_guesses = ''
turns = 10 #the player will have only 10 times to try to figure out the code


while turns > 0:
        left = 0
        for number in code_rip:
            if number in user_guesses:
                print number
            else:
                print "#"
                left += 1
            if left == 0:
                print
                print
                print "Excellent, move on."# move into the next room 
                break
        
      
        
            print 
        
            guess = raw_input("Guess the four Numbers:")
            if guess in ['q','quit','exit']:
                sys.exit(0)
            user_guesses += guess 
            if guess not in code_rip:
                turns -=1
                print "Sorry number not in the secret code. \n\n Please try again"
                print "You have", +turns, 'left'
            if turns == 0:
                print "Sorry you lose"#change
       


