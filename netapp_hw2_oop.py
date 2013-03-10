class webimptce:
    """The class of website"""
    web_id = 0 #the name of the website
    value = 0 #the valude of importance

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
#try:
#    all_the_text = file_o.read();
    #print all_the_text
#finally:
#    file_o.close()
h = []
with open('data_in.txt','r') as f:
    for num in f:
        h.append(list(map(float,num.split())));

pi = [1,0,0,0,0,0,0,0] #result

for i in range(0,8):
    for j in range(0,8):
        h[i][j] = h[i][j] * 0.85
        h[i][j] += 0.15 * 0.125
#print "h is ",h
next_pi = pi[:];
cnt = 0;
while(1):
    cnt = cnt + 1  #counter
    calc_matrix_product(h,pi,next_pi);  #to calculate next_pi
    #print cnt,next_pi,pi,"\n"
    if( judge(pi,next_pi) == 1 ):
        break;
    pi = next_pi[:];
    
for i in range(0,8):
    print "%.5f\t" % pi[i]

mylist = []
for i in range(0,8):
    mylist.append((i,pi[i])); #make pair

new_list = sorted(mylist,key = lambda mylist:mylist[1],reverse = True)
print "the sorted is: \n"
for num in new_list:
   print num[0]+1


