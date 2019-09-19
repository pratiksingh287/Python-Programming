#Name:Pratik Singh
#Student id: 1001670417

print('The following table shows conversion of Celsius to Farenheit')
print( 'between 0 and 20 degrees Celsius.')
print('')
print('Celsius\t   Farenheit')
print('____________________')
for num in range(1,21):
    to_Farhenite= 9/5*(num)+ 32
    print(" %.f  :   %.2f" % (num, to_Farhenite))
