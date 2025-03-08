def test_config():
    return True
def get_options_ratio(name_options,total):
    #this function gets the option ratio
    name_options=float(input('enter name option'))
    total=float(input('enter total'))
    ratio=name_options/total
    return ratio
def get_faculty_rating(ratio):
    #this function gets the faculty rating
    if ratio>=.9:
        if ratio<1:
            print('excellent')
    elif ratio>=.8:
        print('very good')
    elif ratio>=.7:
        print('good')
    elif ratio>=.6:
        print('needs improvement')
    else:
        if ratio<.59:
            if ratio>0:
                print('unacceptable')
            else:
                print('out of range')
            