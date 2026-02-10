phone = (input("phone number: ")).strip()
if phone[:].isdigit() and phone.startswith("09") and len(phone) == 10:
        print(f'+251{phone[1:]}')
elif phone.startswith("+251") and phone[1:].isdigit() and len(phone) == 13:
        print(f'09{phone[5:]}')
else:
    #raise ValueError("Invalid phone number")
    print('Invalid phone number')
