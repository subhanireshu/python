np=5
nb=2
sc=True
for pc in range(1,np+1):
    for bc in range(1,nb+1):
        if(sc==True):
            print("Security check for Passanger:", pc, "bag:", bc, "cleared")
        else:
            print("Not checked")
