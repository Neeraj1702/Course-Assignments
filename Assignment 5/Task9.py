# Create a Dictionary of Students

Dict={'Mike' : '79', 'Ron' : '58','Sally' : '51','Tony': '85', 'Astor' : '97', 'Cody': '83'}
user=input('Enter Student name:')
if user in Dict:
    print(f"{user}'s Marks: {Dict.get(user)}")
else:
    print(f"{user} not found")