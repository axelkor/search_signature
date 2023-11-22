def seacrh(file_name,file_signature):
    signature_file = open(file_signature, "r")
    file_for_check=open(file_name,"r")
    text=file_for_check.read()
    for i in signature_file:
        if i.strip() in text:
            print(i)
            print("true")
            break
    else:
        print("false")
seacrh("testing.txt","signature.txt")