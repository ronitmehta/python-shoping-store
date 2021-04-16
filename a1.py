list1=[]
quantities=[]
appearls_cost=0
electronics_cost=0
eatables_cost=0
tup1 = ()
tup2 = ()
tup3 = ()
tup = ()


def show_menu():
	print('===================================================')
	print('                      MY BAZAAR                   ')
	print('===================================================')
	print('Hello! Welcome to my grocery store!')
	print('Following are the Products available in the shop: ')
	print(" ")
	print('--------------------------------------------------')
	print('CODE  |  DDESCRIPTION  |  CATEEGORY   |  COST(RS) ')
	print('--------------------------------------------------')
	print('  0   |  Tshrits       |  Appereals   |  500  ')
	print('  1   |  Trousers      |  Appereals   |  600  ')
	print('  2   |  Scarf         |  Appereals   |  250  ')
	print('  3   |  Smartphone    |  Electronics |  20,000  ')
	print('  4   |  iPad          |  Electronics |  30,000  ')
	print('  5   |  Laptop        |  Electronics |  50,000  ')
	print('  6   |  Eggs          |  Eatables    |  5  ')
	print('  7   |  Chocolate     |  Eatables    |  10  ')
	print('  8   |  juice         |  Eatables    |  100  ')
	print('  9   |  Milk          |  Eatables    |  45  ')
	print('\n')
	inp1 = str(input('Would you like to buy in bulk? (y or Y for Yes , n or N for No '))
	print('\n')
	
	while True :
		if inp1=='y':
			get_bulk_input()
			break
		elif inp1=='n':
			get_regular_input()
			break
		else:
			inp1 = str(input('Would you like to buy in bulk? (y or Y for Yes , n or N for No '))


def get_regular_input():

	print('\n')
	print('-------------------------------------------------')
	print('ENTER ITEMS YOU WISH TO BUY ')
	print('-------------------------------------------------')
	
	s=input('Enter the item codes (space-separated): ')
	l0=s.split()
	
	l1=[]
	for i in range(len(l0)):
		if len(l0[i])>=2:
			print(l0[i],' is INVALID CODE ')
		
		else :
			if ord(l0[i])>=48 and ord(l0[i])<=57:
				l1.append(int(l0[i]))
			else:
				print(l0[i],' is INVALID CODE ')
	global quantities
	quantities=[l1.count(0),l1.count(1),l1.count(2),l1.count(3),l1.count(4),l1.count(5),l1.count(6),l1.count(7),l1.count(8),l1.count(9)]
	
	return quantities

        
def get_bulk_input():
	global list1 
	list1=[ ['Tshrits' , 'Appereals' , '500' ] , [ 'Trousers' , 'Appereals' , '600'] , [ 'Scarf' , 'Appereals' , '250'] , [ 'Smartphone' , 'Electronics' , '20000'] , [ 'iPad' , 'Electronics' , '30000'] , ['Laptop' , 'Electronics' , '50000'] , ['Eggs' , 'Eatables' ,'5' ] , ['Chocolate' , 'Eatables' , '10' ] , ['juice' , 'Eatables' , '100'] , ['Milk' , 'Eatables' , '45']]
	print('\n')
	print('-------------------------------------------------')
	print('ENTER ITEMS YOU WISH TO BUY ')
	print('-------------------------------------------------')
	l1=[]
	l2=[]
	while True :
		inp=input('enter code and quantity : ')
		s=inp.split()
		if inp=='':
			break	
		else :
			if len(s[0])>=2 :
				print('INVALID CODE , TRY AGAIN ')

			else :
				if ord(s[0])>=48 and ord(s[0])<=57:
					print('you added ',s[1],' ',list1[int(s[0])][0] )
					l2.append(s[0]*int(s[1]))
				else :
					print('INVALID CODE , TRY AGAIN ')
			
	for i in range(len(l2)):
		for j in l2[i] :
			l1.append(j)
	global quantities 
	quantities=[l1.count('0'),l1.count('1'),l1.count('2'),l1.count('3'),l1.count('4'),l1.count('5'),l1.count('6'),l1.count('7'),l1.count('8'),l1.count('9')]
	
	return quantities




def print_order_details(quantities):

	global list1 
	list1=[ ['Tshrits' , 'Appereals' , '500' ] , [ 'Trousers' , 'Appereals' , '600'] , [ 'Scarf' , 'Appereals' , '250'] , [ 'Smartphone' , 'Electronics' , '20000'] , [ 'iPad' , 'Electronics' , '30000'] , ['Laptop' , 'Electronics' , '50000'] , ['Eggs' , 'Eatables' ,'5' ] , ['Chocolate' , 'Eatables' , '10' ] , ['juice' , 'Eatables' , '100'] , ['Milk' , 'Eatables' , '45']]
	print('\n')
	print('-------------------------------------------------')
	print('ORDER DETAILS')
	print('-------------------------------------------------')
	lis=[]
	lis1=[]
	lis2=[]
	
	for i in range(0,10):
		if quantities[i]==0:
			continue
		lis.append(int(list1[i][2])*int(quantities[i]))
		lis1.append(quantities[i])
		lis2.append(list1[i][0])
	print(lis)
	for i in range (0,len(lis)):
		#if quantities[i]==0:
		#	continue
		print('[',i+1,']',lis2[i],"x",lis1[i]," = Rs ",lis[i])
	print('\n')
	print('TOTAL COST = ',int(sum(lis)))	


def calculate_category_wise_cost(quantities):
	global list1
	list1=[ ['Tshrits' , 'Appereals' , '500' ] , [ 'Trousers' , 'Appereals' , '600'] , [ 'Scarf' , 'Appereals' , '250'] , [ 'Smartphone' , 'Electronics' , '20000'] , [ 'iPad' , 'Electronics' , '30000'] , ['Laptop' , 'Electronics' , '50000'] , ['Eggs' , 'Eatables' ,'5' ] , ['Chocolate' , 'Eatables' , '10' ] , ['juice' , 'Eatables' , '100'] , ['Milk' , 'Eatables' , '45']]
	print('\n')
	print('-------------------------------------------------')
	print('CATEGORY-WISE COST')
	print('-------------------------------------------------')

	appearls=[]	
	electronics=[]
	eatables=[]
	for i in range(0,10):
		if i>=0 and i<=2 :
			appearls.append(int(quantities[i])*int(list1[i][2]))
		elif i>=3 and i<=5 :
			electronics.append(int(quantities[i])*int(list1[i][2]))
		else :
			eatables.append(int(quantities[i])*int(list1[i][2]))
	
	global appearls_cost
	global electronics_cost
	global eatables_cost

	appearls_cost=sum(appearls)
	electronics_cost=sum(electronics)
	eatables_cost=sum(eatables)
	if int(appearls_cost)!=0:
		print("Appereals = Rs", appearls_cost)
	
	if int(electronics_cost)!=0:
		print("Electronics = Rs",electronics_cost)

	if int(eatables_cost)!=0:
		print("Eatables = Rs",eatables_cost)

	global tup1
	tup1= (appearls_cost,electronics_cost,eatables_cost)
	return tup1



def get_discount(cost, discount_rate):
	
	return int(cost * discount_rate)



def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	print('\n')
	print('-------------------------------------------------')
	print('DISCOUNTS')
	print('-------------------------------------------------')

	list10=[]
	list11=[]

	if int(apparels_cost)>=2000:
		discounted_apparels_cost = apparels_cost - get_discount(int(apparels_cost),0.1)
		print('[APPAREL] Rs ',int(apparels_cost),' - Rs ',get_discount(int(apparels_cost),0.1),' = Rs ',int(apparels_cost) - get_discount(int(apparels_cost),0.1) )
		list11.append(get_discount(int(apparels_cost),0.1))
		
	else :
		discounted_apparels_cost=apparels_cost
		list11.append(0)
	list10.append(int(discounted_apparels_cost))


	if int(electronics_cost)>=25000:
		discounted_electronics_cost = int(electronics_cost) - get_discount(int(electronics_cost),0.1)
		print('[ELECTRONICS] Rs ',int(electronics_cost),' - Rs ', get_discount(int(electronics_cost),0.1),' = Rs ',electronics_cost - get_discount(int(electronics_cost),0.1) )
		list11.append( get_discount(int(electronics_cost),0.1))

	else :
		discounted_electronics_cost=electronics_cost
		list11.append(0)
	list10.append(discounted_electronics_cost)


	if int(eatables_cost)>=500:
		discounted_eatables_cost = eatables_cost - get_discount(int(eatables_cost),0.1)
		print('[EATABLES] Rs ',int(eatables_cost),' - Rs ',get_discount(int(eatables_cost),0.1),' = Rs ',eatables_cost - get_discount(int(eatables_cost),0.1) )
		list11.append(get_discount(int(eatables_cost),0.1))

	else :
		discounted_eatables_cost = eatables_cost
		list11.append(get_discount(int(eatables_cost),0.1))
	list10.append(discounted_eatables_cost)


	print('TOTAL DISCOUNT = Rs ', sum(list11) )
	print('TOTAL COST = Rs ',sum(list10) )

	global tup2
	tup2= (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost )
	return tup2
	



def get_tax(cost, tax):
	return int(cost * tax)



def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	print('\n')
	print('-------------------------------------------------')
	print('TAX')
	print('-------------------------------------------------')
	print('\n')
	
	list12=[]
	list13=[]

	if apparels_cost>=1:
		tax_apparels_cost = apparels_cost + get_tax(int(apparels_cost),0.1)
		print('[APPAREL] Rs ',int(apparels_cost),' * 0.1 = Rs ',  get_discount(int(apparels_cost),0.1) )
		list13.append(get_tax( (apparels_cost) , 0.1) )
		list12.append(tax_apparels_cost)

	if electronics_cost>=1:
		tax_electronics_cost = electronics_cost + get_tax(int(electronics_cost),0.15)
		print('[ELECTRONICS] Rs ',int(electronics_cost),' * 0.15 = Rs ',get_tax(int(electronics_cost),0.15) )
		list13.append( get_tax((electronics_cost),0.15))
		list12.append(tax_electronics_cost)
		
	if eatables_cost>=1:
		tax_eatables_cost = eatables_cost + get_tax(int(eatables_cost),0.05)
		print('[EATABLES] Rs ',int(eatables_cost),' * 0.05 = Rs ',get_tax(int(eatables_cost),0.05) )
		list13.append(get_tax(int(eatables_cost),0.05))
		list12.append(tax_eatables_cost)


	total_cost_including_tax = sum(list12)
	total_tax = sum(list13)

	print('\n')
	print('TOTAL COST = Rs ', total_cost_including_tax )
	print('TOTAL TAX = Rs ',total_tax)

	global tup3
	tup3 = ( total_cost_including_tax, total_tax )
	return tup3



def apply_coupon_code(total_cost):
	
	print('\n')
	print('-------------------------------------------------')
	print('COUPON CODE')
	print('-------------------------------------------------')
	list15=[]

	inp4=input('Enter coupon code (else leave blank): ')
	while True :
		if inp4=='HELLE25' and int(total_cost)>=5000:
			print('[HELLE25] offers ',min(5000,( int(total_cost) *0.25)))
			print('TOTAL COUPON DISCOUNT = Rs ',min(5000, (int(total_cost)) *0.25 ) )
			print('TOTAL COST = Rs ',( int(total_cost) ) - int(min(5000,( ( int(total_cost) ) *0.25))))
			list15.append(min(5000, (int(total_cost)) *0.25 ) )
			break

		elif inp4=='CHILL50' and int(total_cost)>=10000:
			print('[CHILL50] offers ' ,min(10000,(int(total_cost)*0.5)) )
			print('TOTAL COUPON DISCOUNT = Rs ',min(10000, (int(total_cost)) *0.5 ) )
			print('TOTAL COST = Rs ',(int(total_cost))-min(10000,((int(total_cost))*0.5)))
			list15.append(min(10000, (int(total_cost)) *0.5 ) )
			break

		elif inp4=='CHILL50' and int(total_cost) <10000:
			print('YOU ARE NOT ELIGIBLE \n TOTAL COUPON DISCOUNT = Rs 0' )
			print('TOTAL COST = Rs ',( int(total_cost)) )
			list15.append(0)
			break
		
		elif inp4=='HELLE25' and int(total_cost)<5000:
			print('TOTAL COUPON DISCOUNT = Rs 0' )
			print('TOTAL COST = Rs ',( int(total_cost)))
			list15.append(0)
			break
			

		elif inp4=='':
			print('No coupon code applied.')
			print('\n')
			print('TOTAL COUPON DISCOUNT = Rs 0')
			print('TOTAL COST = Rs ',int(total_cost))
			break 
		else :
			print('Invalid coupon code. Try again.')
			inp4=input('Enter coupon code (else leave blank): ')

	total_discount=int(sum(list15))

	print("\nThank you for visiting!")
	global tup
	tup=(total_cost,total_discount)
	return tup


def main():
	show_menu()
	print_order_details(quantities)
	calculate_category_wise_cost(quantities)
	calculate_discounted_prices(tup1[0] , tup1[1] , tup1[2])
	calculate_tax(tup2[0], tup2[1], tup2[2])
	apply_coupon_code(tup3[0])
	
if __name__ == '__main__':
	main()



