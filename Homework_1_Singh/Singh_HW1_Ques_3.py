#Name:Pratik Singh
#Student id: 1001670417

noOfPackages = int(input('Enter the number of packages:'))
discount = '0'

if noOfPackages >=10 and noOfPackages <=19:
    discount = '10%'
    purchaseAmount = 99 * noOfPackages - (0.1 * 99 * noOfPackages)
    print('Amount of discount: ', discount)
    print('Amount of purchase: $', purchaseAmount)
elif noOfPackages >=20 and noOfPackages <=49:
    discount = '20%'
    purchaseAmount = 99 * noOfPackages - (0.2 * 99 * noOfPackages)
    print('Amount of discount: ', discount)
    print('Amount of purchase: $', purchaseAmount)
elif noOfPackages >=50 and noOfPackages <=99:
    discount = '30%'
    purchaseAmount = 99 * noOfPackages - (0.3 * 99 * noOfPackages)
    print('Amount of discount: ',discount)
    print('Amount of purchase: $', purchaseAmount)
elif noOfPackages >=100:
    discount = '40%'
    purchaseAmount = 99 * noOfPackages - (0.4 * 99 * noOfPackages)
    print('Amount of discount: ', discount)
    print('Amount of purchase: $', purchaseAmount)
else:
    purchaseAmount = 99 * noOfPackages
    print('Amount of discount: ', discount)
    print('Amount of purchase:$',purchaseAmount)
                   
