##Program multi-line-stmts.py
#Prog to demo multi-line stmts using \(continuation-char)

a = 10
b = 20
c = 30
sum = a+b+c
print(sum)

sum =   a+\
        b+\
        c

print(sum) 

#Sp-Case without \ continuation-char (Collections)

months = ['Jan','Feb', 'Jun',
                'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep',
                            'Oct', 'Nov', 'Dec']
print(months)

weeks = ['Sun', 'Mon', 'Tue'
                'Wed', 'Thu',
                        'Fri', 'Sat']
print(weeks)