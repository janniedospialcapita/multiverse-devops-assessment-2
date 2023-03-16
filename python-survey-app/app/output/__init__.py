from input import get_input

def read_output(filepath=None, data=None):

    if data is None:
        data = get_input(filepath)        

    user_id = []
    first_name = []
    last_name = []
    answer_1 = []
    answer_2 = []
    answer_3 = []

    for i in data:
        user_id.append(i[0])
        first_name.append(i[1])
        last_name.append(i[2])
        answer_1.append(i[3])
        answer_2.append(i[4])
        answer_3.append(i[5])

    user_id = [str(x) for x in user_id]
    answer_3 = [str(x) for x in answer_3]    
    
    more_space = 2


    user_id_max = len(max(user_id, key=len)) + more_space
    first_name_max = len(max(first_name, key=len)) + more_space
    last_name_max = len(max(last_name, key=len)) + more_space
    answer_1_max = len(max(answer_1, key=len)) + more_space
    answer_2_max = len(max(answer_2, key=len)) + more_space
    answer_3_max = len(max(answer_3, key=len)) + more_space

    for col in data:
        print(
            "{:<{}} {:<{}} {:<{}} {:<{}} {:<{}} {:<{}}".format(
                col[0], 
                user_id_max, 
                col[1], 
                first_name_max, 
                col[2], 
                last_name_max,
                col[3], 
                last_name_max, 
                col[4], 
                last_name_max, 
                col[5], 
                last_name_max,
                )
                )

    return data
