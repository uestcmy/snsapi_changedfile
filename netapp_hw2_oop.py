def calc_matrix_product(h,pi,next_pi):
    """the fuction to calc the importance"""
    for i in range(0,8):
        tmp = 0.0
        for j in range(0,8):
            tmp += pi[j] * h[j][i];
        next_pi[i] = tmp;
def judge(pi,next_pi):
    """to compare 2 website"""
    for i in range(0,8):
        if abs(pi[i]-next_pi[i]) > 0.00000001:
            return 0;
    return 1;


file_o = open('./data_in.txt');

h = []
fout = open('./dataout.txt','w')
with open('data_in.txt','r') as f:#read the data from the file
    for num in f:
        h.append(list(map(float,num.split())));

pi = [1,0,0,0,0,0,0,0] #result
for i in range(0,8):
    for j in range(0,8):
        h[i][j] = h[i][j] * 0.85
        h[i][j] += 0.15 * 0.125
#print "h is ",h
next_pi = pi[:];#next_pi : next round of pi
cnt = 0;
while(1):
    cnt = cnt + 1  #counter
    calc_matrix_product(h,pi,next_pi);  #to calculate next_pi
    #print cnt,next_pi,pi,"\n"
    if( judge(pi,next_pi) == 1 ):
        break;
    pi = next_pi[:];

mylist = []
for i in range(0,8):
    mylist.append((i,pi[i])); #make pair

new_list = sorted(mylist,key = lambda mylist:mylist[1],reverse = True)
fout.write("The result is: \n")
for num in mylist:
   fout.write(str(num[0]+1))
   fout.write(' , ')
   fout.write(str(num[1]))
   fout.write('\n')

fout.close()
