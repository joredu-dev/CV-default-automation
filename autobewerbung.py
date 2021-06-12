''' Este programa pretende automatizar el proceso de organizar las solicitudes de empleo
    por empresas '''

import os, shutil
from subprocess import call


ruta ='/home/jmoram/Documents/Bewerbung'
lebenslauf = '/home/jmoram/Documents/Bewerbung/Lebenslauf_J.E.MoraMontes.docx' #Path of CV File
Anschreiben = '/home/jmoram/Documents/Bewerbung/Anschreiben_J.E.MoraMontes.docx'
Zeugnisse = '/home/jmoram/Documents/Bewerbung/Zeugnisses.pdf'
Azubi_Anschreiben = '/home/jmoram/Documents/Bewerbung/Anschreiben_azubi.docx'


# Funcion para elegir el directorio de trabajo dependiendo del tipo de Bewerbung, navega al path seleccionado y devuelve la ruta
def path_wahl():  # Funcion para elegir el tipo de Bewerbung 
    job_path = '/home/jmoram/Documents/Bewerbung/Job'
    azubi_path = '/home/jmoram/Documents/Bewerbung/Ausbildung'
    type_bewerbung = int(input('Bewerbung um  Job oder Ausbildung:\n 1. Job\n 2. Ausbildung\n '))
    if type_bewerbung == 1:
        os.chdir(job_path)
        return job_path
    elif type_bewerbung == 2:
        os.chdir(azubi_path)
        return azubi_path

#def file_directoy():
#    job_file_lebenslauf = lebenslauf
#    azubi_file_lebenslauf = lebenslauf
#    job_file_anschreiben = Anschreiben
#    azubi_file_anschreiben = Azubi_Anschreiben



# Funtion to create la carpeta segun la ruta y el nombre defidos en la funtion create_work_directory
def navegator(path,name): # funcion para crear carpetas y mover en a la ruta
    os.mkdir(name)
    name_path = path + '/' + name 
    os.chdir(name_path)

# Solicita los nombre de los nuevo directorio, se move la ruta con la ayuda de navegator y copia los archivos desde la ruta master.
def create_work_directory(path):  # path viene la funcion path_wahl
    print('Configurando directorios y documentos\n')
    firma = input('Nombre de la firma: ')
    navegator(path,firma)
    arbeitstelle = input('Nombre del puesto: ')
    work_path = os.getcwd()
    navegator(work_path,arbeitstelle)
    shutil.copy(lebenslauf, '.')# copia los archivos desde la ruta master
    shutil.copy(Anschreiben,'.')
    shutil.copy(Zeugnisse,'.')
    work_path = os.getcwd()  #Actualiza la ruta de trabajo
    return work_path

#Muestra la lista de los archivo, me permite elegir el archivo a editar, lo abre.
def open_file(work_path):
    ls_file = os.listdir(work_path)                      # guarda la lista de los archivos disponible
    indice = list(range(len(ls_file)))                  # genera la un indice para mostrar
    input_list = dict(zip(indice,ls_file))             # Convierte a tipo diccionario para luego accder al por su llave
    for num, name_file  in input_list.items():           # Muestra las opciones
        print(str(num) + '.' + name_file)
    file_to_edit = input_list[int(input('Choose the file to edit: '))] # Obtenemos el nombre del archivo
    open_cmd = ['xdg-open', file_to_edit] # comando xdg-open abre el archivo con el programa prederterminado del sistema + nombre del archivo
    call(open_cmd) # ejecuta el comando con el nombre de archivo recuperdo y elegido
    nautilus_cmd = ['nautilus', '-s', work_path]
    call(nautilus_cmd)


def main():
    
    open_file(create_work_directory(path_wahl()))

if __name__ == '__main__':
    main()
