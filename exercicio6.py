a = ["tudo bem?","como foi seu dia?","cadê você?","você gosta de banana?","como é morar no cabo?","você gosta de shopping?","sua mãe é bonita?","sua cor favorita é rosa?","você gosta do sesi?","você gosta do seu professor?"]
b = ["sim", "bom", "no salão", "sim", "bom", "sim", "sim", "não", "sim", "sim"]

nota=0

for i in range (10):
    x= input(a[i])
    if x==b[i]:
        print("parabéns, você acertou!")
        nota+=1
    else:
        print("você errou")

if nota==0:
    print(f"sua nota foi {nota}, parabéns")
else:
    print(f"sua nota foi {nota}")