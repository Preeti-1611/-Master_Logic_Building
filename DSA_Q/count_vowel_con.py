# count the vowels and consonants  in the str


s1 = "Preetinagaraleeee"
ss=s1.lower()
count_vowel=0
count_con=0
for i in ss:
    if i in 'aeiou':
        count_vowel+=1
    else:
        count_con+=1
print("the vowels are",count_vowel)
print("the consonants are",count_con)