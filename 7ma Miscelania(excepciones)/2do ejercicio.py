'''Solucionar el siguiente problema usando excepciones'''

blog_posts = [{'Photos': 3, 'Me gusta': 21, 'comentarios': 2}, 
              {'Me gusta': 13, 'comentarios': 2, 'compartido': 1}, 
              {'Photos': 5, 'Me gusta': 33, 'comentarios': 8, 'compartido': 3},
              {'comentarios': 4, 'compartido': 2}, 
              {'Photos': 8, 'comentarios': 1, 'compartido': 1},
              {'Photos': 3, 'Me gusta': 19, 'comentarios': 3}]

total_Megusta = 0

for post in blog_posts:
    try:
        total_Megusta+=post['Me gusta']
    except KeyError:
        print('No contiene la palabra clave "Me gusta"')
print('El total de me gustas es',total_Megusta)