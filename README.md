# phe-bee 🐝 | Partially Homomorphic Encryption Sandbox

![ElGamal Encryption Scheme](./ElGamal-Encryption-Scheme.png "ElGamal Encryption Scheme")

## Description

This Python sandbox is an implementation of the **Partially Homomorphic Encryption** scheme using the **ElGamal Cryptosystem**. We first cover the key generation, encryption, and decryption, by following the mathematical principles behind the **ElGamal’s Partially Homomorphic** features, which allow for certain computations to be performed on encrypted data.

The **phe-bee** can perform two types of **Homomorphic** operations:

* Homomorphic Addition: Allows adding two encrypted values to get the encrypted sum or to add an encrypted value to a **constant**.

![ElGamal Additive Homomorphic](./ElGamal-Additive-Homomorphic.png "ElGamal Additive Homomorphic")

* Homomorphic Multiplication: Allows us to multiply an encrypted value by a **constant** to get the encrypted product.

![ElGamal Multiplicative Homomorphic](./ElGamal-Multiplicative-Homomorphic.png "ElGamal Multiplicative Homomorphic")

## Usage

```console
python phe-bee.sandbox.py
```

OR

```console
python3 phe-bee.sandbox.py
```
