# 要計算數學公式，所以匯入數學的 module
import math

while True:
	# 印出可以讓使用者觀看的 menu
    print('\nChoose the math operation:\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Lograithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n')
    
    # 讓使用者自己輸入想要使用的數學運算
    choose = input('\nYour option from the menu is: ')
    
    # 加法
    if choose == '0':
        num1 = float(input('\nFirst value is: '))
        num2 = float(input('\nSecond value is: '))
        print('\nThe result is: ' + str(num1 + num2) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        # 如果使用者不想繼續使用這個計算機，則直接跳出 loop
        if back == 'y':
            continue
        else:
            break
    
    # 減法        
    elif choose == '1':
        num1 = float(input('\nFirst value is: '))
        num2 = float(input('\nSecond value is: '))
        
        print('\nThe result is: ' + str(num1 - num2) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 乘法        
    elif choose == '2':
        num1 = float(input('\nFirst value is: '))
        num2 = float(input('\nSecond value is: '))
        
        print('\nThe result is: ' + str(num1 * num2) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 除法    
    elif choose == '3':
        num1 = float(input('\nFirst value is: '))
        num2 = float(input('\nSecond value is: '))
        
        print('\nThe result is: ' + str(num1 / num2) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 取餘數        
    elif choose == '4':
        num1 = float(input('\nFirst value is: '))
        num2 = float(input('\nSecond value is: '))
        
        print('\nThe result is: ' + str(num1 % num2) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 平方
    elif choose == '5':
        num1 = float(input('\nFirst value is: '))
        num2 = float(input('\nSecond value is: '))
        
        print('\nThe result is: ' + str(math.pow(num1,num2)) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 取完全平方根        
    elif choose == '6':
        num1 = float(input('\nEnter value for extracting the square root: '))
    
        print('\nThe result is: ' + str(math.sqrt(num1)) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 取log，並以2為底
    elif choose == '7':
        num1 = float(input('\nEnter value for calculatin the logarithm to base 2: '))
    
        print('\nThe result is: ' + str(math.log(num1,2)) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 三角函數 - sin        
    elif choose == '8':
        num1 = float(input('\nEnter value (in degree) for calculating the sine: '))
        
        print('\nThe result is: ' + str(math.sin(math.radians(num1))) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 三角函數 - cos
    elif choose == '9':
        num1 = float(input('\nEnter value (in degree) for calculating the cosine: '))
        
        print('\nThe result is: ' + str(math.cos(math.radians(num1))) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 三角函數 - tan
    elif choose == '10':
        num1 = float(input('\nEnter value (in degree) for calculating the tangent: '))
        
        print('\nThe result is: ' + str(math.tan(math.radians(num1))) + '\n')
        
        back = input("\nGo back to the main menu? (y/n)")
        
        if back == 'y':
            continue
        else:
            break
    
    # 如果當使用者輸入的運算值，並非在 0-10之間，則回傳錯誤選擇，並回到原始的menu
    else:
        print('\nInvalid option\n')
        continue