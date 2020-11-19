#Implementing RSA encryption algorithm in pure python
import random
def check_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0 :
                return False
            else:
                return True
    else:
        return False

def gcd(a,b):
    while b!=0:
        c=a%b
        a=b
        b=c
    return a
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def gen_e(a):
    while(True):
        e = random.randrange(2,a)
        if(gcd(e,a)==1):
            return e

def encrypt(p,e,n):
    x=[]
    m=0
    for i in p:
        m=ord(i)
        c=(m**e)%n
        x.append(c)
    return x
def decrypt(c,d,n):
    txt=c.split(',')
    x=''
    m=0
    for i in txt:
        m=(int(i)**d)%n
        c=chr(m)
        x+=c
    return x

def encrypt_choice(s):
    p=int(input("Enter prime number p: "))
    q=int(input("Enter prime number q: "))
    check_p=check_prime(p)
    check_q=check_prime(q)
    while((check_p==False)or(check_q==False)or(p==q)):
        print("Please Enter  Valid prime numbers....\n")
        p = int(input("Enter a prime number for p: "))
        q = int(input("Enter a prime number for q: "))
        check_p = check_prime(p)
        check_q = check_prime(q)
    n=p*q
    phi=(p-1)*(q-1) #Euler's function(totient) phi(n)
    e=gen_e(phi)
    print("\nYour Public key pair is: ["+str(n)+","+str(e)+"]")
    d=modinv(e,phi)
    print("\nYour Private key pair is: ["+str(n)+","+str(d)+"]")
    print("\nPlain message: " + s + "\n")
    enc = encrypt(s,e,n)
    print("Encrypted message: ",enc)

def decrypt_choice(enc):
    n=int(input("\nPlease Enter the 1st number of private  key pair:"))
    d=int(input("\nPlease Enter the 2nd number of private  key pair:"))
    dec = decrypt(enc,d,n)
    print("Decrypted message: ",dec)

def main():
    print("\nWhat would you like to do ? ")
    choice=int(input("\n  1. Encrypt \n  2. Decrypt \nChoice: "))
    if(choice==1):
        s =input("Enter a message to encrypt: ")
        if(len(s)!=0):
            encrypt_choice(s)
        else:
            print("\n Please Enter a valid message.")
            main()
    elif(choice==2):
        enc_s =input("Enter a message to decrypt: ")
        if(len(enc_s)!=0):
            decrypt_choice(enc_s)
        else:
            print("\n Please Enter a valid message.")
            main()
    else:
        print("Enter a valid Choice .")
        main()

if __name__ == "__main__":
    main()
