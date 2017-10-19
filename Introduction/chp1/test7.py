people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):

    array = person.split(' ')
    title = array[0]
    lastname = array[-1]
    return title + lastname


print(list(map(split_title_and_name,people)))