import re

def main():
    informe = """Informe clínico de Urgencias
    Nombre: Juan Pérez López
    Género: Hombre
    Fecha de nacimiento: 12/05/1980
    Motivo de consulta: dolor abdominal
    12/05/2023 Dr. Ramírez
    Tratamiento: reposo y analgésicos"""

    fecha = re.compile(r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b')
    
    informe = re.sub(r'Nombre:\s*.+', 'Nombre: PACIENTE', informe) 
    # . no incluye los saltos de línea por eso para después de López
    # + es porque hay más de una palabra
    
    fecha_nacimiento = re.search(r'Fecha de nacimiento:\s*(\d{1,2}/\d{1,2}/\d{4})', informe)
    dia_n, mes_n, ano_n = fecha_nacimiento.group(1).split('/')

    fecha_consulta = re.search(r'(\d{1,2}/\d{1,2}/\d{4})\s+(?:Dr\.|Dra\.)', informe)
    dia_c, mes_c, ano_c = fecha_consulta.group(1).split('/')

    dia_n, mes_n, ano_n = int(dia_n), int(mes_n), int(ano_n)
    dia_c, mes_c, ano_c = int(dia_c), int(mes_c), int(ano_c)

    edad = ano_c - ano_n
    if (mes_c, dia_c) < (mes_n, dia_n):
        edad -= 1

    informe = re.sub(r'Fecha de nacimiento:\s*\d{1,2}/\d{1,2}/\d{4}', f'Edad: {edad}', informe)
   
    informe = fecha.sub("FECHA", informe)
    informe = re.sub(r'(Dr\.|Dra\.).*', 'MEDICO', informe)
    print(informe)


if __name__ == "__main__":
    main()




















































































