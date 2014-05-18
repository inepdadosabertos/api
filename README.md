
## **SITE DADOS ABERTOS INEP**

### Objetivos do projeto
* Mostrar que é possível disponibilizar dados do INEP seguindo as recomendações da Cartilha de Dados Abertos (http://dados.gov.br/cartilha-publicacao-dados-abertos/)
* Disponibilizar os dados mais brutos e permitir que seja feito o acesso simplificado, com considerações semânticas da URL e com identificadores únicos e persistentes

### URLs de chamadas da API

* retorna escolas com um determinado filtro (não exclusivo) [micro-dado]
⋅⋅* /ideb/escolas.{json|csv}?uf=[sigla]&codigo_municipio=[cod_municipio]&rede=[rede]
* retorna resumo dos dados de um determinado filtro (não exclusivo)
⋅⋅* /ideb.{json|csv}?uf=[sigla]&rede=[rede]
* retorna uma escola específica
⋅⋅* /ideb/escola/[código_escola].{json|csv}
* (FUTURO) retorna resumo agrupado de uma UF específica
⋅⋅* /ideb/uf/[uf].{json|csv}?rede=[rede]
* (FUTURO) retorna resultado agrupado de um município específico
⋅⋅* /ideb/municipio/[código_municipio].{json|csv}

### Roadmap do projeto

1. refinar a lógica de organização dos dados

⋅⋅1. criar “bucket único das escolas” agrupando dados das escolas dos censos (educação básica e ensino superior) com as informações únicas das escolas (inclusive dados de geolocalização)
⋅⋅1. criar “bucket do censo escolar” com os dados de estrutura, cursos, docentes e alunos
⋅⋅1. criar “bucket de cada indicador” com o código da escola como chave. Exemplo: bucket “ideb”, com a chave “11046430” ([código_escola]_[indicador]) e nesse índice exibir os dados agrupados por ano
⋅⋅1. estudar e identificar modelo de buckets para as pesquisas (SAEB, ENEM, PADAE, PNERA, PROVAO, PROVA BRASIL, CENSO MAGISTERIO)
