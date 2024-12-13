from pypdf import PdfReader
import re

# Leer el archivo PDF
reader = PdfReader("Historias.pdf")

# Concatenar el texto de todas las páginas
full_text = "\n".join([page.extract_text() for page in reader.pages])

# Acortar múltiples saltos de línea que hay entre historia e historia a 2 para tener un separador homogeneo
texto = re.sub(r'(\n\s*){3,}', '\n \n', full_text)

#Separar historias
# Usamos re.split() para separar el texto en cada salto de línea
historias = re.split(r'\n \n', texto)

#Crear diccionario de historias Llave: Titulo; Valor: historia
historias_dict={}

    # Seleccionar titulo
for i in range(len(historias)):
        # Usamos re.match() para extraer la primera línea
    titulo = re.match(r'^[^\n]+', historias[i]).group(0)
        # Unimos el resto de las líneas sin saltos de línea
    lineas = historias[i].splitlines()

    # Tomamos la primera línea
    primera_linea = lineas[0]

    # Unimos el resto de las líneas sin saltos de línea
    resto_texto = ' '.join(lineas[1:])

    historias_dict[titulo] = { "title": titulo,
        "content": resto_texto
    }


"""""
{
"title": "Sol y Luna", 
"content": "Sol y Luna eran dos pequeños gatitos que habían nacido en la misma camada, pero sus  personalidades no podían ser más diferentes. Sol, de un brillante color anaranjado, era  aventurero y curioso; siempre buscando nuevas experiencias y explorando cada rincón de  su hogar. Luna, en cambio, era de un suave pelaje gris y tenía un temperamento más  sereno y observador. Pasaba horas contemplando el mundo desde la ventana, como si en  cada sombra descubriera un misterio oculto.  Una tarde, mientras Sol correteaba por el jardín persiguiendo mariposas, Luna permanecía  en el alféizar, vigilando desde lejos. De repente, una fuerte tormenta comenzó a formarse  en el horizonte. El viento sacudía las ramas de los árboles, y las gotas de lluvia empezaron  a caer pesadamente. Sol, atrapado por su espíritu inquieto, no se dio cuenta de lo rápido  que se acercaba la tormenta. Luna, desde su posición, sintió una inquietud que la hizo  saltar del alféizar y correr hacia la puerta.  Cuando Sol se dio cuenta de que estaba solo bajo la lluvia, el jardín que antes le parecía  un paraíso se volvió un laberinto de sombras y ruidos extraños. La tormenta lo había  desorientado, y por primera vez, el gatito sintió miedo. Justo cuando pensaba que no  encontraría el camino de regreso, un suave maullido lo guió. Luna había salido a buscarlo,  siguiendo su instinto y los rastros de su hermano. Juntos, bajo la lluvia, encontraron el  camino de regreso a casa, compartiendo el calor de su compañía.  De regreso al hogar, la tormenta se convirtió en un recuerdo lejano mientras los dos gatitos  se acurrucaban cerca del fuego. Sol, agotado por la aventura, dormitaba tranquilo,  mientras Luna lo vigilaba con ojos atentos. En ese momento, comprendieron que aunque  eran diferentes como el día y la noche, siempre estarían ahí el uno para el otro. Su vínculo  era más fuerte que cualquier tormenta.  Desde aquel día, Sol aprendió a valorar la calma y la paciencia que Luna representaba,  mientras que ella se permitió, de vez en cuando, dejarse llevar por la curiosidad de su  hermano. Juntos, equilibraban sus mundos, iluminando cada rincón de su hogar con la  calidez del Sol y el misterio de la Luna."
}
"""""

"""""
{
"title": "La tortuga Tica", 
"content": "Una tortuga llamada Tica vivía en un tranquilo estanque rodeado de árboles frondosos. A  diferencia de sus compañeras, Tica soñaba con explorar más allá del agua tranquila y la  suave hierba. Un día, decidió emprender una aventura, dejando atrás la comodidad de su  hogar. Se adentró en el bosque, donde todo era nuevo: el susurro de las hojas, los aromas  desconocidos y el crujir de las ramas bajo sus patas lentas pero firmes.  Durante su viaje, Tica encontró un riachuelo de corriente rápida. Al principio, la idea de  cruzarlo la asustó, pero recordó que cada desafío era una oportunidad. Con paciencia y  determinación, encontró piedras que sobresalían del agua, usándolas como un puente  improvisado. Paso a paso, logró cruzar, y al llegar al otro lado, sintió una nueva confianza  crecer en su interior. El mundo era vasto, pero cada pequeño triunfo la hacía sentir más  fuerte.  En su camino, Tica conoció a un pájaro herido que no podía volar. Sin dudarlo, decidió  ayudarlo, ofreciéndole un lugar seguro en su caparazón mientras buscaba un sitio  adecuado para él. Después de horas de marcha, encontró un árbol lleno de otros pájaros  que cuidaron de su nuevo amigo. Al despedirse, Tica comprendió que su viaje no solo era  sobre descubrir nuevos lugares, sino también sobre ayudar a otros en el camino.  Finalmente, tras días de aventuras, Tica regresó al estanque. Aunque nada había cambiado  en su hogar, ella ya no era la misma. Había descubierto que, aunque avanzaba despacio,  cada paso contaba. Su viaje le enseñó que la verdadera aventura está en el valor para  enfrentar lo desconocido y la voluntad de ayudar a otros, incluso cuando el camino es  largo y desafiante."
}
"""""

"""""
{
"title": "El Duende", 
"content": "Había un pequeño duende llamado Puck, conocido por su espíritu travieso y su amor por  las bromas. Vivía en lo profundo del bosque, donde las criaturas del lugar sabían que, si  algo extraño sucedía, era obra de él. Puck disfrutaba de hacer desaparecer objetos,  cambiar las señales de los senderos y provocar pequeñas confusiones entre los animales.  Sin embargo, su diversión nunca era malintencionada; simplemente, amaba ver las  reacciones sorprendidas de los demás.  Un día, decidió que quería jugarle una broma a la anciana hada que vivía cerca del arroyo.  Ella, conocida por su sabiduría, siempre estaba en silencio, tejiendo sueños y  pensamientos en su telar. Puck, con una sonrisa pícara, hechizó un par de hojas doradas  para que se posaran sobre el telar de la hada. Cada vez que intentaba mover una hoja, esta  volvía a su lugar, causando que la hada frunciera el ceño y murmurara palabras mágicas,  buscando entender qué ocurría.  Al ver que su broma causaba más confusión de lo esperado, Puck comenzó a sentirse un  poco culpable. No quería que la hada se sintiera mal ni que su pequeña travesura  interfiriera en su trabajo. Decidió entonces poner fin a la broma, pero no sin antes hacer  algo más para solucionar las cosas. Usó su magia para hacer que las hojas se  transformaran en pequeñas flores brillantes, que adornaron el telar y alegraron el entorno.  La hada, al ver el cambio, sonrió, comprendiendo que Puck había hecho su travesura con  buenas intenciones.  Desde ese día, Puck aprendió que, aunque las bromas eran divertidas, también era  importante ser considerado con los demás. Aunque seguía disfrutando de su naturaleza  traviesa, nunca olvidó la lección que le enseñó la sabia hada: las risas compartidas son  mucho más valiosas cuando se hacen con cariño y respeto."
}
"""""




    

