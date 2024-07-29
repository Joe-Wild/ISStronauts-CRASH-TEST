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
    client = MongoClient('mongodb://localhost:27017/')  # Adjust this if your MongoDB is not on localhost
    db = client['actions_database']  # Create or use a database named 'actions_database'
    collection = db['user_actions']  # Create or use a collection named 'user_actions'

    # Prepare the document to insert
    document = {
        "date": datetime.now(),
        "actions": actions
    }

    # Insert the document into the collection
    result = collection.insert_one(document)

    print(f"Actions stored successfully with ID: {result.inserted_id}")

# Usage
if __name__ == "__main__":
    actions = promptAction()
    storeAction(actions)