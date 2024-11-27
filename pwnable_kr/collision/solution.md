hashcode = 0x21DD09EC

if input = 11112222333344445555, the function will casts the input char string into an int*, meaning it interprets
every 4 bytes of the input as a single int.
Chunk Breakdown:
First 4 bytes (31 31 31 31):

Interpreted as: 0x31313131 (ASCII for 1111)
Decimal value: 825373491
Second 4 bytes (32 32 32 32):

Interpreted as: 0x32323232 (ASCII for 2222)
Decimal value: 842150450
Third 4 bytes (33 33 33 33):

Interpreted as: 0x33333333 (ASCII for 3333)
Decimal value: 858927409
Fourth 4 bytes (34 34 34 34):

Interpreted as: 0x34343434 (ASCII for 4444)
Decimal value: 875704868
Fifth 4 bytes (35 35 35 35):

Interpreted as: 0x35353535 (ASCII for 5555)
Decimal value: 892482327

The function sums up these 5 integers:

Result = 825373491 + 842150450 + 858927409 + 875704868 + 892482327

Result = 4298630545

TO GET TO THE HASH

0x21DD09EC / 5 = 6C5CEC8 + ...
6C5CEC8 * 4 = 1B173B20
21DD09EC - 1B173B20 = 6C5CECC
21DD09EC = 6C5CECC + 4(6C5CEC8) 

./col "`python -c "print '\xcc\xce\xc5\x06' + 4*'\xc8\xce\xc5\x06'"`"

flag = daddy! I just managed to create a hash collision :)
