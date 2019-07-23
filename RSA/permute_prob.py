from math import factorial
from math import pow

# of possible RSA key values
rc = pow(6, 9)
rcs = str(rc) #as string
num_digits_to_print = 15

#order matters
def permute_count(n, r):
    return factorial(n)/(factorial(n-r))

#order does not matters
def comb_count(n,r):
    fn = factorial(n)
    print("fn: ", fn)
    fr = factorial(r)
    fnr = factorial(n-r)
    return fn/(fn*fnr)

def compare(x, y):
    return x if (RSA_prob(x)>RSA_prob(y)) else y

#Taken from https://stackoverflow.com/questions/783897/truncating-floats-in-python
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

#where x is the # of occurences
#returns a string of the percentage probability
def RSA_prob( x ):
    return truncate( 100 * (x/rc), num_digits_to_print) + '%'

def check_key_validity( x ):
    print('entering check_key_validity with x as ' + x)
    if x > 999999 or x < 000000:
        print("not a possible key")
        return 0

#occurence functions:

def main():
    #print('Possible # of rsas: ' + rcs)
    print('probability of any unique entry: ' + RSA_prob(1) )
    x = raw_input('enter your key: ')
    check_key_validity(x);
    print('probability of key ' + x + ': ' + RSA_prob(float(5000)))

if __name__ == "__main__":
    main()
