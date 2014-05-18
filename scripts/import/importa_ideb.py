#!/usr/bin/env python
# -*- coding: utf-8 -*-



HOST = "54.207.108.144" #"localhost" #"10.0.0.36"
PORT = 8098
BUCKET_NAME = "ideb_escola"



import riak
import time
import uuid
import csv
import json


def format_number(number, type):

	if (number.lower() == "nd" or number.lower() == "nd*"):
		return None

	return type(number.replace("-", "0").replace(",", "."))



def create_new_item(codigo_escola, row):
	return {

		"codigo_escola": codigo_escola,
		"codigo_municipio": row[1],
		"uf": row[0],
		"nome_municipio": row[2],
		"nome_escola": row[4].decode('UTF-8'),
		"rede": row[5].lower(),

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
escola_bucket = client.bucket(BUCKET_NAME)



print client.get_buckets()


dados = {}
dados_array = []

#i=0



with open("anos_iniciais.csv", "rb") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	headers = spamreader.next()
	for row in spamreader:

		#i+=1
		#if i > 100:
		#	i=0
		#	break;

		codigo_escola = row[3]
		print codigo_escola

		item = create_new_item(codigo_escola, row)
		if codigo_escola in dados:
			item = dados[codigo_escola]



		item["taxa_aprovacao"]["2005"]["anos_iniciais"] = {
			"ano_1a5": format_number(row[6], float),
			"ano_1": format_number(row[7], float),
			"ano_2": format_number(row[8], float),
			"ano_3": format_number(row[9], float),
			"ano_4": format_number(row[10], float),
			"ano_5": format_number(row[11], float),
			"indicador_rendimento": format_number(row[12], float)
		}

		item["taxa_aprovacao"]["2007"]["anos_iniciais"] = {
			"ano_1a5": format_number(row[13], float),
			"ano_1": format_number(row[14], float),
			"ano_2": format_number(row[15], float),
			"ano_3": format_number(row[16], float),
			"ano_4": format_number(row[17], float),
			"ano_5": format_number(row[18], float),
			"indicador_rendimento": format_number(row[19], float)
		}
		item["taxa_aprovacao"]["2009"]["anos_iniciais"] = {
			"ano_1a5": format_number(row[20], float),
			"ano_1": format_number(row[21], float),
			"ano_2": format_number(row[22], float),
			"ano_3": format_number(row[23], float),
			"ano_4": format_number(row[24], float),
			"ano_5": format_number(row[25], float),
			"indicador_rendimento": row[26]
		}
		item["taxa_aprovacao"]["2011"]["anos_iniciais"] = {
			"ano_1a5": format_number(row[27], float),
			"ano_1": format_number(row[28], float),
			"ano_2": format_number(row[29], float),
			"ano_3": format_number(row[30], float),
			"ano_4": format_number(row[31], float),
			"ano_5": format_number(row[32], float),
			"indicador_rendimento": format_number(row[33], float)
		}



		item["nota_prova_brasil"]["2005"]["anos_iniciais"] = {
			"matematica": format_number(row[34], float),
			"lingua_portuguesa": format_number(row[35], float),
			"nota_media_padronizada": format_number(row[36], float)
		}
		item["nota_prova_brasil"]["2007"]["anos_iniciais"] = {
			"matematica": format_number(row[37], float),
			"lingua_portuguesa": format_number(row[38], float),
			"nota_media_padronizada": format_number(row[39], float)
		}
		item["nota_prova_brasil"]["2009"]["anos_iniciais"] = {
			"matematica": format_number(row[40], float),
			"lingua_portuguesa": format_number(row[41], float),
			"nota_media_padronizada": format_number(row[42], float)
		}
		item["nota_prova_brasil"]["2011"]["anos_iniciais"] = {
			"matematica": format_number(row[43], float),
			"lingua_portuguesa": format_number(row[44], float),
			"nota_media_padronizada": format_number(row[45], float)
		}

		item["ideb"]["anos_iniciais"] = {
			"2005": format_number(row[46], float),
			"2007": format_number(row[47], float),
			"2009": format_number(row[48], float),
			"2011": format_number(row[49], float)
		}
		item["projecoes"]["anos_iniciais"] = {
			"2007": format_number(row[50], float),
			"2009": format_number(row[51], float),
			"2011": format_number(row[52], float),
			"2013": format_number(row[53], float),
			"2015": format_number(row[54], float),
			"2017": format_number(row[55], float),
			"2019": format_number(row[56], float),
			"2021": format_number(row[57], float)
		}

		dados[codigo_escola] = item




print "**** DADOS FINAIS ***"

with open("anos_finais.csv", "rb") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	headers = spamreader.next()
	for row in spamreader:


		#i+=1
		#if i > 100:
		#	i=0
		#	break;

		codigo_escola = row[3]
		print codigo_escola

		item = create_new_item(codigo_escola, row)
		if codigo_escola in dados:
			item = dados[codigo_escola]



		item["taxa_aprovacao"]["2005"]["anos_finais"] = {
			"ano_6a9": format_number(row[6], float),
			"ano_6": format_number(row[7], float),
			"ano_7": format_number(row[8], float),
			"ano_8": format_number(row[9], float),
			"ano_9": format_number(row[10], float),
			"indicador_rendimento": format_number(row[11], float)
		}
		item["taxa_aprovacao"]["2007"]["anos_finais"] = {
			"ano_6a9": format_number(row[12], float),
			"ano_6": format_number(row[13], float),
			"ano_7": format_number(row[14], float),
			"ano_8": format_number(row[15], float),
			"ano_9": format_number(row[16], float),
			"indicador_rendimento": format_number(row[17], float)
		}
		item["taxa_aprovacao"]["2009"]["anos_finais"] = {
			"ano_6a9": format_number(row[18], float),
			"ano_6": format_number(row[19], float),
			"ano_7": format_number(row[20], float),
			"ano_8": format_number(row[21], float),
			"ano_9": format_number(row[22], float),
			"indicador_rendimento": format_number(row[23], float)
		}
		item["taxa_aprovacao"]["2011"]["anos_finais"] = {
			"ano_6a9": format_number(row[24], float),
			"ano_6": format_number(row[25], float),
			"ano_7": format_number(row[26], float),
			"ano_8": format_number(row[27], float),
			"ano_9": format_number(row[28], float),
			"indicador_rendimento": format_number(row[29], float)
		}


		item["nota_prova_brasil"]["2005"]["anos_finais"] = {
			"matematica": format_number(row[30], float),
			"lingua_portuguesa": format_number(row[31], float),
			"nota_media_padronizada": format_number(row[32], float)
		}
		item["nota_prova_brasil"]["2007"]["anos_finais"] = {
			"matematica": format_number(row[33], float),
			"lingua_portuguesa": format_number(row[34], float),
			"nota_media_padronizada": format_number(row[35], float)
		}
		item["nota_prova_brasil"]["2009"]["anos_finais"] = {
			"matematica": format_number(row[36], float),
			"lingua_portuguesa": format_number(row[37], float),
			"nota_media_padronizada": format_number(row[38], float)
		}
		item["nota_prova_brasil"]["2011"]["anos_finais"] = {
			"matematica": format_number(row[39], float),
			"lingua_portuguesa": format_number(row[40], float),
			"nota_media_padronizada": format_number(row[41], float)
		}



		item["ideb"]["anos_finais"] = {
			"2005": format_number(row[42], float),
			"2007": format_number(row[43], float),
			"2009": format_number(row[44], float),
			"2011": format_number(row[45], float)
		}
		item["projecoes"]["anos_finais"] = {
			"2007": format_number(row[46], float),
			"2009": format_number(row[47], float),
			"2011": format_number(row[48], float),
			"2013": format_number(row[49], float),
			"2015": format_number(row[50], float),
			"2017": format_number(row[51], float),
			"2019": format_number(row[52], float),
			"2021": format_number(row[53], float)
		}

		dados[codigo_escola] = item



print "salvando no RIAK..."

for codigo_escola in dados:
	print "> %s" % codigo_escola
	item = dados[codigo_escola]
	new_escola = escola_bucket.new(
		"%s" % (codigo_escola), data=item)

	new_escola.add_index('uf_bin', item['uf'])
	new_escola.add_index('codigo_municipio_bin', item['codigo_municipio'])
	new_escola.add_index('rede_bin', item['rede'])
	new_escola.add_index('uf_rede_bin', "%s_%s" % (item['uf'], item['rede']))
	new_escola.add_index('codigo_municipio_rede_bin', "%s_%s" % (item['codigo_municipio'], item['rede']))
	new_escola.store()


	#print row
	#print ', '.join(row)

	#break




print "acabou!"







"""
MAPA DO CSV

0	uf,
1	codigo_municipio,
2	nome_municipio,
3	codigo_escola,
4	nome_escola,
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



