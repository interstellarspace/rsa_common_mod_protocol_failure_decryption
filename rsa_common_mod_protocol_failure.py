print("******************************QUESTION 5******************************")
def Extended_Eucledian_Alg(num, mod):
    qi_list = list()
    remainder_list = list()
    #i_list = list()
    gcd_for_inverse(num, mod, qi_list, remainder_list)
    #print(qi_list)
    #print(remainder_list)
    inv = calculate_inverse(qi_list)
    if inv < 0:
        inv = inv % mod
    if remainder_list[len(remainder_list)-2] == 1.0:
        return inv
    else:
        #print("Error: num '%' mod " + str(mod) + " has not multiplicative inverse")
        return( str(num) + " mod " + str(mod) + " has no multiplicative inverse.")
    
def gcd_for_inverse(a,b, qi_list, remainder_list):
    if b == 0:
        return a
    else:
        qi_list.append(math.trunc(a / b))
        remainder_list.append(a % b)
        return gcd_for_inverse(b, a % b, qi_list, remainder_list)

def calculate_inverse(qi_list):
    xjold = 0
    xjnew = 1
    #print(qi_list)
    for x in range(1,len(qi_list)-1):
        inv = xjold - (qi_list[x] * xjnew)
        xjold = xjnew
        xjnew = inv
    return inv

def rsa_commmon_modulus_decryption(n, b1, b2, y1, y2):
    print("Calculating plaintext for the following parameters:")
    print("n = " + str(n))
    print("b1 = " + str(b1))
    print("b2 = " + str(b2))
    print("y1 = " + str(y1))
    print("y2 = " + str(y2))
    c1 = Extended_Eucledian_Alg(b1,b2)
    c2 = ((c1*b1) - 1) / b2
    x = ((y1**c1)%n) * (Extended_Eucledian_Alg((y2**c2),n)) % n
    print("\nPlaintext: " + str(x) + "\n")
    return x

def rsa_check(x, n, b1, b2, y1, y2):
    sys.stdout.write("Checking plaintext encryption: " + str(x) + " ^ " 
                     + str(b1) + " mod " + str(n) + " = " + str(y1))
    assert(x**b1 % n == y1)
    sys.stdout.write("\t\tOK\n")
    sys.stdout.write("Checking plaintext encryption: " + str(x) + " ^ " 
                     + str(b2) + " mod " + str(n) + " = " + str(y2))
    assert(x**b2 % n == y2)
    sys.stdout.write("\t\tOK\n")

n = 18721
b1 = 43
b2 = 7717
y1 = 12677
y2 = 14702
x = rsa_commmon_modulus_decryption(n, b1, b2, y1, y2)
rsa_check(x, n, b1, b2, y1, y2)