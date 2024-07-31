import inquirer
from pymongo import MongoClient
from datetime import datetime

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


def storeAction(actions):
    # Connect to MongoDB
    myclient = pymongo.MongoClient('mongodb+srv://joewildtoybox:<WbGeAQOlWhTPGtU9>@jwdb.zfw3yct.mongodb.net ')  #Adjust this if your MongoDB is not on localhost
    mydb = myclient['actions_database']  # Create or use a database named 'actions_database'
    collection = mydb['Mydb']  # Create or use a collection named 'user_actions'

    # Prepare the document to insert
    document = {
        "date": datetime.now(),
        "actions": actions
    }

    # Insert the document into the collection
    result = collection.insert_one(document)

    print(f"Actions stored successfully with ID: {result.inserted_id}")


    print(myclient.Mydb())

# Usage
if __name__ == "__main__":
    actions = promptAction()
    storeAction(actions)