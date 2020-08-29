'''pasar de lista de strings  a frase de una sola estring

%Write a function that takes a list value as an argument and returns
%a string with all the items separated by a comma and a space, with and
%inserted before the last item. For example, passing the previous spam list to
%the function would return 'apples, bananas, tofu, and cats' . But your
%function should be able to work with any list value passed to it.'''
import copy

spam=['perro','gato','sapo','rata']


def ComasEspacios(boxlist):

    NewSpam=copy.copy(boxlist)  # esto es debido a que la lista es una referencia a una
            # a una direccion de memoria, hay que duplicarla en otra direccion de memoria 
    for i in range(len(NewSpam)):
        NewSpam[i]=NewSpam[i]+','+' '
    OnlyWord=['']  #creacion de una lista de un index o un 1x1 array para meter los
                   # datos de la lista concatenados ojo indentaciones 
    for i in range(len(NewSpam)):
        OnlyWord[0]=OnlyWord[0]+NewSpam[i]  # concateno de lista a un solo string'''
    return print(OnlyWord)
ComasEspacios(spam)





    
