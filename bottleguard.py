import os 
os.system('cls')

while True:
    print("""
    ======================================
    -          BOTTLEGUARD V1.0           -
    --------------------------------------
    -      QUALITY INSPECTION SYSTEM      -
    ======================================
          """)
    
    print("[1] Start Inspection")
    print("[2] System Information")
    print("[3] Exit\n")
    
    user_input = input("Enter Choice : ").lower()

    if user_input == '1' or user_input == 'start inspection':
        print('===============================')
        print("===> INSPECTION IS STARTED <===")
        print('===============================')
        
        bottle_input = input("IS THE BOTTLE DETECTED?(y/n) : ").lower()
        
        if bottle_input == 'y' or bottle_input == 'yes':
                cap_input = input("ARE THE BOTTLE CAPS DETECTED?(y/n) : ").lower()
                if cap_input == 'y' or cap_input == 'yes':
                    height_bottle = float(input("INPUT HEIGHT OF BOTTLE : "))
                    width_bottle = float(input("INPUT WIDTH OF BOTTLE : "))
                    
                    if (height_bottle < 10 or height_bottle > 20) and width_bottle < 5:
                        print("==========================================")
                        print('==========> INSPECTION RESULT <===========')
                        print("==========================================")
                        
                        print('Bottle Presence : Detected')
                        print('Cap Detection   : Detected')
                        print(f'Bottle Height  : {height_bottle}cm - FAILED')
                        print(f'Width Bottle   : {width_bottle}cm - FAILED')
                        
                        print('==========================================')
                        print('=======> FINAL RESULT : REJECTED <========')
                        print('==========================================')
                    elif height_bottle < 10 or height_bottle > 20:
                        print("==========================================")
                        print('==========> INSPECTION RESULT <===========')
                        print("==========================================")
                                            
                        print('Bottle Presence : Detected')
                        print('Cap Detection   : Detected')
                        print(f'Bottle Height  : {height_bottle}cm - FAILED')
                        print(f'Width Bottle   : {width_bottle}cm')
                                            
                        print('==========================================')
                        print('=======> FINAL RESULT : REJECTED <========')
                        print('==========================================')
                    elif width_bottle < 5:
                        print("==========================================")
                        print('==========> INSPECTION RESULT <===========')
                        print("==========================================")
                                                                
                        print('Bottle Presence : Detected')
                        print('Cap Detection   : Detected')
                        print(f'Bottle Height  : {height_bottle}cm')
                        print(f'Width Bottle   : {width_bottle}cm - FAILED')
                                                                
                        print('==========================================')
                        print('=======> FINAL RESULT : REJECTED <========')
                        print('==========================================')
                    elif height_bottle >= 10 and height_bottle <= 20 and width_bottle >= 5:
                        print("==========================================")
                        print('==========> INSPECTION RESULT <===========')
                        print("==========================================")
                                                                                    
                        print('Bottle Presence : Detected')
                        print('Cap Detection   : Detected')
                        print(f'Bottle Height  : {height_bottle}cm')
                        print(f'Width Bottle   : {width_bottle}cm')
                                                                                    
                        print('==========================================')
                        print('=======> FINAL RESULT : ACCEPTED <========')
                        print('==========================================')
                elif cap_input == 'n' or cap_input == 'no':
                    height_bottle = float(input("INPUT HEIGHT OF BOTTLE : "))
                    width_bottle = float(input("INPUT WIDTH OF BOTTLE : "))
                    if (height_bottle < 10 or height_bottle > 20) and width_bottle < 5:
                        print("==========================================")
                        print('==========> INSPECTION RESULT <===========')
                        print("==========================================")
                                            
                        print('Bottle Presence : Detected')
                        print('Cap Detection   : Not Detected')
                        print(f'Bottle Height  : {height_bottle}cm - FAILED')
                        print(f'Width Bottle   : {width_bottle}cm - FAILED')
                                            
                        print('==========================================')
                        print('=======> FINAL RESULT : REJECTED <========')
                        print('==========================================')
                    elif height_bottle < 10 or height_bottle > 20:
                        print("==========================================")
                        print('==========> INSPECTION RESULT <===========')
                        print("==========================================")
                                                            
                        print('Bottle Presence : Detected')
                        print('Cap Detection   : Not Detected')
                        print(f'Bottle Height  : {height_bottle}cm - FAILED')
                        print(f'Width Bottle   : {width_bottle}cm')
                                                            
                        print('==========================================')
                        print('=======> FINAL RESULT : REJECTED <========')
                        print('==========================================')
                    elif width_bottle < 5:
                        print("==========================================")
                        print('==========> INSPECTION RESULT <===========')
                        print("==========================================")
                                                                                
                        print('Bottle Presence : Detected')
                        print('Cap Detection   : Not Detected')
                        print(f'Bottle Height  : {height_bottle}cm')
                        print(f'Width Bottle   : {width_bottle}cm - FAILED')
                                                                                
                        print('==========================================')
                        print('=======> FINAL RESULT : REJECTED <========')
                        print('==========================================')
                else:
                    print('INVALID INPUT')

        elif bottle_input == 'n' or bottle_input == 'no':
                cap_input = input("ARE THE BOTTLE CAPS DETECTED?(y/n) : ").lower()
                if cap_input == 'y' or cap_input == 'yes':
                        height_bottle = float(input("INPUT HEIGHT OF BOTTLE : "))
                        width_bottle = float(input("INPUT WIDTH OF BOTTLE : "))
                
                print("==========================================")
                print('==========> INSPECTION RESULT <===========')
                print("==========================================")
                                                                            
                print('Bottle Presence : Not Detected')
                print('Cap Detection   : Error')
                print(f'Bottle Height  : Error')
                print(f'Width Bottle   : Error')
                                                                            
                print('==========================================')
                print('=======> FINAL RESULT : REJECTED <========')
                print('==========================================')
        else:
                print("INVALID INPUT")
                print("Input Y or N")
        
    elif user_input == '2' or user_input == 'system information':
        print("=========================================")
        print('===| BOTTLEGUARD SYSTEM INFORMATION | ===')
        print("=========================================\n")
        
        print("SYSTEM NAME    : BottleGuard")
        print("VERSION        : 1.0")
        print("TYPE           : Quality Inspection")
        print("LANGUAGE       : Python")
        print("INSPECTION     : Bottle Quality Control\n")
        
        print("=========================================\n")
    elif user_input == '3' or user_input == 'exit':
        print("SYSTEM CLOSE")
        break
    else:
        print("Invalid Choice!")