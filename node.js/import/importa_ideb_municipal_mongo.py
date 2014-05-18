#!/usr/bin/env python
# -*- coding: utf-8 -*-



HOST = "localhost" #"10.0.0.36"
PORT = 8098
BUCKET_NAME = "ideb_municipio"

HOST_MONGO = "localhost"
PORT_MONGO = 27017
DATA_BASE_NAME = "ideb"


import riak
import pymongo
import time
import uuid
import csv
import json


def format_number(number, type):

	if (number.lower() == "nd" or number.lower() == "nd*"):
		return None

	return type(number.replace("-", "0").replace(",", "."))



def create_new_item(codigo_municipio, row):
	return {
		"codigo_municipio": codigo_municipio,
		"uf": row[0],
		"nome_municipio": row[2],
		"redes": {}
	}

def create_new_rede(codigo_rede):
	return {
		"taxa_aprovacao": {
			"2005": {},
			"2007": {},
			"2009": {},
			"2011": {}
		},

		"nota_prova_brasil": {
			"2005": {},
			"2007": {},
			"2009": {},
			"2011": {}
		},

		"ideb": {},
		"projecoes": {}
	}





client = riak.RiakClient(host=HOST, http_port=PORT)


municipio_bucket = client.bucket(BUCKET_NAME)
mongoClient = MongoClient(HOST_MONGO, PORT_MONGO)
mongoDB = mongoClient[DATA_BASE_NAME]

# We're creating the user data & keying off their username.
# Note that the user hasn't been stored in Riak yet.


print client.get_buckets()


dados = {}
dados_array = []





i=0


with open("D:/Data/INEP/IDEB/divulgacao-anos-iniciais-escolas-2011.xls", "rb") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	headers = spamreader.next()
	for row in spamreader:

		#i+=1
		#if i > 100:
		#	i=0
		#	break;

		codigo_municipio = row[1]
		codigo_rede = row[3]
		print codigo_municipio

		item = create_new_item(codigo_municipio, row)
		if codigo_municipio in dados:
			item = dados[codigo_municipio]

		rede = create_new_rede(codigo_rede)
		if codigo_rede in item["redes"]:
			rede = item["redes"][codigo_rede] 

		
		rede["taxa_aprovacao"]["2005"]["anos_iniciais"] = {
			"ano_1a5": format_number(row[4], float),
			"ano_1": format_number(row[5], float),
			"ano_2": format_number(row[6], float),
			"ano_3": format_number(row[7], float),
			"ano_4": format_number(row[8], float),
			"ano_5": format_number(row[9], float),
			"indicador_rendimento": format_number(row[10], float)
		}

		rede["taxa_aprovacao"]["2007"]["anos_iniciais"] = {
			"ano_1a5": format_number(row[11], float),
			"ano_1": format_number(row[12], float),
			"ano_2": format_number(row[13], float),
			"ano_3": format_number(row[14], float),
			"ano_4": format_number(row[15], float),
			"ano_5": format_number(row[16], float),
			"indicador_rendimento": format_number(row[17], float)
		}
		rede["taxa_aprovacao"]["2009"]["anos_iniciais"] = {
			"ano_1a5": format_number(row[18], float),
			"ano_1": format_number(row[19], float),
			"ano_2": format_number(row[20], float),
			"ano_3": format_number(row[21], float),
			"ano_4": format_number(row[22], float),
			"ano_5": format_number(row[23], float),
			"indicador_rendimento": row[24]
		}
		rede["taxa_aprovacao"]["2011"]["anos_iniciais"] = {
			"ano_1a5": format_number(row[25], float),
			"ano_1": format_number(row[26], float),
			"ano_2": format_number(row[27], float),
			"ano_3": format_number(row[28], float),
			"ano_4": format_number(row[29], float),
			"ano_5": format_number(row[30], float),
			"indicador_rendimento": format_number(row[31], float)
		}



		rede["nota_prova_brasil"]["2005"]["anos_iniciais"] = {
			"matematica": format_number(row[32], float),
			"lingua_portuguesa": format_number(row[33], float),
			"nota_media_padronizada": format_number(row[34], float)
		}
		rede["nota_prova_brasil"]["2007"]["anos_iniciais"] = {
			"matematica": format_number(row[35], float),
			"lingua_portuguesa": format_number(row[36], float),
			"nota_media_padronizada": format_number(row[37], float)
		}
		rede["nota_prova_brasil"]["2009"]["anos_iniciais"] = {
			"matematica": format_number(row[38], float),
			"lingua_portuguesa": format_number(row[39], float),
			"nota_media_padronizada": format_number(row[40], float)
		}
		rede["nota_prova_brasil"]["2011"]["anos_iniciais"] = {
			"matematica": format_number(row[41], float),
			"lingua_portuguesa": format_number(row[42], float),
			"nota_media_padronizada": format_number(row[43], float)
		}

		rede["ideb"]["anos_iniciais"] = {
			"2005": format_number(row[44], float),
			"2007": format_number(row[45], float),
			"2009": format_number(row[46], float),
			"2011": format_number(row[47], float)
		}
		rede["projecoes"]["anos_iniciais"] = {
			"2007": format_number(row[48], float),
			"2009": format_number(row[49], float),
			"2011": format_number(row[50], float),
			"2013": format_number(row[51], float),
			"2015": format_number(row[52], float),
			"2017": format_number(row[53], float),
			"2019": format_number(row[54], float),
			"2021": format_number(row[55], float)
		}

		item["redes"][codigo_rede] = rede
		dados[codigo_municipio] = item



print "**** DADOS FINAIS ***"

with open("D:/Data/INEP/IDEB/divulgacao-anos-finais-municipios-2011.csv", "rb") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	headers = spamreader.next()
	for row in spamreader:


		#i+=1
		#if i > 100:
		#	i=0
		#	break;

		codigo_municipio = row[1]
		codigo_rede = row[3]
		print codigo_municipio

		item = create_new_item(codigo_municipio, row)
		if codigo_municipio in dados:
			item = dados[codigo_municipio]

		rede = create_new_rede(codigo_rede)
		if codigo_rede in item["redes"]:
			rede = item["redes"][codigo_rede] 

		
		rede["taxa_aprovacao"]["2005"]["anos_iniciais"] = {
			"ano_6a9": format_number(row[4], float),
			"ano_6": format_number(row[5], float),
			"ano_7": format_number(row[6], float),
			"ano_8": format_number(row[7], float),
			"ano_9": format_number(row[8], float),
			"indicador_rendimento": format_number(row[9], float)
		}

		rede["taxa_aprovacao"]["2007"]["anos_iniciais"] = {
			"ano_6a9": format_number(row[10], float),
			"ano_6": format_number(row[12], float),
			"ano_7": format_number(row[13], float),
			"ano_8": format_number(row[14], float),
			"ano_9": format_number(row[15], float),
			"indicador_rendimento": format_number(row[16], float)
		}
		rede["taxa_aprovacao"]["2009"]["anos_iniciais"] = {
			"ano_6a9": format_number(row[17], float),
			"ano_6": format_number(row[18], float),
			"ano_7": format_number(row[19], float),
			"ano_8": format_number(row[20], float),
			"ano_9": format_number(row[21], float),
			"indicador_rendimento": row[22]
		}
		rede["taxa_aprovacao"]["2011"]["anos_iniciais"] = {
			"ano_6a9": format_number(row[22], float),
			"ano_6": format_number(row[23], float),
			"ano_7": format_number(row[24], float),
			"ano_8": format_number(row[25], float),
			"ano_9": format_number(row[26], float),
			"indicador_rendimento": format_number(row[27], float)
		}



		rede["nota_prova_brasil"]["2005"]["anos_iniciais"] = {
			"matematica": format_number(row[28], float),
			"lingua_portuguesa": format_number(row[29], float),
			"nota_media_padronizada": format_number(row[30], float)
		}
		rede["nota_prova_brasil"]["2007"]["anos_iniciais"] = {
			"matematica": format_number(row[31], float),
			"lingua_portuguesa": format_number(row[32], float),
			"nota_media_padronizada": format_number(row[33], float)
		}
		rede["nota_prova_brasil"]["2009"]["anos_iniciais"] = {
			"matematica": format_number(row[34], float),
			"lingua_portuguesa": format_number(row[35], float),
			"nota_media_padronizada": format_number(row[36], float)
		}
		rede["nota_prova_brasil"]["2011"]["anos_iniciais"] = {
			"matematica": format_number(row[37], float),
			"lingua_portuguesa": format_number(row[38], float),
			"nota_media_padronizada": format_number(row[39], float)
		}

		rede["ideb"]["anos_iniciais"] = {
			"2005": format_number(row[40], float),
			"2007": format_number(row[41], float),
			"2009": format_number(row[42], float),
			"2011": format_number(row[43], float)
		}
		rede["projecoes"]["anos_iniciais"] = {
			"2007": format_number(row[44], float),
			"2009": format_number(row[45], float),
			"2011": format_number(row[46], float),
			"2013": format_number(row[47], float),
			"2015": format_number(row[48], float),
			"2017": format_number(row[49], float),
			"2019": format_number(row[50], float),
			"2021": format_number(row[51], float)
		}

		item["redes"][codigo_rede] = rede
		dados[codigo_municipio] = item




print "salvando no MongoDB..."

municipiosDB = mongoDB.municipio;
municipiosDB.insert(dados)


print "acabou!"





#print dados







"""
0	uf,
1	codigo_municipio,
2	nome_municipio,
5	rede,
6	2005_aprov_1a5,
7	2005_ano_1,
8	2005_ano_2,
9	2005_ano_3,
10	2005_ano_4,
11	2005_ano_5,
12	2005_indicador_1a5,
13	2007_aprov_1a5,
14	2007_ano_1,
15	2007_ano_2,
16	2007_ano_3,
17	2007_ano_4,
18	2007_ano_5,
19	2007_indicador_1a5,
20	2009_aprov_1a5,
21	2009_ano_1,
22	2009_ano_2,
23	2009_ano_3,
24	2009_ano_4,
25	2009_ano_5,
26	2009_indicador_1a5,
27	2011_aprov_1a5,
28	2011_ano_1,
29	2011_ano_2,
30	2011_ano_3,
31	2011_ano_4,
32	2011_ano_5,
33	2011_indicador_1a5,
34	2005_provabrasil_Matemática,
35	2005_provabrasil_Língua Portuguesa,
36	2005_provabrasil_Nota Média Padronizada (N),
37	2007_provabrasil_Matemática,
38	2007_provabrasil_Língua Portuguesa,
39	2007_provabrasil_Nota Média Padronizada (N),
40	2009_provabrasil_Matemática,
41	2009_provabrasil_Língua Portuguesa,
42	2009_provabrasil_Nota Média Padronizada (N),
43	2011_provabrasil_Matemática,
44	2011_provabrasil_Língua Portuguesa,
45	2011_provabrasil_MEDIA_PADRONIZADA,
46	Ideb_2005,
47	Ideb_2007,
48	Ideb_2009,
49	Ideb_2011,
50	Proj_2007,
51	Proj_2009,
52	Proj_2011,
53	Proj_2013,
54	Proj_2015,
55	Proj_2017,
56	Proj_2019,
57	Proj_2021

"""