#basic ex1
'''
data=[2.3, 3.5, -5.7, 6.9, -4.2, 8.2, 1.1, -1.5, 3.8, .2]
average=sum(data)/len(data)
print("average = ", round(average,2))
'''

#basic ex2
'''
n=int(input("Enter number: "))
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Output = ", rev)
'''

#basic ex3
'''
n=int(input("Enter natural number : "))
i=0
while(n>0):
    n=n//10
    i+=1
print("The number of digits in a number is ", i)
'''

#basic ex4
'''
qunum=int(input("Enter number: "))
n=qunum
ansnum=0
while (n>0):
    dig=n%10
    ansnum=ansnum*10+dig
    n=n//10
if qunum==ansnum:
   print("The number you enter is a palindrome")
else: print("The number you enter is not a palindrome")
'''

#list ex1
'''
def func_list_ex1(f_list_ex1):
    check_list_ex1=list(reversed(list(sorted(f_list_ex1))))
    return check_list_ex1
list_ex1=[1.5,-1,0,8.5,73]
print("The largest number in a list_ex1 is ", func_list_ex1(list_ex1)[0])
print("The second largest number in a list_ex1 is ", func_list_ex1(list_ex1)[1])
'''


#list ex2
'''
def func_list_ex2(f_list_ex2_1,f_list_ex2_2):
    full_list_ex2=list_ex2_1+list_ex2_2
    answer_list_ex2=list(sorted(full_list_ex2))
    return answer_list_ex2
list_ex2_1=[5,-8,0,5.4,-1.2]
list_ex2_2=[4.2,9.8,-456]
print(func_list_ex2(list_ex2_1,list_ex2_2))
'''

#list ex3
'''
def func_list_ex3(f_list_ex3):
    to_first_num=[]
    to_last_num=[]
    n=len(f_list_ex3)
    to_first_num=[f_list_ex3.pop(n-1)]
    to_last_num=[f_list_ex3.pop(0)]
    answer_list_ex3=to_first_num+f_list_ex3+to_last_num
    return answer_list_ex3
list_ex3=[5.2,16,8,985,6521]
print(func_list_ex3(list_ex3))
'''

#list ex4
'''
def func_list_ex4(f_list_ex4):
    set_list_ex4=set(f_list_ex4)
    answer_list_ex4=list(set_list_ex4)
    return answer_list_ex4
list_ex4=[4,5,6,8,8,9,4]
print(func_list_ex4(list_ex4))
'''

#list ex5
'''
def func_list_ex5(f_list_ex5):
    n=len(f_list_ex5)
    word_len_list_ex5=[]
    a=[]
    b=0
    for i in range(0,n):
        a=f_list_ex5[i]
        b=len(str(a))
        word_len_list_ex5=word_len_list_ex5+[b]
    check_list_ex5=list(reversed(list(sorted(word_len_list_ex5))))
    return check_list_ex5
list_ex5=["aef","aefa","XrFdv"]
print("The length of the longest word in list_ex5 is", func_list_ex5(list_ex5)[0])
'''

#strings ex1
'''
def func_str_ex1(f_str_ex1_1,f_str_ex1_2):
    mes_str_ex1=""
    if list(reversed(f_str_ex1_1))!=list(f_str_ex1_2):
        mes_str_ex1="2 strings aren't anagram"
    else:
        mes_str_ex1="2 strings are anagram"
    return mes_str_ex1
str_ex1_1="asdf"
str_ex1_2="asdf"
print(func_str_ex1(str_ex1_1,str_ex1_2))
'''
#strings ex2
'''
def func_str_ex2(f_str_ex2):
    n=0
    vowels_ex2=0
    for i in str_ex2:
        if i in ["a","e","i","o","u","A","E","I","O","U"]:
            n=1
        else:
            n=0
        vowels_ex2=vowels_ex2+n
    return vowels_ex2
str_ex2="3fawefsd"
print("The number of vowels in a str_ex2 is", func_str_ex2(str_ex2))
'''

#strings ex3
'''
def func_str_ex3(f_str_ex3):
    u=0
    l=0
    number_upp_ex3=0
    number_low_ex3=0
    for i in str_ex3:
        u=0
        l=0
        if ord(i) in range(65,91):
            u=1
        elif ord(i) in range(91,123):
            l=1
        else:
            u=0
            l=0
        number_upp_ex3=number_upp_ex3+u
        number_low_ex3=number_low_ex3+l
    return [number_upp_ex3,number_low_ex3]
str_ex3="lsdkIWEAJFWfuhposaij"
print("The number of upper case letters in a str_ex3 is", func_str_ex3(str_ex3)[0])
print("The number of lower case letters in a str_ex3 is", func_str_ex3(str_ex3)[1])
'''

#dictionary ex1
'''
def func_dict_ex1(f_dict_ex1_1,f_dict_ex1_2):
    answer_dict_ex1_items=list(f_dict_ex1_1.items())+list(f_dict_ex1_2.items())
    return dict(answer_dict_ex1_items)
dict_ex1_1={"a":1, "b":2}
dict_ex1_2={"c":3, "d":4}
print(func_dict_ex1(dict_ex1_1,dict_ex1_2))
'''
#dictionary ex2
'''
def func_dict_ex2(f_dict_ex2):
    sum=0
    for i in f_dict_ex2:
        sum=sum+f_dict_ex2[i]
    return sum
dict_ex2={"a":1, "b":2, "c":3, "d":4}
print("Sum of all items in a dictionary is :",func_dict_ex2(dict_ex2))
'''

#dictionary ex3
'''
def func_dict_ex3(f_dict_list_ex3_1,f_dict_list_ex3_2):
    answer_dict_ex3=dict(zip(f_dict_list_ex3_1,f_dict_list_ex3_2))
    return answer_dict_ex3
dict_list_ex3_1=[1,2,4,5]
dict_list_ex3_2=["a","s","j","e"]
print(func_dict_ex3(dict_list_ex3_1,dict_list_ex3_2))
'''

#dictionary ex4
'''
def func_dict_ex4(f_dict_list_ex4):
    keys=[]
    for i in f_dict_list_ex4:
        first_cha=list(i)[0]
        keys=keys+[first_cha.lower()]
    return dict(zip(keys,f_dict_list_ex4))
dict_list_ex4=["Cha","wef","sh"]
print(func_dict_ex4(dict_list_ex4))
'''

#set ex1
'''
def func_set_ex1(f_set_str_ex1):
    vowel={"a","e","i","o","u","A","E","I","O","U"}
    vowel_count=0
    for a in f_set_str_ex1:
        if a in vowel:
            vowel_count+=1
    if vowel_count in {0,1}:
        plural_check="vowel"
    else:
        plural_check="vowels"
    print("The string has", vowel_count, plural_check)
f_set_str_ex1="sdasdfASDFfF"
func_set_ex1(f_set_str_ex1)
'''
        
#set ex2
'''
def func_set_ex2(f_set_str_ex2_1,f_set_str_ex2_2):
    set2_1=set(list(f_set_str_ex2_1.replace(" ","")))
    set2_2=set(list(f_set_str_ex2_2.replace(" ","")))
    set_ex2=set2_1.isdisjoint(set2_2)
    ans_set_ex2=(False==set_ex2)
    return ans_set_ex2
set_str_ex2_1="asd"
set_str_ex2_2="fghj"
print(func_set_ex2(set_str_ex2_1,set_str_ex2_2))
'''

#recursion ex1
'''
def func_rec_ex1(f_rec_list_ex1):
    if len(f_rec_list_ex1)==0:
        return 0
    return func_rec_ex1(f_rec_list_ex1[1:])+f_rec_list_ex1[0]
f_rec_list_ex1=[1,2,5]
print(func_rec_ex1(f_rec_list_ex1))
'''

#recursion ex2
'''
def func_rec_ex2(n):
    if n<1:
        return 1
    else:
        ans_rec_ex2=n*func_rec_ex2(n-1)
        return ans_rec_ex2
print(func_rec_ex2(15))
'''

#recursion ex3
'''
def func_rec_ex3(f_rec_str_ex3):
    if len(f_rec_str_ex3)==0:
        return ""
    return func_rec_ex3(f_rec_str_ex3[1:])+f_rec_str_ex3[0]

f_rec_str_ex3="asdf"
print(func_rec_ex3(f_rec_str_ex3))
'''