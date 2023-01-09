# La clase que se creará en este documento de Python permitirá trabajar con la información en formato XML. Esta clase contará con métodos para leer y transformar el contenido de los documentos XML. Estos métodos permitirán transformar el contenido de las cadenas de caracteres en XML a propiedades de la clase. Esto ayudará a procesar la información de manera más fácil y eficiente. Además, la clase también tendrá métodos que permitirán realizar consultas y acceder a los datos contenidos en los documentos XML. Esto permitirá obtener información de forma rápida y sencilla.


import xml.etree.ElementTree as ET

class XmlMatches:

    # Inicializar las propiedades de la clase
    def __init__(self):
        self.scorers = None
        self.shotOns = None
        self.shotOffs = None
        self.faults = None
        self.cardsYellow = None
        self.cardsRed = None
        self.cross = None
        self.corner = None
        self.homePos = None
        self.awayPos = None

    # Agregando como lista las id de los jugadores que convirtieron gol
    def xmlGoals(self, xml):

        try:
            self.scorers = []
            # Creando objeto que permite acceder a la información de la cadena de caracteres en el xml
            xml_data = ET.fromstring(xml)

            # Recuperar los datos de un bloque VALUE
            lst_value = xml_data.findall("value") # lista con todos los elementos value

            # Loop en el que se agregan a la lista del objeto los goleadores del partido
            for value in lst_value:
                try:
                    self.scorers.append(value.find("player1").text)

                # Se salta el error en el caso de AtributeError dado que este error ocurre cuando hay un none, es decir que la información no existe en la base de datos
                except AttributeError:
                    pass

        except TypeError:
            self.scorers = None

        except Exception as err:
            raise
    
    # Agregando como lista las id de los jugadores que dispararon al arco
    def xmlShotOn(self, xml):

        try:
            self.shotOns = []
            # Creando objeto que permite acceder a la información de la cadena de caracteres en el xml
            xml_data = ET.fromstring(xml)

            # Recuperar los datos de un bloque VALUE
            lst_value = xml_data.findall("value") # lista con todos los elementos value

            # Loop en el que se agregan a la lista del objeto los rematadores que dispararon hacia el arco
            for value in lst_value:
                try:
                    self.shotOns.append(value.find("player1").text)

                # Se salta el error en el caso de AtributeError dado que este error ocurre cuando hay un none, es decir que la información no existe en la base de datos
                except AttributeError:
                    pass

        except TypeError:
            self.shotOns = None

        except Exception as err:
            raise

    # Agregando como lista las id de los jugadores que dispararon fuera del arco
    def xmlShotOff(self, xml):

        try:
            self.shotOffs = []
            # Creando objeto que permite acceder a la información de la cadena de caracteres en el xml
            xml_data = ET.fromstring(xml)

            # Recuperar los datos de un bloque VALUE
            lst_value = xml_data.findall("value") # lista con todos los elementos value

            # Loop en el que se agregan a la lista del objeto los rematadores que dispararon fuera del arco
            for value in lst_value:
                try:
                    self.shotOffs.append(value.find("player1").text)

                # Se salta el error en el caso de AtributeError dado que este error ocurre cuando hay un none, es decir que la información no existe en la base de datos
                except AttributeError:
                    pass

        except TypeError:
            self.shotOffs = None


        except Exception as err:
            raise

    # Agregando como lista las id de los jugadores que cometieron falta
    def xmlFault(self, xml):

        try:
            self.faults = []
            # Creando objeto que permite acceder a la información de la cadena de caracteres en el xml
            xml_data = ET.fromstring(xml)

            # Recuperar los datos de un bloque VALUE
            lst_value = xml_data.findall("value") # lista con todos los elementos value

            # Loop en el que se agregan a la lista del objeto los jugadores que realizaron falta
            for value in lst_value:
                try:
                    self.faults.append(value.find("player1").text)

                # Se salta el error en el caso de AtributeError dado que este error ocurre cuando hay un none, es decir que la información no existe en la base de datos
                except AttributeError:
                    pass

        except TypeError:
            self.faults = None

        except Exception as err:
            raise

    # Agregando como lista las id de los jugadores que recibieron tarjeta
    def xmlCard(self, xml):

        try:
            self.cardsYellow = []
            self.cardsRed = []
            # Creando objeto que permite acceder a la información de la cadena de caracteres en el xml
            xml_data = ET.fromstring(xml)

            # Recuperar los datos de un bloque VALUE
            lst_value = xml_data.findall("value") # lista con todos los elementos value

            # Loop en el que se agregan a la lista del objeto los jugadores que recibieron tarjeta
            for value in lst_value:
                try:
                    # Separar jugadores que recibieron amarilla de los que recibieron roja
                    if value.find("card_type").text == "y":
                        self.cardsYellow.append(value.find("player1").text)
                    elif value.find("card_type").text == "r":
                        self.cardsRed.append(value.find("player1").text)

                # Se salta el error en el caso de AtributeError dado que este error ocurre cuando hay un none, es decir que la información no existe en la base de datos
                except AttributeError:
                    pass

        except TypeError:
            self.cardsYellow = None
            self.cardsRed = None

        except Exception as err:
            raise
        
    # Agregando como lista las id de los jugadores que realizaron centro
    def xmlCross(self, xml):

        try:
            self.cross = []
            # Creando objeto que permite acceder a la información de la cadena de caracteres en el xml
            xml_data = ET.fromstring(xml)

            # Recuperar los datos de un bloque VALUE
            lst_value = xml_data.findall("value") # lista con todos los elementos value

            # Loop en el que se agregan a la lista del objeto los jugadores que realizaron centro
            for value in lst_value:
                try:
                    self.cross.append(value.find("player1").text)

                # Se salta el error en el caso de AtributeError dado que este error ocurre cuando hay un none, es decir que la información no existe en la base de datos
                except AttributeError:
                    pass

        except TypeError:
            self.cross = None

        except Exception as err:
            raise

    # Agregando como lista las id de los jugadores que realizaron corners
    def xmlCorner(self, xml):

        try:
            self.corner = []
            # Creando objeto que permite acceder a la información de la cadena de caracteres en el xml
            xml_data = ET.fromstring(xml)

            # Recuperar los datos de un bloque VALUE
            lst_value = xml_data.findall("value") # lista con todos los elementos value

            # Loop en el que se agregan a la lista del objeto los jugadores que realizaron corners
            for value in lst_value:
                try:
                    self.corner.append(value.find("player1").text)

                # Se salta el error en el caso de AtributeError dado que este error ocurre cuando hay un none, es decir que la información no existe en la base de datos
                except AttributeError:
                    pass

        except TypeError:
            self.corner = None

        except Exception as err:
            raise