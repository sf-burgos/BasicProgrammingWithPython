
def selectionSort(lista):
    """"Compare N items in the list, choosing the least.
Exchange the lower encountered the top of the list.
The new list has N-1 elements, because the
ﬁrst element is the least.
Repeat the above process with the remaining elements.
""""
    for fillslot in range(len(lista)-1,0,-1):
        posicionmax=0
        for location in range(1,fillslot+1):
            if lista[location]>lista[posicionmax]:
                posicionmax = location

        temp = lista[fillslot]
        lista[fillslot] = lista[posicionmax]
        lista[posicionmax] = temp

lista=[54,26,93,17,77,31,44,55,20]
selectionSort(lista)
print(lista)
