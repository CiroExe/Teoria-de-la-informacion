import ej14
import ej15

mensaje1 = ".;.:.:.::;:,::.;:,::,;,:;.:.;.;;:,.::.:,.:.;:::::."
mensaje2 = "+-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+"
mensaje3 = "]]]([[]))([(])]([]([([([)([([([[([))][([([[([)([(]"
mensaje4 = ";;,;,;:,,,.;,,.,,,::,;;;,:;.,,;:,,,:..;,;;.,;,,.:;"
mensaje5 = "-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//"
mensaje6 = ")[))[([()))()[[]](([[)))])))][))(][)[[[)()]))[)[])"

mensajes = [
    ("a", mensaje1),
    ("b", mensaje2),
    ("c", mensaje3),
    ("d", mensaje4),
    ("e", mensaje5),
    ("f", mensaje6),
]

for inc, msg in mensajes:
    mat = ej15.getMatTransicion(msg)
    alfabeto = ej15.getAlfabeto(msg)

    if ej15.es_memoria_nula(mat):
        tipo = "Fuente de memoria nula"
        # ¡OJO AQUÍ!: Se pasa 'msg', NO 'mensaje1' ni 'mensaje4'
        h = ej14.calcular_entropia_memoria_nula(msg, alfabeto)
    else:
        tipo = "Fuente con memoria    "
        vec_est = ej14.vector_estacionario(mat)
        h = ej14.calcular_entropia_fuente(vec_est, mat)

    print(f"{inc})_ {tipo}        H(S) = {h} bits")