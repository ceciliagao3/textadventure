import time

start = '''
Today is the big day! You are launching your own business. It will manufacture disposable cups. What will you call it?
'''
building = '''
Okay! Ready to start up this company?! Let's get you situated. What kind of property would you like? You have two options. You can either rent an existing property
or you can buy a new property. What kind of property will your company be in?
'''
rent = '''
Because you rented space for an existing building, you saved lots of money and prevented the destruction of many trees. Way to go!
'''
build = '''
You have bought land and have started building up your new property. Unfortunately, the contractors had to tear down 2 dozen trees in the process.
This has affected the local ecosystem negatively. The locals revolt against your company. The government hears word of this and fines your company.
This leads your new company to go into bankruptcy.
'''
cups = '''
Now that you know where your property is, it is time to figure out your merchandise. What material will you make your cups out of? Paper is
biodegradeable, but styrofoam costs less money.
'''
paper = '''
By choosing to maufacture your cups out of biodegradeable paper, your company has suffered a small monetary loss. However, when your cups are
thrown away, they will decompose, unlike styrofoam cups. Your strong sense of enviromental ethics is appalauded!
'''
styrofoam = '''
Your cups will profit you because styrofoam is so cheap! Unfortunately, what you saved in money the Earth had to pay for, because styrofoam
is not compostable. Its presence will plague the Earth in landfills forever.
'''

fail = '''
Sorry, better luck next time! Always keep the Earth in mind.
'''
success = '''
Well done! Your business is thriving. You have gotten much support from the community and enviromental activists who all love your cups!
Your profits should keep rising, and the Earth shall keep living.
'''

end = '''
Thank you for playing! Remember to recycle and conserve the Earth's resources. Protect the Earth!
'''

print(start)
name = input("Type the name of your new business!")
print ("Congratulations {}!".format(name))
print (building)
done = False
while not done:
    user_input = input("Type 'rent' or 'build':  ")
    if user_input == "rent":
        print(rent)
        print(cups)
        done = True
    elif user_input == "build":
        print(build)
        print(fail)
        print(end)
        time.sleep(10)
        done = True
        exit()
    else:
        print("please type 'rent' or 'buy'");


done = False
while not done:
    user_input = input("Type 'paper' or 'styrofoam' to determine your cup material. ")
    if user_input == "paper":
        print(paper)
        print(success)
        print(end)
        time.sleep(10)
        done = True
    elif user_input == "styrofoam":
        print(styrofoam)
        print(fail)
        print(end)
        time.sleep(10)
        done = True
    else:
        print("Please type 'paper' or 'styrofoam'.");

        exit()
