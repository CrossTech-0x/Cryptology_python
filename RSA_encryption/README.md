<h4>RSA Encryption algorithm by CrossTech-0x
<img src="encrypt.png">
<br>

<img src="Decrypt.png">
<br>

<h2>Step 1 :</h1>
Take two prime number p and q as input from user.
<h2>Step 2:</h2>
Compute n = pq. n is used as the modulus for both the public and private keys. Its length is the key length.
<br>
<i>n = p * q</i>

<h2>Step 3:</h2>
Compute φ(n) = (p − 1)(q − 1) where φ is Euler’s totient function.
<br><i>phi = (p - 1) * (q - 1)</i>
<h2>Step 4:</h2>
Choose an random integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1; 
i.e., e and φ(n) are coprime. e is released as the public key exponent.
<br>
<pre>
def gen_e(a):
    while(True):
        e = random.randrange(2,a)
        if(gcd(e,a)==1):
            return e
</pre>
<h2>Step 5: </h2>
Determine d,the multiplicative inverse of e (modulo φ(n)) and main part of private key.
<br><i>d = modinv(e, phi)</i><br>
modinv is calculated using Extended Euclidean Algorithm.
<br>
<pre>
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
</pre>
<br><br>
<h2>Step 6:Encryption</h2>
If ‘m’ is the message to be transmitted, it is encrypted as c.
<br><i>c = (m**e) % n</i>


<h2>Step 7:Decryption</h2>
Take private key as a input.Private key pair is [n,d]. 
And if the encrypted message is c . Then orginal message m would be..
<br><i>m = (c**d) % n</i>
