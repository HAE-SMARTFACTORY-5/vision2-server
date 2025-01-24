from fastapi import HTTPException
import mysql.connector
from dto.myIngredient import MyIngredientResponse
from db.database import get_db_connection


def findAll():
    query = '''
        SELECT *
        FROM my_ingredient
            left join ingredient on ingredient.ingredient_id=my_ingredient.ingredient_id
        ORDER BY my_ingredient.created_at DESC
    '''
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(query)
        results = cursor.fetchall()
        
        return [
            MyIngredientResponse(
                ingredientId=row['ingredient_id'], 
                name=row['name'],
                image=row['image'],
            ) for row in results
        ]
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error fetching my_ingredient: {e}")
    finally:
        cursor.close
        connection.close
