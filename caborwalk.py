n,v1,v2 = input().split()

n = int(n)
v1 = int(v1)
v2 = int(v2)

st_d = pow(2,1/2)*n
st_t = st_d/v1

el_d = 2*n
el_t = el_d/v2

if(st_t<el_t):
    print("Walk")
else:
    print("Cab")