<h2>Step 1 :</h1>
Take two prime number p and q as input from user.
<h2>Step 2:</h2>
Compute n = pq. n is used as the modulus for both the public and private keys. Its length is the key length.
<b>n = p * q

<h3>Step 3:</h3>
Compute φ(n) = (p − 1)(q − 1) where φ is Euler’s totient function.
<br>phi = (p - 1) * (q - 1)
<h4>Step 4:</h4>
Choose an random integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1; i.e., e and φ(n) are coprime. e is released as the public key exponent.
