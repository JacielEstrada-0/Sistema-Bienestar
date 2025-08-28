#1. Estructura de Datos
fechas = ["24/11/2003","25/11/2003","26/11/2003"]
horas_sueño = [8,12,9]
vasos_agua = [6,8,4]
minutos_actividad = [15,30,45]
niveles_estres = [7,2,4]
estado_animo = ["Neutral","Contento","Triste"]
opciones_animo = ["Muy Triste" , "Triste" , "Neutral" , "Contento" , "Muy Contento"]
opcion=0
suma_sueño=0
suma_agua=0
suma_actividad=0
suma_estres=0
indice_a_eliminar=0 #Todas las variantes necesarias para el sistema
#2. Menú Principal
while opcion==0:
    print("=================================")
    print("||      Menú Principal         ||")
    print("=================================")
    print("1-Registrar datos de hoy")
    print("2-Ver historial de datos")
    print("3-Análisis de bienestar")
    print("4-Recomendaciones personalizadas")
    print("5-Eliminar un registro")
    print("6-Salir")

#3. Funcionalidades Específicas 3.1 Registrar datos de hoy
    opcion = int(input("Seleccione una opcion valida: "))
#-------------------------------------------Registrar Datos de Hoy-------------------------------------------
    if opcion == 1:  
    
        print("=========================================")
        print("||     REGISTRAR DATOS DE HOY          ||")
        print("=========================================")
        for fecha in fechas:  
            fecha = input("Indica la fecha (DD/MM/AAAA): ")  # Solicita la fecha
            if fecha == fecha in fechas:# Verifica si la fecha ya existe en la lista
                print("La fecha ya está en el sistema. Indique otra.")
            else:
                if len(fecha) == 10 and fecha[2] == '/' and fecha[5] == '/':
                    fechas.append(fecha)  # Agrega la fecha a la lista si no está repetida
                    print("La fecha se ha añadido al sistema.")
                    break
                else:
                    print("Ingrese una fecha y formato correcta")
        while True:
            if len(fechas)==0:
                break
            try:
                h_sueño = float(input("Indique las horas que duerme: "))
                if 0 <= h_sueño <= 24:
                    horas_sueño.append(h_sueño)
                    print("Se han anadido sus horas de sueno")
                    break  # Salir del bucle si la entrada es válida
                else:
                    print("Por favor, ingrese un número entre 0 y 24.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número válido.")
        while True:
            if len(horas_sueño)==0:
                break
            try:
                vasagua = int(input("Cantidad de vasos con agua que toma a diario:"))
                if 0<=vasagua<=20 :  # Aseguramos que la cantidad de vasos sea positiva
                    vasos_agua.append(vasagua)
                    print("Cantidad de vasos con agua anadidos")
                    break  # Si es válida, se sale del bucle
                else:
                    print("Por favor, ingrese un número entre 0 y 20.")
            except ValueError:
                print("Por favor, ingrese un número entero positivo.")
        while True:
            if len(vasos_agua)==0:
                break
            try:
                minacti = int(input("Indique el tiempo de actividad en minutos:"))
                if minacti > 0:  # Aseguramos que el tiempo de actividad sea positiva
                    minutos_actividad.append(minacti)
                    print("Sus minutos de actividad se anadieron")
                    break  # Si es válida, se sale del bucle
                else:
                    print("Por favor, ingrese un número entre mayor a 0.")
            except ValueError:
                print("Por favor, ingrese números enteros positivos.")
        while True:
            if len(minutos_actividad)==0:
                break
            try:
                n_estres = int(input("Indique su nivel de estres del 1 al 10:"))
                if 1<= n_estres <= 10:
                    niveles_estres.append(n_estres)
                    print("Su nivel de estres se anadio")
                    break  # Si se ingresa correctamente, se sale del bucle
                else:
                    print("Por favor, ingrese un número entre 1 y 10 .")
            except ValueError:
                print("Por favor indique un numero entre 1 y 10:")
        while True:
            if len(niveles_estres)==0:
                break
            try:
                print("Opciones de estado de ánimo:")
                for opcion in opciones_animo:  # Recorre la lista opciones_animo y por cada opción la imprime en la consola, una por una.
                    print(opcion)
                opanimo = input("Indique su estado de ánimo: ")  # Pedimos la entrada del usuario
                if opanimo in opciones_animo:  # Verifica si el estado de ánimo es válido
                    estado_animo.append(opanimo)
                    print("Su estado de animo se añadio")
                    break  # Si la entrada es válida, salimos del bucle
                else:
                    print("Indique un estado de ánimo válido.")  # Mensaje si no es válido
            except ValueError:  # Captura cualquier otro tipo de error
                print("Ocurrió un error. Intente de nuevo.")
        opcion=0
#-------------------------------------------Historial de Datos------------------------------------------#
    if opcion == 2:
    # 3.2 Ver historial de datos
        print("=========================================")
        print("||        HISTORIA DE DATOS            ||")
        print("=========================================")
        if len(fechas)==0:  # Si la lista fechas está vacía
            print("No hay registros disponibles.")
            while True:
                opcion=int(input("Ingrese 0 para volver al menú: "))
                if opcion==0:
                    break
                elif opcion!=0:# hacer que el usuario introduzca 0
                    print("Por favor ingrese un valor válido")
        elif len(horas_sueño) and len(vasos_agua) and len(minutos_actividad) and len(niveles_estres)>= 1:
            while True:
                print("\nHistorial de Datos Registrados:")
                for indice in range(len(fechas)):  # Recorremos los índices de las listas
                    print(f"Fecha: {fechas[indice]} | Horas de sueño: {horas_sueño[indice]} | Vasos de agua: {vasos_agua[indice]} | Minutos de actividad: {minutos_actividad[indice]} | Estrés: {niveles_estres[indice]} | Estado de ánimo: {estado_animo[indice]}\n")
                opcion=int(input("Ingrese 0 para volver al menú: "))
                if opcion==0:
                    break
                else:# hacer que el usuario introduzca 0
                    print("Por favor ingrese un valor válido")
#-----------------------------------Análisis de Bienestar----------------------------------------------#
    if opcion==3:
        print("=========================================")
        print("||      ANÁLISIS DE BIENESTAR          ||")
        print("=========================================")
        for h_sueño in horas_sueño:
            suma_sueño += h_sueño/len(horas_sueño)
        for vasagua in vasos_agua:
            suma_agua+= vasagua/len(vasos_agua)
        for minacti in minutos_actividad:
            suma_actividad += minacti/len(minutos_actividad)
        for n_estres in niveles_estres:
            suma_estres += n_estres/len(niveles_estres) #Suma los valores de las listas y luego los divide entre la cantidad total en la lista
            print("\nEL promedio de cada registro es el siguiente\n")
            print(f"Promedio Horas de sueño:\n{(suma_sueño)}\n\nPromedio Vasos de Agua:\n{(suma_agua)}\n\nPromedio Minutos de Actividad\n{(suma_actividad)}\n\nPromedio Niveles de Estres\n{(suma_estres)}")
            if len(horas_sueño) and len(vasos_agua) and len(minutos_actividad) and len(niveles_estres)>=3:#Si en cada lista hay almenos 3 items, se ejecuta      
                print("\nTiempo de sueño:")
                if horas_sueño[-1]>horas_sueño[-3]:#Dependiendo de los datos, imprime uno u otro resultado
                    print("[✓] Tu tiempo de sueño ha mejorado")
                elif horas_sueño[-1]<horas_sueño[-3]:
                    print("[✕] Tu tiempo de sueño ha disminuido")
                else:
                    print("[=] Tienes un tiempo de sueño estable")
                print("\nConsumo de agua:")
                if vasos_agua[-1]>vasos_agua[-3]:
                    print("[✓] Excelente, hoy bebiste más agua")
                elif vasos_agua[-1]<vasos_agua[-3]:
                    print("[✕] Hoy no llegaste al mínimo recomendado de agua")
                else:
                    print("[=] Muy bien, tu consumo de agua permanece igual")
                print("\nTiempo de actividad:")
                if minutos_actividad[-1]>minutos_actividad[-3]:
                    print("[✓] Hoy te mantuviste bastante activo")
                elif minutos_actividad[-1]<minutos_actividad[-3]:
                    print("[✕] Hoy no llegaste a la meta de 30 minutos")
                else:
                    print("[=] Lo estás haciendo bien, sigue así")
                print("\nNiveles de estres:")
                if niveles_estres[-1]>niveles_estres[-3]:
                    print("[✕] Hoy estas más estresado...Eso no es bueno")
                elif niveles_estres[-1]<niveles_estres[-3]:
                    print("[✓] Hoy disminuiste tus niveles de estrés, sigue así")
                else:
                    print("[=] Hoy no hubo variaciones en tu estrés")
            opcion=int(input("Ingrese 0 para volver al menú: "))
            if opcion==0:
                    break
            elif opcion!=0:# hacer que el usuario introduzca 0
                print("\nPor favor ingrese un valor válido")
#-----------------------------------Recomendaciones Personalizadas--------------------------------------------#
    if opcion==4:
        print("=========================================")
        print("||  RECOMENDACIONES PERSONALIZADAS     ||")
        print("=========================================")
        if len(fechas)>=1:#Si hay almenos 1 item en la lista, se ejecuta
            if horas_sueño[-1]<7:#Según el registro más reciente,imprime una recomendación
                print("\nHoy has dormido menos de lo recomendado, intenta acostarte 30 minutos antes hoy")
            elif horas_sueño[-1]>9:
                print("\nHoy dormiste más de lo que deberias, esto puede afectar tu energía")
            else:
                print("\nMuy bien, hoy has dormido el tiempo recomendado")
            if vasos_agua[-1]<8:
                print("\nPoco consumo de agua, es recomendable mas de 8 vasos al dia")
            else:
                print("\nMuy bien, llevas un buen consumo de agua")
            if minutos_actividad[-1]<30:
                print("\nEs recomendable hacer mínimo 30 minutos de ejercicio al día")
            else:
                print(f"\nMuy bien hoy hiciste {[minutos_actividad[-1]]} minutos de actividad, sigue así")
            if niveles_estres[-1]<=3:
                print("\nTienes niveles estables de estres, sigue con una rutina saludable\n")
            elif niveles_estres[-1]<=6:
                print("\nTienes niveles en un rango medio, medita y realiza ejercicios de relajacion\n")
            elif niveles_estres[-1]<=10:
                print("\n Consulte ayuda profesional y priorice su bienestar, niveles de estres alto\n")
        while True:
            opcion=int(input("Ingrese 0 para volver al menú: "))
            if opcion==0:
                break
            elif opcion!=0:# hacer que el usuario introduzca 0
                print("Por favor ingrese un valor válido")
#------------------------------------Eliminar un Registro-----------------------------------------------#
    if opcion==5:
        print("=========================================")
        print("||       ELIMINAR REGISTRO             ||")
        print("=========================================")
        if len(horas_sueño) and len(vasos_agua) and len(minutos_actividad) and len(niveles_estres)==0:#Si no hay registros, no avanza
            print("No hay datos registrados")
            opcion=("Ingrese 0 para volver al menú: ")
            if opcion==0:
                break
            elif opcion!=0:# hacer que el usuario introduzca 0
                print("Por favor ingrese un valor válido")
        elif len(horas_sueño) and len(vasos_agua) and len(minutos_actividad) and len(niveles_estres)>0:#Si hay mas de un registro, ejecuta
            while True:
                for indice in range(len(fechas)):
                    print(f"Indice: {indice}\nFecha: {fechas[indice]},| Horas de sueño: {horas_sueño[indice]} | Vasos de agua: {vasos_agua[indice]} | Minutos de actividad: {minutos_actividad[indice]} | Estrés: {niveles_estres[indice]} | Estado de ánimo: {estado_animo[indice]}\n")
                try:
                    indice_a_eliminar = int(input("Digite el Índice a eliminar o digite -1 para salir: "))
                    
                    if indice_a_eliminar == -1:
                        opcion=0
                        break
                    
                    if 0 <= indice_a_eliminar < len(fechas):
                        # Eliminar todos los elementos del índice especificado
                        fechas.pop(indice_a_eliminar)
                        horas_sueño.pop(indice_a_eliminar)
                        vasos_agua.pop(indice_a_eliminar)
                        minutos_actividad.pop(indice_a_eliminar)
                        niveles_estres.pop(indice_a_eliminar)
                        estado_animo.pop(indice_a_eliminar)
                        print("El registro a sido eliminado")
                    else:
                        print("El indice no esta dentro del rango, ingrese un indice válido")
                    
                except ValueError:
                    print("Por favor ingrese un número válido.")
#----------------------------------Salir del Programa-------------------------------------------------#
    if opcion==6:
        print(">>> >>> >>> SALIENDO DEL SISTEMA <<< <<< <<<")
        print("Gracias por confiar en el SSBP\n¡Te esperamos pronto!")
        break