#Programmed by: Marie Fiona S. Velasquez
#CITCS 1B
#CC2 - 1

#pounds to kilograms
pounds = float(input("Input weight in pounds: "))
converted_pounds = float(pounds * 0.45359237)

print(str("Weight in pounds = ") + str(pounds) + str("lbs"))
print(str("Weight converted to kilograms = ") + str(converted_pounds) + str("kg"))
print("===============================================================")

#miles to kilometers
miles = float(input("Input length in miles: "))
converted_miles = float(miles * 1.609344)

print(str("Weight in miles = ") + str(miles) + str("mi"))
print(str("Length converted to kilometers = ") + str(converted_miles) + str("km"))
print("===============================================================")

#fahrenheit to celsius
fahrenheit = float(input("Input temperature in Fahrenheit: "))
converted_fah = float((fahrenheit - 32) * 5/9)

print(str("Temperature in Fahrenheit = ") + str(converted_fah) + str("°F"))
print(str("Temperature converted to Celsius = ") + str(converted_fah) + str("°C"))
print("===============================================================")

#average age of students
student1 = int(input("Input age: "))
student2 = int(input("Input age: "))
student3 = int(input("Input age: "))
student4 = int(input("Input age: "))
student5 = int(input("Input age: "))
student6 = int(input("Input age: "))
student7 = int(input("Input age: "))
student8 = int(input("Input age: "))
student9 = int(input("Input age: "))
student10 = int(input("Input age: "))
students = (int(student1 + student2 + student3 + student4 + student5 + student6 + student7 + student8 + student9 + student10))
ave = float(students / 10)

print(str("Age of Student 1: ") + str(student1))
print(str("Age of Student 2: ") + str(student2))
print(str("Age of Student 3: ") + str(student3))
print(str("Age of Student 4: ") + str(student4))
print(str("Age of Student 5: ") + str(student5))
print(str("Age of Student 6: ") + str(student6))
print(str("Age of Student 7: ") + str(student7))
print(str("Age of Student 8: ") + str(student8))
print(str("Age of Student 9: ") + str(student9))
print(str("Age of Student 10: ") + str(student10))
print(str("The average age of the students is: ") + str(ave))
print("===============================================================")

#story
#story
char1 = ("Atlas")
char2 = ("Avery")
char3 = ("Slade")
char4 = ("Kaori")
char5 = ("Vera")
ab1 = ("Everlast Compass")
ab2 = ("Phantasmal Wrath")
ab3 = ("Mighty Axe")
ab4 = ("Seraphic Gaze")
ab5 = ("Psychomancer")
en1 = ("Razorback Cat")
en2 = ("Torment Viper")
place = ("Nottpil")

mult_str = (f"""In search of a cure for their father, 3 siblings went on a journey to the highest mountain called {place}.
The eldest one named {char1} is the one navigating and leading them. Together with his {ab1}, which aside from giving directions can also transform 
into a shield that will protect them from getting harmed, is his only remembrance from their mother. She always tells him that he must, at all costs, 
protect his siblings using it. The middle one, {char2}, is known to have a {ab2}. This ability allows her to transform into anything she thinks of 
making her the most dangerous among the siblings. Her ability was more of a curse rather than an ability. The youngest one is {char3}, even at a young 
age, he was already known to be a great wielder with his {ab3} which allows him to move swiftly.

As they continued their journey, they faced unimaginable opponents along the way who were also in search of a cure.
The first one was a {en1} who had very long and sharp nails that could pierce through someone’s body very easily.  Showing off to his siblings,
{char3} used his {ab3} to instantly kill the opponent. Having a competitive mindset, {char2} became irritated by his actions.
The next opponent was a {en2} which has three heads that multiply once a head is being cut off. {char2} grabbed the opportunity to show
what she could do. Using her intelligent mind, she transformed herself into a three-tailed scorpion as big as the {en2} which easily stung
the three of them simultaneously. This only proved how great and dangerous her {ab2} is.

As they were getting near {place}, they saw two figures that were ahead of them.
{char1} called them to ask if it was the right way to the peak of the mountain. As the two figures looked, he immediately shielded themselves with
the {ab1} because he recognized the two of them. They belong to the group of perilous people who like to collect different cures and treasures and 
keep them to themselves. The first one is {char4}, known to have a {ab4} which makes the people who look into her eyes controlled and addicted.
The other one is {char5}, known to have {ab5} or the ability to manipulate thoughts and actions. {char1} knew that being together would make the two 
of them unbeatable.

Not knowing what was happening, {char3} immediately got out of the shield and looked at the two of them and he was already under the spell of {char4}.
He began to walk towards her and knelt down. {char2} saw what happened and he looked at {char1} who had a very worried face. They decided to come
near to them by hiding behind the shield. However, Vera used her ability to make them come out. {char2} was able to cover her ears but Atlas was able 
to be under her spell. He began to let go of the shield but {char2} was not letting her go. Left with no choice, she used her {ab2} and transformed
into a big wild boar and came running toward {char4} and {char5} while her eyes closed so she would not be able to look at Kaori and roared very loudly 
so she would not be able to hear {char5}. She grabbed both of them and not knowing where she was going, the three of them fell from the mountain.

When {char1} and {char3} were already out of the spell, they realized what {char2} did. Looking around, {char1} saw the shield moving and when he lifted it up, 
they saw {char2} and hugged her. It was her curse that died because it was what keeps her from connecting with her siblings. She always thought that she 
was dangerous and having it gone, she can safely say that they are safe with her already. As they reached the mountain peak, they saw the cure placed at 
the top of a rock and immediately took it. Not only did it cure their father but also their relationship as siblings.""")

print(mult_str)