'''- Detetrminar que tipo de palabra es: aguda, grave, 
esdrujula sobre esdrujula
'''
def aguda1(strr):
    vo_d=['ad','ed','id','od','ud','AD','ED','ID','OD','UD']
    vo_r=['ar','er','ir','or','ur','AR','ER','IR','OR','UR']
    vo_l=['al','el','il','ol','ul','AL','EL','IL','OL','UL']
    vo_z=['az','ez','iz','oz','uz','AZ','EZ','IZ','OZ','UZ']
    vo_n1=['án','én','ín','ón','ún','ÁN','ÉN','ÍN','ÓN','ÙN']
    vo_s1=['ás','és','ís','ós','ús','ÁS','ÉS','ÍS','ÓS','ÚS']
    vocales1=['á','é','í','ó','ú','Á','É','Í','Ó','Ú']
    for i in strr:
        if i[-1] in vocales1 or i[-2:] in vo_n1 or i[-2:] in vo_s1:
            print('La palabra\"',strr,'\" es aguda')
            break
        elif i[-2:] in vo_d or i not in vocales1:
            print('La palabra\"',strr,'\" es aguda')
            break
        elif i[-2:] in vo_l or i not in vocales1:
            print('La palabra\"',strr,'\" es aguda')
            break
        elif i[-2:] in vo_z or i not in vocales1:
            print('La palabra\"',strr,'\" es aguda')
            break
        elif i[-2:] in vo_r or i not in vocales1:
            print('La palabra\"',strr,'\" es aguda')
            break
def grave(strr):
    vocales=['a','a','i','o','u','A','E','I','O','U']
    vo_n=['n','N']
    vo_s=['s','S']
    tildes=['á','é','í','ó','ú','Á','É','Í','Ó','Ú']
    for i in strr:
        if i[-1] in vocales and i[-2:0] not in tildes:
            print('La palabra\"',strr,'\" es grave')
            break
        elif i[-1] in vo_s and i[-2:0] not in tildes:
            print('La palabra\"',strr,'\" es grave')
            break            
        elif i[-1] in vo_n and i[-2:0] not in tildes:
            print('La palabra\"',strr,'\" es grave')
            break
        elif i[0:-2] in tildes and i[-1] not in vocales:
            print(('La palabra\"',strr,'\" es grave'))
            break
        elif i[0:-2] in tildes and i[-1] not in vo_n:
            print('La palabra\"',strr,'\" es grave')
            break
        elif i[0:-2] in tildes and i[-1] not in vo_s:
            print('La palabra\"',strr,'\" es grave')
            break
def esdrujula(strr):
    tildes=['á','é','í','ó','ú','Á','É','Í','Ó','Ú']
    l_be=len(strr)//2
    l_en=len(strr)//2+2
    for i in strr:        
        if i[:l_be] in tildes:
            print('La palabra \"',strr,'\" es esdrujula')
            break
        elif i[l_be:l_en] in tildes:
            print('La palabra \"',strr,'\" es esdrujula')
            break
def s_esdrujula(strr):
    tildes=['á','é','í','ó','ú','Á','É','Í','Ó','Ú']
    l=len(strr)//2+1
    if len(strr)>=6:
        for i in strr:        
            if i[0:l] in tildes:
                print('La palabra\"',strr,'\" es sobre esdrujula')
                break
    elif len(strr)>=6:
        for i in strr:
            if i not in tildes:
                print('La palabra \"',strr,'\" no es sobre esdrujula')
                break
    elif len(strr)<6:
        print('La palabra\"',strr,'\" no es sobre esdrujula')
