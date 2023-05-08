

def main():
    

    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)
    print(ideas)

    file_pointer = open("assets/ideas.txt: ")
    ideas = file_pointer.readline()
    print(ideas)
    ideas = file_pointer.readline()
    print(ideas)

main()