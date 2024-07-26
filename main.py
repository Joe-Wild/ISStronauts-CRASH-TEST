import inquirer

def promptAction():

    questions = [
        inquirer.List('action',
            message="qu'est ce que tu viens de faire?",
            choices=[
                "j'ai fait du sport", 
                "j'ai lu",
                "j'ai pris des photos", 
                "j'ai fait l'apéro",
                "rien, mais je veux voir mes actions"
            ]        
        )
    ]

    answers = inquirer.prompt(questions)

    return answers.get('action')


def storeAction(action):

    print('the action "' + action + "' has been stored into the database")
    print()

def getAllStoredActions():

    print("actions of today are: apero, apero , apero")



while True:

    action = promptAction()

    if action == "rien, mais je veux voir mes actions":
        getAllStoredActions()
    else:
        storeAction(action)

