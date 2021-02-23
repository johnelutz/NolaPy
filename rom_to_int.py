
rom = input("Enter your Roman Numeral: ")

def rom_to_int(rom):
    rom_num_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    mid_list = []
    thru_list = []

    for i in rom:
        mid_list.append(i)

    for i in range((len(rom)-1)):
        if mid_list[i] == 'I':
            if mid_list[(i+1)] in ['V','X']:
                    x = -rom_num_dict.get('I')
            else:
                x = rom_num_dict.get('I')
        if mid_list[i] == 'V':
            x = rom_num_dict.get('V')
        if mid_list[i] == 'X':
            if mid_list[(i+1)] in ['L','C']:
                x = -rom_num_dict.get('X')
            else:
                x = rom_num_dict.get('X')
        if mid_list[i] == 'L':
            x = rom_num_dict.get('L')
        if mid_list[i] == 'C':
            if mid_list[(i+1)] in ['D','M']:
                x = -rom_num_dict.get('C')
            else:
                x = rom_num_dict.get('C')
        if mid_list[i] == 'D':
            x = rom_num_dict.get('D')
        if mid_list[i] == 'M':
            x = rom_num_dict.get('M')
        thru_list.append(x)
        
    thru_list.append(rom_num_dict.get(mid_list[-1]))

    print(sum(thru_list))

rom_to_int(rom)
        
