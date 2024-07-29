import inquirer

def promptAction():

    questions = [
        inquirer.Checkbox('done',
            message="What have you done?",
            choices=[
                "1H Sport", 
                "30mn Reading ",
                "1H Foreign languages", 
                "30mn Pictures of Earth",
                "2H Scientific Researches"
            ]        
        )
    ]

    answers = inquirer.prompt(questions)

    return answers.get('done')


def storeAction(action):

    print['action ' + action + " has been stored into the database "]
    print()

string = "action" "done"
list_elements = ["World", "!"]
for element in list_elements:
    string += " " + element
print(string)  # Output: Hello World !



def getAllStoredActions():

    print("actions of today are: apero, apero , apero")



while True:

    action = promptAction()

    if action == "rien, mais je veux voir mes actions":
        getAllStoredActions()
    else:
        storeAction(action)

